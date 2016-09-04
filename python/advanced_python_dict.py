####Q6.  Create a dictionary in the below format:
# ```
# faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

# ```
# Print the first 3 key and value pairs of the dictionary:

# >> REPLACE THIS WITH YOUR RESPONSE

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

# ```
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
# ```

# -*- coding: utf-8 -*-

# pandas
import pandas as pd
# regex
import re

faculty = pd.read_csv('faculty.csv')

#print faculty

faculty_dict = {}
professor_dict = {}

degrees = list(faculty[' degree'])
titles = list(faculty[' title'])
emails = list(faculty[' email'])
names = list(faculty['name'])

def titles_clean(lst):
	for i in range(0,len(lst)):
		# regex for titles to remove everything after r and a word break, (technically it replaces the r+what follows with just r). could have just split and deleted everything after "Professor" but wanted some regex practice.
		lst[i] = re.sub(r'r\b.*$','r', lst[i])
	return lst

	

def lastname(lst):
	for i in range(0,len(lst)):
		# regex to get lastname, .search returns object, call group(0) to get first (only) result
		lst[i] = re.search(r'(\w+)$', lst[i]).group(0)
	return lst

def firstname(lst):
	for i in range(0,len(lst)):
		# regex to get first name, .search returns object, call group(0) to get first (only) result
		lst[i] = re.search(r'\w*\b', lst[i]).group(0)
	return lst

last = lastname(names)
#need to redefine names due to variable mutability
names = list(faculty['name'])
first = firstname(names)
# one last redefine
names = list(faculty['name'])

# we now run titles_clean; and will -not- be redefining it afterwards
titles_clean(titles)


# q6: 
# creating faculty_dict
for i in range(0,len(names)):
	faculty_dict[last[i]] = [degrees[i],titles[i],emails[i]]

print "q6:"
for key in sorted(faculty_dict.keys())[:3]:
	print(key,faculty_dict[key])

# q7:
# creating professor_dict
for i in range(0,len(names)):
	# key needs to be a tuple rather than a list, as keys need to be immutable
	professor_dict[tuple([first[i],last[i]])] = [degrees[i],titles[i],emails[i]]

print "q7:"
# list slicing the first 3 answers
for key in sorted(professor_dict.keys())[:3]:
	print(key,professor_dict[key])

# q8
print "q8:"
# to sort by lastname we sort by the second element of the tuple, which contains the surname
# take a look at the sort_last from basic python
for key in sorted(professor_dict.keys(),key=lambda x: x[1])[:3]:
	print(key,professor_dict[key])
