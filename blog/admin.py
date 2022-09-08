from django.contrib import admin

from .models import *

# Register your mod
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Comment)
