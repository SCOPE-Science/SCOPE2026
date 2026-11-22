#!/usr/bin/env python3
"""Supplementary finite checks of a two-channel mean-field branching theorem.
Finite checks do not substitute for the analytic proof.
"""
from fractions import Fraction as Q
import random
from math import sqrt, exp
from scipy.linalg import expm
from scipy.optimize import brentq
import numpy as np

# Exact witness algebra
A=Q(7,10); D=Q(1,5); B=Q(2); C=Q(1,10)
assert B*C<A*(A-D) and B*(1-A+C)>A*(1-D)
assert C<A-D
assert Q(1)/(1-A)==Q(10,3)
M1=np.array([[0.,float(C)],[float(B),float(D)]])
U=Q(1)
den=(1-A)*(1-D)+U*(A*(1-D)-B*C)
volume=(1-D+B*U)/den
assert volume==Q(14,3)
assert (1+sqrt(21))/10<.7

def s(a,d,b,c,u,t):
    m=np.array([[a*(1-u),c],[b*u,d]])
    # gauge by baseline exponential so no overflow in moderately sized sample
    return float(np.sum(expm((m-a*np.eye(2))*t)[:,0]))

def classified(a,d,b,c):
    B=b-a; Delta=b*c-a*(a-d)
    if B>1e-9 and Delta<-1e-9:return 'down_cross'
    if B<-1e-9 and Delta>1e-9:return 'up_cross'
    if B>=-1e-9 and Delta>=-1e-9:return 'above'
    if B<=1e-9 and Delta<=1e-9:return 'below'
    return 'boundary'

# Numerically find sign in each strict region, verify one crossover and resolvent formula.
rng=random.Random(20261120)
regions={'down_cross':0,'up_cross':0,'above':0,'below':0}
tests=0
for j in range(1600):
    a=rng.uniform(.25,.96); d=rng.uniform(.02,a-.01)
    b=rng.uniform(.02,2.5); c=rng.uniform(.01,2.5)
    region=classified(a,d,b,c)
    if region=='boundary':continue
    regions[region]+=1
    u=rng.uniform(.02,1)
    m=np.array([[a*(1-u),c],[b*u,d]])
    eig=np.linalg.eigvals(m)
    lam=max(eig.real)
    Delta=b*c-a*(a-d)
    assert (lam>a)==(Delta>0)
    # Check against exact 2-exponential decomposition at several moderate times.
    lm=min(eig.real)
    x1=a+(b-a)*u
    coeff=(x1-lm)/(lam-lm)
    for t in (.002,.1,.4,1,2,5,10,18):
        val=s(a,d,b,c,u,t)
        exact=coeff*exp((lam-a)*t)+(1-coeff)*exp((lm-a)*t)
        assert abs(val-exact)<1e-7*(1+abs(exact)),(region,j,t,val,exact)
        if t<=.002:
            assert (val>1)==(b>a)
        tests+=1
    if region=='above':
        for t in (.2,1,4,9):assert s(a,d,b,c,u,t)>1
    if region=='below':
        for t in (.2,1,4,9):assert s(a,d,b,c,u,t)<1
    # Formula for total progeny when subcritical
    if lam<1:
        matres=np.sum(np.linalg.inv(np.eye(2)-m)[:,0]);
        den=(1-a)*(1-d)+u*(a*(1-d)-b*c)
        exact=(1-d+b*u)/den
        assert abs(matres-exact)<1e-8*(1+exact)

# In opposite-sign cases: uniqueness from proof; here verify numerically bracketing selected cases.
for k in range(120):
    a=rng.uniform(.5,.95); d=rng.uniform(.1,a-.1)
    c=rng.uniform(.02,a-d)
    low=a*(1-d)/(1-a+c)
    high=a*(a-d)/c
    b=(low+high)/2
    u=rng.uniform(.05,1)
    assert b>a and b*c<a*(a-d)
    assert (b*(1-a+c)-a*(1-d))>0
    assert s(a,d,b,c,u,.01)>1
    # total expected progeny larger despite smaller Perron growth
    m=np.array([[a*(1-u),c],[b*u,d]])
    assert max(np.linalg.eigvals(m).real)<a
    assert np.sum(np.linalg.inv(np.eye(2)-m)[:,0])>1/(1-a)

v=lambda t:s(.7,.2,2,.1,1,t)-1
root=brentq(v,1e-3,30,xtol=1e-12)
assert 6<root<7
print('Exact witness progeny: 10/3 -> 14/3; spectral 7/10 -> (1+sqrt(21))/10')
print('Finite sampled regions:',regions,'two-exponential checks:',tests)
print('Paradox wedge checks: 120; witness unique-crossing numerical location:',format(root,'.12f'))
print('PASS (finite checks; analytic proof required)')

# Finite-horizon integrated exposure: exact matrix exponential formula.
def integrated(a,d,b,c,u,T):
    m=np.array([[a*(1-u),c],[b*u,d]])
    return float(np.sum((np.linalg.solve(np.eye(2)-m, np.eye(2)-expm((m-np.eye(2))*T)))[:,0]))

a=.7; d=.2; c=.1; u=1.
low=a*(1-d)/(1-a+c)
high=a*(a-d)/c
assert abs(low-1.4)<1e-12 and abs(high-3.5)<1e-12
for b,classification in [(1.0,'cumulative_crosses'),(1.4,'critical'),(2.0,'cumulative_always_exceeds')]:
    values=[]
    for T in (.01,.1,1,3,7,12,25,60):
        v=integrated(a,d,b,c,u,T)-(1-exp(-(1-a)*T))/(1-a)
        values.append(v)
    if classification=='cumulative_crosses':
        assert values[0]>0 and values[-1]<0
    else:
        assert all(t>0 for t in values), (classification,values)
print('Finite-horizon integrated phase classification: PASS (3 rational regimes, 8 horizons each)')
