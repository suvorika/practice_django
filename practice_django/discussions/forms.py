from .models import Discussion
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError


class DiscussionCreateForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ("title", "content")


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()