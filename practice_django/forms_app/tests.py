# -*- coding: utf-8 -*-
# from django.test import TestCase
from forms_app.forms import ContactForm
import pytest
from django import forms
import datetime


# @pytest.mark.parametrize(
#     "date_creation, subject, message, sender, cc_myself, validity",
#     [("2023-07-03", "Что-то", "Hello", "cxz@mail.ru", "cc_myself", True)],
# )
# def test_valid_contact_form(
#     date_creation, subject, message, sender, cc_myself, validity
# ):
#     form = ContactForm(
#         data={
#             "date_creation": date_creation,
#             "subject": subject,
#             "message": message,
#             "sender": sender,
#             "cc_myself": cc_myself,
#         }
#     )

#     f = form.errors.as_data()
#     print(f)

#     assert form.is_valid() is validity

# @pytest.mark.parametrize(

# )