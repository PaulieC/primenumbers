#!/usr/bin/env python

'''
    Checks if the provided input is a prime number
'''
def checkPrime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
# end checkPrime

'''
    Begin script execution
'''
# accept input from user
# Bill: added the int fucntion here.
x = int(input("What is the limit for prime number checks? :"))

# check input
if x > 2: # number is within the range of prime numbers
    list1 = []
    for i in range(2,x):
        # call prime number checker
        if checkPrime(i):
            # appends integer to end of list
            list1.append(i)
    # prints entire list
   # for item in list1:
       # print item,
    print(str(list1)[1:-1]) # condensed way to print numbers
elif x == 2: # number is the lowest prime number
    print(x)
else: # no prime numbers found within range of input
    print("No prime numbers found.\nCheck input!")
