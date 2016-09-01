# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count < 10:
        return ("Number of donuts: %(count)s." % locals())
    elif count >= 10:
         return "Number of donuts: many"

    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError

# testing
# print donuts(4)
# print donuts(9)
# print donuts(10)
# print donuts(99)

    # works

def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        first_2 = s[:2]
        last_2 = s[-2:]
        return first_2 + last_2 

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError
#testing
# print both_ends('spring')
# print both_ends('Hello')
# print both_ends('a')
# print both_ends('xyz')
# works

def fix_start(s):
    first_char = s[0]
    lst = list(s)
    for i in range(1,len(lst)):
        if lst[i] == first_char:
            lst[i] = "*"
    new_word = "".join(lst)
    return new_word

    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError
#testing 
# print fix_start('babble')
# print fix_start('aardvark')
# print fix_start('google')
# print fix_start('donut')
# works


def mix_up(a, b):
    first_2_a = a[:2]
    first_2_b = b[:2]
    after_2_a = a[2:]
    after_2_b = b[2:]
    new_a = first_2_b+after_2_a
    new_b = first_2_a+after_2_b
    return new_a+" "+new_b

# this could definitely be more elegant, to the point of a one-line solution

    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError

#testing
# print mix_up('mix', 'pod')
# print mix_up('dog', 'dinner')
# print mix_up('gnash', 'sport')
# print mix_up('pezzy', 'firm')
# works

def verbing(s):
    # ing case
    if len(s) >= 3 and s[-3:] == "ing":
        s = s + "ly"
    elif len(s) >= 3:
        s = s+ "ing"
    # no need to create else case, since we are leaving it unchanged and doing nothing else    
    return s

    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError

#tests
# print verbing('hail')
# print verbing('swiming')
# print verbing('do')
# works

# -----------

# old version, failed when punctuation was used. need regex to solve the general case which includes punctuation, but regex is not taught in thinkpython or codeacademy.

# def not_bad(s):
#     # splits into list of words
#     lst = s.split()
#     not_marker = False
#     bad_marker = False
#     for i in range(0, len(lst)):
#         if lst[i] == "not":
#             not_marker = i
#         elif lst[i] == "bad":
#             bad_marker = i
#     if not_marker and bad_marker and not_marker < bad_marker:
#         new_lst = []
#         # modify things
#         for i in range(0, len(lst)):
#             if i == not_marker:
#                 new_lst.append("good")
#             elif i > not_marker and i <= bad_marker:
#                 continue
#             else:
#                 new_lst.append(lst[i])
#         return " ".join(new_lst)
#     else:
#         return s
# edit: yeah, I think we need regex here to cover the "bad!" case.

import re

def not_bad(string):
    return re.sub(r'\bnot\b.*\bbad\b' ,'good', string)
    # note - this version is case sensitive, but so was my original

# from dave: (And r'asggs' = raw string, very useful when using regular expressions to avoid a forest of backslashes.) (\b = word boundary)

    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError

#tests
# print "one case of not_bad (with a !) still non-functional, non-regex implementation?"
print not_bad('This movie is not so bad')
print not_bad('This dinner is not that bad!')
print not_bad('This tea is not hot')
print not_bad("It's bad yet not")
# text cases pass with regex


def front_back(a, b):
    a_back = a[-(len(a)/2):]
    b_back = b[-(len(b)/2):]
    if len(a) % 2 == 0:
        a_front = a[:(len(a)/2)]
    else:
        a_front = a[:int((len(a)/2)+1)]
    if len(b) % 2 == 0:
        b_front = b[:(len(b)/2)]
    else:
        b_front = b[:int((len(b)/2)+1)]  
    return a_front + b_front + a_back + b_back

    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
#tests
# print front_back('abcd', 'xy') 
# print front_back('abcde', 'xyz')
# print front_back('Kitten', 'Donut')
#all pass
