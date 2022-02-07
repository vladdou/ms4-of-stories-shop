from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Creates Contact table in database """
    class Meta:
        model = Contact
        fields = ['email_address', 'name', 'message']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting placeholders on fields
        placeholders = {
            'email_address': 'Your Email',
            'name':  'Your Name',
            'message': 'Your Message'
        }

        self.fields['email_address'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
