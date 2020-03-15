from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
admin.site.register(Payment)
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(DistributorDetail)
admin.site.register(SalesmanDetail)
admin.site.register(OrderDetail)