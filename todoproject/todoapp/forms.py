from . models import Task
from django import forms

class form_task(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']