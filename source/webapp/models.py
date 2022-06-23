from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Announce(models.Model):
    description = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateField(auto_now=True)
    phone = models.CharField(max_length=24, null=True, blank=True)


class Photo(models.Model):
    photo = models.ImageField(upload_to="uploads/")
    announce = models.ForeignKey('webapp.Announce', on_delete=models.PROTECT,
                                 related_name='photos')



