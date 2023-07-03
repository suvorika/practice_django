# -*- coding: utf-8 -*-
from django.http import request
from django.shortcuts import render
from django.urls import is_valid_path
from forms_app.forms import ContactForm


def contact_send(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            date_creation = form.cleaned_data["date_creation"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]
            recipients = ["abcdef@mail.com"]

            if cc_myself:
                recipients.append(message)

            try:
                send_mail(sender, subject, message, recipients, date_creation)

            except BadHeaderError:
                return HttpResponse("Неверное заполнение")
            # return redirect("success")
            form = ContactForm()
            message.success(request, "Сообщение успешно отправлено")

        else:
            message.error(request, "Error")
    return render(request, "forms_app/email.html", {"form": form})
