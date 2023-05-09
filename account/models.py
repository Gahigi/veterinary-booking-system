from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(verbose_name= "First Name", max_length=60, blank=False)
    last_name = models.CharField(verbose_name= "Last Name", max_length=60, blank=False)
    email = models.EmailField(verbose_name= "Email", max_length=255, unique=True, blank=False)
    is_veterinary = models.BooleanField(verbose_name="Is veterinary",default=False)
    is_veterinary = models.BooleanField(verbose_name="Is pet owner",default=False)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()
    
    #Change from default user model to custom user model
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
           