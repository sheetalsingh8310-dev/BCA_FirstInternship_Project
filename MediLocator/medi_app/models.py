from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import re



# Custom Gmail Validator
def validate_gmail(value):
    """Allow only Gmail addresses"""
    if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', value):
        raise ValidationError("Only Gmail addresses are allowed!")

# class UserProfile(models.Model):
#     email = models.EmailField(validators=[validate_gmail])   # Gmail check
#     profile_image = models.FileField(
#         upload_to="profile_images/",
#         validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "gif"])] ,
#         null=True,
#         blank=True
#         # Only images
#     )

#     def __str__(self):
#         return self.email



# Create your models here.
class FeedBack (models.Model):
    Email =models.CharField(max_length=45,primary_key=True)
    name=models.CharField(max_length=55,null=False)
    rating=models.CharField(max_length=5,null=False)
    remark=models.TextField(default="")
    date=models.DateField(default=timezone.now)
    user_pic=models.CharField(max_length=255,default="")

    def __str__(self): # it represnt object into string form
         return self.name



##contact table model###
class Contact(models.Model):
      Email =models.CharField(max_length=45)
      name=models.CharField(max_length=55,null=False)
      phone=models.CharField(max_length=13,null=False)
      question=models.TextField()
      date=models.DateField(default=timezone.now)
      def __str__(self): # it represnt object into string form
         return self.name
      
class User(models.Model):
       name=models.CharField(max_length=60)
       email=models.EmailField(max_length=60,primary_key=True,validators=[validate_gmail])
       password=models.CharField(max_length=45)
       phone=models.CharField(max_length=13)
       pic_name=models.FileField(upload_to="user_pic/",default="",
       validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "gif"])] ,
       null=True,
       blank=True
       )
       def __str__(self): # it represnt object into string form
          return self.name

class shopowner(models.Model):
       name=models.CharField(max_length=60)
       email=models.EmailField(max_length=60,primary_key=True)
       password=models.CharField(max_length=45)
       phone=models.CharField(max_length=13)
       pic_name=models.FileField(upload_to="owner_pic/",default="")
       def __str__(self): # it represnt object into string form
          return self.name


class ShopDetail(models.Model):
    owner=models.ForeignKey(shopowner,on_delete=models.DO_NOTHING)
    shop_name = models.CharField(max_length=255)
    gst_number= models.CharField(max_length=255,primary_key=True)
    description = models.TextField(blank=True, null=True)
    location_lat = models.CharField(max_length=100)
    location_long = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)  
    city=models.CharField(max_length=100)
    address = models.TextField(default="")
    def __str__(self): # it represnt object into string form
          return self.shop_name

status_type = [
    ('REQUESTED', 'Requested'),      
       
    ('RECEIVED', 'Medicine Received'), 
    ('CANCELLED', 'Request Cancelled'),
]

class MedicineRequest(models.Model):
    user_email=models.CharField(max_length=100,null=False)
    user_whatsapp=models.CharField(max_length=13,null=False)
    medicine_name=models.CharField(max_length=100,null=False)
    refer_doctor_name=models.CharField(max_length=100,null=True)
    user_message=models.TextField(default="",null=True)
    medicine_status=models.CharField(max_length=30,choices=status_type,default="REQUESTED")
    def __str__(self): # it represnt object into string form
          return self.user_whatsapp