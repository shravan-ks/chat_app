from datetime import timedelta
import online_users.models
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from chats.models import Chat

# To Get user DB
User = get_user_model()

# Home Page
def home(request):
    return render(request, 'index.html')


# Chat Room Page
def chat(request):
    chats = Chat.objects.all()
    ctx = {
        'chat': chats,
    }
    if request.user.is_authenticated:
        return render(request, 'chat.html', ctx)
    else:
        return render(request, 'index.html', None)


# Message POST Function
def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        print('Our value = ', msg)
        chat_message = Chat(sender=request.user, message=msg)
        if msg != '':
            chat_message.save()
        return JsonResponse({'msg': msg, })
    else:
        return HttpResponse('Request must be POST.')


# Message GET
def messages(request):
    chat = Chat.objects.all()
    return render(request, 'messages.html', {'chat': chat})


# Online User GET
def users(request):
    all_users = User.objects.all()
    user_status = online_users.models.OnlineUserActivity.get_user_activities(timedelta(seconds=5))
    users = (user for user in user_status)
    print('user')
    return render(request, 'users.html', {'users': users, 'all_users': all_users})
