from collections import Counter

from .models import Priority, Task, TaskStatus


class TaskAnalytics:
    def __init__(self, tasks: list[Task]) -> None:
        self.tasks = tasks

    def count_by_status(self) -> dict[TaskStatus, int]:
        counts = Counter(task.status for task in self.tasks)
        return {status: counts.get(status, 0) for status in TaskStatus}

    def count_by_priority(self) -> dict[Priority, int]:
        counts = Counter(task.priority for task in self.tasks)
        return {priority: counts.get(priority, 0) for priority in Priority}

    def completion_rate(self) -> float:
        if not self.tasks:
            return 0.0
        completed = sum(task.status == TaskStatus.DONE for task in self.tasks)
        return completed / len(self.tasks)

    def high_priority_open_tasks(self) -> list[Task]:
        return [
            task
            for task in self.tasks
            if task.priority == Priority.HIGH and task.status != TaskStatus.DONE
        ]
