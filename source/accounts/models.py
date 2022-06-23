from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Client(AbstractUser):
    phone = models.CharField(max_length=24, default="+996771111111")
    pass
