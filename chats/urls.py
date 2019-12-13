from django.conf.urls import url
from django.conf.urls import url
from django.urls import path

from chats import views
from chats.views import home, chat, post, messages

urlpatterns = [
    path('', home, name='index'),
    path('chat/', views.chat, name='home'),
    path('chat/post/', views.post, name='post'),
    path('messages/', views.messages, name='messages'),
]
