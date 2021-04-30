"""
input:5
        1
      2 3 2       
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
"""
def Pattern(no):
    try:
        if type(no)!=int or no<=0:
            raise ValueError
        temp=2
        for i in range(1,no+1):
            temp1=i
            for j in range(1,no*2):
                if i==1 and j==no:
                    print(1,end=" ")
                elif j>=(no-i)+1 and j<no:
                    print(temp1,end=" ")
                    temp1+=1
                elif j<=(no+i)-1 and j>=no:
                    print(temp1,end=" ")
                    temp1-=1
                else:
                    print(" ",end=" ")
            print()
    except ValueError: 
        print("ERROR: Invalid Input")

#test Cases
Pattern(8)
Pattern(5)
Pattern(6.5)
Pattern(-8)
Pattern(0)
Pattern("string")
