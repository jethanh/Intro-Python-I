"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

dateData = input("Enter a month and year:").split(',')
print(len(dateData))


def myCalendar(*args):
    date = datetime.now()
    if len(args[0]) == 0: #this is best way of identifying empty input, len(args) is still 1, even if they don't input anything - this checks to see if the length of the input is 0
        print(calendar.month(date.year, date.month))
        print("Try searching for a different month! i.e. --> '5, 1994'")
    elif len(args) == 1:
        print(calendar.month(date.year, int(args[0])))
    elif len(args) == 2:
        print(calendar.month(int(args[1]), int(args[0])))
    else:
        print("don't forget the comma, i.e. --> 6, 2020")

myCalendar(*dateData)

print(sys.argv)