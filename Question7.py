import pickle as p


def CreateFile():
    with open("Book.dat", 'ab') as f:
        print("Enter the details:")
        bkn = int(input("BOOKNO: "))
        bknm = input("BOOKNAME: ")
        athr = input("AUTHOR: ")
        prc = float(input("PRICE: "))
        bd = [bkn, bknm, athr, prc]
        p.dump(bd, f)
        print("RECORD SUCCESSFULLY ADDED !!!")


def CountRec(Author):
    with open("Book.dat", 'rb') as f:
        nb = 0
        while True:
            try:
                bd = p.load(f)
                if bd[2] == Author:
                    nb += 1

            except EOFError:
                break
        print(f"The no. of books written by {Author}: {nb}")


CreateFile()
a = 'Robin Sharma'
CountRec(a)
