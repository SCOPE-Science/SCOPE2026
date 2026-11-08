#!/usr/bin/env python3
"""Independent cyclic gap-color checker; standard-library only."""
from itertools import product
from collections import Counter,deque
from math import comb

def expected(n):
    k=n//2
    if n%2: return n*3*2**(k-1),[n*3*2**(k-1)]
    sizes=[]
    for p in range(k+1):
        if (2*p-k)%3==0:
            if p==0 or p==k:sizes += [1]*6
            else:sizes += [3*comb(k,p)]*2
    return 2*(2**k+2*(-1)**k),sorted(sizes)

def states(n):
    k=n//2
    # Every gap between occupied columns is at least two; slack is n-2k (0 or 1).
    for s in range(n):
        for gaps_extra in ([[0]*k] if n%2==0 else [[int(j==0) for j in range(k)]]):
            # For odd n, generate all rotations via s. For even n, repeated
            # anchors are deduplicated below.
            cols=[];x=s
            for d in gaps_extra:
                cols.append(x);x=(x+2+d)%n
            if x!=s:raise AssertionError('gap sum')
            for rows in product(range(3),repeat=k):
                if any(gaps_extra[i]==0 and rows[i]==rows[(i+1)%k] for i in range(k)):
                    continue
                yield tuple(sorted(zip(cols,rows)))

def run(n):
    S=set(states(n));expected_count,sizes=expected(n)
    assert len(S)==expected_count,(n,len(S),expected_count)
    unvisited=set(S);comps=[];arcs=0
    while unvisited:
        root=unvisited.pop();todo=[root];length=0
        while todo:
            A=todo.pop();length+=1
            for i,(col,row) in enumerate(A):
                for nc,nr in [(col,(row+1)%3),(col,(row+2)%3),((col+1)%n,row),((col-1)%n,row)]:
                    if any(c==nc for j,(c,r) in enumerate(A) if i!=j):continue
                    B=tuple(sorted(A[:i]+A[i+1:]+((nc,nr),)))
                    if B in S:
                        arcs+=1
                        if B in unvisited:unvisited.remove(B);todo.append(B)
        comps.append(length)
    assert sorted(comps)==sizes,(n,sorted(comps),sizes)
    return f'n={n} states={len(S)} components={len(comps)} profile={dict(sorted(Counter(comps).items()))} directed_arcs={arcs}'

if __name__=='__main__':
    for n in range(5,20):print(run(n))
    print('PASS: cyclic-gap enumeration and full transition graph checks')
