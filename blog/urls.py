from django.urls import path
from . import views
urlpatterns = [
    #path("base/", views.base, name ="base" ),
    path("", views.home, name ="home" ),
    # path("about", views.about, name ="about"),
    # path("category", views.category, name ="category"),
    # path("contact", views.contact, name ="contacte" ),
    # path("search", views.search, name ="search" ),
    # path("single", views.single, name ="single" )
]
