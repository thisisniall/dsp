# -*- coding: utf-8 -*-

# The football.csv file contains the results from the English Premier League. 
# The columns labeled 'Goals' and 'Goals Allowed' contain the the toal number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

import pandas

football = pandas.read_csv('football.csv')
# print football

# we can print football to take a basic look at the information provided 

# we now build a difference variable, we use abs to make sure that we're truly getting the difference between goals scored/against - not super important here since we're trying to find the -smallest- difference but if we were trying to find the largest difference it would be very important.
football['difference'] = abs(football['Goals']-football['Goals Allowed'])

# we can take a look at the new football table, which now includes our difference measure and is sorted by that measure
# print football.sort_values('difference')

#the top line of this output clearly shows Aston Villa is the team with the lowest goal differential, so we call that particular value in isolation now.
print football.sort_values('difference')['Team'].values[0]


# resources: 
# http://pandas.pydata.org/pandas-docs/stable/tutorials.html
# http://pandas.pydata.org/pandas-docs/stable/cookbook.html