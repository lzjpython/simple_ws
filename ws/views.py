# Create your views here.
from django.views.generic.base import TemplateView

from ws.connection import WebSocket, wsm


class IndexView(TemplateView):
    template_name = "index.html"


async def websocket_view(socket: WebSocket):
    await socket.accept()

    wsid = wsm.add_websocket(socket)
    print(f'接受连接，目前长度{wsm.length}')
    try:
        while True:
            message = await socket.receive_text()
            await socket.send_text(message)
    except (RuntimeError, AssertionError):
        wsm.remove_websocket(wsid)
        print(f'断开连接，目前长度{wsm.length}')
