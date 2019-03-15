#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Find a substring by Knuth-Morris-Pratt
# jill-jênn vie et christoph dürr - 2014-2018
# inspired by a code from David Eppstein


# snip{
def ref_knuth_morris_pratt(t, s):
    """Find a substring by Knuth-Morris-Pratt
    :param s: the haystack string
    :param t: the needle string
    :returns: index i such that s[i: i + len(t)] == t, or -1
    :complexity: O(len(s) + len(t))
    """
    assert t != ''
    len_s = len(s)
    len_t = len(t)
    r = [0] * len_t
    j = r[0] = -1
    for i in range(1, len_t):
        while j >= 0 and t[i - 1] != t[j]:
            j = r[j]
        j += 1
        r[i] = j
    j = 0
    res = []
    for i in range(len_s):
        while j >= 0 and s[i] != t[j]:
            j = r[j]
        j += 1
        if j == len_t:
            res.append(i - len_t + 1)
            if len_t == 1:
                j = 0
            else:
                j = r[j-1]
    return res
# snip}
