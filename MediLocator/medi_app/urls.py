from django.urls import path ,include
from .import views ,user_views,owner_views
from django.contrib.auth import views as auth_views

urlpatterns = [
  

    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

    path("",views.home,name="home"),
    path("about/",views.about,name="about_us"),
    path("contact/",views.contact,name="contact"),
    path("all_feedback/",views.all_feedback,name="all_feedback"),
    path("testing/",views.testing,name="testing"),



    
    path("user_feedback/",user_views.user_feedback,name="user_feedback"),
    path("user_login/",user_views.user_login,name="user_login"),
    path("user_home/",user_views.user_home,name="user_home"),
    path("user_logout/",user_views.user_logout,name="user_logout"),
     path("view_shopkeeper/",user_views.view_shopkeeper,name="view_shopkeeper"),
     path("view_map/",user_views.view_map,name="view_map"),
     path("medicine_request/",user_views.medicine_request,name="medicine_request"),
     path("update_request/",user_views.update_request,name="update_request"),
     path("update_status/<int:id>/",user_views.update_status,name="update_status"),
     path("user_edit_profile/",user_views.user_edit_profile,name="use_edit_profile"),





    path("user_reg/",user_views.user_reg,name="user_reg"),
    path("owner_login/",owner_views.owner_login,name="owner_login"),
    path("owner_feedback/",owner_views.owner_feedback,name="owner_feedback"),
    path("owner_reg/",owner_views.owner_reg,name="owner_reg"),
    path("owner_home/",owner_views.owner_home,name="owner_home"),
    path("owner_logout/",owner_views.owner_logout,name="owner_logout"),
    path("shop_detail/",owner_views.shop_detail,name="shop_detail"),
    path("map_location/",owner_views.map_location,name="map_location"),
    path("view_medicine/",owner_views.view_medicine,name="view_medicine"),
    path("owner_edit_profile/",owner_views.owner_edit_profile,name="owner_edit_profile"),
 
   
  


  
]
