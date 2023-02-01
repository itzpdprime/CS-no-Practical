#[TestId, Subject, MaxMarks, ScoredMarks]
import pickle as p


def DisplayAvgMarks(Sub):
    with open("TEST.dat", 'rb') as f:
        s = 0
        n = 0
        while True:
            try:
                d = p.load(f)

                if Sub == d[1]:
                    print(d[3])
                    s += d[3]
                    n += 1
                avmrk = (s / n)

            except EOFError:
                break
        print(f'Average Marks in {Sub} : {avmrk}')


Sub = 'English'
DisplayAvgMarks(Sub)
