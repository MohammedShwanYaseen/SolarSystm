from django.contrib import admin
from  .models import Category, User, Post, order

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(order)
