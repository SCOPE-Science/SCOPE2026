#!/usr/bin/env python3
"""Exact rational and independent semigroup checks for a coordinate-reset gyrator.
Standard library only. Run: python3 checker.py
"""
from fractions import Fraction as F
import math
import random

def solve3(M, b):
    A = [list(map(F, row)) + [F(rhs)] for row, rhs in zip(M,b)]
    for j in range(3):
        k=next(i for i in range(j,3) if A[i][j])
        A[j],A[k]=A[k],A[j]
        d=A[j][j]
        for v in range(j,4): A[j][v]/=d
        for i in range(3):
            if i!=j:
                z=A[i][j]
                for v in range(j,4):A[i][v]-=z*A[j][v]
    return [row[3] for row in A]

def compute(a,b,c,dx,dy,r):
    den=b*(2*a+r)*(a+b+r)-c*c*(2*(a+b)+r)
    X=2*(dx*b*(a+b+r)-dx*c*c+dy*c*c)/den
    Y=(2*dx*c*c+dy*((2*a+r)*(a+b+r)-2*c*c))/den
    Z=c*(2*b*dx+(2*a+r)*dy)/den
    Jc=c*(4*(dx-dy)*(a*b-c*c)+2*r*(b*dx-(a+b)*dy)-dy*r*r)/den
    Jlag=2*c*(2*(dx-dy)*(a*b-c*c)+b*r*(2*dx-dy))/den
    return X,Y,Z,Jc,Jlag,den

rng=random.Random(241126)
checks=0
for i in range(420):
    a=F(rng.randint(2,15),rng.randint(1,5))
    b=F(rng.randint(2,15),rng.randint(1,5))
    c=F(rng.randint(1,9),20)*min(a,b)
    dx=F(rng.randint(1,20),rng.randint(1,6))
    dy=F(rng.randint(1,20),rng.randint(1,6))
    r=F(rng.randint(0,25),rng.randint(1,6))
    assert a*b>c*c
    X,Y,Z,Jc,Jlag,den=compute(a,b,c,dx,dy,r)
    assert den>0;checks+=1
    xx,yy,zz=solve3([[2*a+r,0,-2*c],[0,2*b,-2*c],[-c,-c,a+b+r]],[2*dx,2*dy,0])
    assert (X,Y,Z)==(xx,yy,zz);checks+=1
    assert Jc==c*(xx-yy)+(a-b)*zz;checks+=1
    assert Jlag==c*(xx-yy)+(a+r-b)*zz;checks+=1
    assert Jlag-Jc==r*zz;checks+=1
    # The two sign classifications have direct, independent inequalities.
    if dx>=dy:
        assert Jlag>=0;checks+=1
    if dx<=dy:
        assert Jc<=0;checks+=1
    if dx<=dy/2:
        assert Jlag<=0;checks+=1
    if dx>dy:
        A0=4*(dx-dy)*(a*b-c*c)
        B0=2*(b*dx-(a+b)*dy)
        root=(float(B0)+math.sqrt(float(B0*B0+4*dy*A0)))/(2*float(dy))
        if root>1e-8 and abs(float(r)-root)>1e-8:
            assert (Jc>0)==(float(r)<root);checks+=1
    if dy/2<dx<dy:
        root=2*(dy-dx)*(a*b-c*c)/(b*(2*dx-dy))
        if r!=root:
            assert (Jlag>0)==(r>root);checks+=1
    # Compare semigroup covariance, directly multiplying independent exponentials.
    aa,bb,cc,rr=map(float,(a,b,c,r))
    xf,yf,zf=map(float,(X,Y,Z))
    m=(aa+rr+bb)/2
    eta=math.sqrt(((aa+rr-bb)/2)**2+cc**2)
    lag=0.2+0.11*(i%13)
    pref=math.exp(-m*lag)
    e12=pref*cc*math.sinh(eta*lag)/eta
    e11=pref*(math.cosh(eta*lag)-(aa+rr-bb)*math.sinh(eta*lag)/(2*eta))
    e22=pref*(math.cosh(eta*lag)+(aa+rr-bb)*math.sinh(eta*lag)/(2*eta))
    anti=(xf-yf)*e12+zf*(e22-e11)
    expect=float(Jlag)*pref*math.sinh(eta*lag)/eta
    assert math.isclose(anti,expect,rel_tol=1e-10,abs_tol=1e-10);checks+=1

# Test exact positive-r thresholds with rational illustrations.
a,b,c=F(2),F(1),F(1,2)
for dx,dy in [(F(2),F(1)),(F(1),F(1)),(F(3,4),F(1)),(F(2,5),F(1))]:
    for r in [F(1,20),F(1),F(2),F(10),F(100)]:
        X,Y,Z,jc,jlag,den=compute(a,b,c,dx,dy,r)
        if dx>dy:
            assert jlag>0; checks+=1
        if dx==dy:
            assert jc<0 and jlag>0;checks+=1
        if dx<dy:
            assert jc<0;checks+=1
print(f'PASS {checks} deterministic assertions; exact rational moment and sign checks, independent semigroup covariance checks')
