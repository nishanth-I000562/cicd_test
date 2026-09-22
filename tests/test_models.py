import pytest

from src.task_manager.models import Priority, Task, TaskStatus


def test_new_task_defaults_to_todo():
    task = Task(id=1, title="Write documentation")
    assert task.status == TaskStatus.TODO
    assert task.priority == Priority.MEDIUM


def test_start_moves_task_to_in_progress():
    task = Task(id=1, title="Implement feature")
    task.start()
    assert task.status == TaskStatus.IN_PROGRESS


def test_completed_task_cannot_be_started():
    task = Task(id=1, title="Release feature")
    task.mark_done()

    with pytest.raises(ValueError, match="cannot be started"):
        task.start()
