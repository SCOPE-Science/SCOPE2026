#!/usr/bin/env python3
"""Reproduce an exact reset-trap transverse-autocovariance inverse theorem.

Only public scientific details are included in this standalone checker.
Requires Python 3, sympy, scipy and numpy. The mathematical proof is separate.
"""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np
from scipy.linalg import expm

checks=0

def eq(a,b,name='identity'):
    global checks
    assert a==b,(name,a,b)
    checks+=1

def near(a,b,tol=1e-10,name='numerical identity'):
    global checks
    assert abs(a-b)<tol*(1+abs(b)),(name,a,b)
    checks+=1

def model(r,b,d,v,Dt):
    S=2*d/(r+4*d)
    H=v*S/(r+b+d)
    V=(2*Dt+2*v*H)/(2*b+r)
    return S,H,V

def derivs(r,b,d,v,Dt):
    S,H,V=model(r,b,d,v,Dt)
    x,y=V,H
    out=[]
    for _ in range(4):
        out.append(x)
        x,y=-(r+b)*x+v*y, -(r+d)*y
    return out

def prony(c):
    c0,c1,c2,c3=c
    Delta=c0*c2-c1*c1
    if Delta==0:
        return ('single',-c1/c0)
    return ('two', (c1*c2-c0*c3)/Delta, (c1*c3-c2*c2)/Delta)

def solve_rates(c,v,Dt):
    c0,c1=c[:2]
    r=-2*(c1+Dt)/c0
    assert r>0
    p=prony(c)
    if p[0]=='single':
        l=p[1]
        d=l-r
        assert d>0
        K=2*v*v*d/(c0*(r+4*d))
        # Positive root b>d of (b-d)(b+d+r)=K.
        b=(-float(r)+math.sqrt(float((r+2*d)**2+4*K)))/2
        return r,b,float(d)
    S,P=p[1:]
    disc=S*S-4*P
    assert disc>=0
    l1=float((S-math.sqrt(float(disc)))/2)
    l2=float((S+math.sqrt(float(disc)))/2)
    p1,p2=l1-float(r),l2-float(r)
    assert p1>0 and p2>0
    # Choose the orientation of spectral poles by the measured stationary variance.
    e1=abs(float(model(float(r),p1,p2,float(v),float(Dt))[2]-c0))
    e2=abs(float(model(float(r),p2,p1,float(v),float(Dt))[2]-c0))
    if e1<=e2:return float(r),p1,p2
    return float(r),p2,p1

# Exact rational stationary generator and derivative tests on a nontrivial grid.
for i,j,k,l,m in product((1,2,3), (1,2,4), (1,2,3), (1,3), (1,2)):
    r,b,d,v,Dt=F(i,3),F(j,2),F(k,3),F(l,2),F(m,4)
    S,H,V=model(r,b,d,v,Dt)
    eq((4*d+r)*(1-2*S),r,'orientation generator')
    eq((r+b+d)*H,v*S,'mixed generator')
    eq((2*b+r)*V,2*Dt+2*v*H,'squared-position generator')
    c=derivs(r,b,d,v,Dt)
    eq(c[1],-Dt-r*V/2,'universal right slope')
    eq(c[2]+(b+d+2*r)*c[1]+(b+r)*(d+r)*c[0],0,'lag ODE')
    eq(c[3]+(b+d+2*r)*c[2]+(b+r)*(d+r)*c[1],0,'lag ODE derivative')
    p=prony(c)
    if p[0]=='two':
        eq(p[1],b+d+2*r,'sum of observable roots')
        eq(p[2],(b+r)*(d+r),'product of observable roots')
    else:
        # There can be a genuine single visible exponential, never a spurious repeated-root loss.
        eq(c[2]*c[0],c[1]**2,'single-mode geometry')
    rr,bb,dd=solve_rates(c,v,Dt)
    near(rr,float(r),name='recover r')
    near(bb,float(b),name='recover trap rate')
    near(dd,float(d),name='recover rotational diffusivity')

# Fully rational exact exceptional cancellation: C(t)=exp(-2t).
r,b,d,v,Dt=map(F,(1,3,1,5,F(3,2)))
S,H,V=model(r,b,d,v,Dt)
eq(V,F(1),'single-mode variance')
eq(v*H,F(2),'single-mode cross correlation')
eq(prony(derivs(r,b,d,v,Dt)),('single',F(2)),'exact hidden pole')
rr,bb,dd=solve_rates(derivs(r,b,d,v,Dt),v,Dt)
near(bb,3,name='hidden pole recovery');near(dd,1,name='visible pole recovery')

# Confluent double root has a nonzero Jordan coefficient and is not single exponential.
r,b,d,v,Dt=map(F,(1,2,2,3,1))
S,H,V=model(r,b,d,v,Dt)
eq(V,F(18,25),'confluent variance')
eq(v*H,F(4,5),'confluent coefficient')
c=derivs(r,b,d,v,Dt)
eq(c[0]*c[2]-c[1]**2,-(v*H)**2,'confluent determinant')
eq(prony(c),('two',F(6),F(9)),'confluent Prony')
rr,bb,dd=solve_rates(c,v,Dt)
near(bb,2,name='confluent beta');near(dd,2,name='confluent d')

# Independent matrix-generator calculation for each member of a sample grid.
for ii in range(30):
    r,b,d,v,Dt=(0.1+0.21*ii,0.25+0.14*ii,0.45+0.09*ii,0.7+0.03*ii,0.3+0.02*ii)
    s,H,V=model(r,b,d,v,Dt)
    # Stationary moments of observables (cos2theta, Y sintheta, Y^2).
    A=np.array([[-(4*d+r),0,0],[-v/2,-(b+d+r),0],[0,2*v,-(2*b+r)]],float)
    z=np.linalg.solve(A,-np.array([r,v/2,2*Dt]))
    near(z[0],1-2*s,name='generator angular moment')
    near(z[1],H,name='generator cross moment')
    near(z[2],V,name='generator variance')
    M=np.array([[-(b+r),v],[0,-(d+r)]],float)
    for t in (0.07,0.37,1.2,3.1):
        Cmatrix=(expm(M*t)@np.array([V,H]))[0]
        if abs(b-d)>1e-10:
            Cclosed=V*math.exp(-(b+r)*t)+v*H*(math.exp(-(d+r)*t)-math.exp(-(b+r)*t))/(b-d)
        else:
            Cclosed=(V+v*H*t)*math.exp(-(b+r)*t)
        near(Cmatrix,Cclosed,name='matrix semigroup vs explicit covariance')

print(f'PASS: {checks} exact/rational/numerical checks')
