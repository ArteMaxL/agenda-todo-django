from unicodedata import name
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def index(request):
    req_search = request.GET.get('search', '')

    if req_search:
        contacts = Contact.objects.filter(name__contains=req_search)
    else:
        contacts = Contact.objects.all()

    context = {'contacts': contacts}

    return render(request, 'contact/index.html', context)

def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {'contact': contact}
    return render(request, 'contact/detail.html', context)

def edit(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'GET':
        form = ContactForm(instance= contact)
        context = {'form': form, 'id': id}

        return render(request, 'contact/edit.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance= contact)
        context = {'form': form, 'id': id}

        if form.is_valid():
            form.save()
        
        messages.success(request, 'Contacto actualizado.')
        return render(request, 'contact/edit.html', context)

def create(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}

        return render(request, 'contact/create.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            
        return redirect('contact')