from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Edit(models.Model):
    user = models.CharField(User, max_length=18)