from django.db import models

# Create your models here.

class About(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Resume(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Projects(models.Model):
    name= models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    
    @classmethod
    def all_projects(self):

        return Projects.objects.all()
    
    
    


