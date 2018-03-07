from .helpers import *
import os
from collections import deque

def start_testing():
    number_of_messages = 0

    log_number=10
    deq=[]
    messages=Messages()
    fops=open('message_process/tests/messages.txt')
    fop=open(os.path.join('message_process','log','log.txt'),'w')
    for message_string in fops:
        fop.write(messages.parse_message(message_string.strip().lower().split(' ')) + "\n")#.get_report()
        # messages.parse_message(message_string.strip().lower().split(' '))
        # print(message_string)
        number_of_messages+=1
        if number_of_messages==log_number:
            print('============')
            print('Sales until now %i messages' %number_of_messages)
            get_log(messages)
            print('++++++++++++')
            log_number+=10

    fop.close()
    print('Pausing')
    get_adjustments(messages)
    print('**********FINISH***********')

def start_recording():
    number_of_messages = 0

    log_number=10
    deq=[]
    messages=Messages()
    fop=open(os.path.join('message_process','log','log.txt'),'w')
    while number_of_messages< 50:
        fop.write(messages.parse_message(message_string.strip().lower().split(' ')) + "\n")#.get_report()
        number_of_messages+=1
        if number_of_messages==log_number:
            print('============')
            print('Sales until now %i messages' %number_of_messages)
            get_log(messages)
            print('++++++++++++')
            log_number+=10

    fop.close()
    print('Pausing')
    get_adjustments(messages)
    print('**********FINISH***********')

def get_log(messages):
    for k,v in messages.sales.items():

        print('%i Sales of %s with total value %i' %(v['sale'],k,v['value']))
def get_adjustments(messages):
    for k,vv in messages.adjustments.items():
        for v in vv:
            print('Product %s got %s by %i in value' %(k,v.operator,v.volume))

if __name__ == '__main__':
    start_recording()
    # start_testing()
