#!/bin/env python3
"""
Think Stats Chapter 2 Exercise 4
 effect size of Cohen's d

Cohen's D is an example of effect size. Other examples of effect size are:
    correlation between two variables,
    mean difference,
    regression coefficients and
    standardized test statistics such as: t, Z, F ...
In this example, you will compute Cohen's D to quantify (or measure) the
difference between two groups of data.

You will see effect size again and again in results of algorithms that
are run in data science. For instance, in the bootcamp, when you run a
regression analysis, you will recognize the t-statistic as an example of
effect size.

Exercise 4:
    Using the variable totalwgt_lb, investigate whether first babies are
    lighter or heaver than others. Compute Cohen's d to quantify the
    difference between groups. 
    How does it compare to the difference in pregnancy length?

"""


import math
import nsfg
import sys
import thinkplot
import thinkstats2


# debug = True
debug = False


def dprint(s):
    if debug == True:
        print(repr(s))


def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    dprint('var1: ' + repr(var1))
    var2 = group2.var()
    dprint('var2: ' + repr(var2))
    n1 = len(group1)
    dprint('n1: ' + repr(n1))
    n2 = len(group2)
    dprint('n2: ' + repr(n2))

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    dprint('pooled_var: ' + repr(pooled_var))
    d = diff / math.sqrt(pooled_var)
    dprint('d: ' + repr(d))
    return d


def GetCohenForCol(df, column_name):
    firsts_col = df[df.birthord == 1][column_name]
    others_col = df[df.birthord != 1][column_name]
    return CohenEffectSize(firsts_col, others_col)


if __name__ == '__main__':
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]

    # firsts = live[live.birthord == 1]
    # others = live[live.birthord != 1]
    # first_hist = thinkstats2.Hist(firsts.totalwgt_lb)
    # print('smallest firsts: {}'.format(first_hist.Smallest(3)))
    # print('largest firsts: {}'.format(first_hist.Largest(3)))
    #
    # other_hist = thinkstats2.Hist(others.totalwgt_lb)
    # print('smallest others: {}'.format(other_hist.Smallest(3)))
    # print('largest others: {}'.format(other_hist.Largest(3)))

    # sys.exit()
    # width = 0.45
    # thinkplot.PrePlot(2)
    # thinkplot.Hist(first_hist, align='right', width=width)
    # thinkplot.Hist(other_hist, align='left', width=width)
    # thinkplot.Show(xlabel='total weight/pounds', ylabel='frequency',
    #                xlim=[0, 16])
    # From histogram examination:
    # left tail of others more visible in histogram,
    # suspect others heavier, firsts lighter.

    for i in ['totalwgt_lb', 'prglngth']:
        cohen_d = GetCohenForCol(live, i)
        print('Cohen d for column {}: {:.4f}'.format(i, round(cohen_d, 4)))
