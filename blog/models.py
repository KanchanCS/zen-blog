from django.db import models
import datetime as dt
# Create your models here.
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
    