from django.shortcuts import render
from .models import ChatRoom, ChatMessage

# Create your views here.
def index(request):
    chatrooms = ChatRoom.objects.all()
    context= {
        'chatrooms':chatrooms,
    }
    return render(request, 'chatapp/index.html', context)

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]

    return render (request,'chatapp/room.html',{'chatroom':chatroom,"messages":messages})
