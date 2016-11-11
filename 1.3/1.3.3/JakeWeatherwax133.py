from __future__ import print_function 

def age_limit_output(age):
    AGE_LIMIT = 13
    if age < AGE_LIMIT:
        print(age,'is below the age limit')
    else:
        print(age, 'is old enough')
    print(' Minimum age is ' , AGE_LIMIT)

def report_grade(percent):
    PERCENT_LIMIT = 80