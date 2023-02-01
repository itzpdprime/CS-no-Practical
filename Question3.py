import pickle


def menu():
    while True:
        print("1.Add Student: ")
        print("2.Display: ")
        o = int(input("Enter your option: "))
        if o == 1:
            AddStudents()
        elif o == 2:
            GetStudents()
        else:
            break


def AddStudents():
    with open("STUDENT.DAT", 'ab') as f:
        print("Enter your details: ")
        rln = int(input("RollNo: "))
        nm = input("Name: ")
        mrk = int(input("Marks: "))
        d = [rln, nm, mrk]
        pickle.dump(d, f)
        print("STORED SUCCESSFULLY!!!")


def GetStudents():
    with open("STUDENT.DAT", 'rb') as f:
        pl = []
        while True:
            try:
                rec = pickle.load(f)
                if rec[2] > 75:
                    print(rec[1], " : ", rec[2])
                    pl.append(rec[2])

            except EOFError:
                break

        if len(pl) == 0:
            print("No Student has Percentage above 75.")
        else:
            n = 0
            for p in pl:
                n += p
            ap = n / len(pl)
            print("Average percentage: ", ap)


menu()
