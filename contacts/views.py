from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, NewsletterForm
from .models import Contact, Newsletter

def contact(request):
    """Vue pour le formulaire de contact"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contacts:contact')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contact.html', {
        'form': form,
    })

def subscribe(request):
    """Vue pour le formulaire d'inscription"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merci de votre inscription à la newsletter!')
            return redirect('main:home')
    else:
        form = NewsletterForm()
    
    return render(request, 'contacts/subscribe.html', {
        'form': form,
    })

def success(request):
    """Page de confirmation"""
    return render(request, 'contacts/success.html') 