from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    picture=models.ImageField(upload_to="images",null=True)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.name
    
class Carts(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")    
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)   