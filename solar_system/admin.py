from django.contrib import admin
from  .models import Profile
from django.contrib.auth.models import User
from .models import User, SolarPanel, Battery, SensorData, Report

admin.site.register(User)
admin.site.register(SolarPanel)
admin.site.register(Battery)
admin.site.register(SensorData)
admin.site.register(Report)
admin.site.register(Profile)
	






