#!/usr/bin/env python3
"""Exact finite checks of the arithmetic obstruction; not a proof of the topology."""
from math import gcd


def primes_up_to(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]


def obstruction(q,p):
    if p <= 2*q or p%2==0:
        raise ValueError('require odd prime p>2q')
    subgroup = {pow(a,q,p) for a in range(1,p)}
    allowable = subgroup | {(-a)%p for a in subgroup}
    return 2 not in allowable

ps = [p for p in primes_up_to(199) if p>4]
for p in ps:
    assert obstruction(2,p) == (p%8 == 5), (p,obstruction(2,p))
print('q=2, primes 5..199: obstruction iff p mod 8=5; cases:',len(ps))
for q in (2,3,4,5):
    hits = [p for p in primes_up_to(101) if p>2*q and obstruction(q,p)]
    print('q=%d, obstructed primes <=101: %s' % (q,','.join(map(str,hits))))
# Geometric input check: a nonidentity rotation of order p cannot preserve
# a nonempty finite set with at most 2q points when p>2q.
for q in range(2,7):
    for p in primes_up_to(101):
        if p>2*q:
            assert not any(k%p==0 for k in range(1,2*q+1))
print('orbital-size arithmetic checks: passed')
