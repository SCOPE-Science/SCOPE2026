"""Exact two-landmark distance-profile check on antipodal binary-cube quotients.
Finite checks corroborate the accompanying all-dimension proof; not a replacement.
"""
from collections import defaultdict
from math import comb

def predicted(n,h):
    if h==1:return n-1
    if n==4 and h==2:return 2
    if n%2==0 and h==n//2:return n
    return h

def coefficient_table(n,h):
    # Choose first sensor 0^n and second with h initial ones.
    full=defaultdict(int)
    for i in range(h+1):
        for j in range(n-h+1):
            a=i+j; b=h-i+j
            full[(min(a,n-a),min(b,n-b))]+=comb(h,i)*comb(n-h,j)
    assert all(v%2==0 for v in full.values())
    C={sig:v//2 for sig,v in full.items()}
    C[(0,h)]-=1;C[(h,0)]-=1
    assert sum(C.values())==2**(n-1)-2
    assert all(v>=0 for v in C.values())
    return {s:v for s,v in C.items() if v}

for n in range(4,81):
    for h in range(1,n//2+1):
        tab=coefficient_table(n,h)
        got=min(tab.values())
        assert got==predicted(n,h),(n,h,got,predicted(n,h))
print('BINOMIAL_FORMULA_CHECK_OK n=4..80, every sensor separation')
