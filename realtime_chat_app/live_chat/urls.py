from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('<str:room_name>/', views.room, name='room'), 
    path('check_room_name', views.check_room_name, name='check_room_name'), 
    path('send', views.send, name='send'),
    path('get_messages/<str:the_room_name>', views.get_messages, name='get_messages'),
]
