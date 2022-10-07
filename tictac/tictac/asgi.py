from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

import os

from django.core.asgi import get_asgi_application
from home.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tictac.settings')

application = get_asgi_application()

ws_pattern = [
    path('ws/game/<room_code>',GameConsumer)
]

application = ProtocolTypeRouter({
    "websocket" : AuthMiddlewareStack(URLRouter(
        ws_pattern
    ))
})