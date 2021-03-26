'''
55555
54444
54333
54322
54321
'''

def Pattern(row,col):
    if (row < 0):
        row = -row

    if (col < 0):
        col = -col

    if(row!=col):
        return
    for i in range(row,0,-1):
        for j in range(col,0,-1):
            if(j>=i):
                print(j,end="")
            else:
                print(i,end="")
        print()

iRow=int(input("Enter the row\n"))
iCol=int(input("Enter the col\n"))

Pattern(iRow,iCol)