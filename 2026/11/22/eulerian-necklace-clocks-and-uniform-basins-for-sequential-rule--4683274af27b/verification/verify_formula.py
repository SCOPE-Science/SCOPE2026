#!/usr/bin/env python3
"""Independent symbolic schedule and necklace-count checks for sequential Rule 170.

Only the Python standard library is needed.
"""
from itertools import permutations
from math import factorial, comb
from collections import Counter


def eulerian(n):
    row=[1]
    for m in range(2,n+1):
        row=[(j+1)*(row[j] if j<len(row) else 0) + (m-j)*(row[j-1] if j else 0)
             for j in range(m)]
    return row


def mobius(n):
    if n==1:return 1
    p=2;count=0
    while p*p<=n:
        if n%p==0:
            n//=p;count+=1
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:count+=1
    return (-1)**count


def aprime(p):
    return sum(mobius(p//d)*2**d for d in range(1,p+1) if p%d==0)


def signature(order):
    n=len(order)
    t=[0]*n
    for a,i in enumerate(order):t[i]=a
    return tuple(i for i in range(n) if t[(i-1)%n]<t[i])


def copy_source_map(order):
    n=len(order)
    # Track source labels independently of bit values, executing the local rule once.
    sources=list(range(n))
    for i in order:sources[i]=sources[(i+1)%n]
    return sources


def predicted_source_map(order):
    n=len(order);S=signature(order)
    assert 1<=len(S)<=n-1
    return [next(s for s in ([(v+i)%n for i in range(1,n+1)]) if s in S)
            for v in range(n)]


def main():
    for n in range(3,9):
        counts=Counter()
        for order in permutations(range(n)):
            S=signature(order);counts[len(S)]+=1
            assert copy_source_map(order)==predicted_source_map(order)
            # The formula's range blocks are exactly the k-dimensional periodic core.
            r=copy_source_map(order)
            assert len(set(r))==len(S)
            assert set(r)==set(S)
            for j in S:
                q=r[j]
                assert q==next(s for s in [(j+i)%n for i in range(1,n+1)] if s in S)
        expected={k:n*eulerian(n-1)[k-1] for k in range(1,n)}
        assert dict(counts)==expected,(n,counts,expected)
        assert sum(counts.values())==factorial(n)
        print('n=',n,'schedule_histogram=',[counts[k] for k in range(1,n)])
    for k in range(1,25):
        aps={p:aprime(p) for p in range(1,k+1) if k%p==0}
        assert sum(aps.values())==2**k
        assert all(v%p==0 and v>0 for p,v in aps.items())
    print('FORMULA_CHECK_OK')

if __name__=='__main__':main()
