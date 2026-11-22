#!/usr/bin/env python3
"""Exact algebraic checks for a two-stage pulsed-population allocation theorem.

Standard library only.  Exact checks are certificates for the displayed witness;
the general optimization proof is analytic and is not established by sampling.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import sqrt
from random import Random

A = ((F(-3,2), F(15,4)), (F(1), F(-1,2)))
I = ((F(1), F(0)), (F(0), F(1)))

def mul(X, Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in (0,1)) for j in (0,1)) for i in (0,1))
def add(X,Y):
    return tuple(tuple(X[i][j]+Y[i][j] for j in (0,1)) for i in (0,1))
def smul(s,X):
    return tuple(tuple(s*X[i][j] for j in (0,1)) for i in (0,1))
def det(X):
    return X[0][0]*X[1][1] - X[0][1]*X[1][0]

def spectral(X):
    t=float(X[0][0]+X[1][1]); d=float(det(X))
    return (t + sqrt(t*t-4*d))/2

assert add(add(mul(A,A), smul(F(2),A)), smul(F(-3),I)) == ((F(0),F(0)),(F(0),F(0)))
Pplus = smul(F(1,4),add(A,smul(F(3),I)))
Pminus = smul(F(1,4),add(I,smul(F(-1),A)))
assert add(Pplus,Pminus)==I
assert mul(Pplus,Pplus)==Pplus and mul(Pminus,Pminus)==Pminus
assert mul(Pplus,Pminus)==((F(0),F(0)),(F(0),F(0)))
E = add(smul(F(2),Pplus),smul(F(1,8),Pminus))
assert E == ((F(53,64),F(225,128)),(F(15,32),F(83,64)))
assert det(E)==F(1,4)
assert E[0][0]+E[1][1]==F(17,8)
assert spectral(E)==2.0

q=F(13,50)
s1=F(3,5)
s2=F(13,30)
assert s1*s2==q
M=mul(((s1,F(0)),(F(0),s2)),E)
assert M[0][0]+M[1][1]==F(2033,1920)
assert det(M)==F(13,200)
assert 1-(M[0][0]+M[1][1])+det(M)==F(59,9600)>0
assert det(M)<1 and spectral(M)<1
assert 4*q>1  # uniform survival sqrt(q) has spectral radius 2 sqrt(q)

# Exact polynomial signs delimit the sharp optimal-budget threshold.
def poly(q): return 64*q*q-3887*q+1024
assert poly(F(1,4))>0
assert poly(q)>0
assert poly(F(27,100))<0
assert F(1,4)<q<F(27,100)<1
assert F(1,4)<F(53,83)  # unconstrained optimizer feasible at transition

with localcontext() as ctx:
    ctx.prec=70
    disc=Decimal(3887)**2-Decimal(4*64*1024)
    qcrit=(Decimal(3887)-disc.sqrt())/Decimal(128)
    assert Decimal('0.26459')<qcrit<Decimal('0.26460')
    assert qcrit<Decimal(53)/Decimal(83)
    print('critical product q* =',qcrit)

rng=Random(20260905)
for _ in range(300):
    qfloat=rng.uniform(0.002,0.998)
    xstar=min(1.0,max(qfloat,sqrt(qfloat*float(E[1][1])/float(E[0][0]))))
    Tstar=float(E[0][0])*xstar+float(E[1][1])*qfloat/xstar
    for k in range(20):
        x=qfloat+(1-qfloat)*k/19
        T=float(E[0][0])*x+float(E[1][1])*qfloat/x
        assert T>=Tstar-1e-12
print('PASS: rational projector/exponential identities; exact persistence reversal; 6000 sampled optimizer comparisons')
