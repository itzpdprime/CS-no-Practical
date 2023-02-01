def PushOn(Book):
    a = input("Enter the book name: ")
    Book.append(a)
    print("Added Successfully!!!")
    print(Book)


def Pop(Book):
    Book.pop()
    print("Popped Successfully!!!")
    print(Book)


book = ['Ikigai', 'Rich Dad Poor Dad', 'Atomic Habits', 'Rework']
PushOn(book)
Pop(book)
