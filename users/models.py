# users/models.py
from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone

class CustomUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True,related_name='custom_user')
    current_score  = models.IntegerField(null=True,default=0)
    high_score  = models.IntegerField(null=True,default=0)
    date = models.DateTimeField(null=True,default=timezone.now)
    gender = models.CharField(null=True,max_length=25,default="male")
    age = models.IntegerField(null=True,default=22)

    def __str__(self):
        return self.user.username
    
    