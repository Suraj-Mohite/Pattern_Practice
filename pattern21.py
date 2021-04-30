"""
input=5

********1********
*******2*2*******
******3*3*3******
*****4*4*4*4*****
****5*5*5*5*5****

"""

def Pattern(no):
    try:
        no=str(no)
        no =int(no)
        if no<=0:
            print("ERROR: 0 and Negative numbers are not allowed")
            return
        n=no+(3*(no-1))
        n1=(n//2)+1
        for i in range(1,no+1):
            val=i
            for j in range(1,n+1):
                if j>=(2*no)-i and j<=n1+(i-1) and val!="*":
                    print(val,end="")
                    val="*"
                elif j>=(2*no)-i and j<=n1+(i-1) and val=="*":
                    print(val,end="")
                    val=i
                else:
                    print("*",end="")
            print()
    except ValueError:
        print("ERROR : Invalid Input")


#Test Cases

Pattern(3)
Pattern(5)
Pattern(9)
Pattern(-6) 
Pattern(0) 
Pattern(9.3)
Pattern("string")
            