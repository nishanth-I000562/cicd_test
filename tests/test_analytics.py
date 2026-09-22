from src.task_manager.analytics import TaskAnalytics
from src.task_manager.models import Priority, TaskStatus


def test_count_by_status(service):
    service.create_task("One")
    second = service.create_task("Two")
    service.complete_task(second.id)

    counts = TaskAnalytics(service.repository.list_all()).count_by_status()

    assert counts[TaskStatus.TODO] == 1
    assert counts[TaskStatus.DONE] == 1
    assert counts[TaskStatus.IN_PROGRESS] == 0


def test_count_by_priority(service):
    service.create_task("Low", priority=Priority.LOW)
    service.create_task("High", priority=Priority.HIGH)

    counts = TaskAnalytics(service.repository.list_all()).count_by_priority()

    assert counts[Priority.LOW] == 1
    assert counts[Priority.HIGH] == 1
    assert counts[Priority.MEDIUM] == 0


def test_completion_rate(service):
    service.create_task("One")
    second = service.create_task("Two")
    service.complete_task(second.id)

    analytics = TaskAnalytics(service.repository.list_all())

    assert analytics.completion_rate() == 0.5


def test_empty_completion_rate():
    assert TaskAnalytics([]).completion_rate() == 0.0


def test_high_priority_open_tasks(service):
    service.create_task("Open high", priority=Priority.HIGH)
    done = service.create_task("Done high", priority=Priority.HIGH)
    service.complete_task(done.id)
    service.create_task("Open low", priority=Priority.LOW)

    result = TaskAnalytics(service.repository.list_all()).high_priority_open_tasks()

    assert [task.title for task in result] == ["Open high"]
