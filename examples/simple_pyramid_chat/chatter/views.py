import logging

log = logging.getLogger(__name__)

from socketio.decorators import namespace


def index(request):
    """ Base view to load our template """
    return {}


@namespace('')
class ChatNamespace(object):
    # This example will not work well with multiple workers
    clients = {}

    @classmethod
    def on_connect(cls, socket):
        log.debug('on connect')
        if socket.id not in cls.clients:
            cls.clients[socket.id] = socket

    @classmethod
    def on_disconnect(cls, socket):
        cls.clients.pop(socket.id, None)

    @classmethod
    def on_message(cls, socket, message):
        log.debug('received new message: "{0}"'.format(message))
        for socket_id, s in cls.clients.items():
            s.emit('message', message)


from pyramid.response import Response


def socketio(request):
    log.debug("...Entering socketio view...")
    try:
        socket = request.environ.get('engine_socket', None)
        log.debug("[SocketIOView] Got engine_socket %s" % socket)
        if socket is not None:
            log.debug("[SocketIOView] Set request to context")
            socket.context['request'] = request
    except Exception:
        log.error("[SocketIOView] Exception while handling socketio connection", exc_info=True)

    return Response('')
