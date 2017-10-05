class Date:
    # A dictionary of how many days there are in each month
    months = {
        1: 31,
        2: [28, 29],
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, month, day, year):
        ''' Initalization of an object of Date. '''
        self.month = month
        self.day = day
        self.year = year
        # Check year is called to determined whether or not it is a leap year
        self.checkYear()

    def addDays(self, days):
        ''' Date function, adds 'days' to self.day and
recalculates accordingly.'''
        # Used to 1 day at a time to self.day
        while days > 0:
            self.day += 1
            # If the month is Feb.
            if self.month == 2:
                # If it is a leap year
                if self.isLeapYear:
                    # Use the 29 or the second-index of the list of num of days
                    # For Feb.
                    i = 1
                else:
                    # Otherwise, use 28 or the normal number of days
                    i = 0
                if self.day > Date.months[2][i]:
                    # Check if the self.day is greater than number of days
                    # in Feb at index i
                    self.day = 1
                    # Reset to the first day
                    self.month += 1
                    # Increment the month
            else:
                # For all other months
                if self.day > Date.months[self.month]:
                    # If self.day is greater than the len of days of self.month
                    self.day = 1
                    # Reset to 1
                    self.month += 1
                    # and increment month
            if self.month > len(Date.months):
                # If self.month is greater than 12
                self.month = 1
                # Reset back to 1 (January)
                self.year += 1
                # Increment the year
                self.checkYear()
                # Check if it is a leap year
            days -= 1
            # Subtract a day and check while condition

    def addWeeks(self, weeks):
        ''' Date function, for number of 'weeks', add 7-day increments to
self.day by using addDays(7).'''
        if not weeks == 0:
            # Preventing silly input, when weeks > 0
            for w in range(weeks):
                # for w number of weeks
                self.addDays(7)
                # Add 7 days at a time

    def checkYear(self):
        ''' Date function, checks self for whether or not it is a leap year.'''
        if not self.year % 4 == 0:
            self.isLeapYear = False
        elif not self.year % 100 == 0:
            self.isLeapYear = True
        elif not self.year % 400 == 0:
            self.isLeapYear = False
        else:
            self.isLeapYear = True

    def __str__(self):
        ''' Overwriting built-in method, str() function for Date objects'''
        return str(self.month) + "-" + str(self.day) + "-" + str(self.year)


def Main():  # Test Code only for this .py file
    global date
    date = Date(1, 1, 2014)
    print(date)

if __name__ == "__main__":  # Only called when this .py file is run
    Main()
