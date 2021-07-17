from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
import json


# Create your views here.
def home(request):
    return demo_uploadfiles_v1(request)


def demo_uploadfiles_v1(request):
    return render(request, 'uploadfiles/index.html')
