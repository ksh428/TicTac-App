
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('play/<room_code>',views.play,name="play"),
]
