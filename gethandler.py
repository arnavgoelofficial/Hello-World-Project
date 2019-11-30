import tornado.web
import product
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, product):
        self.product = product
        
    def get(self):
        self.write(self.product.json_list())
