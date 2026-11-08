#!/usr/bin/env python3
"""Exact integer checks for the dyadic quartic-graph energy identity.
No external data or packages required.  Execute: python3 verify.py
"""
from collections import Counter

BASE = {1: 8, 2: 48, 3: 384, 4: 3072}
B = {1: 17, 2: 19, 3: 23, 4: 30}

def formula(k):
    assert k >= 1
    m, r = divmod(k - 1, 4)
    r += 1
    n = 1 << k
    return n*n*(B[r]*(1 << m) - (k+14))

def direct_energy(k):
    n = 1 << k
    powers = [pow(x, 4, n) for x in range(n)]
    total = 0
    odd_s = even_s_odd_x = even_s_even_x = 0
    for s in range(n):
        hist = Counter((powers[x] + powers[(s-x)%n])%n for x in range(n))
        total += sum(t*t for t in hist.values())
        if s%2:
            odd_s += sum(t*t for t in hist.values())
        else:
            h_odd = Counter((powers[x]+powers[(s-x)%n])%n for x in range(1,n,2))
            h_even = Counter((powers[x]+powers[(s-x)%n])%n for x in range(0,n,2))
            even_s_odd_x += sum(t*t for t in h_odd.values())
            even_s_even_x += sum(t*t for t in h_even.values())
            if k >= 2:
                assert not (h_odd.keys() & h_even.keys()), (k,s)
    return total,odd_s,even_s_odd_x,even_s_even_x

def square_energy(m):
    n=1<<m
    h=Counter(pow(x,2,n) for x in range(n))
    return sum(t*t for t in h.values())

if __name__=='__main__':
    for m in range(1,12):
        assert square_energy(m)==m*(1<<m),m
    for k in range(1,12):
        n=1<<k
        got,os,eo,ee=direct_energy(k)
        want=formula(k)
        assert got==want,(k,got,want)
        if k>=5:
            assert os==8*n*n,(k,'odd s',os)
            assert eo==(k-2)*n*n,(k,'even s odd x',eo)
            assert ee==512*formula(k-4),(k,'even s even x',ee)
            assert want==(k+6)*n*n+512*formula(k-4)
        print(f'k={k} N={n} E={got} normalized={got//(n*n)}',flush=True)
    print('DYADIC_QUARTIC_GRAPH_ENERGY_CHECK_PASS')
