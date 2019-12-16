from django.urls import path
from chats import views
from chats.views import home, chat, post, messages

urlpatterns = [
    # Home  Url
    path('', home, name='index'),
    # Chat Room Url
    path('chat/', views.chat, name='home'),
    # message POST URL
    path('chat/post/', views.post, name='post'),
    # message GET URL
    path('messages/', views.messages, name='messages'),
    # GET Online User URL
    path('users/', views.users, name='users'),
]
