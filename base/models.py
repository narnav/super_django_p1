from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
   
    def __str__(self):
        return self.title
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    img = models.ImageField()
    def __str__(self):
        return self.description


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    price  = models.FloatField()
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    createdTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user  


class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def total_price(self):
        return self.product.price * self.amount

    def __str__(self):
        return f"{self.order} - {self.product} ({self.quantity} items)"