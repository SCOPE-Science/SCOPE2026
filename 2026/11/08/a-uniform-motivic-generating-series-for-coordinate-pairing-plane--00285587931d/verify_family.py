"""Standalone verification of the first four dimensions of the matching-plane union.
Pure Python; exact finite-field projective point enumeration and coefficient arithmetic.
"""
from fractions import Fraction
from math import factorial
from itertools import product
from collections import Counter

def matchings(remaining):
    if not remaining:
        yield ()
        return
    i,*tail=remaining
    for j,k in enumerate(tail):
        for m in matchings(tail[:j]+tail[j+1:]):
            yield ((i,k),)+m

def canonical(v,q):
    v=tuple(v)
    u=pow(next(x for x in v if x), -1, q)
    return tuple((u*x)%q for x in v)

def directly(q,m):
    out=set()
    for matching in matchings(list(range(2*m))):
        for entries in product(range(q),repeat=m):
            if not any(entries):
                continue
            v=[0]*(2*m)
            for (i,j),a in zip(matching,entries):
                v[i],v[j]=a,(-a)%q
            out.add(canonical(v,q))
    return len(out)

def formula(q,m):
    # Coefficient of t^(2m) in cosh(t)*Phi(t)^R, via ordinary truncation
    r=(q-1)//2
    v=[Fraction(0) for _ in range(m+1)]
    v[0]=Fraction(1)
    for _ in range(r):
        n=[Fraction(0) for _ in range(m+1)]
        for a in range(m+1):
            for b in range(m-a+1):
                n[a+b]+=v[a]/factorial(b)**2
        v=n
    x=sum(v[m-j]/factorial(2*j) for j in range(m+1))
    n=factorial(2*m)*x-1
    assert n.denominator==1 and n.numerator%(q-1)==0
    return n.numerator//(q-1)

P = {
    1:lambda q:1,
    2:lambda q:3*q,
    3:lambda q:15*q*q-30*q+25,
    4:lambda q:105*q**3-525*q*q+1120*q-917,
}
for m in (1,2,3,4):
    for q in (3,5,7):
        a=directly(q,m)
        b=formula(q,m)
        c=P[m](q)
        assert a==b==c, (m,q,a,b,c)
        print('m',m,'q',q,'points',a)
print('PASS')
