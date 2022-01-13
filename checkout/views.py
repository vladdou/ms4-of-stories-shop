from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K7g8iLhcMTNqNlVkjUoaTFQsl1ITD2zkbw3SJ71LNQV4zdExeOSzcY5s2qhPHyeZ4INEf4sTU3dS4tHG8t49PCp00jdh5i4Wb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)