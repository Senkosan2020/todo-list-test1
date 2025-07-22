from django import forms
from django.utils import timezone
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if not self.instance.pk and deadline < timezone.now():
            raise forms.ValidationError("Deadline cannot be in the past when creating a task.")
        return deadline
