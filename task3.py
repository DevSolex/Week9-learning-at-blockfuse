'''
MOVIE TICKET DISCOUNT:

you are building a movie ticketing system.

Instruction: ask user for their age:
1. person 18 or older can buy a ticket.
output 'can buy a ticket'

2. if the are 60 or older, they get 'senior discount':
output: 'senior discount'

3. if the are lessthan 18 and 12 or older, the can buy teen ticket.
output: 'teen ticket' 

Otherwise, the can buy 'kids ticket'

'''




Input = int(input('enter your age: '))

if Input >= 18:
    print('Can buy a ticket')
    if Input >= 60:
        print('Senior discount')
else:
    if Input < 18 and Input >= 12:
        print('Teen ticket')
    else:
        print('Kid ticket')



