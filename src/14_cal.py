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


inputs = sys.argv

today = datetime.today()
month = today.month
year = today.year

if len(inputs) == 1:
  print("\nHere is this month's calendar\n")

elif len(inputs) == 2 and inputs[1].isdigit() == True and  (1 <= int(inputs[1]) <= 12):
  month = int(inputs[1])
  print("\nHere is the calendar for the month of {}, 2020.\n".format(calendar.month_name[month]))

elif len(inputs) == 3 and inputs[1].isdigit() == True and  (1 <= int(inputs[1]) <= 12) and inputs[2].isdigit() == True:
  print(inputs)
  month = int(inputs[1])
  year = int(inputs[2])
  print("\nHere is the calendar for the month of {:s}, {:d}.\n".format(calendar.month_name[month], year))

else:
  print("\nInvalid Input. Months must be numbers between 1 and 12. Years must be numbers.")
  sys.exit()

print(calendar.TextCalendar().formatmonth(year,month))