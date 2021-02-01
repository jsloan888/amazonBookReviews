from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request,'index.html')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)
        

def register(request):
    errors = User.objects.reg_val(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(
        ), bcrypt.gensalt()).decode()  # to encode the password from the form

        new_user = User.objects.create(
            f_name=request.POST['f_name'], l_name=request.POST['l_name'], email=request.POST['email'], password=hashed_pw)
        request.session['user_id'] = new_user.id
        return redirect('/success')


def login(request):
    errors = User.objects.log_val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return redirect('/')
    else:
        existing = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = existing.id
        return redirect('/success')


def logout(request):
    request.session.clear()
    return redirect('/')