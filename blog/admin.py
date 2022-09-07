from django.contrib import admin
from .models import Post , Category ,Banner, About,Contact
# Register your mod
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(About)
admin.site.register(Contact)