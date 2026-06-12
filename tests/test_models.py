import pytest

from models.task import Task
from models.user import User
from services.project_manager import ProjectManager


def test_user_import_and_email_validation():
    user = User("Alice", 30, "alice@example.com", "alice")

    assert user.email == "alice@example.com"
    assert user.username == "alice"

    with pytest.raises(ValueError):
        user.email = "not-an-email"


def test_task_completion_tracks_status_changes():
    task = Task("Write tests", "Cover model behavior")

    task.update_status("Complete")
    assert task.is_complete is True

    task.update_status("In Progress")
    assert task.is_complete is False


def test_project_manager_user_project_summary_includes_added_projects():
    manager = ProjectManager()
    user = manager.create_user("Alice", 30, "alice@example.com", "alice")
    project = manager.create_project("CLI", "Build project CLI", "2026-06-01", "2026-06-30")

    assert manager.add_user_to_project(project.project_id, user) is True

    summary = manager.get_user_summary(user)
    assert summary["Total Projects"] == 1
    assert summary["Projects"] == ["CLI"]
