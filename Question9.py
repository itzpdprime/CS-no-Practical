# Please first create a database BILL in mysql and you don't need to create any tables just the database


'''
Write a Python-MySQL Connectivity code to perform the following operation with “Bill” Database Inventory Table.
Operations:
    1. Make Entry of New Goods [ItemNo, Iname, Price, Quantity, Make]
    2. Print Status of Stock
    3. Modify Regular Selling Item Stock.
    4. Search Item with Name of Item.
'''

import mysql.connector as msc
mydb = msc.connect(
    host='localhost',
    user='root',
    passwd='',
    database='BILL')
mycur = mydb.cursor()


def menu():

    while True:
        print("-"*17)
        print("1.New Entry.")
        print("2.Display.")
        print("3.Update.")
        print("4.Search.")
        print("0.EXIT")
        print("-"*17)
        o = int(input("Enter your Choice: "))
        if o == 1:
            NEntry()
        elif o == 2:
            display()
        elif o == 3:
            update()
        elif o == 4:
            search()
        else:
            print("THANKS FOR USING..........")
            mydb.close()
            break

#[ItemNo, Iname, Price, Quantity, Make]


def NEntry():
    mycur.execute(
        "CREATE TABLE IF NOT EXISTS INVENTORY (ITEMNO INT PRIMARY KEY, INAME VARCHAR(20), PRICE FLOAT, QUANTITY INT, MAKE FLOAT)")
    itno = int(input("Enter Item No: "))
    inm = input("Enter Item Name: ")
    pric = float(input("Enter Price: "))
    qt = int(input("Enter Quantity: "))
    mke = float(input("Enter Make: "))
    query = 'INSERT INTO INVENTORY VALUES(%s,%s,%s,%s,%s)'
    vl = (itno, inm, pric, qt, mke)
    mycur.execute(query, vl)
    mydb.commit()


def display():
    mycur.execute('SELECT * FROM INVENTORY')
    d = mycur.fetchall()
    t = "| {:<7} | {:<20} | {:<7} | {:<8} | {:<6} |".format(
        "ITEMNO", "INAME", "PRICE", "QUANTITY", "MAKE")
    print('-'*len(t))
    print(t)

    print('-'*len(t))
    for i in d:
        print("| {:<7d} | {:<20} | {:<7} | {:<8d} | {:<6} |".format(
            i[0], i[1], i[2], i[3], i[4]))
        print('-'*len(t))


def update():
    itn = int(input("Enter ItemNo to update: "))
    mycur.execute('SELECT ITEMNO FROM INVENTORY')
    ds = mycur.fetchall()
    itns = [x for i in ds for x in i]
    if itn in itns:
        print("Enter the new details.....")
        inm = input("Enter IName: ")
        prc = float(input("Enter Price: "))
        qt = int(input("Enter Quantity: "))
        mk = float(input("Enter Make: "))
        query = (
            "UPDATE INVENTORY SET INAME = %s, PRICE = %s, QUANTITY = %s, MAKE = %s WHERE ITEMNO = %s ")
        val = (inm, prc, qt, mk, itn)
        mycur.execute(query, val)
        mydb.commit()
        display()
        print("Details Updated!!")
    else:
        print("ITEM NOT FOUND!!")


def search():
    inm = input("Enter INVENTORY Name to search: ")
    mycur.execute('SELECT INAME FROM INVENTORY')
    ds = mycur.fetchall()
    inms = [x for i in ds for x in i]
    if inm in inms:
        query = ("SELECT * FROM INVENTORY WHERE INAME = '{}'".format(inm))
        mycur.execute(query)
        d = mycur.fetchall()
        t = "| {:<7} | {:<20} | {:<7} | {:<8} | {:<6} |".format(
            "ITEMNO", "INAME", "PRICE", "QUANTITY", "MAKE")
        print('-'*len(t))
        print(t)

        print('-'*len(t))
        for i in d:
            print("| {:<7d} | {:<20} | {:<7} | {:<8d} | {:<6} |".format(
                i[0], i[1], i[2], i[3], i[4]))
            print('-'*len(t))

        mydb.commit()
    else:
        print("INVENTORY NOT FOUND!!")


menu()
