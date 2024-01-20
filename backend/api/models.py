from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products (models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL)
    name=models.CharField(max_length=20)
    brand=models.CharField(max_length=20)
    description=models.TextField()
    image=models.CharField(max_length=2000)
    price=models.DecimalField(default=0.0,decimal_places=2)
    ratings=models.DecimalField(default=0.0,decimal_places=1)
    num_reviews=models.IntegerField(default=0)
    in_stock=models.BooleanField(default=False)
    _id=models.AutoField(primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand+' | '+self.name
    
class reviews (models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    comment=models.TextField()
    name=models.CharField(max_length=200)
    _id=models.AutoField(primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating
    
class orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=50)
    tax_price=models.DecimalField(decimal_places=2)
    shipping_price=models.DecimalField(decimal_places=2)
    total_price=models.DecimalField(decimal_places=2)
    is_paid=models.BooleanField(default=False)
    delivered_at=models.DateTimeField(auto_now_add=False)
    created_at=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.created_at
    
class order_items(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    order=models.ForeignKey(orders,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    name=models.CharField(max_length=50)
    image=models.CharField(max_length=2000)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name 
    
class shipping_address(models.Model):
    order=models.OneToOneField(on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    postal_code=models.IntegerField()
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.city




    


