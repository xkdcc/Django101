from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'ajax/index.html')


def demo_ajax_v1_addition(request):
    return render(request, 'ajax/index.html')


def demo_ajax_v2_addition(request):
    return render(request, 'ajax/index.html')


def demo_ajax_v3_addition(request):
    return render(request, 'ajax/index.html')
