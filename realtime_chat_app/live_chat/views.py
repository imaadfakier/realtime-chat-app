from django.shortcuts import render, redirect
# from .models import Room, Message
from live_chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request, room_name):
    username = request.GET.get('username')
    room = Room.objects.get(name=room_name)
    return render(request, 'room.html', {'username': username, 'room': room})


def check_room_name(request):
    room_name = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room_name).exists():
        return redirect('/{the_room_name}/?username={user}'.format(the_room_name=room_name, user=username))
    else:
        new_room_name = Room.objects.create(name=room_name)
        new_room_name.save()
        return redirect(f'/{room_name}/?username={username}')


def send(request):
    room_id = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']
    new_message = Message.objects.create(message_content=message, sent_by_user=username, from_which_room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully!')


def get_messages(request, the_room_name):
    room = Room.objects.get(name=the_room_name)
    all_messages = Message.objects.filter(from_which_room=room.id)
    return JsonResponse({'all_messages_list': list(all_messages.values())})