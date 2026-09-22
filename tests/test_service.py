import pytest

from src.task_manager.models import Priority, TaskStatus


def test_create_task_assigns_incrementing_ids(service):
    first = service.create_task("First")
    second = service.create_task("Second")

    assert first.id == 1
    assert second.id == 2


def test_create_task_normalizes_title_and_tags(service):
    task = service.create_task(
        "  Build API  ",
        description="  backend service  ",
        tags=["api", "python", "api"],
    )

    assert task.title == "Build API"
    assert task.description == "backend service"
    assert task.tags == ["api", "python"]


def test_create_task_rejects_empty_title(service):
    with pytest.raises(ValueError, match="cannot be empty"):
        service.create_task("   ")


def test_complete_task_changes_status(service):
    task = service.create_task("Finish tests")

    result = service.complete_task(task.id)

    assert result.status == TaskStatus.DONE


def test_start_task_changes_status(service):
    task = service.create_task("Implement feature")

    result = service.start_task(task.id)

    assert result.status == TaskStatus.IN_PROGRESS


def test_missing_task_raises_key_error(service):
    with pytest.raises(KeyError, match="Task 99 not found"):
        service.get_task(99)


def test_delete_task(service):
    task = service.create_task("Temporary")

    assert service.delete_task(task.id) is True
    assert service.delete_task(task.id) is False


def test_search_by_keyword(service):
    service.create_task("Build API", "REST backend")
    service.create_task("Write docs", "API documentation")
    service.create_task("Fix database")

    results = service.search(keyword="api")

    assert [task.title for task in results] == ["Build API", "Write docs"]


def test_search_by_status_and_priority(service):
    service.create_task("Normal", priority=Priority.MEDIUM)
    high = service.create_task("Urgent", priority=Priority.HIGH)
    service.complete_task(high.id)

    results = service.search(status=TaskStatus.DONE, priority=Priority.HIGH)

    assert [task.title for task in results] == ["Urgent"]


def test_update_task(service):
    task = service.create_task("Old title")

    updated = service.update_task(
        task.id,
        title="New title",
        description="Updated description",
        priority=Priority.HIGH,
    )

    assert updated.title == "New title"
    assert updated.description == "Updated description"
    assert updated.priority == Priority.HIGH
