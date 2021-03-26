#accept row and column from user and disply
'''
* * * *
$ $ $ $
* * * *
$ $ $ $
'''

def Pattern2(iRow,iCol):
    for x in range(1,iRow+1):
        for y in range(1,iCol+1):
            if(x%2==0):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()

iRow=int(input("Enter the number of rows.\n"))
iCol=int(input("Enter the number of columns.\n"))
Pattern2(iRow,iCol)