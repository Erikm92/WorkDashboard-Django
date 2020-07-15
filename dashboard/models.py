from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class userlinks(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,  on_delete=models.CASCADE)
    main = models.CharField (max_length=200,default='')
    mainname = models.CharField (max_length=200,default='')
    mainfavicon = models.CharField (max_length=200,default='')
    table_id =  models.CharField (max_length=200,default='')
    

    
    
class userheader(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,  on_delete=models.CASCADE)
    header_id = models.CharField (max_length=200,default='')
    header_name = models.CharField (max_length=200,default='')
   


class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    main = models.CharField (max_length=200,default='')
    main2 = models.CharField (max_length=200,default='')
    main3 = models.CharField (max_length=200,default='')
    main4 = models.CharField (max_length=200,default='')
    main5 = models.CharField (max_length=200,default='')
    main6 = models.CharField (max_length=200,default='')



def create_profile(sender, **kwargs):
    if kwargs['created']:
        create_profile=userprofile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, sender=User)

