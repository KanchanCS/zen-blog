from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    #path("base/", views.base, name ="base" ),
    path("", views.home, name ="home" ),
    path("single-post/<id>/" , views.post_details, name="single_post"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("category/", views.category, name="category"),
    path("result/", views.category, name="search")
]
