from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    points = models.BigIntegerField(default=0)

    def __str__(self):
        return self.username