from django.contrib import admin

# Register your models here.

from .models import FeedBack,Contact,User,ShopDetail,shopowner, MedicineRequest
class FeedBack_admin(admin.ModelAdmin):
  list_display=["name","Email","rating","remark","date"]

class Contact_admin(admin.ModelAdmin):
    list_display=["name","Email","phone","question"]

class User_admin(admin.ModelAdmin):
    list_display=["name","email","phone"]

class ShopDetail_admin(admin.ModelAdmin):
    list_display=["shop_name","gst_number","phone_no","description","city","address"]

class shopowner_admin(admin.ModelAdmin):
    list_display=["name","email","phone"]

class medicine_admin(admin.ModelAdmin):
    list_display=["user_email","user_whatsapp","medicine_name","user_message","medicine_status"]



admin.site.register(FeedBack,FeedBack_admin)
admin.site.register(Contact,Contact_admin)
admin.site.register(User,User_admin)
admin.site.register(ShopDetail,ShopDetail_admin)
admin.site.register(shopowner,shopowner_admin)
admin.site.register( MedicineRequest,medicine_admin)


admin.site.site_header="Medilocator dashboard"
admin.site.site_title="Find pharmacy nearby you easily"
admin.site.index_title="Medilocator Portal"


