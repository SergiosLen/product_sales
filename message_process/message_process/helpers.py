import string
from collections import Counter
import inflect
 
singular= inflect.engine()
class Product:
    """ """
    def __init__(self, name, price):
        self.name = name
        self.price = int(price.replace('p',''))
    # def get_name(self):
    #     return self.name
    # def get_value(self):
    #     return self.price
    def subtract_to_price(self, ammount=0):
        self.price -=ammount
    def add_to_price(self,ammount=0):
        self.price += ammount

    def multiply_to_price(self, ammount=1):
        self.price *=ammount
    



class Sale:

    def __init__(self, product, price, number_of_sales=1):
        # if number_of_sales>1:
        self.product = product #singular.singular_noun(product,2)
        self.price= int(price.replace('p',''))
        self.number_of_sales=number_of_sales
        # print('Sale has been added')
    def get_report(self):
        # print(self.number_of_sales,singular.plural('Sale', self.number_of_sales), self.product.name, self.price) 
        return '%i %s of %s with price %i ' %(self.number_of_sales,singular.plural('Sale', self.number_of_sales), self.product.name, self.price)
    

class Operation:

    def __init__(self,operator, volume, product):
        self.volume = volume
        self.product = product
        self.operator=operator
        if operator =='add':

            self.product.add_to_price(volume)
        elif operator=='subtract':
            self.product.subtract_to_price(volume)
        elif operator=='multiply':
            self.product.multiply_to_price(volume)
        else:
            raise ValueError()

    def get_report(self):
        return 'Operation %s for product %s final price %i ' %(self.operator,self.product.name, self.product.price)

class Messages:
    """ """
    def __init__(self):
        # self.message = message
        self.products={}
        self.messages=[]
        self.sales={}
        self.adjustments={}


    def parse_message(self,message):

        if len(set(message).intersection(set(['add','multiply','subtract']))) >0:
            product_name=singular.plural(message[2],2)
            if not product_name in self.products:
                raise ValueError('Product not defined')
            product=self.products[product_name]
            operation=Operation(message[0],int(message[1].replace('p','')),product)
            self.adjustments[product_name].append(operation)
            # self.sales[product_name]+=1
            return operation.get_report()

        elif message[0].isdigit():

            product_name=singular.plural(message[3],2)
            if not product_name in self.products:
                self.products[product_name]=Product(product_name,message[5])
                self.sales[product_name]={'sale':0,'value':0}
                self.adjustments[product_name]=[]
            product=self.products[product_name]
            self.sales[product_name]['sale']+=int(message[0])
            self.sales[product_name]['value']+=int(message[0])*product.price
            return Sale(product,message[5],number_of_sales=int(message[0])).get_report()
        elif len(message) == 3 :
            product_name=message[0]#singular.plural(message[0],2)
            if not product_name in self.products:
                self.products[product_name]=Product(product_name,message[2])
                self.sales[product_name]={'sale':0,'value':0}
                self.adjustments[product_name]=[]
            product=self.products[product_name]
            self.sales[product_name]['sale']+=1
            self.sales[product_name]['value']+=product.price
            product=self.products[product_name]
            # self.sales[product_name]+=1
            return Sale(product,message[2]).get_report()
        else:
            return 'Message out of format.!'

        self.messages.append(message)



