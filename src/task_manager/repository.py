from .models import Task


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}

    def add(self, task: Task) -> Task:
        if task.id in self._tasks:
            raise ValueError(f"Task {task.id} already exists")
        self._tasks[task.id] = task
        return task

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def update(self, task: Task) -> Task:
        if task.id not in self._tasks:
            raise KeyError(f"Task {task.id} not found")
        self._tasks[task.id] = task
        return task

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def clear(self) -> None:
        self._tasks.clear()
