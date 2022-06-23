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
        if not EMAIL_REGEX.match(PostData['Email']):             
            errors['email'] = "Invalid email address!"
        if len(PostData ['Password'])<8:
            errors['Password']='password should be at least 8 characters'

        if not PostData ['Password']==PostData['confirm_pw']:
            errors['confirm_pw']='Password and confirm should be match'
        
        return errors
    




class users(models.Model):
    Fname= models.CharField(max_length=255)
    Lname= models.CharField(max_length=255)
    Email= models.EmailField(max_length=255)
    Password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects= UserManger()


