from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.db import connection
from django.contrib.auth.models import Group

def get_user_groups(user_id):
    cursor_get_group = connection.cursor()
    cursor_get_group.execute("""SELECT ag.id, ag.name FROM auth_user_groups aug 
                                JOIN auth_group ag ON ag.id = aug.group_id
                                WHERE aug.user_id = %s""", [user_id])
    groups = cursor_get_group
    return groups

def get_groups_name(group_id):
    cursor_get_group = connection.cursor()
    cursor_get_group.execute("SELECT * FROM auth_user_groups WHERE group_id = %s", [group_id])
    groups = cursor_get_group
    return groups
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
    args['groups_id'] = list(get_user_groups(args['id']))
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

def all_elective(request):
    #return render(request, 'registration/test.html')
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['id'] = auth.get_user(request).id
    args['groups_id'] = list(get_user_groups(args['id']))
    return render(request, 'registration/all_elective.html', args)
# Create your views here.
