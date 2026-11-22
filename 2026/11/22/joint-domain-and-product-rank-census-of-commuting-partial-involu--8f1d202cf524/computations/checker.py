#!/usr/bin/env python3
"""Independent finite checks for commuting partial involution tuple census."""
import itertools,math
from functools import lru_cache
from collections import Counter


def involutions_on(labels):
    labels=tuple(labels)
    if not labels:
        yield {}
        return
    x=labels[0]
    for m in involutions_on(labels[1:]):
        yield {**m,x:x}
    for i,y in enumerate(labels[1:],1):
        rest=labels[1:i]+labels[i+1:]
        for m in involutions_on(rest):
            yield {**m,x:y,y:x}

def partial_involutions(n):
    for mask in range(1<<n):
        dom=tuple(i for i in range(n) if mask>>i&1)
        for m in involutions_on(dom):
            yield tuple(m.get(i,-1) for i in range(n))

def commute(a,b):
    for i in range(len(a)):
        j=b[i]
        ab=a[j] if j>=0 else -1
        j=a[i]
        ba=b[j] if j>=0 else -1
        if ab!=ba:return False
    return True

def gaussian2(k,r):
    if r<0 or r>k:return 0
    num=den=1
    for j in range(r):
        num*=2**k-2**j
        den*=2**r-2**j
    assert num%den==0
    return num//den

def exponent_monomials(t):
    # Per point full-domain subset S and orbit index d: multiplicity Gaussian /d.
    from fractions import Fraction
    ans={}
    for k in range(t+1):
        for S in itertools.combinations(range(t),k):
            for r in range(k+1):
                d=2**r
                rank=tuple(d if i in S else 0 for i in range(t))
                key=(d,rank,d if k==t else 0)
                ans[key]=ans.get(key,0)+Fraction(gaussian2(k,r),d)
    return ans

def prediction(t,N):
    from fractions import Fraction
    ex=exponent_monomials(t)
    # EGF exponential recurrence, multivariate ranks and common intersection size
    a=[Counter() for _ in range(N+1)]
    a[0][((0,)*t,0)]=1
    for n in range(1,N+1):
        # n*a_n = sum_d d*e_d*a_{n-d}; integer n! coefficients for speed
        o=Counter()
        for (d,rank,product),coeff in ex.items():
            if d>n:continue
            for (r0,p0),value in a[n-d].items():
                o[(tuple(x+y for x,y in zip(rank,r0)),product+p0)]+=d*coeff*value
        a[n]=Counter({key:value/n for key,value in o.items()})
    from fractions import Fraction
    return [Counter({key:int(v*math.factorial(n)) for key,v in vals.items()}) for n,vals in enumerate(a)]

def brute(t,n):
    maps=list(partial_involutions(n))
    compat=[[commute(a,b) for b in maps] for a in maps]
    ranks=[sum(x>=0 for x in a) for a in maps]
    C=Counter()
    for inds in itertools.product(range(len(maps)),repeat=t):
        if any(not compat[inds[i]][inds[j]] for i in range(t) for j in range(i+1,t)):
            continue
        intersection=sum(all(maps[inds[i]][x]!=-1 for i in range(t)) for x in range(n))
        C[(tuple(ranks[i] for i in inds),intersection)]+=1
    return C,len(maps)

if __name__=='__main__':
    for t,n in [(1,5),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,0),(3,1),(3,2),(3,3),(3,4),(4,2),(4,3)]:
        actual,m=brute(t,n)
        expected=prediction(t,n)[n]
        if actual!=expected:
            print('FAILED',t,n,m,'actual',sum(actual.values()),'expected',sum(expected.values()),'differences',(actual-expected).most_common(5),(expected-actual).most_common(5))
            raise SystemExit(1)
        print('PASS',t,n,'partial_involutions',m,'tuple_count',sum(actual.values()),'joint_statistics',len(actual))
    print('ALL CHECKS PASS')
