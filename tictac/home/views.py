from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *

def home(request):
    if request.method=="POST":
        username=request.POST.get('username')
        option=request.POST.get('option')
        room_code=request.POST.get('room_code')
        if option=='1':
            game=Game.objects.filter(room_code=room_code).first()
            if not game:
                messages.error(request, 'Room does not exist')
                return redirect('home')
            if game.is_over:
                messages.error(request, 'Game is over')
                return redirect('home')

            game.game_opponent=username
            game.save()
            return redirect(f'play/{room_code}?username={username}')
        else:
            game=Game.objects.create(room_code=room_code,game_creator=username)
            game.save()
            return redirect(f'play/{room_code}?username={username}')

    return render(request,'home/home.html')

def play(request,room_code):
    username=request.GET.get('username')
    context={
        'room_code':room_code,
        'username':username,
    }
    return render(request,'home/play.html',context)
