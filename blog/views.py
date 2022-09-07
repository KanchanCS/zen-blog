from django.shortcuts import render, get_object_or_404 , redirect
from .models import *
from .form import ContactForm

# Create your views here.
def home(request):
    all_post = Post.objects.all().order_by('-create_date')
    banner = Banner.objects.all()
    recent_post = all_post[:6]
    part_one  = recent_post[:3]
    part_two = recent_post[3:6]
    last = recent_post[0]
    context = {
        "part_one":part_one,
        "part_two":part_two,
        "recent_post":recent_post,
        "all_post":all_post,
        "last":last, 
        "banner":banner,
    }
    return render(request, 'home.html', context)

def category(request):
    category = Category.objects.all()  

    return render (request, 'category.html',{'category':category})

def post_details(request, id):
    single_post = get_object_or_404(Post, id = id)
    context = {
        "single_post":single_post,
    }
    template_name = 'post_detail.html'
    return render(request, 'post_detail.html', context)


def about(request):
    about = About.objects.all().order_by('-id')[:4]

    return render(request, 'about.html',{'about':about})  
                       
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:home")
    else:
        form = Contact()
    context = {'form': form}
    return render(request, 'contact.html', context)

# def contact(request): 
#     if request.method == 'POST':
#             name = request.POST('name')
#             email= request.POST('email')
#             sub = request.POSTt('sub')
#             message = request.POST('message')
             
#             app=Contact(
#             name = name,
#             email= email,
#             sub = sub,
#             message = message)
#             app.save() 
#             messages.add_message(request, messages.INFO, 'Send message succesfully.') 
#             return redirect('home.html') 
#     else:
#         return render(request, 'contact.html')