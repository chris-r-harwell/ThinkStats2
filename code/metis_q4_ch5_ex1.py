#!/bin/env python3


import brfss
import scipy.stats
import sys


def FeetAndInchesToCentimeters(feet, inches):
    """
    INPUT: feet and inches
    OUTPUT: centimeters
    """
    cm_per_inch = (2.54/1.0)
    return (feet*12 + inches) * cm_per_inch


y1 = low_cm = FeetAndInchesToCentimeters(5, 10)
y2 = high_cm = FeetAndInchesToCentimeters(6, 1)

df = brfss.ReadBrfss()

column = 'htm3'
heights = df[df.sex == 1][column]
mean = heights.mean()
standard_deviation = heights.std()
cdf_at_y1, cdf_at_y2 = scipy.stats.norm.cdf([y1, y2], loc=mean, scale=standard_deviation)
probability_in_range = cdf_at_y2 - cdf_at_y1
print('Model from cummulative distribution function of normal distribution predicts {:.1f} percent males with height in range 5\'10" to 6\'1"'.format(100 * probability_in_range))
