# from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime

class userPost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=35)
    category = models.CharField(max_length=10)
    itemPhoto = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.description
