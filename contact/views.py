from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


def contact(request):
    form = ContactForm

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            email_address = form.cleaned_data.get('email')
            phone = form.cleaned_data.get("phone")
            msg = form.cleaned_data.get('message')
            body = f'Name: {name}\nEmail: {email_address}\nPhone: {phone}\n\nMessage: {msg}'

            email = EmailMessage(
                'Za Motors - Contact Us',
                body,
                settings.EMAIL_HOST_USER,
                ['zamotors14@gmail.com'],
            )

            email.fail_silently = False
            email.send()

            messages.success(
                request, f'Thank you, {name} for sending a message!')

            return redirect("contact")

    context = {
        "form": form
    }
    return render(request, "contact/contact.html", context)
