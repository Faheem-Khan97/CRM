from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)
admin.site.register(tag)

