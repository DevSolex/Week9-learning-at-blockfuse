'''
student = {
    "name": 'legolas',
    "is_registered": True,
    "has_paid": True,
    "has_internet": False
}

Only students that have registered are aligible for exam. 
any student that has not registered should denied access with the message "Access denied"

1. in as much as students have registered, if the haven't paid fees, 
the should be denied access to exam with message "pay your fees".

2. if the have paid and have internet access, message 
"Allow access", else "check your internet connection" 
'''


student = {
    "name": 'legolas',
    "is_registered": True,
    "has_paid": True,
    "has_internet": False
}

if student["is_registered"] == True:
    if student["has_paid"] == True:
        if student["has_internet"] == True:
            print("Allow access")
        else:
            print("Check your internet connection")
    else:
        print("Pay your fees")
else:
    print("access denied")
