#!/usr/bin/python
# Takes user input & prints calendar for that month

import calendar

year=raw_input("Enter a number")
mon=raw_input("Enter a number")

cal = calendar.month(int(year), int(mon))
print "Here is the calendar:"
print cal;
