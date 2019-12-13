from django.urls import path

from chats.views import home

urlpatterns = [
    path('', home, name='home' ),
]
