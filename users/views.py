from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from .models import CustomUser
from game.views import home

def profile(request):
    current_user = CustomUser.objects.filter(user__username=request.user).order_by('-high_score')
    if len(current_user) == 0 :
        return redirect(home)
    current_user = current_user[0]
    return render(request,'registration/profile.html',{'current_user':current_user})