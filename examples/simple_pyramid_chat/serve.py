from socketio.server import SocketIOWSGIServer
from pyramid.paster import get_app

from gevent import monkey
monkey.patch_all()

if __name__ == '__main__':
    app = get_app('development.ini')
    SocketIOWSGIServer(('0.0.0.0', 6543), app).serve_forever()
