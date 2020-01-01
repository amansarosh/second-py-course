import calendar  # calender import to give functionality
import datetime
import time

print(calendar.weekheader(2))  # shows days of week
print()  # line spacing
print(calendar.firstweekday())  # spits value from 0-6 on day of week

print(calendar.month(2020, 1, 3))  # shows calendar and displays y / m / spacing
print()  # line spacing

print(calendar.monthcalendar(2019, 3))  # prints out array of calendar days
print()  # spacing

print(calendar.calendar(2019))  # prints out whole year of provided date

# cannot print out 3d array of years

day_of_the_week = calendar.weekday(2020, 12, 4)
print(day_of_the_week)  # tells what day dec 4 2020 will be on
print()

is_leap = calendar.isleap(2020)  # this tells if there is a leap year
print(is_leap)  # prints t/f

print()

how_many_leap_days = calendar.leapdays(2000, 2005)  # views all params (2) given and calculates when there was a leap year EXCLUSIVE
print(how_many_leap_days)  # prints int based on given values
