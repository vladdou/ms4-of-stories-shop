from django import forms
from .models import ContactEmail


class ContactForm(forms.ModelForm):
    """ Creates Contact table in database """
    class Meta:
        model = ContactEmail
        fields = ['email_address', 'name', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting placeholders on fields
        placeholders = {
            'email_address': 'Email',
            'name':  'Name',
            'message': 'Message'
        }

        self.fields['email_address'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
