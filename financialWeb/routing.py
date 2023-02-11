

from django.urls import path 
from chatgpt import consumers


urlpatterns = [
            
    path('chatgpt', consumers.chatGptConsumer())
]
