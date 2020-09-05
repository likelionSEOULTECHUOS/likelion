from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/uploaded/')
    else:
        form = UploadFileForm()


    file_name = ""
    save_file_name = ""
    
    directory = []
    for direc in directory:
 
        path_dir = "/yunjee/media/Static/pdf/"+direc+"/"
        file_list = os.listdir(path_dir)
        file_list.sort()

        for i in file_list:
            file_name=path_dir+i+"[0]"

    save_file_name = "/yunjee/media/Static/pdf/"+direc+"/"+i.split(".")[0]+".jpg"

    try:
        with Image(filename=file_name) as img:
             img.save(filename=save_file_name)
    except:
        pass
 

    return render(request, 'upload.html', {'form': form})



def uploaded(request):
    return render(request, 'uploaded.html')



    