from django.shortcuts import render,redirect
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required,user_passes_test
import os


# Create your views here.
def home(request):
    return render(request, 'index.html')

def doctorclick(request):
    return render(request, 'doctorclick.html')

def patientclick(request):
    return render(request, 'patientclick.html')

def doctor_signup(request):
        userForm=forms.DoctorUserForm()
        doctorForm=forms.DoctorForm()
        if request.method=='POST':
            userForm=forms.DoctorUserForm(request.POST)
            doctorForm=forms.DoctorForm(request.POST,request.FILES)
            if userForm.is_valid() and doctorForm.is_valid():
                user=userForm.save()
                user.save()
                emp=doctorForm.save(commit=False)
                emp.user=user
                emp=emp.save()
                my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
                my_doctor_group[0].user_set.add(user)
                messages.success(request, "Account Created Successfully.!!")
                userForm=forms.DoctorUserForm()
                doctorForm=forms.DoctorForm()
        else:
            userForm=forms.DoctorUserForm()
            doctorForm=forms.DoctorForm()
        mydict={'userForm':userForm,'doctorForm':doctorForm}
        return render(request, 'doctorsignup.html',mydict)

def patient_signup(request):
        userForm=forms.DoctorUserForm()
        doctorForm=forms.PatientForm()
        if request.method=='POST':
            userForm=forms.DoctorUserForm(request.POST)
            doctorForm=forms.PatientForm(request.POST,request.FILES)
            if userForm.is_valid() and doctorForm.is_valid():
                user=userForm.save()
                user.save()
                emp=doctorForm.save(commit=False)
                emp.user=user
                emp=emp.save()
                my_patient_group = Group.objects.get_or_create(name='PATIENT')
                my_patient_group[0].user_set.add(user)
                messages.success(request, "Account Created Successfully.!!")
                userForm=forms.DoctorUserForm()
                doctorForm=forms.PatientForm()
        else:
            userForm=forms.DoctorUserForm()
            doctorForm=forms.PatientForm()
        mydict={'userForm':userForm,'patientForm':doctorForm}
        return render(request, 'patientsignup.html',mydict)



def all_login(request):
        if request.method == "POST":
            fm=forms.LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('AfterLogin')
        else:
            fm=forms.LoginForm()
        return render(request, 'login.html', {'form': fm})

def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


def AfterLogin(request):
    if is_doctor(request.user):
        return HttpResponseRedirect('Dashboard')
    elif is_patient(request.user):
        return HttpResponseRedirect('Dashboard')

def all_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def doctor_dashboard(request):
    if request.user.is_authenticated:
        if is_doctor(request.user):
            doct = models.Doctor.objects.get(user=request.user)
        elif is_patient(request.user):
            doct = models.Patient.objects.get(user=request.user)
        context = {
            'doct': doct,
            'blog': models.Blog.objects.all().order_by('-id'),
            'img': models.BlogImages.objects.all(),
            'data':models.Doctor.objects.all()
        }
        return render(request, 'doctordashboard.html', context)
    else:
        return redirect('all_login')

def patient_dashboard(request):
    if request.user.is_authenticated:
        context = {
            'patient':models.Patient.objects.get(user_id=request.user.id),
            
        }
        return render(request,'patientdashboard.html',context)
    else:
        return redirect('all_login')


def blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            category = request.POST['category']
            summary = request.POST['summary']
            content = request.POST['content']
            is_draft = request.POST.get('draft')
            files=request.FILES.getlist('file')
            doctor = models.Doctor.objects.get(user_id=request.user.id)
            # name = doctor.get_name
            # imgpath = doctor.profile_pic.path
            if is_draft:
                reg = models.Blog(doctor=doctor.id, title=title, category=category, Summary=summary, content=content, is_draft=is_draft)
                reg.save()
                for images in files:
                    reg1=models.BlogImages(images=images,imgid=reg.id).save()
                messages.info(request, 'Your blog has been saved as a draft')
            else:
                reg = models.Blog(doctor=doctor.id,title=title,category=category,
                Summary=summary,content=content)
                reg.save()
                for images in files:
                    reg1=models.BlogImages(images=images,imgid=reg.id).save()
                messages.success(request, 'Your blog has been published')

        return render(request,'blog.html',{'doct':models.Doctor.objects.get(user=request.user)})
    else:
        return redirect('all_login')


def draft(request):
    if request.user.is_authenticated:
        context = {
            'doct':models.Doctor.objects.get(user=request.user),
            'blog':models.Blog.objects.all().order_by('-id'),
            'img':models.BlogImages.objects.all(),
        }
        return render(request,'draft.html',context)
    else:
        return redirect('all_login')


def blogdelete(request,id):
    if request.user.is_authenticated:
        blog = models.Blog.objects.get(pk=id)
        img = models.BlogImages.objects.get(imgid=blog.id)
        img.delete()
        os.remove(img.images.path)
        blog.delete()
        return redirect('draft')
    else:
        return redirect('all_login')

def postdraft(request,id):
    if request.user.is_authenticated:
        blog = models.Blog.objects.get(pk=id)
        blog.is_draft = 'No'
        blog.save()
        
        return redirect('doctor_dashboard')
        
    else:
        return redirect('all_login')
        

