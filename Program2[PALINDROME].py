#Kweku Agyeman Baffoe-Bonnie
#Lab 01
#9th July 2020
#This program checks if a sequence is aplindrome
# A palindrome is a sequence of numbers that can be read the same way front to backa and back reverse.

#a take is the user sequence
a = input("Please type in your sequence: ")
#b will reprent the reversed copy into the variable b
#::-1 helps to repren reversed copy
b = a[::-1]
if a==b:
    print("This is a palindrome")
else:
    print("This is not a palindrome")