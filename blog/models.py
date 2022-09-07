from django.db import models
import datetime as dt
# Create your models here.
class Banner(models.Model):
    image          = models.ImageField(upload_to ='uploads/')
    title          = models.CharField(max_length=100)
    content        = models.TextField()

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name           = models.CharField(max_length=100)
    create_date    = models.DateTimeField(default=dt.datetime.now())
    updated_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):   
    category       = models.ForeignKey('Category', on_delete=models.CASCADE)
    title          = models.CharField(max_length=100)
    content        = models.TextField()
    image          = models.ImageField(upload_to ='uploads/')
    create_date    = models.DateTimeField(default=dt.datetime.now())
    updated_at     = models.DateTimeField(auto_now_add=True)
    publish        = models.BooleanField(default=True)
    auther         =models.CharField(max_length=100)

    def __str__(self):
        return self.title

class About(models.Model):
    image        = models.ImageField(upload_to ='uploads/')
    name         = models.CharField(max_length=50)
    generic      =  models.CharField(max_length=50)
    paragraph      = models.TextField()

    def __str__(self):
        return self. name

class Contact(models.Model):
    name=models .CharField(max_length=50) 
    email=models.EmailField(max_length=100) 
    sub  =models .CharField(max_length=50)
    message=models.TextField()  

    def __str__(self):
        return self.name

