CStack = []


def DeleteCustomer():
    if (CStack == []):
        print("UNDERFLOW!")
    else:
        print("Record deleted: ", CStack.pop())
