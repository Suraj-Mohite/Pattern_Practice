"""
input:4

1
2*2
3*3*3
4*4*4*4
4*4*4*4
3*3*3
2*2
1

"""

def Pattern(no):
    try:
        no=str(no)
        no=int(no)
        if no<=0:
            print("ERROR: 0 and Negative numbers are not allowed")
            return
        for i in range(1,2*no+1):
            if i==1 or i==2*no:
                print("1")
            elif i<=no:
                print(f"{i}*"*(i-1)+str(i))
            elif i==no+1:
                print(f"{i-1}*"*(i-2)+str(i-1))
            elif i>no+1:
                print(f"{2*no-i+1}*"*(2*no-i)+str(2*no-i+1))

                
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