#!/usr/bin/env python3
"""Independent finite-size checks for the binary multiset matching law.

No external dependencies. All exact finite checks use fractions; asymptotic
checks use log-gamma mass functions and are diagnostic, not an infinite proof.
"""
from fractions import Fraction
from math import comb, lgamma, log, exp, sqrt, erf, isclose
from itertools import combinations

def ph(x):
    return (1+erf(x/sqrt(2)))/2

def limit(c):
    h = c*c+(1-c)*(1-c)
    v = 4*c*c*(1-c)*(1-c)
    y = sqrt(2*v*h/(h-v)*log(2*sqrt(h/v)))
    return 0.5+1-ph(y/sqrt(h))-2*(1-ph(y/sqrt(v)))

def conditioned_limit(c):
    h=c*c+(1-c)*(1-c)
    v=4*c*c*(1-c)*(1-c)
    y=sqrt(v*h/(h-v)*log(h/v))
    return 2*(ph(y/sqrt(v))-ph(y/sqrt(h)))

def exact_W(n,a):
    b=n-a
    denom=comb(n,a)
    out={}
    for x in range(max(0,2*a-n),a+1):
        w=n-2*a+2*x
        out[w]=Fraction(comb(a,x)*comb(b,a-x),denom)
    return out

def numeric_tv(n,a, conditioned=False):
    h=(a*a+(n-a)*(n-a))/n
    d=exact_W(n,a)
    q=[exp(-h+j*log(h)-lgamma(j+1)) for j in range(n+int(10*sqrt(n))+20)]
    if conditioned:
        parity=n%2
        normalization=sum(q[j] for j in range(len(q)) if j%2==parity)
        return 0.5*sum(abs(float(d.get(j,0))-(q[j]/normalization if j%2==parity else 0)) for j in range(len(q)))
    return 0.5*sum(abs(float(d.get(j,0))-q[j]) for j in range(len(q)))

assertions=0
for n in range(2,12):
    for a in range(1,n):
        counts={}
        for subset in combinations(range(n),a):
            word=['B']*n
            for j in subset: word[j]='A'
            w=sum(word[j]==('A' if j<a else 'B') for j in range(n))
            counts[w]=counts.get(w,0)+1
        dist=exact_W(n,a)
        assert sum(dist.values())==1
        assertions+=1
        for w in range(n+1):
            assert dist.get(w,Fraction(0))==Fraction(counts.get(w,0),comb(n,a))
            assertions+=1
        mu=sum(w*p for w,p in dist.items())
        var=sum((w-mu)**2*p for w,p in dist.items())
        assert mu==Fraction(a*a+(n-a)*(n-a),n)
        assert var==Fraction(4*a*a*(n-a)*(n-a),n*n*(n-1))
        assertions+=2

print('Exact exhaustive assertions:',assertions)
for c in (0.1,0.25,0.5):
    print('composition',c,'limit',round(limit(c),12),'parity-conditioned limit',round(conditioned_limit(c),12))
    for n in (100,400,1600,6400):
        a=round(c*n)
        print('  n',n,'TV',round(numeric_tv(n,a),10),'conditional',round(numeric_tv(n,a,True),10))
assert abs(limit(0.5)-0.533230687960033)<1e-11
assert abs(conditioned_limit(0.5)-0.166064074983513)<1e-11
print('All checks PASS')
