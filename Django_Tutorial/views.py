#from django.http import HttpResponse
#
#def welcome(request):
#    return HttpResponse("Hello, World!")

from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    return render(request, 'welcome.html')