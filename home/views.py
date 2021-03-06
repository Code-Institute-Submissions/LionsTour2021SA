from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings


email_host = settings.EMAIL_HOST_USER

def home_view(request):
    return render(request, "home.html")

def history_view(request):
    return render(request, "history.html", {"home": "history"})

def fixtures_view(request):
    return render(request, "fixtures.html", {"home": "fixtures"})

def tickets_view(request):
    return render(request, "tickets.html", {"home": "tickets"})


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message + " was sent from " +contact_email, contact_email, [email_host])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Thank you for your message, we will contact you shortly.')
            return redirect('home')
    return render(request, "contact.html", {'form': form})

