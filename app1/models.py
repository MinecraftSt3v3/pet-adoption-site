# from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime

class userPost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CATEGORY_CHOICES = (
        ('----------', '----------'),
		('1 Month', '1 Month'),
		('2 Month', '2 Month'),
        ('3 Month', '3 Month'),
        ('4 Month', '4 Month'),
        ('5 Month', '5 Month'),
        ('6 Month', '6 Month'),
        ('7 Month', '7 Month'),
        ('8 Month', '8 Month'),
        ('9 Month', '9 Month'),
        ('10 Month', '10 Month'),
        ('11 Month', '11 Month'),
        ('1 Year', '1 Year'),
		('2 Year', '2 Year'),
        ('3 Year', '3 Year'),
        ('4 Year', '4 Year'),
        ('5 Year', '5 Year'),
        ('6 Year', '6 Year'),
        ('7 Year', '7 Year'),
        ('8 Year', '8 Year'),
        	
    )
    description = models.CharField(max_length=35)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=25, default='----------')
    itemPhoto = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.description
