#accept row and column from user and disply
'''
* * * *
* * * *
* * * *
* * * *
'''

def pattern1(row,column):
    for i in range(row):
        for j in range(column):
            print("*",end=" ")
        print()


iRow=int(input("Enter the number of rows.\n"))
iCol=int(input("Enter the number of columns.\n"))
pattern1(iRow,iCol)