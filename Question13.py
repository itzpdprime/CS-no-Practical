CStack = []


def AddCustomer(Customer):
    CStack.append(Customer)
    if len(CStack) == 0:
        print("UNDERFLOW")
    else:
        print(CStack)
