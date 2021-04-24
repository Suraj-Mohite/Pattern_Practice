#accept row and column from user and display
'''
# * * *
* # * *
* * # *
* * * #
'''
def Pattern3(iRow,iCol):
    if (iRow < 0):
        iRow = -iRow

    if (iCol < 0):
        iCol = -iCol
        
    if(iRow!=iCol):
        print("ERROR:Invalid Input")
        return
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            if(i==j):
                print("#",end=" ")
            else:
                print("*",end=" ")
        print()

iRow=int(input("Enter the number of rows.\n"))
iCol=int(input("Enter the number of columns.\n"))
Pattern3(iRow,iCol)
