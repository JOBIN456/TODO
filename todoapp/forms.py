from django import forms
from.models import duty

class Todo(forms.ModelForm):
    class Meta:
        model=duty
        fields=['name','priorty','date']