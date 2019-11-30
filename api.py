import tornado.ioloop
import tornado.web
from product import product
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

product = product()
# This is is the main handler that class
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Microservice")

#This will fork out to the specific handlers based on the request
def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addbook", AddHandler, dict(product = product)),
        (r"/v1/delbook", DelHandler, dict(product = product)),
        (r"/v1/getbooks", GetHandler, dict(product = product)),
        ])
#This is the deamon that listens on port 8888 for http requests
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
