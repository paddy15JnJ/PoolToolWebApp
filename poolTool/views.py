# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateContactForm
from django.http import HttpResponseRedirect
from .models import Contact

def index(request):
    if request.method == 'POST':
        print("Got post request")
        # create a form instance and populate it with data from the request:
        form = CreateContactForm(request.POST)

        print (request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateContactForm(label_suffix="")

    return render(request, 'createContact.html', {'form': form})


def thanks(request):


    return render(request, 'thanks.html', {})
