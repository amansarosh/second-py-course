import datetime
import pytz

today = datetime.date.today()  # finds system date
print(today)

birthday = datetime.date(2005, 9, 11)  # int is required
print(birthday)  # datetime object

# find days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

# 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today + tdelta)  # can be used to add and subtract dates

print(today.day)
print(today.weekday())  # monday = 0 sunday = 6
print(today.month)
print(today.year)


print(datetime.time(7, 2, 20, 15))

# datetime.day (Y,  M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime ( Y, M, D, h, m, s, ms)

#  add 10 hrs to day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

for tz in pytz.all_timezones:
    print(tz)  # prints all timezones

# string formatting with dates
# 2019-12-31 -> December 31, 2019
# strftime (f = formatting)
print(datetime_pacific.strftime('%B %d, %Y'))

# December 31, 2019 -> datetime(2019-12-31)
# strptime (p = parsing)
"""
datetime_thing = datetime.datetime.strptime('December 31, 2019', '%B %d, %Y')
print(datetime_thing)
"""
