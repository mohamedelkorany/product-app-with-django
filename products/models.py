from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return self.name


class Product(models.Model):
    # categories = [
    # ('Fruits', 'Fruits'),
    # ('Vegetables', 'Vegetables'),
    # ('Spices', 'Spices'),
    # ('Dairy', 'Dairy'),
    # ]
    
    id = models.AutoField(primary_key = True )
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateField()
    expiry_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,blank=True, null=True)
    price = models.FloatField()
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

class User(models.Model):
    username = models.CharField( unique=True , max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    def _str_(self):
        return self.username

