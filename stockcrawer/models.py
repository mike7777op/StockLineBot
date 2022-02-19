from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')
    name = models.CharField(max_length=255,blank=True,null=False)


class UserInfo2(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')
    name = models.CharField(max_length=255,blank=True,null=False)
    days = models.IntegerField(blank=True, default='')
