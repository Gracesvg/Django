from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')


def services(request):
    return render(request, 'services.html')
