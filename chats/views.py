from datetime import timedelta

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from online_users.models import OnlineUserActivity

from chats.models import Chat

def home(request):
    return render(request, 'index.html')

from datetime import timedelta
def chat(request):
    chats = Chat.objects.all()
    ctx = {
        'chat': chats
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

