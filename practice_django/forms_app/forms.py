# -*- coding: utf-8 -*-
from django import forms
import datetime


class ContactForm(forms.Form):
    date_creation = forms.DateField(
        initial=datetime.date.today, help_text="Заполнить форму"
    )
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=True)

    def clean_date_creation(self):
        data = self.cleaned_data["date_creation"]
        if data < datetime.date.today():
            raise forms.ValidationError(
                ("Дата отправки должна быть сегодняшним днем, день в день")
            )
        return data
