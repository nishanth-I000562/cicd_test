from .models import Task


def validate_title(title: str) -> str:
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Task title cannot be empty")
    if len(cleaned) > 100:
        raise ValueError("Task title cannot exceed 100 characters")
    return cleaned


def validate_priority(priority) -> None:
    from .models import Priority
    if not isinstance(priority, Priority):
        raise ValueError("Invalid priority")


def validate_task(task: Task) -> None:
    validate_title(task.title)
    validate_priority(task.priority)
