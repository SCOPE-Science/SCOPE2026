#!/usr/bin/env python3
from fractions import Fraction
import math

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def scale(q,a):
    return tuple(q*x for x in a)

for n in range(3,101):
    v={}
    v[1]=tuple(range(1,n+1))
    for k in range(2,n+1):
        v[k]=tuple(list(range(2,k+1))+[1]+list(range(k+1,n+1)))
    d={k:sub(v[k],v[1]) for k in range(2,n+1)}

    for k in range(2,n+1):
        assert dot(d[k],d[k])==k*(k-1)
        for ell in range(k+1,n+1):
            assert dot(d[k],d[ell])==0

    # Inradius facet identity.
    A=sum(1/math.sqrt(k*(k-1)) for k in range(2,n+1))
    B=math.sqrt((n-1)/n)
    r=1/(A+B)
    assert abs((1-r*A)/B-r)<2e-13

    # All-vertex circumsphere.
    C2=Fraction(n*(n*n-1),12)
    halfsum=tuple(
        Fraction(sum(d[k][j] for k in range(2,n+1)),2)
        for j in range(n)
    )
    for k in range(1,n+1):
        rel=tuple(Fraction(v[k][j]-v[1][j])-halfsum[j] for j in range(n))
        assert sum(x*x for x in rel)==C2

    q=min(q for q in range(2,n) if q*(q+1)>=2*n)
    assert q*(q-1)<2*n<=q*(q+1)
    m=n-q+1
    mu=Fraction(n*(m-1)*(q-2),q)
    lam={
        k: Fraction(1,2)*(1-mu/Fraction(k*(k-1),1))
        for k in range(m,n+1)
    }
    assert all(x>0 for x in lam.values())
    assert sum(lam.values())==1

    center_rel=[Fraction(0) for _ in range(n)]
    for k,w in lam.items():
        for j in range(n):
            center_rel[j]+=w*d[k][j]

    R2=Fraction(1,4)*(
        sum(k*(k-1) for k in range(m,n+1))
        -mu*(q-2)
    )

    contacts=[]
    for k in range(1,n+1):
        rel=[
            Fraction(v[k][j]-v[1][j])-center_rel[j]
            for j in range(n)
        ]
        dist2=sum(x*x for x in rel)
        assert dist2<=R2
        if dist2==R2:
            contacts.append(k)

    expected=list(range(m,n+1))
    if q*(q+1)==2*n:
        expected=[m-1]+expected
    assert contacts==expected,(n,q,m,contacts,expected)

    if n>=4:
        assert R2<C2

print("VERIFY_OK stack-sorting-right-simplex n=3..100 exact_MEB=yes")
