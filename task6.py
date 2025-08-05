'''

You try to withdraw money from a Nigerian ATM.
  The ATM has only ₦1000 notes and you have ₦10,000 in your account.
   The machine allows withdrawal only if the amount requested is less than or equal to your balance.
  The user enters the amount.
   
   Your  program  should decide:
   Whether to allow the transaction?
   Or deny it with a message: 
   “Insufficient funds or invalid amount”?

   '''
Acc_balance = 10_000
Naira_note = 1000

amount = float(input('Enter amount to withdraw:\n >>>'))

if amount <= Acc_balance:
	if amount > 0 and amount % Naira_note == 0:
		print(f'Withdrawal successful, you withdraw {amount}')
		#balance = amount -  
	else:
		print('INVALID INPUT')
else:
	print('INSUFFICIENT FUNDS')

print(f'Your balance is {Acc_balance - amount}')
