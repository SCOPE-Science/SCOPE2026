"""Exhaustive Gaussian-order verification for split-hypersimplex normal cones.
Each permutation of n independent continuous Gaussian coordinates is equally likely.
Python 3 standard library only.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial
from fractions import Fraction


def check(n,h,k,r):
    q=n-h; lo=max(0,k-q);hi=min(k,h)
    assert lo<r<hi
    N=lambda t: comb(h,t)*comb(q,k-t)
    M=comb(n,k)
    S=sum(N(t) for t in range(lo,r))
    B=sum(N(t) for t in range(r,hi+1))
    H=frozenset(range(h))
    feasible=[frozenset(x) for x in combinations(range(n),k) if len(H.intersection(x))<=r]
    observed=Counter()
    for perm in permutations(range(n)):
        top=frozenset(perm[:k])
        if len(top.intersection(H))<=r: v=top
        else:
            topH=[a for a in perm if a<h][:r]
            topQ=[a for a in perm if a>=h][:k-r]
            v=frozenset(topH+topQ)
        if n<=6: # genuinely independent exhaustive optimization for small cases
            vals={a:n-j for j,a in enumerate(perm)}
            assert sum(vals[i] for i in v)==max(sum(vals[i] for i in y) for y in feasible)
        observed[v]+=1
    assert len(observed)==len(feasible)
    for v in feasible:
        t=len(v.intersection(H))
        expect=Fraction(factorial(n),M) if t<r else Fraction(factorial(n)*B,M*N(r))
        assert observed[v]==expect,(n,h,k,r,observed[v],expect)
    pred=Fraction(S,M*M)+Fraction(B*B,M*M*N(r))
    emp=sum((Fraction(c,factorial(n))**2 for c in observed.values()),Fraction())
    assert pred==emp,(pred,emp)
    return str(pred)

if __name__=='__main__':
    total=0
    for n in range(4,9):
        for h in range(1,n):
            for k in range(1,n):
                lo=max(0,k-(n-h));hi=min(k,h)
                for r in range(lo+1,hi):
                    result=check(n,h,k,r)
                    total+=1
                    if n==8 and (h,k,r) in [(3,4,2),(4,4,2)]:print('n,h,k,r,collision',n,h,k,r,result)
    print('SPLIT_ANGLE_EXACT_PASS',total)
