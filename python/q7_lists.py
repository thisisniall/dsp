# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0
    for i in range(0,len(words)):
        if len(words[i]) >= 2 and words[i][0] == words[i][-1:]:
            count +=1
    return count

    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    raise NotImplementedError

#tests
# print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
# print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
# print match_ends(['aaa', 'be', 'abc', 'hello'])
#all work

def front_x(words):
    #psuedocode:
    # break words into 2 lists, one with strings that begin with x, one without
    # sort both lists
    # combine lists
    x_start = []
    non_x_start = []
    for word in words:
        if word[0].lower() == "x": #.lower() for case sensitivity
            x_start.append(word)
        else:
            non_x_start.append(word)
    x_start.sort()
    non_x_start.sort()
    return x_start + non_x_start

    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    raise NotImplementedError

#tests
# print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
# print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
# print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
# all tests pass

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """

    # x = sorted(tuples,key= lambda x: x[1])
    # note that this technically works for the above examples, but doesn't work in the general case, i have added an additional 4th example that this fails for
    x = sorted(tuples,key= lambda x: x[len(x)-1])
    return x


    raise NotImplementedError
# #test cases
# print sort_last([(1, 3), (3, 2), (2, 1)])
# print sort_last([(2, 3), (1, 2), (3, 1)])
# print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
# # extra test case
# print sort_last([(1, 7), (1, 3), (1, 8, 5), (2, 6, 12)])
# #test cases clear

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    # trick is to embed while within for loop to ensure it runs as many times as necessary rather than just using an if statement
    for i in nums:
        while i < len(nums)-1 and nums[i] == nums[i+1]:
            del nums[i]
    return nums

    raise NotImplementedError
# tests 
# print remove_adjacent([1, 2, 2, 3])
# print remove_adjacent([2, 2, 3, 3, 3])
# print remove_adjacent([3, 2, 3, 3, 3])
# all tests pass

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    # am i missing something here? this seems childishly simple compared to previous problems. or does the built-in sorted algorithm not work in linear time?
    return sorted(list1+list2)

    raise NotImplementedError

print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])