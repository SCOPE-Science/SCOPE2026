#!/usr/bin/env python3
"""Exact lattice and fundamental-parallelepiped checks for odd-cycle edge simplices.

Runs entirely with Python's standard library.  All inequalities and counts are
integer statements; no floating-point tolerance or external files are used.
"""
from collections import Counter
from itertools import product
from math import comb


def numerator(n, w, x, i):
    # A = I + wS, (A inverse) = sum((-w S)^j)/(1+w**n).
    return sum((-w) ** j * x[(i - j) % n] for j in range(n))


def hstar(n, w):
    assert n >= 3 and n % 2 == 1 and w >= 2
    by_degree = Counter({0: 1})
    for x in product(range(1, w + 1), repeat=n):
        if sum(x) % (w + 1) == 0:
            by_degree[sum(x) // (w + 1)] += 1
    return by_degree


def direct_lattice_count(n, w, t):
    total = (w + 1) * t
    count = 0
    x = [0] * n
    def walk(pos, rest):
        nonlocal count
        if pos == n-1:
            x[pos] = rest
            if all(numerator(n, w, x, i) >= 0 for i in range(n)):
                count += 1
            return
        for z in range(rest+1):
            x[pos] = z
            walk(pos+1, rest-z)
    walk(0, total)
    return count


def ehrhart_from_h(n, h, t):
    # Dimension n-1, denominator (1-z)^n.
    return sum(c*comb(t-k+n-1,n-1) for k,c in h.items() if k<=t)


def check():
    params = [(3,2,5),(3,4,4),(5,2,4),(5,3,3),(5,4,3),(7,2,3),(7,3,3)]
    cases = 0
    dilation_cases = 0
    for n,w,tmax in params:
        h = hstar(n,w)
        q = (w**n + 1)//(w+1)
        assert sum(h.values()) == q, (n,w,'volume')
        assert min(k for k in h if k>0 and h[k]) == (n+w)//(w+1)
        assert all(h.get(k,0) == h.get(n-k,0) for k in range(1,n))
        for x in product(range(1,w+1),repeat=n):
            a = [numerator(n,w,x,i) for i in range(n)]
            assert all(1<=v<=w**n for v in a), (n,w,x,a)
            assert sum(a) * (w+1) == (1+w**n)*sum(x), (n,w,x,a)
            cases += 1
        for t in range(tmax+1):
            got=direct_lattice_count(n,w,t)
            expected=ehrhart_from_h(n,h,t)
            assert got==expected, (n,w,t,got,expected)
            dilation_cases += 1
        print('PASS n={} w={} h*={} normalized_volume={} direct_dilations=0..{}'.format(
            n,w,[h.get(i,0) for i in range(n)],q,tmax))
    print('PASS exact checks: {} interior candidates plus {} independent lattice-point dilations'.format(cases, dilation_cases))

if __name__=='__main__':
    check()
