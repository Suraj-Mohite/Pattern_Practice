"""
input=5

    *
   * *
  *   *
 *     *
*       *
*       *
 *     *
  *   *
   * *
    *

"""

def Pattern(no):
    try:
        no=int(no)
        if no<=0:
            print("ERROR: 0 and Negative numbers are not allowed")
            return
        for i in range(2*no):
            if i==0 :
                print(" "*(no-1-i)+"*")
            elif i==2*no-1:
                print(" "*(i-no)+"*")
            elif i==no-1 or i==no:
                print("*"+" "*(2*(no-1)-1)+"*")
            elif i<no-1:
                print(" "*(no-1-i)+"*"+" "*(2*(i)-1)+"*")
            elif i>no:
                print(" "*(i-no)+"*"+" "*(2*(2*no-1-i)-1)+"*")
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
    Pattern("5")
    print()
    Pattern("-6") 
    print()
    Pattern("0") 
    print()
    Pattern("9.3")
    print()
    Pattern("string")
    print()
        