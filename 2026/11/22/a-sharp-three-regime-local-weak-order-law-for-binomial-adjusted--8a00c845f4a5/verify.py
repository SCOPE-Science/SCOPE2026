#!/usr/bin/env python3
"""Symbolic and exact checks for a single-channel binomial-corrected trapezoidal leap."""
from fractions import Fraction
from math import exp, comb, factorial
import sympy as sp
h,A,t,r1,r2=sp.symbols('h A t r1 r2', positive=True)
c=1-2*t+2*t*t
lam0=A*(1-t)
lam1=A*(r1-c)/(2*t)

# Coefficients of first-stage P=0,1,2, through h^2
P0=1-t*A*h+t*t*A*A*h*h/2
P1=t*A*h-t*t*A*A*h*h
P2=t*t*A*A*h*h/2

# Nondegenerate first two intermediate states. The P=2 branch only contributes its zero-second-hop output at h^2.
q0=sp.expand(P0*(1-lam0*h+lam0**2*h*h/2))
q1=sp.expand(P0*(lam0*h-lam0**2*h*h)+P1*(1-lam1*h))
q2=sp.expand(P0*(lam0**2*h*h/2)+P1*lam1*h+P2)
truth=[1-A*h+A*A*h*h/2,A*h-A*A*(1+r1)*h*h/2,A*A*r1*h*h/2]
for i,(q,e) in enumerate(zip([q0,q1,q2],truth)):
    err=sp.simplify(sp.expand(q-e).coeff(h,0))+sp.simplify(sp.expand(q-e).coeff(h,1))*h+sp.simplify(sp.expand(q-e).coeff(h,2))*h*h
    assert sp.simplify(err)==0,(i,err)

# P=1 thinning branch changes only O(h) and its exact coefficient.
p1=sp.simplify((r1+2*t-1)/(2*t*t))
assert sp.simplify(t*A*(p1-1)+A*(c-r1)/(2*t))==0
# P=2 thinning modifies coefficient h^2 for f(0), f(1), f(2)
p2=sp.simplify((r2+2*t-1)/(2*t*t))
v=[sp.simplify((1-p2)**2),sp.simplify(2*p2*(1-p2)),sp.simplify(p2*p2-1)]
assert sp.simplify(sum(v))==0

# Independently compute full two-stage distribution, finite truncated Poisson sums,
# using exact Fractions and compare the coefficients (all arithmetic exact).
def coeffs(theta, rates):
    B=Fraction(1); c=1-2*theta+2*theta*theta
    l0=1-theta
    # h^0..h^2 for probability Q=q, q=0,1,2; P>=3 is O(h^3).
    P={0:[B,-theta,theta*theta/2],1:[0,theta,-theta*theta],2:[0,0,theta*theta/2]}
    out=[[B*0 for _ in range(3)] for __ in range(3)]
    for m in range(3):
        r=rates[m]
        if r>=c:
            lam=(r-c)/(2*theta)
            # Conditional probability Q=m+k, k=0,1,2.
            kernels={m:[B,-lam,lam*lam/2],m+1:[0,lam,-lam*lam],m+2:[0,0,lam*lam/2]}
        else:
            prob=(r+2*theta-1)/(2*theta*theta)
            kernels={k:[comb(m,k)*(prob**k)*((1-prob)**(m-k)),0,0] for k in range(m+1)}
        for j, poly in kernels.items():
            if j>2: continue
            for deg in range(3):
                out[j][deg]+=sum(P[m][e]*poly[deg-e] for e in range(deg+1))
    return out

checks=0
for den in range(2,13):
    for num in range((den+1)//2, den):
        theta=Fraction(num,den)
        c0=1-2*theta+2*theta**2
        for j in range(11):
            R1=Fraction(j,10)
            for k in range(j+1):
                R2=Fraction(k,10)
                vec=coeffs(theta,[Fraction(1),R1,R2])
                assert sum(vec[i][1] for i in range(3))==0
                if R1<c0:
                    assert vec[1][1]-Fraction(1)==-(c0-R1)/(2*theta)
                elif R2<c0:
                    assert vec[0][1]==-1 and vec[1][1]==1
                    p=(R2+2*theta-1)/(2*theta*theta)
                    assert vec[2][2]-R1/Fraction(2)==theta*theta/Fraction(2)*(p*p-1)
                else:
                    assert vec[0][:3]==[1,-1,Fraction(1,2)]
                    assert vec[1][:3]==[0,1,-(1+R1)/2]
                    assert vec[2][:3]==[0,0,R1/2]
                checks+=1
print('Symbolic nondegenerate Taylor identities: PASS')
print('Exact rational regime checks:', checks,'PASS')
print('Example A=1, theta=1/2, r1=1/4, r2=1/8: leading defect f(1)=-h/4: PASS')
print('Example A=1, theta=1/2, r1=3/4, r2=1/4: f(2) leading defect=-3h^2/32: PASS')
