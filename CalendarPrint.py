#!/usr/bin/python
# Takes user input & prints calendar for that month
# Validation includes if user input for year is 4 digits & month falls between 1 to 12
# PS: cal function by default throws error if its our of range. I wanted to display understandable message.

import calendar
year = raw_input("Enter a year: ")

if year.isdigit() and len(year) == 4:
    mon = raw_input("Enter a month: ")
    if (int(mon) >=1 and int(mon) <=12):
        cal = calendar.month(int(year), int(mon))
        print "Here is the calendar:"
        print cal
    else:
        print "Value entered is out of range"
else:
    print "Enter a valid 4 digit integer for year"
