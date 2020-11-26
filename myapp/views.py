from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Student1
from .forms import StudentForm,MailSendingForm,ContactLoginForm
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from rest_framework import generics
from .import serializers
from django.views.generic import View
# Create your views here.

def login(request):
    # return HttpResponse("Welcome to Django....")

    name = "Divya"
    mylist1 = [1,2,3,4,5]
    return render(request,"home.html",{'name1':name,'mylist1':mylist1})

def displaydetails(request):

    details = Student.objects.all()

    return render(request,'displaydetails.html',{'details':details})

def details(request,id):
    student_detail = Student.objects.get(id=id)
    return render(request, 'displayindividualdetail.html', {'student_detail': student_detail})

def displayform(request):
   if request.method=='POST':
       form = StudentForm(request.POST,request.FILES)
       if form.is_valid():
           name = form.cleaned_data['Name']
           address = form.cleaned_data['Address']
           file = form.cleaned_data['FileUpload']
           student = Student()
           student.student_name = name
           student.student_address=address
           student.student_file = file
           student.save()
           return HttpResponse('Saved to DB..')
   else:
       form = StudentForm()
   return render(request, 'displaystdform.html', {'form': form})

def displayfiles(request):

    details = Student.objects.all()
    return render(request,'displayfiles.html',{'details':details})

def email(request):

    # send_mail('subject','Hello world','abc@gmail.com',['tomail'],fail_silently=False)
    if request.method=='POST':
        form = MailSendingForm(request.POST,request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            frommail = form.cleaned_data['frommail']
            tomail = form.cleaned_data['tomail']
            attachment = form.cleaned_data['attachment']
            email = EmailMessage(subject,message,frommail,[tomail])
            email.attach(attachment.name,attachment.read(),attachment.content_type)
            email.send()
    else:
        form = MailSendingForm()
    return render(request,'mailwithattachment.html',{'form':form})

def session1(request):
    if request.method=='POST':
        username =  request.POST.get('username')
        # print(username)
        password = request.POST.get('password')
        request.session['sessionuser']=username
        request.session['sessionpwd']=password
        # return HttpResponse("SESSION VARIABLE SET.....")
        return redirect('/getsession')


    return render(request,'sessiondemo.html')
def sessionshow(request):
    username1 =  request.session['sessionuser']
    password1 = request.session['sessionpwd']
    return render(request,'homepage.html',{'username1':username1,'password1':password1})


class ListStudent(generics.ListAPIView):
    queryset = Student1.objects.all()
    serializer_class = serializers.StudentSerializer

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student1.objects.all()
    serializer_class = serializers.StudentSerializer

class ContactView(View):

    def get(self,request):
        form  = ContactLoginForm()
        context = {'form' : form}
        return render(request,"homepage.html",context)

    def post(self,request):
        form = ContactLoginForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data['username']
            context = {"form" : username}
            return render(request,"homepage.html",context)


