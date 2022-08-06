from email.mime import image
from django.shortcuts import render
from django.http import HttpResponse,Http404
from.models import*
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    about=About.objects.all()
    projects=Projects.objects.all()
    contact=Contacts.objects.all()
    resume=Resume.objects.all()
    image = Image.objects.all()
    
    
    return render (request,"all-von/von.html",{"about":about,"projects":projects,"contact":contact,"resume":resume,"image":image} )

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})
    
    
