from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class profile(models.Model):
     User = models.OneToOneField(User ,on_delete= models.CASCADE)
     first_name = models.CharField(max_length=30,null=False)
     lost_name = models.CharField(max_length =30,null=False)
     email = models.EmailField(null=False,unique=True)
     address_user = models.CharField(max_length =250,null=False)
     city = models.CharField(max_length =250,null=False)
     country = models.CharField(max_length =250,null=False)
     phone_number= models.IntegerField(null=False,unique=True)

     def __str__(self):
          return self.User.username

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



