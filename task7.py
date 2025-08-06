'''password = input('Enter password: ')
confirm_password = input('Confirm password: ')
if confirm_password == password:
	print('password match!')
else:
	print('password does no match')

user_db = ['core', 'tk', 'mp']
user_name = input('Enter user name: ')
if user_name == user_db[0] or user_name == user_db[1] or user_name == user_db[2]:
	print('user has an account')
else:
	print('invalid user name')
'''
'''
create an login 
prompt the user to enter login or register
if login then prompt the user to enter username
	if the user name is in user_details
		prompt the user to enter password
		if password is correct like in user_details
			print login successful.
		else:
			print('Invalid password:')
	else:
		print('invalid user name')
if the user enter 

'''
user_detials = {
	'user_name':
	'balace':
	'password':
	'is_verified':
}


user_db = ['core', 'tk', 'mp']
user_name = input('Enter user name: ')
if user_name in user_db:
	print('VALID ACCOUNT!')
	password = input('Enter password: ')
	confirm_password = input('Confirm password: ')
	if confirm_password == password:
		print('LOGIN SUCCESSFUL!')
		is_verified = True
		if is_verified:
			print('ALSO A VERIFIED MEMBER!')
	else:
		print('WRONG PASSWORD!')
else:
	print('INVALID USER!')
