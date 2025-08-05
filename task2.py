"""
Task 2: Smart Restaurant Discount System

You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:
1. Customers with a loyalty card get a 10% discount.
2. If the customer's order amount is above 20,000 NGN:
    - Loyalty card holders get an additional 5% discount.
    - Non-loyalty card holders get a free soft drink instead.
3. Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.

Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:
1. Calculates the final discount or freebie for the customer.
2. Stores the result in a dictionary called order_summary.
3. Prints out a summary for the cashier.
"""



customer = {
'name': 'Godiya',
'order_amount': 25000,
'loyalty_card': True,
'is_student': False
}

discount_percentage = 0

if customer["loyalty_card"]:
    discount_percentage += customer["order_amount"] // 100 * 10
    if customer["order_amount"] > 20000:
        if customer["loyalty_card"]:
            discount_percentage += customer["order_amount"] // 100 * 5
        else:
            print('Free drink for you')
    elif customer['is_student']:
        discount_percentage += customer["order_amount"] // 100 * 5

final = customer['order_amount'] - discount_percentage

order_summary = {
	"order_amount": customer['order_amount'],
	'Discount_percentage': discount_percentage,
	'amount_to_pay': final
	}

print(order_summary)
