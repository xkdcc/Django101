import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
from django.utils.safestring import mark_safe


# Create your views here.
def home(request):
    return render(request, 'uploadfiles/index.html')


def demo_uploadfiles_v1(request):    
    '''
    Using open/write/close.
    Not using form, model
    '''    
    if request.method == 'POST' and request.FILES['v1file']:
        myfile = request.FILES['v1file']
        path = myfile.name
        dest = open(os.path.join(settings.MEDIA_ROOT, myfile.name), 'wb') # Writing in byte as file.chunks return bytes.
        if myfile.multiple_chunks:
            for c in myfile.chunks():
                dest.write(c) # If not using wb, here it will fail as "write() argument must be str, not bytes"
        else:
            dest.write(myfile.read())
        dest.close()
            
        messages.add_message(request, messages.SUCCESS, "Upload {} successfully!".format(myfile.name))
        
        return render(request, 'uploadfiles/index.html', context = {'version': "v1"})
    
    return render(request, 'uploadfiles/index.html')

def demo_uploadfiles_v2(request):    
    '''
    Using FileSystemStorage.
    Not using form, model
    '''
    if request.method == 'POST' and request.FILES['v2file']:
        myfile = request.FILES['v2file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
            
        messages.add_message(request, messages.SUCCESS, mark_safe("Upload <a href='{}'>{}</a> successfully!".format(uploaded_file_url, myfile.name)))
        
        return render(request, 'uploadfiles/index.html', context = {'version': "v2", 'uploaded_file_url': uploaded_file_url})
    
        
    
    return render(request, 'uploadfiles/index.html')