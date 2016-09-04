# pandas
import pandas as pd

faculty = pd.read_csv('faculty.csv')
my_list = list(faculty[' email'])

# basic structure from codeacademy exercises on text files
my_file = open("emails.csv", "w+")

for item in my_list:
    my_file.write(str(item)+'\n')

my_file.close()	