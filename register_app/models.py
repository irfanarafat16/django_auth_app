from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('type1', 'User Type 1'),
        ('type2', 'User Type 2'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='type1')
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)

    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        help_text='Required. Letters and digits only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
