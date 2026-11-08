#!/usr/bin/env python3
"""Reproduce exact local linearization of a deterministic circle EMA map."""
import math
import sympy as sp
b,theta,c,lam=sp.symbols('b theta c lam',positive=True,real=True)
A=sp.Matrix([[-theta*(1-c),-theta],[c,-1]])
C=sp.Matrix([[-theta*c,theta],[0,0]])
B=sp.eye(2)+b*A+b*b*C
assert sp.simplify(A.det()-theta)==0
assert sp.simplify(A.trace()-(theta*(c-1)-1))==0
assert sp.simplify((lam*sp.eye(2)-A).det()-(lam**2+(1+theta*(1-c))*lam+theta))==0
assert sp.simplify(B.det()-(1-b)*(1-theta*b*(1-c)))==0

def one_step(phi,ux,uy,t,th,cc):
    beta=t**(-0.5)
    uxnew=(1-beta)*ux+beta*cc*math.sin(phi)
    uynew=(1-beta)*uy+beta*(1-cc*math.cos(phi))
    q=math.cos(phi)*uxnew+math.sin(phi)*uynew
    phinew=phi-math.atan(th*beta*q)
    return (phinew,uxnew,uynew)

# Numerical differentiation at exact equilibrium: columns (angle, old-x-memory, old-y-memory).
for th,cc,t in [(0.5,0.0,100),(0.5,4.0,100),(0.3,-2.0,81),(0.8,3.0,625)]:
    beta=t**(-0.5)
    expected=[[1-th*beta*(1-cc)-th*cc*beta*beta,-th*beta*(1-beta),0],
              [cc*beta,1-beta,0],[0,0,1-beta]]
    y0=1-cc;h=1e-6
    for j in range(3):
        plus=[0.0,0.0,y0];minus=plus.copy()
        plus[j]+=h;minus[j]-=h
        rp=one_step(*plus,t,th,cc);rm=one_step(*minus,t,th,cc)
        for i in range(3):
            measured=(rp[i]-rm[i])/(2*h)
            assert abs(measured-expected[i][j])<1e-7,(th,cc,t,i,j,measured,expected[i][j])
print('Symbolic identities and 36 original-map Jacobian checks passed.')
