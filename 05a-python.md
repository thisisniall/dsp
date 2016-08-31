# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Lists and Tuples are similar in their core structure; at the risk of using a word in its definition they are both data structures of ordered lists of items with an index. Their primary difference is that Lists are mutable (they can be changed) while Tuples are not. For example, we cannot append, slice, pop, or otherwise change a tuple. However, this very immutabilty allows us to use tuples as dictionary keys; you can only use immutable objects (such as tuples and strings) as dictionary keys in python.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Sets are similar to lists, but cannot contain duplicate entries.

```bash
lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# if we change the data type to a set
# all duplicate entries will be removed
set(lst)
# output should be {1,2,3,4,5}
# another example of removing duplication, this time in letters, here:
set('abracadabra')
# output should be {'a', 'b', 'c', 'd', 'r'}
```

 > Sets are typically faster for seeing if an entry is present, but Lists are faster if you wish to iterate over the elements. This is because sets use hashtable lookup to check for presence, while Lists use search-based iteration.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List Comphrensions are a way of creating lists with some built-in logic. For example, building a list purely out of even numbers. Here's an example of one (taken from a codeacademy excercise) that takes the numbers 1-10, then compiles a list of numbers whose cubes are divisible by 4:
```bash
cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]
```


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





