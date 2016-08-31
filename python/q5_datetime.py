# Hint:  use Google to find python function

# https://docs.python.org/3/library/datetime.html

# Conversely, the datetime.strptime() class method creates a datetime object from a string representing a date and time and a corresponding format string.

from datetime import datetime
def change_date(date_start, date_stop, date_format):
	a = datetime.strptime(date_start, date_format)
	b = datetime.strptime(date_stop, date_format)
	change = b - a
	return change.days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'
print change_date(date_start, date_stop, "%m-%d-%Y")   

####b)  
date_start = '12312013'  
date_stop = '05282015' 
print change_date(date_start, date_stop, "%m%d%Y")    

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'
print change_date(date_start, date_stop, "%d-%b-%Y")      