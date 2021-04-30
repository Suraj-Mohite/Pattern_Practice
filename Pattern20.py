"""
input:5
1 2 3 4 5 
2     5
3   5
4 5
5

"""

def pattern(no):
    try:
        if type(no)!=int or no<=0:
            raise ValueError
        for i in range(1,no+1):
            for j in range(i,no+1):
                if i==1:
                    print(j,end=" ")
                elif j==i or j==no:
                    print(j,end=" ")
                else:
                    print(" ",end=" ")
            print()
    except ValueError: 
        print("ERROR: Invalid Input")

#Test Cases

pattern(5)
pattern(-10)
pattern(0)
pattern("str")
pattern(6.3)
pattern(8)