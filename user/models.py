from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Email is Required")
        if not username:
            raise ValueError("Username is Required")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,password):
        user = self.create_user(email,username,password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
       
    

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(verbose_name='email', unique=True)
    username = models.CharField(max_length=40,unique=True)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    

    def __str__(self):
        return f'Username: {self.username} | Email: {self.email}' + " | Admin" if self.is_admin else ""