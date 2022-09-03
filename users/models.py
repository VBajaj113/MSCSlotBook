from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, null=True, default='', unique=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(default='default.png', upload_to='profile_pics')
    first_name = models.CharField(max_length = 255, null=True, default='')
    last_name = models.CharField(max_length = 255, null=True, default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

