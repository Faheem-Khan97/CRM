from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):

    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20, null= True)
    phone = models.CharField(max_length = 20, null= True)
    email = models.CharField(max_length = 20, null= True)
    #profile_pic = models.ImageField(null = True, blank = True)
    dateCreated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name



class tag(models.Model):
    name = models.CharField(max_length = 20, null= True)


    def __str__(self):
        return self.name


class product(models.Model):
    PRODUCT_CHOICES = (
        ('indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )

    name = models.CharField(max_length = 20, null= True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 20, null = True, choices = PRODUCT_CHOICES)
    description = models.CharField(max_length = 20, blank = True, null= True)
    dateCreated =  models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(tag)

    def __str__(self):
        return self.name



class order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('out For Delivery', 'Out For Delivery'),
        ('delivered', 'Delivered'),

    ]
    customer = models.ForeignKey(customer, null = True, on_delete = models.SET_NULL )
    product = models.ForeignKey(product, null = True, on_delete = models.SET_NULL )
    
    dateCreated =  models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 20, null = True, choices = STATUS_CHOICES)


    def __str__(self):
        return (self.product.name)

