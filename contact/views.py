from unicodedata import name
from django.shortcuts import render
from .models import Contact


def index(request):
    req_search = request.GET.get('search', '')

    if req_search:
        contacts = Contact.objects.filter(name__contains=req_search)
    else:
        contacts = Contact.objects.all()

    context = {'contacts': contacts}

    return render(request, 'contact/index.html', context)
