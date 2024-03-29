from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
import json


# Create your views here.

# HttpRequest.is_ajax() method is deprecated in Django 3.1
# This is our own AJAX detection method.
def is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def home(request):
    return demo_ajax_v1_addition(request)


def demo_ajax_v1_addition(request):
    if request.method == 'POST':
        addend1 = int(request.POST['v1_addend1'])
        addend2 = int(request.POST['v1_addend2'])
        data = addend1 + addend2
        return HttpResponse(data)
    else:
        return render(request, 'ajax/index.html')


def demo_ajax_v2_addition(request):
    if is_ajax(request) and request.method == 'POST':
        response_data = {}
        addend1 = int(request.POST['v2_addend1'])
        addend2 = int(request.POST['v2_addend2'])
        response_data['results'] = str(addend1 + addend2)
        return JsonResponse(response_data)
        # Note:
        # Instead of using below code, in Django 1.7, we can use JsonResponse now.
        # data = json.dumps(response_data)
        # return HttpResponse(data, content_type='application/json')
    else:
        return render(request, 'ajax/index.html')


def demo_ajax_v3_addition(request):
    return render(request, 'ajax/index.html')
