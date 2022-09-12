def fibonnaci():
    iterations = 10
    a = 1
    b = 1
    c = 0
    numlist = [a, b]
    while len(numlist) < iterations:
        c = a + b
        numlist.append(c)
        a = b
        b = c
    else:
        print(numlist)

fibonnaci()