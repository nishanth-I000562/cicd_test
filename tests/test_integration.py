from src.task_manager.analytics import TaskAnalytics
from src.task_manager.models import Priority, TaskStatus


def test_complete_task_management_flow(service):
    task = service.create_task(
        "Release API",
        description="Prepare the API release",
        priority=Priority.HIGH,
        tags=["release", "api"],
    )

    service.start_task(task.id)
    service.complete_task(task.id)

    stored = service.get_task(task.id)
    analytics = TaskAnalytics(service.repository.list_all())

    assert stored.status == TaskStatus.DONE
    assert analytics.completion_rate() == 1.0
    assert analytics.high_priority_open_tasks() == []
