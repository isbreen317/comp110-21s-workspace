"""An exercise in remainders and boolean logic."""

__author__ = "730320065"


# Begin your solution here...
x = int( input ("Enter an int: "))
if (x % 2 == 0) and (x % 7 == 0):
    print("TAR HEELS")
else:
    if (x % 7 == 0):
        print("HEELS")
    else:
        if (x % 2 == 0):
            print("TAR")
        else: 
            print("CAROLINA")