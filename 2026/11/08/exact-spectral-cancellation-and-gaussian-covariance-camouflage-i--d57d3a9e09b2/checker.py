"""Separate finite checks for on/off harmonic covariance camouflage theorem.
Uses Python standard library; exact rational generator and moment recursions.
This program is a finite diagnostic, not a proof of statements for all parameters.
"""
from fractions import Fraction as F
from math import sqrt,exp,isclose
from itertools import product

def moments(a,b,k,D):
    t=a+b
    pi0=b/t; pi1=a/t
    m1=D/k
    m0=(2*D*pi0+b*m1)/a
    v=m0+m1
    n1=3*D*v/k
    n0=(12*D*m0+b*n1)/a
    return (m0,m1,v,n0,n1,n0+n1-3*v*v)

def matrix(M,v):
    return (M[0][0]*v[0]+M[0][1]*v[1],M[1][0]*v[0]+M[1][1]*v[1])

def residues(a,b,k,D):
    t=float(a+b);k=float(k);a=float(a);D=float(D)
    v=float(moments(F(str(a)),F(str(b)),F(str(k)),F(str(D)))[2])
    disc=sqrt((k+t)**2-4*a*k)
    low=(k+t-disc)/2; high=(k+t+disc)/2
    fast=(D-low*v)/(high-low)
    return low,high,v-fast,fast

n=0
rates=[F(1,4),F(1,2),F(1),F(2),F(3),F(5),F(8)]
for a,b,k,D in product(rates,rates,rates,[F(1,3),F(1),F(3)]):
    t=a+b; m0,m1,v,n0,n1,kap=moments(a,b,k,D)
    pi0=b/t;pi1=a/t
    assert 2*D*pi0-a*m0+b*m1==0
    assert 2*D*pi1+a*m0-(b+2*k)*m1==0
    assert 12*D*m0-a*n0+b*n1==0
    assert 12*D*m1+a*n0-(b+4*k)*n1==0
    assert kap==6*D*D*b*(t*t+2*k*(2*a+b))/(a*a*k*t*t)
    z=(m0,m1); M=((-a,b),(a,-b-k))
    seq=[]
    for j in range(7):
        seq.append(sum(z));z=matrix(M,z)
    assert seq[0]==v and seq[1]==-D
    assert seq[2]==D*k*(a-b)/t
    for j in range(5):
        assert seq[j+2]==-(k+t)*seq[j+1]-a*k*seq[j]
    low,high,slow,fast=residues(a,b,k,D)
    h=float(t*t+2*k*(b-a))
    assert fast*h <= 1e-9
    for lag in (0.0,0.07,0.25,1.0,2.0):
        rhs=slow*exp(-low*lag)+fast*exp(-high*lag)
        # Matrix ODE solution: e^{M t} = e^{-Tt/2}(cosh(delta t/2) I + 2 sinh(delta t/2)/delta*(M+T/2 I)).
        center=(float(k+t))/2;half=(high-low)/2
        import math
        c=math.cosh(half*lag);sh=math.sinh(half*lag)/half
        zp0=float(m0);zp1=float(m1)
        zsum=exp(-center*lag)*(c*(zp0+zp1)+sh*(-float(k)*zp1+center*(zp0+zp1)))
        assert isclose(rhs,zsum,rel_tol=1e-11,abs_tol=1e-10), (a,b,k,D,lag,rhs,zsum)
    n+=1
# Critical identity for exact rational rates: a>b and k=(a+b)^2/(2(a-b)).
for a,b in product(rates,rates):
    if a<=b:continue
    k=(a+b)**2/(2*(a-b)); D=F(5,3);t=a+b
    m0,m1,v,n0,n1,kap=moments(a,b,k,D)
    assert v==2*D/t
    assert kap==36*D*D*b/(a*t*t)
    assert kap/(3*v*v)==3*b/a
    low,high,slow,fast=residues(a,b,k,D)
    assert abs(fast)<1e-10 and isclose(low,float(t)/2,rel_tol=1e-12)
    n+=1
print(f'PASS: {n} exact-rational parameter cases with 5 independent-lag matrix exponential checks each')
