from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class userlinks(models.Model):
   
    main = models.CharField (max_length=200,default='')
    mainname = models.CharField (max_length=200,default='')
    mainfavicon = models.CharField (max_length=200,default='')
    table_id =  models.CharField (max_length=200,default='')
    
class userheader(models.Model):
       
    header_id = models.CharField (max_length=200,default='')
    header_name = models.CharField (max_length=200,default='')
   


class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    main = models.CharField (max_length=200,default='')
    olive = models.CharField (max_length=200,default='')
    admin = models.CharField (max_length=200,default='')
    confluence = models.CharField (max_length=200,default='')
    apps = models.CharField (max_length=200,default='')
    report = models.CharField (max_length=200,default='')



def create_profile(sender, **kwargs):
    if kwargs['created']:
        create_profile=userprofile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, sender=User)

