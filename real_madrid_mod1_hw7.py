#!/usr/bin/env python3
import sys


def unlock(conditions):
    """
    Test the condition given to see if the side doors of the van can be opened.
    """
    #list of valid values for gs
    gs_values = ["P","N","D","1","2","3","R"]
    #read in all the values
    #LD = Left Dashboard switch
    ld = str(conditions[1])
    #RD = Right Dashboard switch
    rd = str(conditions[2])
    #CL = Child Lock switch
    cl = str(conditions[3])
    #ML = Master Unlock switch
    ml = str(conditions[4])
    #LI = Left Inside handle
    li = str(conditions[5])
    #LO = Left Outside handle
    lo = str(conditions[6])
    #RI = Right Inside handle
    ri = str(conditions[7])
    #RO = Right Inside handle
    ro = str(conditions[8])
    #GS = Gear Shift Position (Valid values: P, N, D, 1, 2, 3, R
    gs = str(conditions[9])
    #validate GS, if not in valid values print that error
    if gs not in gs_values:
        print("Invalid Gear Shift Setting. No Doors Will Open")
        print("Valid Gear Shift Settings: P, N, D, 1, 2, 3, R")
    #check if GS = P, if not doors cannot open
    elif gs is not "P":
        print("Gear Not in Park 'P', doors cannot open.")
    #check if ML is on or off, if ML is on doors cannot open
    elif ml is "0":
        print("Master unlock switch engaged, doors cannot open.")
    #check for childlock engaged and test dashboard switches and outside handles
    elif cl is "0":
        if ((ld is "1" or lo is "1") and (rd is "1" or lo is "1")):
            print("Both doors open.")
        elif ld is "1" or lo is "1":
            print("Left door open.")
        elif rd is "1" or lo is "1":
            print("Right door open.")
    #check for childlock disengaged and test dashboard switches, outside and inside handles
    elif cl is "1":
        if ((ld is "1" or lo is "1" or li is "1") and (rd is "1" or lo is "1" or li is "1")):
            print("Both doors open.")
        elif ld is "1" or lo is "1" or li is "1":
            print("Left door open.")
        elif rd is "1" or lo is "1" or li is "1":
            print("Right door open.")
    


#Main function
def main():
    """
    Test Function
    """
    pass


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
