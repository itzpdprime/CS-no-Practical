def countlines_et():
    f = open(
        r'REPORT.TXT', 'r')
    for line in f.readlines():
        print(line)
    e = 0
    t = 0
    f = open(
        r'REPORT.TXT', "r")
    for line in f.readlines():
        if line[0].lower() == "e":
            e += 1
        elif line[0].lower() == "t":
            t += 1
    print("no. of line strating with e: ", e)
    print("no. of line strating with t: ", t)
    f.close()


countlines_et()

