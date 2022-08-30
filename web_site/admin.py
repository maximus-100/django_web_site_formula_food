from django.contrib import admin
from .models import Category, Post, Profile, Ip, Comments
# Register your models here.
from django.contrib import admin
from .models import Category, Post
from django.utils.safestring import mark_safe

# Register your models here.


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Ip)
admin.site.register(Comments)
