# note: THIS ARE DESIGNED TO BE RUN IN THE /code folder of ThinkStats2, which can be cloned from its repo here: https://github.com/AllenDowney/ThinkStats2

# to get this all to run properly, clone to folder and stick this file in the /code subfolder, then run it!


import numpy as np
import pandas as pd
import nsfg
import thinkstats2
import thinkplot
import math
import random
import scipy.stats

df = nsfg.ReadFemPreg()
df

#Print value counts for prglngth and compare to results published in the codebook#
df.prglngth.value_counts().sort_index()

# question for TA?/classmates: how to properly group these sorted by index entries in this data format to get the result I'm looking for. I'd like to sum the values of index entries 0-13, 14-26, and 27-50 programmatically to see if it matches the expected result at: http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611931


##################################

print '2.4 - Effect Size'
# Exercise 2.4 

# Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference in pregenancy length?

#from p.19
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
# from p.21 
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
#we now use the cohen effect formula from p 24/25 to get the effect size
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
# display method 1
# print 'prglngth: ' + str(CohenEffectSize(firsts['prglngth'],others['prglngth']))
# print 'totalwght: ' + str(CohenEffectSize(firsts['totalwgt_lb'],others['totalwgt_lb']))
# display method 2, slightly more elegant:
for col in ('prglngth','totalwgt_lb'):
    print('{}: {}'.format(col,CohenEffectSize(firsts[col],others[col])))

print "Cohen's d is very small, both for pregnancy length and for total weight. While the (absolute) size of the effect pregnancy length is smaller than that of total weight, total weight's effect size is still small, 0.08 of a standard deviation; although Cohen himself cautions against setting arbitrary cutoff points for d, 0.2 is generally considered a small effect size."

#################################################

print '3.1 - Bias and Oversampling'

# Exercise 3.1 Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
# Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.
# Now compute the biased distribution we would see if we surveyed the chil- dren and asked them how many children under 18 (including themselves) are in their household.
# Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.

# niall's note: honestly, the part i'm having the most trouble with isn't the base-level statistical understanding, it's the number of packages and commands I'm getting thrown at me. just noting a code explanation as I go along for self-clarification.

# simple class-size paradox example, homebrewed: say you have 55 students, in 2 classes. one class is 50 students, the other is 5 students. students are only taking one class at a time, and there is no overlap. if you ask the registrar, they may say: there are 2 classes, one class has 50, the other class has 5, so the average class size (which to them is "students per class") is 27.5. on the other hand, if you survey the 55 students, 50 of them will each say that their class size is 50, and 5 of them will say that their class size is 5. if you take the average of these 55 data points, you'll get something much more heavily weighted towards the 50. for the purposes of these excercises, the "actual" class size is the registrar-measure, and the "bias" measure is the student-measure; the larger size of the larger class "amplifies" its importance in a student based survey - and inherently means larger classes are going to "weigh" more.

# we import the base data from the chap1soln file, which puts it in a readable format for us
import chap01soln
resp = chap01soln.ReadFemResp()

# next we make a PMF of numkdhh, the number of children under 18 in the respondent's household. PMF is short for probability mass function, which is a map of each value to its probability of occuring in a dataset, it's similar to a histogram, but the sum of the values associated with all the keys should equal 1.  (e.g, in a word count histogram with key-value pairs of a document, the values will sum to 1)

# make the pmf
# import thinkstats2 # already done at file top-level
pmf = thinkstats2.Pmf(resp.numkdhh)
# displaying the pmf

# import thinkplot # done at top-level
# commenting out below lines to show final product better
# thinkplot.Pmf(pmf, label='numkdhh')
# thinkplot.Show()

# now we need to create a biased pmf

# Code below and this commentary from p. 34: For each class size, x, we multiply the probability by x, the number of students who observe that class size. The result is a new Pmf that represents the biased distribution.  

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

# need to include the label to get the graph to display properly
pmf = thinkstats2.Pmf(resp.numkdhh, label= 'numkdhh')
biased_pmf = BiasPmf(pmf, label='biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='children per household',ylabel='PMF')
print('Mean Original PMF: {}'.format(pmf.Mean()))
print('Mean Biased PMF: {}'.format(biased_pmf.Mean()))


##################################################
print '4.2 - Random'

# Exercise 4.2 The numbers generated by random.random are supposed to be uniform between 0 and 1; that is, every value in the range should have the same probability.
# Generate 1000 numbers from random.random and plot their PMF and CDF. Is the distribution uniform?

# # import random # DONE AT TOP LEVEL

r = [random.random() for x in range(1000)] # should create a list of 1000 randomly generated numbers, all will be floating-point #s in the range [0.0, 1.0) per https://docs.python.org/2/library/random.html

pmf = thinkstats2.Pmf(r)
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel='number',ylabel='PMF') # tried playing with linewidth=0.01 as an additional argument to make this readable, no dice

print "ok so this graph doesn't really tell us much, just gives us an unreadable blue blob, we're going to want to CDF this due to the high number of unique values"

cdf = thinkstats2.Cdf(r)
#thinkplot provides a function named Cdf that plots Cdfs as lines:
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='number', ylabel='CDF')

print "The distribution appears to be fairly uniform."


##################################################

# Exercise 5.1

#In the BRFSS, the distribution of heights is roughly normal with parameters: mu = 178 cm and sigma = 7.7 cm for men. In order to join the Blue Man Group, you have to be male and between 5'10 and 6'1. What percentage of the US male population is in this range?

# from p. 56:
# The normal distribution is characterized by two parameters: the mean, mu, and standard deviation sigma. The normal distribution with mu = 0 and sigma = 1 is called the standard normal distribution. Its CDF is defined by an integral that does not have a closed form solution, but there are algorithms that evaluate it efficiently. One of them is provided by SciPy: scipy.stats.norm is an object that represents a normal distribution; it provides a method, cdf, that evaluates the standard normal CDF:
# >>> import scipy.stats
# >>> scipy.stats.norm.cdf(0)
# 0.5
# This result is correct: the median of the standard normal distribution is 0 (the same as the mean), and half of the values fall below the median, so CDF(0) is 0.5.

# documentation: http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.stats.norm.html; going to go ahead and note that this is not the most intuitive documentation ever written.

# here we learn: The location (loc) keyword specifies the mean. The scale (scale) keyword specifies the standard deviation. (Also these docs are just -not- intuitively written.) 

# # import scipy.stats # DONE AT TOP LEVEL

# here's a (normal) distribution with the mean and standard deviation
mu = 178
sigma = 7.7
low = scipy.stats.norm.cdf(177.8 , loc=mu , scale=sigma) # 177.8cm = 5'10
high = scipy.stats.norm.cdf(185.4 , loc=mu , scale=sigma) # 185.4cm = 6'1
print('{0:0.1%}'.format(high - low))

# note: don't feel great about this one. Like the methodology makes sense but he's throwing lots of different package commands at us with maybe a line of explanation for how they work. I've just subtracted the probability of it being shorter than 5'10 from the probability of it being shorther than 6'1 to get the "inside the margin" area.

#####################

# covers the mandatory excercises.