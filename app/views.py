from django.shortcuts import render
from app.forms import FaceRecognitionForm
from app.machinelearning import EdgeDetection
from django.conf import settings
from app.models import FaceRecognition
import os

def index(request):
    form = FaceRecognitionForm()
    if request.method == "POST":
        form = FaceRecognitionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)
            # extract image from database
            primary_key = save.pk
            imgobj = FaceRecognition.objects.get(pk = primary_key)
            fileroot = str(imgobj.image)
            filepath = os.path.join(settings.MEDIA_ROOT,fileroot)
            results = EdgeDetection(filepath)
            print("its done")
            
            return render(request,'app/index2.html',{"form":form, "upload" : True, "results":results})
    
    
    return render(request,'app/index2.html',{"form":form, "upload" : False})