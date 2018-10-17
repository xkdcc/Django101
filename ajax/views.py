from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'ajax/index.html', {'version': 'v1'})


def v1(request):
    return render(request, 'ajax/index.html', {'version': 'v1'})


def v2(request):
    return render(request, 'ajax/index.html', {'version': 'v2'})


def v3(request):
    return render(request, 'ajax/index.html', {'version': 'v3'})
