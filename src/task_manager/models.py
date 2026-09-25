from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = TaskStatus.TODO
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def mark_done(self) -> None:
        self.status = TaskStatus.IN_PROGRESS

    def start(self) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Completed task cannot be started")
        self.status = TaskStatus.IN_PROGRESS
