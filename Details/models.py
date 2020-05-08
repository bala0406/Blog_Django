from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class UserInformation(models.Model):
    name = models.CharField(max_length=100)
    
    about = models.TextField(max_length=500)

    email = models.EmailField(max_length=254, unique=True)

    phone = models.CharField(max_length=10, unique=True)

    # Gender choices
    Gender_Choice = [("Male", "Male"),
                     ("Female", "Female"),
                     ("Others", "others")
                     ]

    gender = models.CharField(max_length=6, choices=Gender_Choice)

    currentuser = models.ForeignKey(User,default=None,on_delete=models.CASCADE,null=True)

    #  profilepicture = models.ImageField(width_field= 200,height_field=200)

    def __str__(self):
        return self.name

    
