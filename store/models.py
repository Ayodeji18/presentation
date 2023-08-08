from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_image")


    def __str__(self):
        return self.name
    
    class Meta: verbose_name_plural = ("Category")


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True) #Allows empty values
    image =models.ImageField(upload_to="product_image")
    rating = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    date_field = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=100)


    def __str__(self):
        return self.name
# Create your models here.

