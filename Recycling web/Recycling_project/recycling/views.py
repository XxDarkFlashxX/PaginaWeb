from django.shortcuts import render

def home(request):
    return render(request, 'recycling/home.html')

def mapa(request):
    return render(request, 'recycling/mapa.html')  # Sin necesidad de un token

def material(request):
    return render(request, 'recycling/material.html')

def proceso(request):
    return render(request, 'recycling/proceso.html')
