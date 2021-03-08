from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ACCOUNT_TYPE = (('buyer','Buyer'),('seller','Seller'))
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Products(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=300)


    def __str__(self):
        return self.name

