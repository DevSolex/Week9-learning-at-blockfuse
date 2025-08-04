score = float(input('Enter a number to have a grade: \n >>>'))

if score >= 70 and score <= 100:
    print('Grade is A')
elif score >= 50 and score <= 69.9:
    print('Grade is B')
elif score >= 40 and score <= 49.9:
    print('Grade is C')
elif score >= 30 and score <= 39.9:
    print('Grade is D')
elif score >= 0 and score < 30:
    print('Grade is F')
else:
    print('INVALID SCORE')



#if 70 >= score <= 100
