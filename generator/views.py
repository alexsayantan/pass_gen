from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html',{'password': 'swersder'})

def password(request):

    thepassword = 'testing'
    characteres=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characteres.extend(list('!@#$%^&*()?'))
    if request.GET.get('numbers'):
        characteres.extend(list('1234567890'))

    length=int(request.GET.get('length',12))

    thepassword=''
    for x in range(length):
        thepassword += random.choice(characteres)

    return render(request, 'generator/password.html',{'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')