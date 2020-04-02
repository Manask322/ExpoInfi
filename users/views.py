from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from .models import CustomUser
from game.views import home

def profile(request):
    
    all_users = CustomUser.objects.all()
    if len(all_users) == 0:
        return redirect(home)
    all_users = all_users.order_by('-high_score')
    index = 1 
    for user in all_users :
        if user.user.username == request.user.username:
            break
        index += 1

    current_user = all_users.filter(user=request.user)
    if len(current_user) == 0 :
        return redirect(home)
    return render(request,'registration/profile.html',{'rank':index,'current_user':current_user[0],'users':current_user})