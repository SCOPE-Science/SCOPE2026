#!/usr/bin/env python3
"""Standalone exact checks for a sparse balanced-bipartite peak law."""
from fractions import Fraction
from itertools import combinations, product
from collections import defaultdict
from math import comb, factorial

def side_words(n):
    for pos in combinations(range(2*n),n):
        aa=set(pos)
        yield tuple(0 if j in aa else 1 for j in range(2*n))

def conditional_pmf(word,p):
    q=1-p; counts=[0,0]
    pmf={0:Fraction(1)}
    for side in word:
        prob=q**counts[1-side]
        next_pmf=defaultdict(Fraction)
        for s,weight in pmf.items():
            next_pmf[s+1]+=weight*prob
            next_pmf[s]+=weight*(1-prob)
        pmf=next_pmf
        counts[side]+=1
    return pmf

def direct_pmf(n,p):
    edgepairs=[(a,b) for a in range(n) for b in range(n)]
    ans=defaultdict(Fraction)
    for word in side_words(n):
        vertices=[]; c=[0,0]
        for side in word:
            vertices.append((side,c[side]));c[side]+=1
        for m in range(1 << (n*n)):
            nedge=m.bit_count()
            weight=p**nedge*(1-p)**(n*n-nedge)/comb(2*n,n)
            peaks=0
            for j,(side,k) in enumerate(vertices):
                def present(v):
                    if v[0]==side:return False
                    a,b=(k,v[1]) if side==0 else (v[1],k)
                    return bool(m >> (a*n+b)&1)
                peaks+=int(not any(present(v) for v in vertices[:j]))
            ans[peaks]+=weight
    return ans

def mixture_pmf(n,p):
    ans=defaultdict(Fraction)
    for word in side_words(n):
        for k,v in conditional_pmf(word,p).items():
            ans[k]+=v/comb(2*n,n)
    return ans

def infinite_moments(p):
    q=1-p;r=(1+q)/2;s=(1+q*q)/2
    mean=1/(1-r)
    second=1/(1-s)+(1/(1-r))*(1/(1-s)+q/(1-q))
    var=second-mean**2
    assert var==Fraction(2,1)/(1+q),(var,p)
    return mean,var

for n in (1,2,3):
    for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
        a=direct_pmf(n,p);b=mixture_pmf(n,p)
        assert {k:v for k,v in a.items() if v}=={k:v for k,v in b.items() if v},(n,p,a,b)
        assert sum(a.values())==1
        mean=sum(k*v for k,v in a.items())
        expected=2*n*(1-(1-p)**(n+1))/((n+1)*p)
        assert mean==expected,(n,p,mean,expected)
        print('EXHAUSTIVE_INDEPENDENT_WORD_EDGE_ENUMERATION_PASS',n,str(p), 'total_outcomes',comb(2*n,n)*2**(n*n))
# Independent finite fair-word enumeration of the environmental second moment.
for m in (5,7,10):
    for p in (Fraction(1,3),Fraction(1,5)):
        q=1-p; r=(1+q)/2; s=(1+q*q)/2
        first=Fraction(0); second=Fraction(0)
        for word in product((0,1),repeat=m):
            counts=[0,0]; value=Fraction(0)
            for side in word:
                value+=q**counts[1-side]
                counts[side]+=1
            first+=value/Fraction(2**m)
            second+=value**2/Fraction(2**m)
        predicted_first=sum(r**(i-1) for i in range(1,m+1))
        predicted_second=sum(s**(i-1) for i in range(1,m+1))
        for i in range(1,m+1):
            for j in range(i+1,m+1):
                predicted_second+=(s**(i-1)+q**i)*r**(j-i-1)
        assert first==predicted_first and second==predicted_second,(m,p)
        print('INDEPENDENT_FAIR_WORD_FIRST_SECOND_MOMENTS_PASS',m,str(p))
for p in (Fraction(1,2),Fraction(1,3),Fraction(1,7),Fraction(1,101),Fraction(1,10001)):
    mean,var=infinite_moments(p)
    print('EXACT_INFINITE_CONDITIONAL_MEAN_VARIANCE_IDENTITY_PASS',str(p),'mean',str(mean),'var',str(var))
print('VERIFY_OK')
