from django.shortcuts import render, redirect
from urllib import request
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login,logout
from .form import LoginForm
import math,random
from django.contrib.auth.hashers import make_password

# Create your views here.
OTP_DICT = dict()

User_data = dict()



def LOGOUT(request):
    logout(request)

    return redirect('/')

def LOGIN_VIEW(request):

        form = LoginForm(request.POST or None)
        msg = None
        if request.user.is_authenticated:
            return redirect('dashboard/')
        else:
            if request.method == "POST":

                if form.is_valid():
                    username = form.cleaned_data.get("username")
                    password = form.cleaned_data.get("password")
                    print("Clean data",username," pass ",password)
                    # xx = User.objects.get(username=username)
                    # print(xx)
                    user = authenticate(username=username, password=password)

                    # property check 
                    
                    if user is not None:
                        login(request, user)
                        return redirect('dashboard/')
                    else:    
                        msg = 'Invalid credentials'   
                        return render(request, "login.html",{"msg":msg }) 
                else:
                    msg = 'Error validating the form'    
                    return render(request, "login.html",{"msg":msg} )

            if request.method == "GET":
                return render(request, "login.html",{"msg":msg} )
       


def REGISTRATION(request):

    msg=""
    if request.method == 'POST':
        USERNAME = request.POST.get("username")
        EMAIL=request.POST.get("email")
        


        sudo_rep_username = User.objects.filter(username =USERNAME)
        sudo_rep_email = User.objects.filter(email =EMAIL)
        


        if (len(sudo_rep_username) != 0 or len(sudo_rep_email) != 0  ):
           return render(request, "register.html",{"msg":"The details you entered are not uniq"}) 
        atad = {
            "USERNAME":USERNAME,
            "EMAIL":EMAIL,
           }
        
        # Email Logic
        OO = str(USERNAME[1]+EMAIL[3]+USERNAME[2]+EMAIL[2])
        request.session['asd'] = OO

        print("otp function called")
        Oj = EMAIL_VERF()
        OTP = Oj.GET_OTP()
        print(OTP)

        global OTP_DICT
        OTP_DICT[OO] = OTP
        
        global User_data
        User_data[OO] = atad

        

        status = Oj.Email_send(send_email=EMAIL,otp=OTP)
        
        if status == "Success":
            print("status",status)
            return render(request,"final_reg.html",{"msg":msg})
            # verify_otp(request)
            # return redirect('verify_otp/')
        else :
            return render(request, "register.html",{"msg":"Something went wrong"})
    

    elif request.method == 'GET':
        return render(request, "register.html")


def VERIFY_OTP(request):

    msg=""
    if request.method == 'POST':
        
        get_otp=request.POST.get("otp")
        obj = request.session['asd']
        print("obj:  ",obj)
        # obj = Email_verf()
        # gen_otp = obj.otp

        global OTP_DICT
        # print("global otp dict",OTP_DICT)

        OTP = OTP_DICT[obj]
        
        if (OTP == get_otp):
            print("verify_otp success")

            
            return render(request,'final_reg.html',{"msg":msg,"pass_pass":"pass_pass"})
        else:
            msg = "Otp was incorrect"
            return render(request,'final_reg.html',{"msg":msg,"vrf":"vrf"})
            # return render(request,'email_vrf.html',{"msg":msg})
    elif request.method == 'GET':

            return render(request,'final_reg.html',{"msg":msg,"vrf":"vrf"})    
    
def END_REGISTER(request):

    if request.method == 'POST':
        PASSWORD=request.POST.get("password1")
        Confirm_Password=request.POST.get("password2")
    
        if PASSWORD != Confirm_Password:
            msg = "The Confirm password dosen't match the password"
            return render(request,'final_reg.html',{"msg":msg,"pass_pass":"pass_pass"})

        
        # Get the data
        obj = request.session['asd']

        global User_data

        u_data = User_data[obj]  
        print("data from global dict: ", u_data)
        
        raw_data = User.objects.create_user(
        username=u_data["USERNAME"], 
        email=u_data["EMAIL"], 
        password=PASSWORD, 
        
        )
        raw_data.save()


        print(raw_data)
        if raw_data : 
            return render(request,'login.html',{"msg":"SignIn with the new Account "})

        return render(request,'final_reg.html',{"msg":msg,"pass_pass":"pass_pass","success":"success"})


class EMAIL_VERF():

    otp = str()

    def Email_send(self,send_email,otp):

        try:

  
            print('in the mail func')
            # email= request.user.email
            # print('email',send_email)

            subject= "Email Verification OTP "
            # print('subject',subject)

            message =   '''You\'re OTP for email validation at Health Sure account: 

            OTP = '''   + otp

                        
            
            # print('message',message)
            send_mail(subject, message,'2023segroup17@gmail.com' , [send_email])
            print('Mail has been sent!!')

            

            return "Success"

        except Exception as e:
            print("inside email verify Error:::: ", e)

            return "Success"

    def GET_OTP(self):
        OTP = str()
        digits = "ABCstuvwDEFGHI012345JKLMNOPQRSTUVWXYZ6789abcdefghijklmnQRSTUopqrxyz"
        for i in range(6) :
            OTP += digits[math.floor(random.random() * 10)]
            
        return OTP 
       
       

def FORGOT_PSW(request):
   
    if request.method == 'POST': 
            USERNAME = request.POST.get("username")
            EMAIL=request.POST.get("email")
        
            if User.objects.filter(username =USERNAME,email =EMAIL).exists():
                
                atad = {
                "USERNAME":USERNAME,
                "EMAIL":EMAIL,
                }
                OO1 = str(USERNAME[1]+EMAIL[3]+USERNAME[2]+EMAIL[2])
                request.session['mnc'] = OO1
                
                print("otp function call=======",OO1)
                Oj = EMAIL_VERF()
                OTP = Oj.GET_OTP()
                print(OTP)

                global OTP_DICT
                OTP_DICT[OO1] = OTP
                
                global User_data
                User_data[OO1] = atad

        

                status = Oj.Email_send(send_email=EMAIL,otp=OTP)
                print("status",status)
                if status == "Success":
                    return render(request,'reset_password.html')
                # {'otp':otp_info[EMAIL]}
                else:
                    return render(request,'forgot_password.html')
            else:
                return render(request, "forgot_password.html",{"msg":"Email or Username doesn't exist"})
    else:
        return render(request,"forgot_password.html")
        
        
        


def VERIFY_RESET_OTP(request):

    msg = " "
    if request.method == 'POST':
        
        get_otp=request.POST.get("otp")
        obj = request.session['mnc']
        print("otp function is called",request.session['mnc'])
        # print("obj:  ",obj)
        # obj = Email_verf()
        # gen_otp = obj.otp

        global OTP_DICT
        # print("global otp dict",OTP_DICT)

        OTP = OTP_DICT[obj]

        
        if (OTP == get_otp):
            print("verify_otp success")

            
            return render(request,'reset_password.html',{"msg":msg,"pass_pass":"pass_pass"})
        else:
            msg = "Otp was incorrect"
            return render(request,'reset_password.html',{"msg":msg,"vrf":"vrf"})
            # return render(request,'email_vrf.html',{"msg":msg})
    elif request.method == 'GET':
            return render(request,'reset_password.html',{"msg":msg,"vrf":"vrf"})
        
        

def RESET_PASSWORD(request):
        
            if request.method == 'POST':
                PASSWORD=request.POST.get("password1")
                Confirm_Password=request.POST.get("password2")

                if PASSWORD==Confirm_Password:
                    # global User_data
                    obj = request.session['mnc']

                    global User_data

                    u_data = User_data[obj]  
                    print("data from global dict: ", u_data)
        
                    x = u_data["EMAIL"]
                    y = u_data["USERNAME"]

                    # Password = bytes(PASSWORD,"utf-8")
                    # pwd=base64.b64encode(Password)
                    
                    pwd = make_password(PASSWORD)
                    User.objects.filter(email=x,username = y).update(password=pwd)
                    data = User.objects.get(email = x)
                   
                    
                    return render(request,'login.html',{"msg":"SignIn with the new Account ","home":data})
                else:
                    msg = "The Confirm password dosen't match the password"
                    return render(request,'reset_password.html',{"msg":msg,"pass_pass":"pass_pass"})
            else:

                return render(request,"reset_password.html",{"pass_pass":"pass_pass","success":"success"})




# 59c0fd81972f412cf1dffb3c4e6b26a40c6b0960ccfc7799f3034ba5e26cc7a3



# pbkdf2_sha256$390000$Y4CSefwU2UXjD0i0I5wqdU$8ccK47UwCH0/BaRLYhJg5K3zvoNfKyYGaZntseWpWSM=
    