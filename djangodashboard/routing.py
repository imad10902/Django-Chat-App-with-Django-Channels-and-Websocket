
from django.urls import re_path
from base import consumers

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_box_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]

