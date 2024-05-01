from django.contrib import admin
from django.urls import path
from lin_lout import views
from django.urls.conf import include
import  lin_lout.views as views
# import dashboard
# from dashboard import views as asss
app_name = 'lin_lout'


urlpatterns = [
  
    path('', views.LOGIN_VIEW, name='login'),
    # path("home/",  asss.HOME, name='HOME'),
    path('register/', views.REGISTRATION, name='register'),
    path('logout/', views.LOGOUT, name='logout'),
    path('verify_otp/', views.VERIFY_OTP, name='verify_otp'),
    path('end_register/', views.END_REGISTER, name='end_register'),
    path('forgot_password/', views.FORGOT_PSW, name='for_pswd'),
    path('ver_otp/', views.VERIFY_RESET_OTP, name='Verify_OTP'),
    path('reset_password/', views.RESET_PASSWORD, name='reset_psw'),
]

