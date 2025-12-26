from django.shortcuts import render,HttpResponse,redirect
from .models import FeedBack
from django.contrib import messages

def all_feedback(request):
 ### select * from feedback
 feedback_list= FeedBack.objects.all()
 feedback_dict={
   "feedback_key":feedback_list
     

  }
 return render(request,"medi_app/html/all_feedbacks.html",feedback_dict)

def home(request):
    return render(request,"medi_app/html/index.html")

def about(request):
    return render(request,"medi_app/html/about.html")
def contact(request):
    return render(request,"medi_app/html/contact.html")
def all_feedbacks(request):
    return render(request,"medi_app/html/all_feedbacks.html")
def testing(request):
    return render(request,"medi_app/html/testing.html")
def password_reset(request):
    return render(request,"medi_app/html/password_reset_form.html")

