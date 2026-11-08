#!/usr/bin/env python3
"""Independent finite subset verification for the two-variable Jordan-profile graph polynomial."""
from itertools import product
from collections import Counter
from check_adjoint import inspect,count_components

def matroid_sum(n,E,q,s,t):
    m=len(E);total=0
    for f in range(1<<m):
        F=[E[i] for i in range(m) if (f>>i)&1]
        R=[i for i in range(m) if not (f>>i)&1]
        for h in range(1<<len(R)):
            H=[E[R[j]] for j in range(len(R)) if (h>>j)&1]
            total += ((q-1)**len(F)*s**(n-count_components(n,F)) *
                      (q*t)**(m-len(F)-len(H))*(1-q*t)**len(H)*q**count_components(n,F+H))
    return total

for q,n,E in [(2,3,[(0,1),(1,2),(2,0)]),
              (2,4,[(0,1),(0,2),(0,3)]),
              (2,2,[(0,1),(0,1)]),
              (3,3,[(0,1),(1,2),(2,0)])]:
    D=inspect(n,E,q)
    for s,t in [(0,0),(0,1),(1,0),(1,1),(1,2),(2,3),(3,2)]:
        actual=sum(v*s**rho*t**ell for (ell,rho),v in D.items())
        expect=matroid_sum(n,E,q,s,t)
        assert actual==expect,(q,n,E,s,t,actual,expect)
    print('TUTTE_JORDAN_BIVARIATE_MATCH',q,n,len(E))
print('TUTTE_JORDAN_BIVARIATE_PASS')
