from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    recent_post = Post.objects.all().order_by('-create_date')[:6]
    part_one  = recent_post[:3]
    part_two = recent_post[3:6]
    last = Post.objects.last()
    context = {
        "part_one":part_one,
        "part_two":part_two,
        "recent_post":recent_post,
        "last":last,
    }
    return render(request, 'home.html', context)

def category(request):
    category = Category.objects.all()  
    return render (request, 'category.html',{'category':category})

                 