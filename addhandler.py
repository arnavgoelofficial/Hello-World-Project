import tornado.web
import product
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, product):
        self.product = product
        
    def get(self):
        title = self.get_argument('Xt Pro')
        author = self.get_argument('Oneplus')
        result = self.product.add_product(title, author)
        self.write(result)
