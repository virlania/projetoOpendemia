from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AmigosFacebook
import json
# Create your views here.

def geochart(request):
    dicionario = {"auxpython": [['Country', 'Population',],
        ['Canada', 65746],
        ['United States', 657665],
        ['Brazil', 567676],
        ['Russia',  657000],    
        ['Germany', 818900],
        ['Poland',  385400]]}
    return render(request, 'geochart.html', dicionario)

def submit_geochart(request):
        amigos = AmigosFacebook.objects.all()
        return render(request, 'tela2.html', {'amigos': list(amigos.values())})
