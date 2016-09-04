# -*- coding: utf-8 -*-

# pandas
import pandas as pd
# regex
import re

faculty = pd.read_csv('faculty.csv')
# gets us a list of degrees
list_of_degrees = list(faculty[' degree'])

def cleanup(string):
	# strip removes ending spaces, lower downcases, get rid of periods so ph.d == phd. 
	string = string.strip().lower().replace('.','')
	return string

def titles_clean(lst):
	new_list =[]
	for i in range(0,len(lst)):
		# need to explicitly re-assign list_of_degrees[i] due to base immutability of python strings
		# this cleans up the strings comprising the list components
		lst[i] = cleanup(lst[i])
		x = lst[i].split(' ')
		# inner loop for the sublists
		for i in range(0,len(x)):
			# extend here adds another string item, append here added a list item containing said string item
			new_list.extend(x)
	return new_list

def count(lst):
	d = {}
	for i in range(0,len(lst)):
		# .keys() apparently isn't strictly necessary here, but makes the code more idiomatic / readable.
		if lst[i] in d.keys():
			d[lst[i]] += 1
		else:
			d[lst[i]] = 1
	return d

list_of_titles = list(faculty[' title'])	
list_of_emails = list(faculty[' email'])	

# q1
print "q1:"
print count(titles_clean(list_of_degrees))
print "The '0' here appears to be a non-degree person or a data entry error of some kind. It can be simply ignored."

#q2
# note that we can assume the {Assistant Professor is Biostatistics': 1} entry is a data entry error, and add it to the other assistant profs for final.
print "q2:"
print count(list_of_titles)
print "We can assume that the '{Assistant Professor is Biostatistics': 1}' is a data-enty error and add it to the other Assistant Professors; giving us 12 Assistant Professors, 12 Associate Professors, and 13 Professors." 
# We could build something to handle this into code but that would require very specific modifications; and starting to account for every possible data-enty typo, especially when it comes to mispelling/misentering words starts to lose focus of the core project here.

#q3 
print "q3:"
print list_of_emails

#q4
# simple way to do this is going to involve regex or other formula to simply delete everything up and including the @ sign from the email list, then set it, then list it

print "q4:"

def email_posta(string):
	string =  re.sub(r'^[^@]*@' ,'', string)
	return string

def email_domains(lst):
	for i in range(0,len(lst)):
		lst[i] = email_posta(lst[i])
	return list(set(lst))

print email_domains(list_of_emails)	
print str(len(email_domains(list_of_emails))) + " different email domains"