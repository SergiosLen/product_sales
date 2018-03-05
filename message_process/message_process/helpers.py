import string

class PluralFormatter(string.Formatter):
    def format_field(self, value, format_spec):
        if format_spec.startswith('plural,'):
            words = format_spec.split(',')
            if value == 1:
                return words[1]
            else:
                return words[2]
        else:
            return super().format_field(value, format_spec)
plural = PluralFormatter()
class Product:
    """ """
    def __init__(self, name, price):
        self.name = name
        self.price = price



class Sale:

    def __init__(self, product, price, number_of_sales=1):
        # if number_of_sales>1:
        self.product = plural.format(product,2)
        self.price= price
        print('Sale has been added')

class Operation:

    def __init__(self,operator, volume, product):
        self.operator=operator
        self.volume = volume
        self.product = product
        print('Operation has been added')

class Message:
    """ """
    def __init__(self,message):
        self.message = message
    def parse_message(self):
        # print(len(set(self.message).intersection(set(['add','multiply','subtract']))),set(self.message).intersection(set(['add','multiply','subtract'])))

        if len(set(self.message).intersection(set(['add','multiply','subtract']))) >0:
            return Operation(self.message[0],self.message[1],self.message[2])

        elif self.message[0].isdigit():
            return Sale(self.message[3],self.message[5],quantity=self.message[0])
        elif len(self.message) == 3 :
            return Sale(self.message[0],self.message[2])
        else:
            print('Message out of format.!')