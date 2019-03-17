"""
Ethwan service

Show lease status and current traffic on the routing interface
"""
import logging
from tornado import websocket, web, ioloop


cl = []


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


class SocketHandler(websocket.WebSocketHandler):
    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)


handlers_array = [
    (r'/', IndexHandler),
    (r'/ws', SocketHandler)]

# Static files served with tornado
for path in ['bootstrap-combined.no-icons.min.css', 'jquery.min.js']:
    handlers_array += [(r'/(' + path + ')', web.StaticFileHandler,
                       {'path': './'})]

for path in ['services.proto']:
    handlers_array += [(r'/(' + path + ')', web.StaticFileHandler,
                       {'path': '/proto/'})]

app = web.Application(handlers_array)

# Register recv callback
# stream.on_recv_stream(recv_callback_stream)
# Setup tornado webserver on :8099
app.listen(8099)
# And start the event loop
logging.info('Open a browser to http://localhost:8099')
ioloop.IOLoop.instance().start()
