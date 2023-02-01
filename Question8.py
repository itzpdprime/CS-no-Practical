# Please first create a database SCHOOL in mysql and you don't need to create any tables just the database

import mysql.connector as msc
mydb = msc.connect(
    host='localhost',
    user='root',
    passwd='',
    database='SCHOOL')
mycur = mydb.cursor()


def menu():

    while True:
        print("-"*17)
        print("1.Add Record.")
        print("2.Display.")
        print("3.Update.")
        print("4.Remove.")
        print("5.Search.")
        print("0.EXIT")
        print("-"*17)
        o = int(input("Enter your Choice: "))
        if o == 1:
            add()
        elif o == 2:
            display()
        elif o == 3:
            update()
        elif o == 4:
            remove()
        elif o == 5:
            search()
        else:
            print("THANKS FOR USING..........")
            mydb.close()
            break


def add():
    mycur.execute(
        "CREATE TABLE IF NOT EXISTS EMPLOYEE(EMP_ID INT PRIMARY KEY, EMP_NAME VARCHAR(30), DEPT_ID INT, SALARY FLOAT, BONUS FLOAT)")
    empid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    did = int(input("Enter Dept_id: "))
    sal = float(input("Enter Salary: "))
    bon = float(input("Enter Bonus: "))
    query = 'INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s)'
    vl = (empid, ename, did, sal, bon)
    mycur.execute(query, vl)
    mydb.commit()


def display():
    mycur.execute('SELECT * FROM EMPLOYEE')
    d = mycur.fetchall()
    t = "| {:<7} | {:<30} | {:<7} | {:<8} | {:<6} |".format(
        "EMP_ID", "EMP_NAME", "DEPT_ID", "SALARY", "BONUS")
    print('-'*len(t))
    print(t)

    print('-'*len(t))
    for i in d:
        print("| {:<7d} | {:<30} | {:<7d} | {:<8} | {:<6} |".format(
            i[0], i[1], i[2], i[3], i[4]))
        print('-'*len(t))


def update():
    eid = int(input("Enter Employee id to update: "))
    mycur.execute('SELECT EMP_ID FROM EMPLOYEE')
    ds = mycur.fetchall()
    eids = [x for i in ds for x in i]
    if eid in eids:
        print("Enter the new details.....")
        ename = input("Enter Name: ")
        dpd = int(input("Enter Dept_id: "))
        sal = float(input("Enter Salary: "))
        bo = float(input("Enter Bonus: "))
        query = (
            "UPDATE EMPLOYEE SET EMP_NAME = %s, DEPT_ID = %s, SALARY = %s, BONUS = %s WHERE EMP_ID = %s ")
        val = (ename, dpd, sal, bo, eid)
        mycur.execute(query, val)
        mydb.commit()
        display()
        print("Details Updated!!")
    else:
        print("EMPLOYEE NOT FOUND!!")


def remove():
    eid = int(input("Enter Employee id to remove: "))
    mycur.execute('SELECT EMP_ID FROM EMPLOYEE')
    ds = mycur.fetchall()
    eids = [x for i in ds for x in i]
    if eid in eids:
        query = ("DELETE FROM EMPLOYEE WHERE EMP_ID = {}".format(eid))
        mycur.execute(query)
        display()
        mydb.commit()
    else:
        print("EMPLOYEE NOT FOUND!!")


def search():
    ename = input("Enter Employee Name to search: ")
    mycur.execute('SELECT EMP_NAME FROM EMPLOYEE')
    ds = mycur.fetchall()
    ens = [x for i in ds for x in i]
    if ename in ens:
        query = ("SELECT * FROM EMPLOYEE WHERE EMP_NAME = '{}'".format(ename))
        mycur.execute(query)
        d = mycur.fetchall()
        t = "| {:<7} | {:<30} | {:<7} | {:<8} | {:<6} |".format(
            "EMP_ID", "EMP_NAME", "DEPT_ID", "SALARY", "BONUS")
        print(t)
        print('-'*len(t))
        for i in d:
            print("| {:<7d} | {:<30} | {:<7d} | {:<8} | {:<6} |".format(
                i[0], i[1], i[2], i[3], i[4]))
            print('-'*len(t))

        mydb.commit()
    else:
        print("EMPLOYEE NOT FOUND!!")


menu()
