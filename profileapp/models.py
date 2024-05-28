from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_modified = models.DateTimeField(User, auto_now=True)
	phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200, blank=True)
	country = models.CharField(max_length=200, blank=True)


	def __str__(self):
		return self.user.username

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()

# Automate the profile thing
post_save.connect(create_profile, sender=User)


class Category(models.Model):
     category_name = models.CharField(max_length=50,null=False)

     def __str__(self):
          return self.category_name
     


class custmer(models.Model):
      first_name = models.CharField(max_length=30,null=False)
      lost_name = models.CharField(max_length =30,null=False)
      email = models.EmailField(null=False,unique=True)
      address = models.CharField(max_length =250,null=False)
      #rating
      phone_number= models.IntegerField(null=False,unique=True)
      #number of lost items
      #number of finding items
      password = models.CharField(max_length =250)
      #change_password
      user_picture =  models.ImageField(upload_to='user_pictures/', default='default.jpg')

      def __str__(self):
          return f'{self.first_name} {self.lost_name}'


class Post(models.Model):
    item_name = models.CharField(max_length=30,null=False)
    picture_of_item = models.ImageField(upload_to='item_pictures/', default='default.jpg')
    address = models.CharField(max_length =250,null=False)
    category = models.ForeignKey(Category ,on_delete= models.CASCADE , default=1)
    description = models.TextField(max_length =250)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
          return self.item_name
    
    

class order(models.Model):
     item = models.ForeignKey(Post ,on_delete= models.CASCADE , default=1)
     user = models.ForeignKey(User ,on_delete = models.CASCADE)
     address = models.CharField(max_length =250,null=False)
     quantity = models.CharField(max_length =250,null=False)
     status =models.BooleanField(default=False)
     phone_number = models.IntegerField(null=False,unique=True)



