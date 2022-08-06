from email.mime import image
from django.shortcuts import render
from django.http import HttpResponse
from.models import*

# Create your views here.

def home(request):
    about=About.objects.all()
    projects=Projects.objects.all()
    contact=Contacts.objects.all()
    resume=Resume.objects.all()
    image = Image.objects.all()
    
    
    return render (request,"all-von/von.html",{"about":about,"projects":projects,"contact":contact,"resume":resume,"image":image} )
    
    
