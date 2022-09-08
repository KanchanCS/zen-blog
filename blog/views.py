from django.shortcuts import get_object_or_404, redirect, render

from .form import CommentForm, ContactForm
from .models import *


# Create your views here.
def home(request):
    all_post = Post.objects.all().order_by("-create_date")
    banner = Banner.objects.all()
    recent_post = all_post[:6]
    part_one = recent_post[:3]
    part_two = recent_post[3:6]
    last = recent_post[0]
    context = {
        "part_one": part_one,
        "part_two": part_two,
        "recent_post": recent_post,
        "all_post": all_post,
        "last": last,
        "banner": banner,
    }
    return render(request, "home.html", context)


def category(request):
    category = Category.objects.all()

    return render(request, "category.html", {"category": category})


def post_details(request, id):
    single_post = get_object_or_404(Post, id=id)
    comment = Comment.objects.filter(post=single_post.id).order_by(
        "-timestamp"
    )[:2]

    comments_count = comment.count()
    if request.method == "POST":
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            content = request.POST.get("content")
            comment = Comment.objects.create(
                post=single_post, user=request.user, content=content
            )
            comment.save()
            return redirect("blog:home")
    else:
        cf = CommentForm()

    context = {
        "single_post": single_post,
        "comments_form": cf,
        "comments": comment,
        "comments_count": comments_count,
    }
    return render(request, "post_detail.html", context)


def about(request):
    about = About.objects.all().order_by("-id")[:4]

    return render(request, "about.html", {"about": about})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:home")
    else:
        form = Contact()
    context = {"form": form}
    return render(request, "contact.html", context)
