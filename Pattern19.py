"""
input:5
    1
   1 2   
  1   3
 1     4
1 2 3 4 5

"""
def Pattern19(no):
    try:
        if type(no)!=int or no<=0:
            raise ValueError
        
        temp=2
        for i in range(1,no+1):
            for j in range(1,no*2):
                if i==1 and j==no:
                    print(1,end="")
                elif j==(no-i)+1:
                    print(1,end="")
                elif j==(no+i)-1:
                    print(i,end="")
                elif(i==no and j%2!=0):
                    print(temp,end="")
                    temp+=1
                else:
                    print(" ",end="")
            print()
    except ValueError or Exception: 
        print("ERROR: Invalid Input")


#Test Cases
        
Pattern19(8)
Pattern19(5)
Pattern19(-8)
Pattern19(0)
Pattern19("string")
Pattern19(6.3)
Pattern19(0)
Pattern19(1)