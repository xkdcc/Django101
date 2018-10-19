from django.shortcuts import render
from django.http import Http404, HttpResponse
import json

# Create your views here.


def home(request):
    return demo_ajax_v1_addition(request)


def demo_ajax_v1_addition(request):
    if request.is_ajax() and request.method == 'POST':
        response_data = {}
        addend1 = int(request.POST['addend1'])
        addend2 = int(request.POST['addend2'])
        response_data['results'] = str(addend1 + addend2)
        data = json.dumps(response_data)
        return HttpResponse(data, content_type='application/json')
    else:
        return render(request, 'ajax/index.html')


def demo_ajax_v2_addition(request):
    return render(request, 'ajax/index.html')


def demo_ajax_v3_addition(request):
    return render(request, 'ajax/index.html')
