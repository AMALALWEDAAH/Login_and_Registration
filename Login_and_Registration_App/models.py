from errno import EROFS
from django.db import models
import re
# Create your models here.

class UserManger (models.Manager):
    def validator(self,PostData):
        errors={}
        if len(PostData['firest_name'])<2:
            errors['firest_name']='first name should be at least 2 characters'
        if len(PostData['last_name'])<2:
            errors['last_name']='last name should be at least 2 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(PostData['email']):             
            errors['email'] = "Invalid email address!"
        if len(PostData ['password'])<8:
            errors['password']='password should be at least 8 characters'
        if not PostData ['password']==PostData['confirm_pw']:
            errors['confirm_pw']='Password and confirm should be match'
        
        return errors

class users(models.Model):
    firest_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects= UserManger()


