import tornado.web
import product
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, product):
        self.product = product
        
    def get(self):
        title = self.get_argument('title')
        result = self.product.del_product(title)
        if result:
            self.write("Deleted product title: {0} succsessfully".format(title))
            self.set_status(200)
        else:
            self.write("product '{0}' not found".format(title))
            self.set_status(404)
