#!/usr/bin/env python3
import sys
from real_madrid_mod3_hw7 import *
from urllib.request import urlopen


def testZip():
    """
    Run to test the BarCode function in mod3
    """

    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt") as testCode:
        for line in testCode:
            line_words = line.split()
            for word in line_words:
                printDigit(word.decode("utf-8"))
                printBarCode(word.decode("utf-8"))


#Main function
def main():
    """
    Main Function
    """
    testZip()



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
