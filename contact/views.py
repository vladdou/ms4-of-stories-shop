# Code credits:
# https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend

from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """
    View returning the contact page
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            email_address = contact_form.cleaned_data['email_address']
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            contact_form.save()

            try:
                send_mail(
                    f'Message from {name}',
                    message,
                    email_address,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,  # Raise SMTPException if send fails
                )

                messages.success(
                    request,
                    f'Thank you {name} for contacting Of Stories!')
                return HttpResponseRedirect('/contact/')

            except BadHeaderError:
                return HttpResponse('Invalid header found')

        else:
            messages.error(request, 'Your email could not be sent.\
                    Please check if the contact form is valid')
            return redirect(reverse, 'contact')

    else:
        if request.user.is_authenticated:
            contact_form = ContactForm(
                initial={'email_address': request.user.email}
            )
        else:
            contact_form = ContactForm()

    context = {
            'contact_form': contact_form,
            }

    return render(request, 'contact/contact.html', context)
