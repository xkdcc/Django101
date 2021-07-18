import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages


# Create your views here.
def home(request):
    return demo_uploadfiles_v1(request)


def demo_uploadfiles_v1(request):    
    '''
    Not using form, model
    '''    
    if request.method == 'POST' and request.FILES['myfile']:
        for key, file in request.FILES.items():
            path = file.name
            dest = open(os.path.join(settings.MEDIA_ROOT, file.name), 'wb') # Writing in byte as file.chunks return bytes.
            if file.multiple_chunks:
                for c in file.chunks():
                    dest.write(c) # If not using wb, here it will fail as "write() argument must be str, not bytes"
            else:
                dest.write(file.read())
            dest.close()
            
        messages.add_message(request, messages.SUCCESS, "Upload {} successfully!".format(file.name))
        
        return render(request, 'uploadfiles/index.html', )
    return render(request, 'uploadfiles/index.html')