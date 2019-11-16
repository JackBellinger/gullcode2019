outtype = int(input())

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

if outtype == 0:
    for i in range(1, 102):
        if i in squares:
            print(str(i)+" 1")
        else:
            print(str(i)+" 0")

elif outtype == 1:
    for i in range(0, 10):
        print(str(squares[i])+" 1")
else:
    for i in range(2, 102):
        if not (i in squares):
            print(str(i)+" 0")
