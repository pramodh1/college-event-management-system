from django.shortcuts import render,redirect
from .models import contactus
from django.contrib import messages,auth
def contact(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        designation=request.POST['designation']
        subject=request.POST['subject']
        details=request.POST['details']
        contact=contactus(fullname=fullname,phonenumber=phonenumber,email=email,designation=designation,subject=subject,details=details)
        contact.save()
        messages.success(request,'message sent')
        return redirect('home')
    return render(request,'webpages/contact.html')
