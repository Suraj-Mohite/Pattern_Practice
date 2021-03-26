'''
11111
11122
11333
14444
55555
'''

def Pattern(row,col):
    if (row < 0):
        row = -row

    if (col < 0):
        col = -col

    if(row!=col):
        return
    for i in range(1,row+1):
        for j in range(1,col+1):
            if(j>=((col+1)-i) and j<=col):
                print(i,end=" ")
            else:
                print("1",end=" ")
        print()

iRow=int(input("Enter the row\n"))
iCol=int(input("Enter the col\n"))

Pattern(iRow,iCol)