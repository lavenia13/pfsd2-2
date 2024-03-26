import datetime
import time
print(time.time())
print(time.asctime())

#
lavenia=datetime.datetime.now()
print(lavenia)
print("Year:",lavenia.year)
print("Month:",lavenia.month)

#
import calendar
s=calendar.prcal(2005)
s2=calendar.month(2023,4)
s1=calendar.isleap(2004)
print(s1)

#
import datetime
x=datetime.datetime.now()
from datetime import timedelta
print(x+timedelta(days=-89))

#
import time
from datetime import datetime
import pytz
time1=pytz.timezone('Singapore')
print("current time is: ",datetime.now(time1))

