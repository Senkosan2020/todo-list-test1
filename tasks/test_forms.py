import pytest
from django.utils import timezone
from tasks.forms import TaskForm
from tasks.models import Task
from datetime import timedelta

@pytest.mark.django_db
def test_create_task_with_past_deadline_is_invalid():
    form = TaskForm(data={
        "content": "Invalid task",
        "deadline": timezone.now() - timedelta(days=1)
    })
    assert not form.is_valid()
    assert "deadline" in form.errors

@pytest.mark.django_db
def test_update_task_with_past_deadline_is_allowed():
    task = Task.objects.create(
        content="Valid",
        deadline=timezone.now() + timedelta(days=1)
    )
    form = TaskForm(data={
        "content": "Updated",
        "deadline": timezone.now() - timedelta(days=1)
    }, instance=task)
    assert form.is_valid()
