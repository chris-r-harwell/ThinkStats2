#!/bin/env python3
"""
Q2. Think Stats Chapter 3 Exercise 1 (actual vs. biased)

This problem presents a robust example of actual vs biased data. As a
data scientist, it will be important to examine not only the data that is
available, but also the data that may be missing but highly relevant. You
will see how the absence of this relevant data will bias a dataset,
its distribution, and ultimately, its statistical interpretation.


Solutions to these exercises are in chap03soln.ipynb and chap03soln.py


Example 3-1.


Something like the class size paradox appears if you survey children and
ask how many children are in their family. Families with many children
are more likely to appear in your sample, and families with no children
have no chance to be in the sample.


Use the NSFG respondent variable NUMKDHH to construct the actual
distribution for the number of children under 18 in the household.


Now compute the biased distribution we would see if we surveyed the
children and asked them how many children under 18 (including themselves)
are in their household.


Plot the actual and biased distributions, and compute their means. As
a starting place, you can use chap03ex.ipynb.


"""
import nsfg
import thinkplot
import thinkstats2


def BiasPmf(pmf, label):
    """
    Bias a probability mass function by
    multiplying each item by itself and normalize.
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf


def UnbiasPmf(pmf, label):
    """
    Unbias a probability mass function by
    dividing each item by itself and normalize.
    """

    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, 1.0/x)

    new_pmf.Normalize()
    return new_pmf


if __name__ == '__main__':
    resp = nsfg.ReadFemResp()
    numkdhh = resp['numkdhh']

    numkdhh_hist = thinkstats2.Hist(numkdhh)
    """ comment
    thinkplot.Hist(numkdhh_hist, label='number of children per household')

    thinkplot.Save(root='numkdhh_hist',
                   title='Histogram',
                   xlabel='number of children',
                   ylabel='frequency')

    print('Fewest children:')
    for num, freq in numkdhh_hist.Smallest(10):
        print(num, freq)

    print('Most children:')
    for num, freq in numkdhh_hist.Largest(10):
        print(num, freq)
    end comment """

    # Construct actual distribution for number of children.
    pmf = thinkstats2.Pmf(numkdhh_hist, label='actual')
    # Compute biased distribution if children surveyed.
    biased_pmf = BiasPmf(pmf, label='observed')

    # Plot actual pmf and biased_pmf
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased_pmf])
    thinkplot.Save(root='numkdhh_pmf_and_biased',
                   xlabel='number of children',
                   ylabel='PMF',
                   formats=['png'])

    # Compute means
    actual_mean = pmf.Mean()
    biased_mean = biased_pmf.Mean()
    print('mean:')
    print('actual: {:.4f}'.format(round(actual_mean, 4)))
    print('biased: {:.4f}'.format(round(biased_mean, 4)))

    """
    Comparing the actual and the biased probability mass function plots,
    we see that actual is above when zero children in household, but below
    obeserved with more than one child. This illustrates how households
    with more children will provide more observations in the biased case.

    That is you'd think there were on average two children per household,
    from a survey of children, but there is really an average of one.

    see numkdhh_hist.eps and numkdhh_pmf_and_biased.eps

[crh@xps code]$ ./metis_q2_ch3_ex1.py
Writing numkdhh_hist.pdf
Writing numkdhh_hist.eps
Fewest children:
0 3563
1 1636
2 1500
3 666
4 196
5 82
Most children:
5 82
4 196
3 666
2 1500
1 1636
0 3563
Writing numkdhh_pmf_and_biased.pdf
Writing numkdhh_pmf_and_biased.eps
mean:
actual: 1.0242
biased: 2.4037
    """
