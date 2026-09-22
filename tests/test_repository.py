from src.task_manager.models import Task


def test_repository_add_and_get(repository):
    task = Task(id=1, title="First")
    repository.add(task)

    assert repository.get(1) is task


def test_repository_update(repository):
    task = Task(id=1, title="Old")
    repository.add(task)

    task.title = "New"
    repository.update(task)

    assert repository.get(1).title == "New"


def test_repository_delete(repository):
    repository.add(Task(id=1, title="Delete me"))

    assert repository.delete(1) is True
    assert repository.get(1) is None


def test_repository_delete_missing_task_returns_false(repository):
    assert repository.delete(99) is False
