import pytest

from src.task_manager.repository import TaskRepository
from src.task_manager.service import TaskService


@pytest.fixture
def repository():
    return TaskRepository()


@pytest.fixture
def service(repository):
    return TaskService(repository)
