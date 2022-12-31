from django.shortcuts import render, redirect
from .models import Topic, Room, Message
from django.db.models import Q
from .forms import CreateRoom, AddMessage
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    result = ''
    if request.GET.get('query') != None:
        query = request.GET.get('query')
    else :
        query = ''
    rooms = Room.objects.filter(
        Q(topic__title__contains=query)|
        Q(name__contains=query)|
        Q(host__username__contains=query)
    )
    topics = Topic.objects.all()
    count_room = rooms.count()
    context = {
        'rooms':rooms,
        'topics':topics,
        'count_room':count_room,
    }
    return render(request, 'base/home.html', context)

def add_room(request):
    add_condition = True
    form = CreateRoom()
    if request.method == 'POST':
        #form = CreateRoom(request.POST)
        #if form.is_valid():
        #    form.save()
        topic_name = request.POST['topic']
        topic = Topic.objects.get(pk=topic_name)
        Room.objects.create(
            name=request.POST['name'],
            host = request.user,
            topic = topic,
            description = request.POST['description'],
        )
        messages.success(request, 'The room "<strong>'+str(request.POST['name'])+'</strong>" was created successfully !!!')
        return redirect('base:home')
    context = {
        'form':form,
        'add_condition':add_condition
    }
    return render(request, 'base/add_room.html', context)

def delete_room(request, id):
    room = Room.objects.get(pk=id)
    room.delete()
    return redirect('base:home')

def edit_room(request, id):
    room = Room.objects.get(pk=id)
    form = CreateRoom(instance=room)
    if request.method == 'POST':
        form = CreateRoom(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'The room "<strong>'+str(request.POST['name'])+'</strong>" was edit successfully !!!')
            return redirect('base:home')
    context = {
        'form':form,
    }
    return render(request, 'base/add_room.html', context)

def room(request, id):
    room = Room.objects.get(pk=id)
    room_messages = room.message_set.all()
    form = AddMessage()
    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            room=room,
            body = request.POST['body'],
        )
        room.participant.add(request.user)
        return redirect('base:room',room.id)
    context = {
        'room':room,
        'form':form,
        'room_messages':room_messages,
    }
    return render(request, 'base/room.html', context)


def delete_message(request, id):
    message = Message.objects.get(pk=id)
    room = message.room
    message.delete()
    return redirect('base:room', room.id)
