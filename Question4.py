def SHOW_TODO():
    f = open(
        "ABC.TXT", "r")
    data = f.readlines()
    for line in data:
        if 'TO' in line or 'DO' in line:
            print(line)
    f.close()


SHOW_TODO()
