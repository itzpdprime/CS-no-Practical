# Question No:1
'''
Write a program to define: -
a). Getdata(): - to input five subject marks (out of 100 ).
b). Calculate(): - to calculate percentage and Grade as per the following criteria:-
Percentage Grade
>90%        A1
75-90       A
60-75       B
45-60       C
33-45       D
<33         E
c). Display():- to display percentage and grade on screen.

'''


def Getdata():
    print("Enter the Marks out of 100 ")
    m1 = int(input("Enter Marks of subject 1: "))
    m2 = int(input("Enter Marks of subject 2: "))
    m3 = int(input("Enter Marks of subject 3: "))
    m4 = int(input("Enter Marks of subject 4: "))
    m5 = int(input("Enter Marks of subject 5: "))
    p = (m1+m2+m3+m4+m5) * 100 / 500
    result = round(p, 2)
    return result


def Calculate(result):
    if result >= 90:
        grade = 'A1'
    elif 75 <= result < 90:
        grade = 'A'
    elif 60 <= result < 75:
        grade = 'B'
    elif 45 <= result < 60:
        grade = 'C'
    elif 33 <= result < 45:
        grade = 'D'
    elif result < 33:
        grade = 'E'
    return grade


def Display():
    result = Getdata()
    grade = Calculate(result)
    print("PERCENTAGE: ", result, '%')
    print("GRADE: ", grade)


Display()
