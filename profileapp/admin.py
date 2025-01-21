from django.contrib import admin
from  .models import Category,custmer, Post, order,Profile
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(custmer)
admin.site.register(Post)
admin.site.register(order)
admin.site.register(Profile)
	






