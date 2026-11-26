#!/usr/bin/env python3
"""Finite corroboration of the sharp three-erasure spectral theorem; stdlib only."""
import itertools, math

def top_shift(p,q,r):
    # Largest real root of mu^3-(p^2+q^2+r^2)mu-2pqr=0.
    s=p*p+q*q+r*r
    if s<1e-25:
        return 0.0
    arg=3.0*math.sqrt(3.0)*p*q*r/s**1.5
    arg=max(-1.0,min(1.0,arg))
    return 2.0*math.sqrt(s/3.0)*math.cos(math.acos(arg)/3.0)

def gram_top(n,tup):
    k=lambda d:1.0+2.0*math.cos(2.0*math.pi*d/n)
    a,b,c=tup
    return 3.0+top_shift(k(a-b),k(a-c),k(b-c))

def exact_best(n):
    k=lambda d:1.0+2.0*math.cos(2.0*math.pi*d/n)
    a,b=k(1),k(2)
    return 3.0+(b+math.sqrt(b*b+8.0*a*a))/2.0

def is_consecutive(n,e):
    return any(set(e)=={j%n,(j+1)%n,(j+2)%n} for j in e)

comparisons=0
for n in range(6,37):
    bound=exact_best(n)
    winners=0
    for e in itertools.combinations(range(n),3):
        val=gram_top(n,e)
        consecutive=is_consecutive(n,e)
        # Nearest competing gaps become small, so reserve accurate tolerance.
        if val>bound+2.0e-10*max(1.0,abs(bound)):
            raise AssertionError(('above-sharp',n,e,val,bound))
        equal=abs(val-bound)<=3.0e-10*max(1.0,abs(bound))
        if equal!=consecutive:
            raise AssertionError(('equality-class',n,e,val,bound))
        if equal:
            winners+=1
        comparisons+=1
    if winners!=n:
        raise AssertionError(('count',n,winners))
    if n-bound<=0:
        raise AssertionError(('positivity',n,bound))

assert abs(gram_top(6,(0,1,2))-(3+2*math.sqrt(2)))<1e-11
assert abs(gram_top(6,(0,1,3))-(3+math.sqrt(5)))<1e-11
assert abs(gram_top(6,(0,2,4))-3)<1e-11
for n in (49,64,101,256):
    for e in ((0,1,2),(0,1,3),(0,2,4),(0,n//3,n//2)):
        assert gram_top(n,e)<=exact_best(n)+1e-9
        comparisons+=1
print('VERIFY_OK',comparisons,'finite comparisons; exhaustive N=6..36, unique consecutive worst erasures')
