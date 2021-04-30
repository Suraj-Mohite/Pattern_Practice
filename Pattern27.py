"""
input: 3

*
* 1 *
* 1 2 1 *
* 1 2 3 2 1 *
* 1 2 1 *
* 1 *
*

"""

def Pattern(no):
    try:
        no=str(no)
        no=int(no)
        if no<=0:
            print("ERROR: 0 and Negative numbers are not allowed")
            return
        l1=[str(i) for i in range(1,no+1)]
        for i in range(1,2*no+2):
            if i==1 or i==2*no+1:
                print("*")
            elif i==2 or i==2*no:
                print("* 1 *")
            elif i<=no+1:
                print("* "+" ".join(l1[0:i-1])+" "+" ".join(l1[i-3::-1])+" *")
            elif i>no+1:
                print("* "+" ".join(l1[0:(2*no-i)+1])+" "+" ".join(l1[2*no-i-1::-1])+" *")
            

    except Exception as e:
        print("ERROR: Invalid Input")    

if __name__ == "__main__":
    inp=input("Enter the Number.")
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