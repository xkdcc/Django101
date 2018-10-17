from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime
from pytz import timezone


# Create your views here.

def home(request):
    return render(request, 'index.html')


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404

    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    dt = datetime.datetime.now(timezone('US/Pacific')) + datetime.timedelta(hours=offset)
    return render(request, 'index.html', {'offset': offset, 'dt': dt.strftime(fmt)})
