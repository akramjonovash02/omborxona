from django.db import models
from django.contrib.auth.models import AbstractUser

class Tarqatuvchi(AbstractUser):
    bolim = models.CharField(max_length=255)
    tel = models.CharField(max_length=11)
    manzil = models.TextField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.bolim}: {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Tarqatuwchi'
        verbose_name_plural = 'Tarqatuvchilar'


