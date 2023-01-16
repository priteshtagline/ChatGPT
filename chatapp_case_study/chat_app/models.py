from djongo import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    mobile_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
