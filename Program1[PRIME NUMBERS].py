#Kweku Agyeman Baffoe-Bonnie
#Lab 01
#9th July 2020
#Simple Program to print prime numbers give a users input
# A prime number is one that is a number that is divisible by 1 and itsef ( This means it has two and only two factors )

#This will enable the user to input a number and it wil be stored in the variable (a)
#it takes only integer inputs, Hence [int]
a = int(input("Please type in your number: "))
if a > 1:
    #For every element 
    for x in range(4,a):
        if(a%x)==0:
            print("This number is not prime")
        else:
            print("This Number is prime")
else:
    print("This is not prime")