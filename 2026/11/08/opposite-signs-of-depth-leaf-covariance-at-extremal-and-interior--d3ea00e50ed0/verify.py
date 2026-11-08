#!/usr/bin/env python3
"""Exact finite checks for rank-depth/leaf covariance in random binary search trees.

Standard-library-only; run: python3 verify.py
This enumerates all insertion permutations for 3 <= n <= 8, independently
constructing binary search trees and checking their leaf counts and depths.
"""
import itertools
from fractions import Fraction as F
from math import factorial


def covariance_formula(n, i):
    assert n >= 3 and 1 <= i <= n
    if i == 1 or i == n:
        return F((n+1)*(n-2), 12*n*(n-1))
    if n == 3:
        return F(-1, 3)
    if i == 2 or i == n-1:
        return -F(23*n**3-93*n**2+130*n-48, 72*n*(n-2)*(n-1))
    def g(t):
        return -F(t**4+2*t**3-t**2+10*t+6,
                  18*t*(t-1)*(t+1)*(t+2))
    return g(i) + g(n+1-i)


def conditional_difference(n, j, i):
    """E[L | j is earliest inserted in inclusive key interval j..i] - E[L]."""
    if j > i:  # reflect the whole key line
        j, i = n+1-j, n+1-i
    assert 1 <= j < i <= n
    m = i-j+1
    if m == 2:
        d = F(0)
    else:
        d = -F(4, 3*(m+1)*(m+2))
    if j == 1:
        d += -F(1, 3) + F(1, (m+1)*(m+2))
    elif j == 2:
        d += F(m-2, 3*(m+1)) + F(1, (m+1)*(m+2))
    if i == n-1:
        d += -F(1,12) if m == 2 else -F(1, 3*(m+2))
    elif i == n:
        d += F(1,4) if m == 2 else F(1,3*(m+1)*(m+2))
    return d


def bst_stats_from_priority(p):
    n = len(p)
    order = sorted(range(n), key=lambda a:p[a])
    left = [-1]*n
    right = [-1]*n
    depth = [0]*n
    root = order[0]
    for key in order[1:]:
        current = root
        while True:
            side = left if key < current else right
            if side[current] == -1:
                side[current] = key
                depth[key] = depth[current] + 1
                break
            current = side[current]
    leaves = sum(left[k] == -1 and right[k] == -1 for k in range(n))
    return depth, leaves


def run():
    checks = 0
    for n in range(3,9):
        N = factorial(n)
        sd = [0]*n
        sdl = [0]*n
        sl = 0
        s_cond = {(j,i): [0,0] for j in range(n) for i in range(n) if j != i}
        for p in itertools.permutations(range(n)):
            depth, leaf = bst_stats_from_priority(p)
            localmax = sum((k == 0 or p[k] > p[k-1])
                           and (k == n-1 or p[k] > p[k+1]) for k in range(n))
            assert leaf == localmax
            checks += 1
            for i in range(n):
                # Cartesian ancestor record characterization is a distinct direct check.
                d = sum(p[j] == min(p[j:i+1]) for j in range(i)) + \
                    sum(p[j] == min(p[i:j+1]) for j in range(i+1,n))
                assert d == depth[i]
                checks += 1
                sd[i] += d
                sdl[i] += d*leaf
            sl += leaf
            for j in range(n):
                for i in range(n):
                    if i == j: continue
                    a,b=sorted((i,j))
                    if p[j] == min(p[a:b+1]):
                        entry = s_cond[j,i]
                        entry[0] += 1
                        entry[1] += leaf
        assert F(sl,N) == F(n+1,3)
        checks += 1
        for i in range(n):
            cov = F(sdl[i],N) - F(sd[i]*sl,N*N)
            assert cov == covariance_formula(n,i+1), (n,i+1,cov,covariance_formula(n,i+1))
            checks += 1
        for (j,i),(hits,leafsum) in s_cond.items():
            m=abs(i-j)+1
            assert hits == N//m
            actual = F(leafsum,hits) - F(sl,N)
            predicted = conditional_difference(n,j+1,i+1)
            assert actual == predicted,(n,j+1,i+1,actual,predicted)
            checks += 2
    for n in range(3,121):
        for i in range(1,n+1):
            x=covariance_formula(n,i)
            assert (x>0 if i in (1,n) else x<0)
            checks += 1
            y=sum(conditional_difference(n,j,i)/F(abs(j-i)+1) for j in range(1,n+1) if j!=i)
            assert x==y,(n,i,x,y)
            checks += 1
    print('VERIFY_OK', checks, 'exact assertions; exhaustive n<=8; all ranks n<=120')

if __name__ == '__main__':
    run()
