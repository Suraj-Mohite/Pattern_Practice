"""
input: 4

1      
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1

"""

def Pattern(no):
    try:
        no=str(no)
        no=int(no)
        if no<=0:
            print("ERROR: 0 and Negative numbers are not allowed")
            return
        k=1
        for i in range(1,2*no+1):
            if i==no+1:
                k=k-no
                n=k
            if i>no+1:
                k=n-((2*no-i)+1)
                n=k
            for j in range(1,2*no):
                if j<2*i and i<=no:
                    if j%2!=0:
                        print(k,end="")
                        k+=1
                    else:
                        print("*",end="")
                elif i==no+1 and j<2*no:
                    if j%2!=0:
                        print(k,end="")
                        k+=1
                    else:
                        print("*",end="")
                elif i>no+1 and j<(2*no-i+1)*2:
                    if j%2!=0:
                        print(k,end="")
                        k+=1
                    else:
                        print("*",end="")
                else:
                    print(" ",end="")
            print()            
    except Exception as e:
        print("ERROR: Invalid Input")    

if __name__ == "__main__":
    inp=input("Enter the Number.\n")
    Pattern(inp)
    print()

    #TestCases
    #Different Datatype And Different Value Has been passed as an input to test the function
    Pattern(6) #test with positive integer as input
    print()
    Pattern(-8) #test with negative integer as input
    print() 
    Pattern(0) #test with 0 as input
    print() 
    Pattern(1.3) #test with float as input
    print()
    Pattern("string") #test with string as input
    print()