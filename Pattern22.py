"""
input=5
    * 
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *

"""
def Pattern(no):
    try:
        no =int(no)
        if no<=0:
            print("ERROR: 0 and Negative numbers are not allowed")
            return
        for i in range(1,(2*no)+1):
            if i==no or i==no+1:
                print("* "*no)
            elif i<no:
                print(" "*(no-i)+"* "*i)
            elif i>no+1:
                print(" "*(i-(no+1))+"* "*(2*no-i+1))
    except Exception as e:
        print("ERROR: Invalid Input")


        

if __name__ == "__main__":
    inp=input("Enter the Number.")
    Pattern(inp)
    print()


    #TestCases
    #all inputs are in string format which later will be handled by function
    Pattern("3")
    print()
    Pattern("1")
    print()
    Pattern("-6")
    print() 
    Pattern("0")
    print() 
    Pattern("9.3")
    print()
    Pattern("string")
    print()