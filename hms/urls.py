from django.urls import path
from hms import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('Doctor',views.doctorclick,name='doctorclick'),
    path('Doctor-SignUp',views.doctor_signup,name='doctorsignup'),
    path('Doctor-login',views.all_login,name='all_login'),
    path("AfterLogin", views.AfterLogin,name='AfterLogin'),
    path("Dashboard", views.doctor_dashboard,name='doctor_dashboard'),
    path("patientclick", views.patientclick,name='patientclick'),
    path("Patient-SignUp", views.patient_signup,name='patient_signup'),
    path("patient_dashboard", views.patient_dashboard,name='patient_dashboard'),
    path("all_logout", views.all_logout,name='all_logout'),
    path("blog", views.blog,name='blog'),
    path("draft", views.draft,name='draft'),
    path("blogdelete/<int:id>", views.blogdelete,name='blogdelete'),
    path("postdraft/<int:id>/", views.postdraft,name='postdraft'),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
