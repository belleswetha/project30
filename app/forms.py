from app.models import *
from django import forms


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
    
class AcessRecordsForm(forms.ModelForm):
    class Meta:
        model=AcessRecords
        fields='__all__'
        
