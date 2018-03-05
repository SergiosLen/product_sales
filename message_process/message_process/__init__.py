from .helpers import *

from collections import deque

number_of_messages = 0
log_number=10
# deq=deque()
deq=[]
while number_of_messages< 50:
    message= Message(input().strip().lower().split(' ')).parse_message()

    deq.append(message)
    print(deq)
    number_of_messages+=1
    if number_of_messages==log_number:
        print('log',len(deq))
        log_number+=10
