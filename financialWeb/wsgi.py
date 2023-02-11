# """
# WSGI config for financialWeb project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
# """

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financialWeb.settings')

application = get_wsgi_application()


# import os

# import django
# from channels.routing import ProtocolTypeRouter
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter,URLRouter
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter,get_default_application
# from django.urls import path 
# from finance import consumers

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financialWeb.settings')

# application = ProtocolTypeRouter({
#     "http": get_wsgi_application(),
#     'websocket':AuthMiddlewareStack(
#         URLRouter(
#             [
#                 path('chatgpt/', consumers.chatGptConsumer())
#             ]
#         )
#     )
# })