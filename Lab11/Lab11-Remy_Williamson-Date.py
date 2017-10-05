# Joseph Remy and Daniel Williamson
# C126L - 11 - Date
# 27 November 2015

# IMPORT
from Date import Date
# END - IMPORT

__authors__ = "Joseph Remy and Daniel Williamson"
__title__ = "Lab 11 - Date"
# __class__ = "CS126"
__class__ = "CS126L"
__date__ = "27 November 2015"

# GLOBAL VARIABLES
# exampleVar = "I am globally accessible"

# END - GLOBAL VARIABLES

# FUNCTIONS
# def helloWorld(args=0):
#   return "Hello World!"

# END - FUNCTIONS

# START


def Start():  # Header for the Program before it begins
    print(__class__, "-", __title__ + "\nBy:", __authors__, "\n" +
          __date__, "\n\--------------------------------------")
    Main()
# End - START

# MAIN


def Main():  # Where the magic starts happening
    # Lab test code
    date = Date(1, 1, 2014)
    print(date)
    date.addDays(1)
    print(date)
    date.addDays(29)
    print(date)
    date.addWeeks(4)
    print(date)
    for i in range(365):
        date.addDays(1)
        print(date)
    print()

    # Our own test code for the EC
    print("Demonstrating Leap Year:")
    date2 = Date(2, 28, 2016)
    print(date2)
    date2.addDays(1)
    print(date2)
    print()

    date3 = Date(2, 28, 1800)
    print(date3)
    date3.addDays(1)
    print(date3)
    print()

    date4 = Date(2, 28, 2000)
    print(date4)
    date4.addDays(1)
    print(date4)
# END - MAIN

if __name__ == "__main__":
    Start()  # Start the program
