#!/usr/bin/env python3
"""Independent finite checks for rectangular C2-group transversal counts."""
import itertools
from collections import defaultdict, Counter
from math import factorial, comb

def by_matching(r,s):
    # Algebraic coefficient count computed by multiplying local b-patterns.
    choices=Counter()
    for bs in itertools.product((0,1),repeat=2*r):
        if sum(bs)!=r: continue
        degrees=tuple((bs[2*i]==0)+(bs[2*i+1]==1) for i in range(r))
        choices[degrees]+=1
    dp={tuple([0]*r):1}
    for _ in range(s):
        out=defaultdict(int)
        for a,v in dp.items():
            for b,w in choices.items():
                c=tuple(x+y for x,y in zip(a,b))
                if all(x<=s for x in c):out[c]+=v*w
        dp=out
    return dp.get(tuple([s]*r),0)*factorial(r)**(2*s)*factorial(s)**(2*r)

def by_permutations(r,s):
    elems=list(itertools.product(range(r),range(2),range(s)))
    n=len(elems)
    count=0
    for pi in itertools.permutations(range(n)):
        products={(x[0],x[1]^elems[pi[j]][1],elems[pi[j]][2]) for j,x in enumerate(elems)}
        if len(products)==n:count+=1
    return count

def independent_single_column(r):
    return factorial(r)**2 * comb(r,r//2) if r%2==0 else 0

def independent_two_row(s):
    return (4**s)*factorial(s)**4*sum(comb(s,k)*2**(s-k)*comb(k,k//2)**2 for k in range(0,s+1,2))

checks=0
for r,s in [(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(3,1),(4,1)]:
    a=by_permutations(r,s)
    b=by_matching(r,s)
    assert a==b, (r,s,a,b)
    checks+=1
    print('PERM',r,s,a)
for r in range(1,5):
    for s in range(1,5):
        a=by_matching(r,s)
        assert a==by_matching(s,r)
        assert (a>0)==((r*s)%2==0)
        if s==1:assert a==independent_single_column(r)
        if r==2:assert a==independent_two_row(s)
        checks+=1
print('FORMULA',2,3,by_matching(2,3))
print('FORMULA',2,4,by_matching(2,4))
print('VERIFY_OK cases=%d brute_profiles=8 symmetry_and_boundary=16'%checks)
