
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from django.core.asgi import get_asgi_application
from django.urls import path 
from chatgpt import consumers
from chatgpt.utils.config import load_config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financialWeb.settings')
load_config()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('chatgpt', consumers.chatGptConsumer.as_asgi())
            ])
        )
    )
})