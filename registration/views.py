from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
    #return render(request, 'registration/test.html')
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    return render(request, 'registration/login.html', args)

def test(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['id'] = auth.get_user(request).id
    return render(request, 'registration/test.html',args)

def check_login_password(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        login = request.POST.get('login','')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=login, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/test')
        else:
            args['login_error']="Пользователь не найден"
            return render(request, 'registration/login.html', args)
    else:
        return render(request, 'registration/login.html', args)

# Create your views here.
