"""Exact finite checks for marked coupon-collection likelihood-ratio ordering.

Run with Python 3: python check.py. Mathematical proof is in RESULT.md;
these computations are finite cross-checks, not substitutes for it.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

def coef(weights, N):
    c = [Q(1)] + [Q(0)]*N
    for p in weights:
        d = [Q(0)] + [p**k / factorial(k) for k in range(1,N+1)]
        c = [sum(c[k]*d[t-k] for k in range(t+1)) for t in range(N+1)]
    return c

def marked(weights, limit):
    return [[weights[i]*factorial(t-1)*coef(weights[:i]+weights[i+1:],limit)[t-1]
             for t in range(len(weights), limit+1)] for i in range(len(weights))]

def exhaustive(weights,t):
    m=len(weights); ans=[Q(0)]*m
    for seq in product(range(m),repeat=t):
        if len(set(seq[:-1]))==m-1 and seq[-1] not in seq[:-1]:
            prob=Q(1)
            for s in seq: prob*=weights[s]
            ans[seq[-1]]+=prob
    return ans

checks = 0
for ns in range(2,7):
    for raw in [list(range(1,ns+1)),list(range(ns,0,-1)),[1]*ns,
                [1+((k*k+3*k)%7) for k in range(ns)],
                [2**k for k in range(ns)]]:
        weights=[Q(v,sum(raw)) for v in raw]
        limit = 24
        cs = [coef(weights[:i]+weights[i+1:], limit) for i in range(ns)]
        f = [[weights[i]*factorial(t-1)*cs[i][t-1]
              for t in range(ns,limit+1)] for i in range(ns)]
        for i in range(ns):
            for j in range(ns):
                if weights[i]<=weights[j]: continue
                for idx in range(limit-ns):
                    assert f[i][idx]*f[j][idx+1] > f[i][idx+1]*f[j][idx]
                    checks+=1
                for ti in range(limit-ns+1):
                    for ui in range(ti+1,limit-ns+1):
                        assert f[i][ti]*f[j][ui] > f[i][ui]*f[j][ti]
                        checks+=1
        for i in range(ns):
            g=cs[i]
            start=ns-1
            for k in range(start+1,limit):
                assert g[k]**2>=g[k-1]*g[k+1]
                checks+=1
        if ns<=4:
            for t in range(ns,min(8,limit)+1):
                b=exhaustive(weights,t)
                for i in range(ns):
                    assert b[i]==f[i][t-ns]
                    checks+=1
# Exact fundamental m=3 example
weights=[Q(1,2),Q(3,10),Q(1,5)]
f=marked(weights,8)
assert all(f[i][0]==Q(3,50) for i in range(3))
checks+=3
assert f[0][1]==Q(9,200) and f[1][1]==Q(63,1000)
checks+=2
print(f"PASS: {checks} exact assertions (cross-products, log-concavity, and independent sequence enumeration).")
