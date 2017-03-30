#!/usr/bin/env python3
import sys
from urllib.request import urlopen
from real_madrid_mod1_hw7 import unlock


def i_can_open():
    """
    Pass the values given to check if doors can unlock:
    """
    #load file
    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"
    count = 1
    with urlopen(url) as minivan:
        #skip header line
        next(minivan, None)
        #loop line by line and pass line as a list to unlock()
        for line in minivan:
            conditions = line.split()
            values = []
            for value in conditions:
                values.append(value.decode("utf-8"))
            #print out current record number
            print("Reading Record #",count)
            #print state of each control object
            print("Left Dashboard Switch (0 or 1) = ",values[1])
            print("Right Dashboard Switch (0 or 1) = ",values[2])
            print("Child Lock Switch (0 or 1) = ",values[3])
            print("Master Unlock Switch (0 or 1) = ",values[4])
            print("Left Inside Handle (0 or 1) = ",values[5])
            print("Left Outside Handle (0 or 1) = ",values[6])
            print("Right Inside Handle (0 or 1) = ",values[7])
            print("Right Outside Handle (0 or 1) = ",values[8])
            print("Gear Shift Position (0 or 1) = ",values[9])
            count += 1
            #pass conditions to unlock() to check
            unlock(values)


#Main function
def main():
    """
    Test Function
    """
    i_can_open()


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
