import numpy as np

def printCheckerBoard(n):
    print("Checker board pattern : ")

    # create a n*n pattern
    x = np.zeros((n,n),dtype=int)

    # fill with 1 the alternative rows and columns
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1

    # print the pattern
    for i in range(n):
        for j in range(n):
            print(x[i][j], end=" ")
        print()


# driver code
n = int(input("Enter the number of rows needed : " ))
printCheckerBoard(n)

