"""
A module to print out a given zip code as a bar code 
"""

#!/usr/bin/env python3
import sys
import re

def printDigit(d):
    pass

def printBarCode(zipCode):
    pass

#Main function
def main():
    """
    Test Function
    """
    i= input("Please enter the zip code")
    while not i.isdigit() or len(i) != 5:
        print("Only digits are allowed and must be 5 characters")
        i = input("Please enter the zip code")



if __name__ == "__main__":
    # Call Main
    main() 
    exit(0)
