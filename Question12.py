Lname = ['narender', 'jaya', 'raju', 'ramesh', 'anita', 'Piyush']
Lage = [45, 23, 59, 34, 51, 43]
Lnameage = []


def push_na():
    for x in range(len(Lname)):
        if Lage[x] > 50:
            Lnameage.append((Lname[x], Lage[x]))
    print(Lnameage)


def pop_na():
    if len(Lnameage) == 0:
        print("Underflow")
    else:
        t = Lnameage.pop()
    print("The name removed is ", t[0])
    print("The age of person is ", t[1])


push_na()
pop_na()
