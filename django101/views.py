from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime
import pytz


# Create your views here.

def home(request):
    return render(request, 'index.html')


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404

    dt = datetime.datetime.now(tz=pytz.timezone("America/Los_Angeles")) + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
