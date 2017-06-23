#!/bin/env python3

def PercentileRank(scores, raw_score):
    """
    percentile rank: fraction of people who scored lower than you
      (or the same) as a percent.

    calculates percentile rank of a given value relative to the list
    of all scores.

    INPUT:
        scores - list of all other scores
        raw_score - a single value
    OUTPUT: 
        percentile rank float
    """

    count = 0
    for score in scores:
        if score <= raw_score:
            count += 1

        percentile_rank = 100.0 * count / len(scores)
        return percentile_rank


def Percentile(scores, percentile_rank):
    """
    calculates percentile.
    INPUT: 
        scores - list of all other scores
        percentile_rank float
    OUTPUT:
        raw_score - a single value
    inefficient implementation
    """

    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            raw_score = score
            return raw_score


def Percentile2(scores, percentile_rank):
    """
    caclulates percentile.
    better implementation uses percentile_rank to compute index.
    INPUT: 
        scores - list of all other scores
        percentile_rank float
    OUTPUT:
        raw_score - a single value
    """

    scores.sort()
    index = percentile_rank * (len(scores) - 1) / 100
    raw_score = scores[index]
    return raw_score


def EvalCdf(t, x):
    """
    Evaluate cummulative distribution function (CDF)
    which maps from a value to its percentile rank.
    Nearly ths same as percentile rank, except with
    range 0-1 instead of 0-100, so we omit *= 100.
    
    INPUT: 
        t - list of all values
        x - single value
    OUTPUT: 
        probability float in range 0 - 1
    """

    count = 0.0
    for value in t:
        if value <= x:
            count += 1

    probability = count / len(t)
    return probability
