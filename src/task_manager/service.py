from .models import Priority, Task, TaskStatus
from .repository import TaskRepository
from .validators import validate_priority, validate_title


class TaskService:
    def __init__(self, repository: TaskRepository | None = None) -> None:
        self.repository = repository or TaskRepository()
        self._next_id = 1

    def create_task(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        tags: list[str] | None = None,
    ) -> Task:
        title = validate_title(title)
        validate_priority(priority)

        task = Task(
            id=self._next_id,
            title=title,
            description=description.strip(),
            priority=priority,
            tags=sorted(set(tags or [])),
        )
        self.repository.add(task)
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get(task_id)
        if task is None:
            raise KeyError(f"Task {task_id} not found")
        return task

    def complete_task(self, task_id: int) -> Task:
        task = self.get_task(task_id)
        task.mark_done()
        return self.repository.update(task)

    def start_task(self, task_id: int) -> Task:
        task = self.get_task(task_id)
        task.start()
        return self.repository.update(task)

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)

    def search(
        self,
        keyword: str = "",
        status: TaskStatus | None = None,
        priority: Priority | None = None,
    ) -> list[Task]:
        keyword = keyword.strip().lower()

        return [
            task
            for task in self.repository.list_all()
            if (not keyword or keyword in task.title.lower() or keyword in task.description.lower())
            and (status is None or task.status == status)
            and (priority is None or task.priority == priority)
        ]

    def update_task(
        self,
        task_id: int,
        *,
        title: str | None = None,
        description: str | None = None,
        priority: Priority | None = None,
    ) -> Task:
        task = self.get_task(task_id)

        if title is not None:
            task.title = validate_title(title)
        if description is not None:
            task.description = description.strip()
        if priority is not None:
            validate_priority(priority)
            task.priority = priority

        return self.repository.update(task)
