'''
SMARTPHONE PURCHASE:

Ask user to input budget

1. Check if the budget is atleast $500, if it is, check if the budget is $1000 or more. 
then recommend 'Google pixel 9pro', otherwise, recommend 'Iphone'

2. If budget is below $500, if it is, and atleast $200. then recommend 'Redmi' otherwise, recommend 'Save more'

'''

budget = float(input('Enter your budget: '))

if budget >= 500:
    if budget >= 1000:
        print("You can get an Google Pixel 9pro.")
else:
    if budget >= 200:
        print('You can get a Redmi.')
    else:
        print('Save more.')
