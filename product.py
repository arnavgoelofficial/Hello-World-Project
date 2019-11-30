import json



class product:

    def __init__(self):
        self.product = []

    def add_product(self, title, author):
        new_product = {}
        new_product["Title"] = title
        new_product["Author"] = author
        self.product.append(new_product)
        print("Product: {0}".format(new_product))
        return json.dumps(new_product)

    def del_product(self, title):
        found = False
        for idx, product in enumerate(self.product):
            if product["Title"] == title:
                index = idx
                found = True
                del self.product[idx]
        print("product: {0}".format(json.dumps(self.product)))
        return found

    def get_all_product(self):
        return self.product

    def json_list(self):
        return json.dumps(self.product)
