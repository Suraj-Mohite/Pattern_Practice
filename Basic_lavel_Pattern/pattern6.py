#accept row and column from user and disply
'''
#
$ #
$ @ #
$ @ @ #
$ $ $ $ $
'''
def Pattern6(iRow,iCol):
    if(iRow<0):
        iRow=-iRow

    if(iCol<0):
        iCol=-iCol

    if(iRow!=iCol):
        print("ERROR:Invalid Input")
        return
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            if(i==j):
                print("#",end=" ")
            elif(j==1 or i==iCol):
                print("$",end=" ")
            elif(j<i and j!=1 and i!=iCol):
                print("@", end=" ")
            else:
                print(" ",end=" ")
        print()

iRow=int(input("Enter the number of rows.\n"))
iCol=int(input("Enter the number of columns.\n"))
Pattern6(iRow,iCol)