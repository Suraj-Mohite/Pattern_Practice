'''
Aa
AaBb
AaBbCc
AaBbCcDd
'''

def Pattern(row,col):
    if(row!=col):
        return
    for i in range(row):
        str1="A"
        str2="a"
        for j in range(col):
            if(j<=i):
                print(str1+str2,end="")
            str1=chr(ord(str1)+1)
            str2=chr(ord(str2)+1)
        print()

iRow=int(input("Enter the row"))
iCol=int(input("Enter the col"))

Pattern(iRow,iCol)