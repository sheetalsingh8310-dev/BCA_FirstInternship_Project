from django.shortcuts import render,HttpResponse,redirect
from .models import FeedBack,User,ShopDetail,MedicineRequest
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError


# def user_register(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")
#         profile_image = request.FILES.get("profile_pic")

#         # basic checks
#         if not email.endswith("@gmail.com"):
#             messages.error(request, "Only Gmail addresses are allowed!")
#             return render(request, "medi_app/user/user_reg.html")

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return render(request, "medi_app/user/user_reg.html")

#         try:
#             user = UserProfile(
#                 email=email,
#                 password=make_password(password),
#                 profile_image=profile_image
#             )
#             user.full_clean()  # runs validators (like Gmail + extension)
#             user.save()
#             messages.success(request, "Registration successful. Please log in.")
#             return redirect("user_login")
#         except IntegrityError:
#             messages.error(request, "This email is already registered.")
#         except ValidationError as e:
#             messages.error(request, f"Error: {e}")

#     return render(request, "medi_app/user/user_reg.html")






def user_login(request):
    if request.method=="GET":
     return render(request,'medi_app/user/user_login.html')
    if request.method=="POST":
        user_email=request.POST["email"]
        user_pass=request.POST["password"]

        userList=User.objects.filter(email=user_email,password=user_pass)

        if len(userList)>0:
          #  user_object=userList[0]
           request.session["user_key"]=user_email
          #  request.session["user_role"]="user"
           return redirect("user_home")
        else:
           messages.error(request,"Invalid credentials 🤦‍♀️")
           return redirect("user_login")

def user_edit_profile(request):
    if request.method=="GET":
     user_email=request.session["user_key"]
     user_obj=User.objects.get(email=user_email)  # get return one object
     user_dict={"user_info":user_obj}
     return render(request,'medi_app/user/user_edit_profile.html', user_dict)
    if request.method=="POST":
       profile_pic=request.FILES.get("pic")
       user_phone=request.POST['phone']
       user_name=request.POST['name']
       user_email=request.session["user_key"]
       user_obj=User.objects.get(email=user_email) 
       if profile_pic is not  None:
          user_obj.pic_name=profile_pic
          user_obj.name=user_name
          
          user_obj.phone=user_phone
          user_obj.save()
          messages.success(request,"profile update successfully")
          return redirect(user_home)



def update_status(request,id):
    if request.method=="GET":
       medicie_obj=MedicineRequest.objects.get(id=id)
       medicie_obj.medicine_status="RECEIVED"
       medicie_obj.save()
       messages.success(request,"status updated ")
       return redirect("update_request")


def update_request(request):
    if request.method=="GET":
      user_email= request.session["user_key"]
         
      medicine_list=MedicineRequest.objects.filter(user_email=user_email)
      medicine_dict={"medicine_detail":medicine_list}



      return render(request,'medi_app/user/update_request.html' ,medicine_dict)
       
       


def medicine_request(request):
    if request.method=="GET":
      user_email= request.session["user_key"]
      user_obj=User.objects.get(email=user_email)
      user_dict={"user_detail":user_obj}
        #getting email fom session
      return render(request,'medi_app/user/medicine_request.html', user_dict)
    if request.method=="POST":
       user_email= request.POST["email"]
       user_whatsup= request.POST["whatsupp"]
       user_medicine= request.POST["medicine"]
       refer_doctor=request.POST["refer_doctor"]
       user_message=request.POST["message"]
      #  medicine_status=request.POST["medicine_status"]
       feedback_obj=MedicineRequest(user_email=user_email, user_whatsapp=user_whatsup,medicine_name=user_medicine, refer_doctor_name=refer_doctor,user_message=user_message)
       feedback_obj.save() 
       messages.success(request,"medicine request send successfully" )#it will store data into database
    return redirect("medicine_request")






def view_map(request):
    data = ShopDetail.objects.all()  # Fetch all users from the database
    user_data = []

    for user in data:
        user_data.append({
          
            'shop_name': user.shop_name,
            'lat': user.location_lat,
            'log': user.location_long,
            "icon_class":"fas fa-home",
            "description":user.description,
            
        })
    
 
    return render(request, 'medi_app/user/view_map.html', {
        'users': user_data,
    })





def view_shopkeeper(request):
     if request.method=="GET":
        #getting email fom session
      return render(request,'medi_app/user/view_shopkeeper.html')
     


def user_logout(request):
   request.session.flush() # it will kill ths session
   messages.success(request,"successfully logout ,Thank you🙏")
   return redirect("user_login")


def user_home(request):
  
    ##fetch/get the value from session
    user_email=request.session["user_key"]
    user_obj=User.objects.get(email=user_email)  # get return one object

    #select * from user where email=user_email
    #sending objecy from object from view to temphlate
  #create a dicionary and bind object with a key and send a dictionary

    user_dict={"user_info":user_obj}
    return render(request,'medi_app/user/user_home.html',user_dict)




def user_feedback(request):
  if request.method=="GET":
      user_email= request.session["user_key"]
      user_obj=User.objects.get(email=user_email)
      user_dict={"user_detail":user_obj}
      return render(request,'medi_app/user/user_feedback.html',user_dict)
  if request.method=="POST":
       user_email= request.POST["Email"]
       user_name= request.POST["name"]
       user_rating= request.POST["rating"]
       user_remark= request.POST["remark"]
       user_pic=request.POST["pic_path"]
       feedback_obj=FeedBack(Email=user_email,name=user_name,rating=user_rating,remark=user_remark,user_pic=user_pic)
       feedback_obj.save()  #it will store data into database
       messages.success(request,"Thank you for your Fedback👍")
       
  #  return render(request,'medi_app/user/user_feedback.html')
  return redirect("user_feedback")


def user_reg(request):
     if request.method=="GET":
        #getting email fom session
      return render(request,'medi_app/user/user_reg.html')
     
     if request.method=="POST":
       user_name= request.POST["name"]
       user_email= request.POST["email"]
       user_phone= request.POST["phone"]
       user_password= request.POST.get("password")
       user_pic=request.FILES.get("profile_pic")
       user_obj=User(name=user_name,email=user_email,password=user_password,phone=user_phone,pic_name=user_pic)
       user_obj.save()
       return redirect("user_login")