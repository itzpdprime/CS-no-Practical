# Question 2
''' 
Write a python program to:
i. Create Generate() integer number randomly between 1 to 10 and return generated number.
ii. Define function GetNum() to get integer number and compare with returned number by Generate() function, if number matched then show “You are Won” otherwise “You are Looser”.

'''
import random as ran


def Generate():
    x = ran.randint(1, 10)
    return x


def GetNum():
    x = Generate()
    y = int(input("Enter a number between 1-10: "))
    if x == y:
        print("You are Winner!!")
    else:
        print("You are Looser!!")


GetNum()
