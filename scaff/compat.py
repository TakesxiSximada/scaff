#! /usr/bin/env python
# -*- coding: utf-8 -*-
import six

if six.PY3:
    from itertools import accumulate
else:
    import operator

    def accumulate(iterable, func=operator.add):
        'Return running totals'
        # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
        # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
        it = iter(iterable)
        try:
            total = next(it)
        except StopIteration:
            return
        yield total
        for element in it:
            total = func(total, element)
            yield total


def get_input(*args, **kwds):
    func = input if six.PY3 else raw_input
    return func(*args, **kwds)
