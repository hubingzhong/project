from django.shortcuts import render
from set.models import Set
from django.contrib.auth.models import User
def set_manage(request):
    username = request.session.get('user', '')
    set_list = Set.objects.all()
    return render(request, "set_manage.html", {"user": username, "bugs": set_list})

def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user','')
    return render(request,'set_user.html',{'user':username,'users':user_list})
# Create your views here.
