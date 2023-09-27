# from django.db import models



# class User(models.Model):
#     name = models.CharField(max_length=250)
#     def __str__(self):
#         return self.name
    
# class Password(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     website = models.CharField(max_length=255)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.username
    
from asyncio import AbstractServer
from django.db import models
from django.contrib.auth.models import User


class Foydalanuvchi(AbstractServer):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"Username: {self.username}"

class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)
    veb_sayt = models.CharField(max_length=255)
    foydalanuvchi_nomi = models.CharField(max_length=255)
    parol = models.CharField(max_length=255)
    search = models.CharField(max_length=100)
    
    def __str__(self):
        return self.veb_sayt
    
