from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Apitest,Apistep,Apis
def test(request):
    return HttpResponse('hello test')


def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        #  return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password error'})

    return render(request, 'login.html')


def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()#读取所有的流程接口
    username = request.session.get('user','')#读取浏览器登录session
    #定义流程接口数据的变量并返回前端
    return render(request,'apitest_manage.html',{'user':username,'apitests':apitest_list})

@login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apistep_list = Apistep.objects.all()
    return render(request,'apistep_manage.html',{'user':username,"apisteps":apistep_list})

@login_required
def apis_manage(request):
    username = request.session.get('user','')
    apis_list = Apis.objects.all()
    return render(request,'apis_manage.html',{'user':username,"apiss":apis_list})




