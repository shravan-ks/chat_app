from datetime import timedelta

from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from chats.models import Chat

User = get_user_model()
def home(request):
    return render(request, 'index.html')

def chat(request):
    chats = Chat.objects.all()
    all_users = User.objects.all()
    ctx = {
        'chat': chats,
        'all_users':all_users,
    }
    if request.user.is_authenticated:
        return render(request, 'chat.html', ctx)
    else:
        return render(request, 'index.html', None)



def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        print('Our value = ', msg)
        chat_message = Chat(sender=request.user, message=msg)
        if msg != '':
            chat_message.save()
        return JsonResponse({'msg': msg,})
    else:
        return HttpResponse('Request must be POST.')


def messages(request):
    chat = Chat.objects.all()
    return render(request, 'messages.html', {'chat': chat})

