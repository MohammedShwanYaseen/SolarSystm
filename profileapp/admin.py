from django.contrib import admin
from  .models import Category,custmer, Post, order,Profile
from django.contrib.auth.models import User
from .models import User, SolarPanel, Battery, SensorData, Report

admin.site.register(User)
admin.site.register(SolarPanel)
admin.site.register(Battery)
admin.site.register(SensorData)
admin.site.register(Report)

admin.site.register(Category)
admin.site.register(custmer)
admin.site.register(Post)
admin.site.register(order)
admin.site.register(Profile)
	






