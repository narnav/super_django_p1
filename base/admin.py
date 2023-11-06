from django.contrib import admin
from .models import Task,Category,Product,Order,OrderDetails
# Register your models here.

admin.site.register([Task,Category])
# admin.site.register(Category)
admin.site.register(Product)
admin.site.register([Order,OrderDetails])