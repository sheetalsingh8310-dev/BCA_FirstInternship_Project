from django.shortcuts import render,HttpResponse,redirect
from .models import shopowner,ShopDetail,MedicineRequest
from django.contrib import messages

def owner_edit_profile(request):
    if request.method=="GET":
     owner_email=request.session["owner_key"]
     owner_obj=shopowner.objects.get(email=owner_email)  # get return one object
     owner_dict={"owner_info":owner_obj}
     return render(request,'medi_app/shopowner/owner_edit_profile.html', owner_dict)
    if request.method=="POST":
       profile_pic=request.FILES.get("pic")
       owner_phone=request.POST['phone']
       owner_name=request.POST['name']
       owner_email=request.session["owner_key"]
       owner_obj=shopowner.objects.get(email=owner_email) 
       if profile_pic is not  None:
          owner_obj.pic_name=profile_pic
          owner_obj.name=owner_name
          
          owner_obj.phone=owner_phone
          owner_obj.save()
          messages.success(request,"profile update successfully")
          return redirect(owner_home)

       



def view_medicine(request):
    if request.method=="GET":
       
       medicine_list=MedicineRequest.objects.filter(medicine_status="REQUESTED")
       medicine_dict={"medicine_detail":medicine_list}
        #getting email fom session

       return render(request,'medi_app/shopowner/view_medicine.html',medicine_dict)



def map_location(request):
     if request.method=="GET":
       return render(request,'medi_app/shopowner/map_location.html')
     if request.method=="POST":
      owner_email=request.session["owner_key"]
      owner_obj =shopowner.objects.get(email=owner_email)
      print(owner_obj)
      longitude=request.POST["longitude"]
      latitude=request.POST["lat"]
      print(longitude)
      print(latitude)
      shop_detail_obj= ShopDetail.objects.get(owner=owner_obj)

      shop_detail_obj.location_lat=latitude
      shop_detail_obj.location_long=longitude  ##### saved like this to know that the longitude and latitude is of a particular owner
      shop_detail_obj.save()
      owner_dict={"owner_info": owner_obj}
      return render(request,'medi_app/shopowner/owner_home.html',owner_dict)
    




     

     return render(request,'medi_app/shopowner/owner_home.html',owner_dict)



      

def shop_detail(request):
      if request.method=="GET":
       return render(request,'medi_app/shopowner/shop_detail.html')
      if request.method=="POST":
       email=request.session["owner_key"]
       owner_obj=shopowner.objects.get(email=email)
       temp_shop_details = ShopDetail.objects.filter(owner=owner_obj)
       if len(temp_shop_details)>0:
          messages.error(request,"you are already add a shop with this account please use another account to add other shops.")
          return redirect("shop_detail")
       shop_obj= request.POST["shop_name"]
       gst_obj= request.POST["gst_number"]
       description_obj= request.POST["description"]
       phone_no = request.POST["phone_no"]
       city= request.POST["city"]
      address= request.POST["address"]
      shop_obj=ShopDetail(owner=owner_obj, shop_name=shop_obj,gst_number=gst_obj,description=description_obj,phone_no=phone_no,city=city, address =address)
      shop_obj.save()
      return redirect("owner_home")

      



def owner_logout(request):
   request.session.flush() # it will kill ths session
   messages.success(request,"successfully logout ,Thank you🙏")
   return redirect("owner_login")

def owner_home(request):
  
    ##fetch/get the value from session
    owner_email=request.session["owner_key"]
    owner_obj=shopowner.objects.get(email=owner_email)  # get return one object

    #select * from user where email=user_email
    #sending objecy from object from view to temphlate
  #create a dicionary and bind object with a key and send a dictionary
    owner_dict={"owner_info":owner_obj}

    return render(request,'medi_app/shopowner/owner_home.html',owner_dict)



def owner_login(request):
      if request.method=="GET":
       return render(request,'medi_app/shopowner/owner_login.html')
      if request.method=="POST":
        owner_email=request.POST["email"]
        owner_pass=request.POST["password"]
        ownerList=shopowner.objects.filter(email=owner_email,password=owner_pass)

      if len(ownerList)>0:
          #  user_object=userList[0]
           request.session["owner_key"]=owner_email

          #  request.session["user_role"]="user"
           return redirect("owner_home")
      else:
           messages.error(request,"Invalid credentials 🤦‍♀️")
           return redirect("owner_login")



def owner_feedback(request):
      return render(request,'medi_app/shopowner/owner_feedback.html')

def owner_reg(request):
      if request.method=="GET":
        return render(request,'medi_app/shopowner/owner_reg.html')
     
      if request.method=="POST":
       owner_name= request.POST["name"]
       owner_email= request.POST["email"]
       owner_phone= request.POST["phone"]
       owner_password= request.POST["password"]
       owner_pic=request.FILES.get("profile_pic")

       user_obj=shopowner(name=owner_name,email=owner_email,password=owner_password,phone=owner_phone,pic_name=owner_pic)
       user_obj.save()
      
       return redirect("owner_login")