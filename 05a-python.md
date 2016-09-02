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

>> Sets are similar to lists, but cannot contain duplicate entries.

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

 >> Sets are typically faster for seeing if an entry is present, but Lists are faster if you wish to iterate over the elements. This is because sets use hashtable lookup to check for presence, while Lists use search-based iteration.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lamba` is a method of using anonymous functions. Anonymous functions are simply functions that don't have names, but execute a task regardless. They are typically used for fairly simple operations that don't need to be constantly re-used throughout a larger piece of code. For example:

```bash
lambda x: x % 2 == 0

# is the same thing as

def is_even(x):
	return x%2 == 0
```

>> An anonymous function generated `lambda` can also be used with `filter` or `map` the same way normal functions are, or as a key in 'sorted'.

```bash
# example with filter:

my_list = range(20)
filter(lambda x: x % 2 == 0, my_list)
# is the same as
filter(is_even, my_list)


# example with sorted:
new_list = [[1,2,3], [2,1,4], [3,3]]
# sorts by the size of the item at position 1 in the array
print sorted(new_list, key=lambda x: x[1]) 
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List Comphrensions are a way of creating lists with some built-in logic. For example, building a list purely out of even numbers. Here's an example of one (taken from a codeacademy excercise) that takes the numbers 1-10, then compiles a list of numbers whose cubes are divisible by 4:
```bash
cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]
```

>> We can use map and filter to get a similar effect, and it may be slightly faster in some cases, but list comprehensions are generally seen as more idiomatic in python. Here's the same effect using map and filter.


```bash
items = [1,2,3,4,5,6,7,8,9,10]
def cube(x):
		return x**3

def divisible_by_four(x):
	if x % 4 == 0:
		return True
	else:
		return False

# here we use map to apply the cube to all elements of the list
new_items = list(map(cube, items))
# here we use filter to filter out the elements not divisible by 4
new_items = filter(divisible_by_four,new_items)
print new_items
```

>> Note that both map and filter can still be useful when you don't need a multi-step logic or for simpler list situation.

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





