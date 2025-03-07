from django.shortcuts import render

def home(request):
    return render(request, 'maxim/home.html')

def datenschutz(request):
    return render(request, 'maxim/datenschutz.html')