from django.shortcuts import render, redirect
from .models import User, Products
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def homeView(request):
    return render(request,'home.html')

def registration(request):
    if request.method == 'POST':
        accountType = request.POST.get('account-type')
        email = request.POST.get('email')
        psw = request.POST.get('psw')

        isuser = User.objects.filter(email=email).exists()

        if isuser:
            return render(request, 'registration.html',{'message':'User Already Registered'})
        else:
            data = User(
                account_type=accountType,
                email = email,
                username=email,
            )
            data.set_password(psw)
            data.save()

            return render(request, 'registration.html',{'message':'your account has been successfuly created'})
    else:
        return render(request,'registration.html')


def loginView(request):
    if request.method == "POST":
        accountType = request.POST.get('account-type')
        email = request.POST.get('email')
        psw = request.POST.get('psw')

        if accountType == 'buyer':
            user = authenticate(email=email,password=psw)
            if user is not None:
                login(request,user)
                return redirect('buyer-dashboard')
            else:
                return render(request,'login.html',{'message':'Login Details are Invalid'})
        else:
            user = authenticate(email=email, password=psw)
            if user is not None:
                login(request, user)
                return redirect('seller-dashboard')
            else:
                return render(request,'login.html',{'message':'Login Details are Invalid'})

    return render(request,'login.html')


def logoutView(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def buyerDashboard(request):
    return render(request,'buyer-dashboard.html',)

@login_required(login_url='/login')
def sellerDashboard(request):
    return render(request,'seller-dashboard.html')