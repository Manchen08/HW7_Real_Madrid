"""
A module to print out a given zip code as a bar code 
"""

#!/usr/bin/env python3
import sys

def printDigit(d):
    print(d)

def printBarCode(zipCode):
    code = []
    check = 0
    for x in zipCode:
        check = check + int(x)

    if(check % 10 == 0):
        zipCode += "0"

    else:
        for x in range(1,9):
            check = check + x
            if(check % 10 == 0):
                check = x
                break
        zipCode += str(check)

    # print(check)
    # print(zipCode)

    for x in zipCode:
        d = x

        bars = []
        if(d == "0"):
            bars.append("|")
            bars.append("|")
            bars.append(":")
            bars.append(":")
            bars.append(":")

        else:
            if(int(d) - 7 >= 0):
                bars.append("|")
                d = int(d) - 7
            else:
                bars.append(":")

            if(int(d) - 4 >= 0):
                bars.append("|")
                d = int(d) - 4
            else:
                bars.append(":")

            if(int(d) - 2 >= 0):
                bars.append("|")
                d = int(d) - 2
            else:
                bars.append(":")

            if(int(d) - 1 >= 0):
                bars.append("|")
                d = int(d) - 1
            else:
                bars.append(":")

            if(x == "2" or x == "1" or x == "4" or x == "7"):
                bars.append("|")
            else:
                bars.append(":")

        code.append(bars)

    result = []


    print("|",end="")
    for l in code:
        for b in l:
            print(b,end="") 
    print("|")

    # print("||:|:::|:|:||::::::||:|::|:::|||")
    
#Main function
def main():
    """
    Main function
    """
    i= input("Please enter the zip code: " )
    while not i.isdigit() or len(i) != 5:
        print("Only digits are allowed and must be 5 characters")
        i = input("Please enter the zip code")

    printBarCode(i)


if __name__ == "__main__":
    # Call Main
    main() 
    exit(0)
