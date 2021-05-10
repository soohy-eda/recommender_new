from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import *

def register(request):
    genres = ["발라드", "댄스", "R&B/Soul", "성인가요", "록/메탈",
              "인디", "포크/블루스", "EDM", "랩/힙합"]

    if request.method == "GET":
        return render(request, 'register.html',{'genres':genres})

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        pregenre1 = request.POST.get('pregenre1', None)
        pregenre2 = request.POST.get('pregenre2', None)
        pregenre3 = request.POST.get('pregenre3', None)

        res_data = {}
        if not (username and password and re_password and pregenre1 and pregenre2 and pregenre3):
            res_data['error'] = '모든 값을 입력하세요!'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'

        #elif (pregenre1 == pregenre2 or pregenre1 == pregenre3 or pregenre2 == pregenre3):
           # res_data['error'] = '동일한 선호장르가 존재합니다!'

        else:
            member = Member(
                username=username,
                password=make_password(password),
                pregenre1=pregenre1,
                pregenre2=pregenre2,
                pregenre3=pregenre3
            )
            member.save()
            return redirect('/')

        return render(request, 'register.html', res_data, {'genres':genres})

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

def pregenre(request):
    genres = ["발라드", "댄스", "R&B/Soul", "성인가요", "록/메탈",
            "인디", "포크/블루스", "EDM", "랩/힙합"]
    user_id = request.session.get('user')
    if not user_id:
        return redirect('/member/login/')
    member = Member.objects.get(pk=user_id)
    if request.method == 'GET':
        context = {}
        context = {
            'genres':genres,
            'member':member
        }
        return render(request, 'pregenre.html', context)

    elif request.method == 'POST':
        pregenre1 = request.POST.get('pregenre1', None)
        pregenre2 = request.POST.get('pregenre2', None)
        pregenre3 = request.POST.get('pregenre3', None)
        print(pregenre1, pregenre2, pregenre3)

        member.pregenre1 = pregenre1
        member.pregenre2 = pregenre2
        member.pregenre3 = pregenre3
        member.id = member.id
        member.save()
        return redirect('/')













