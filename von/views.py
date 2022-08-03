from django.shortcuts import render
from django.http import HttpResponse
from.models import*
from.models import about,contact
# Create your views here.

def home(request):
    about=About.objects.all()
    projects=Projects.objects.all()
    contact=Contacts.objects.all()
    resume=Resume.objects.all()
    
    
    return render (request,"all-von/von.html",{"about":about,"projects":projects,"contact":contact,"resume":resume} )
    
    
