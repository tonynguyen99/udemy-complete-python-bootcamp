import datetime

mytime = datetime.time(2,20)

print(mytime)
print(type(mytime))

today = datetime.date.today()

print(today)
print(today.year)

print(today.ctime())

from datetime import datetime

mydatetime = datetime(2021,10,3,14,20,1)

print(mydatetime)

mydatetime = mydatetime.replace(year=2020)

print(mydatetime)

# Date
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2
print(result.days)

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

result1 = datetime1 - datetime2
print(result1)