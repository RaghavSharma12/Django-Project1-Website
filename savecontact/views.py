from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from savecontact.models import contactsave
from django.contrib import messages


# Create your views here.
def home(request):
    messages.success(request,"this is a test message")
    return render(request,'webpage.html')

    
    # return HttpResponse("this is homepage")
def webpage(request):
    return render(request,'webpage.html')
    # context={
    #     'var':"this is the value of variable x"
    # }
# def home(request):
#     return render(request,'webpage.html',context)
def about(request):
    return render(request,'about.html')
    
    # return HttpResponse("this is about page")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message1=request.POST.get('message1')
        message2=request.POST.get('message2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        contact1=contactsave(name=name,email=email,message1=message1,message2=message2,city=city,state=state,zip=zip,date=datetime.today())
        contact1.save()
        messages.success(request, 'Your Message Successfully Sent!..')
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")   
    # ,message2=message2,city=city,state=state,zip=zip,date=datetime.today()