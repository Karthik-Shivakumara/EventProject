from django.shortcuts import render,redirect,get_object_or_404
from . models import*
from .forms import*

def admin(request):
    return render(request,'admin.html')


def admin_update(request):
    return render(request,'admin_update.html')


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def saved(request):
    return render(request,'saved.html')
    

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return saved(request)
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)


def events(request):
    dict_eve={
        'eve': Event.objects.all()
    }
    return render(request,'events.html',dict_eve)

def contact(request):
    return render(request,'contact.html')