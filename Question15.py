'''
Write a Program in Python that defines and calls the following user defined functions:
(i) ADD() – To accept and add data of an employee to a CSV file ‘record.csv’. 
    Each record consists of a list with field elements as empid, name and mobile to store employee id, employee name and employee salary respectively.
(ii) COUNTR() – To count the number of records present in the CSV file named ‘record.csv’.

'''

import csv


def ADD():
    with open("record.csv", 'a', newline='\n') as f:
        wobj = csv.writer(f)
        empid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        mobile = int(input("Enter Salary: "))
        d = [empid, name, mobile]
        wobj.writerow(d)


def COUNTR():
    with open("record.csv", 'r', newline='\n') as f:
        fr = csv.reader(f)
        print("No. of records: ", len(list(fr)))


ADD()
COUNTR()
