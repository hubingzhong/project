from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from webtest.models import Webcase,Webcasestep

#用例管理
@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user','')#读取浏览器session
    return render(request,'webcase_mangege.html',{'user':username,'webcases':webcase_list})

@login_required
def webcasestep_manage(request):
    username = request.session.get('user', '')
    webcasestep_list = Webcasestep.objects.all()
    return render(request, 'webcasestep_manage.html', {'user': username, 'webcasesteps': webcasestep_list})
