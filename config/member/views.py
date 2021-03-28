from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import *

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":

        username = request.POST.get('username', None)

        password = request.POST.get('password', None)

        re_password = request.POST.get('re_password', None)

        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력하세요!'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'

        else:
            member = Member(
                username=username,
                password=make_password(password)
            )
            member.save()
            return redirect('/')

        return render(request, 'register.html', res_data)

def login(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            request.session['user'] = loginform.user_id
            return redirect('/')
    else:
        loginform = LoginForm()

    return render(request, 'login.html', {'loginform': loginform})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

