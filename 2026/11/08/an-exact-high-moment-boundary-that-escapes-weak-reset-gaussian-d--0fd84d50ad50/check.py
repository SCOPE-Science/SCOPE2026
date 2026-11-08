#!/usr/bin/env python3
"""Reproduce exact moment identities and high-order weak-reset boundaries."""
from fractions import Fraction as F
from math import comb, factorial, exp, log
import random

checks = 0

def ok(statement, message):
    global checks
    assert statement, message
    checks += 1

def deltas(s, lam, gamma, p):
    a=1-s
    return (lam/s)*(1-a**(2*p))-2*gamma*p

def gaussian_delta(s, lam, gamma, p):
    return 2*p*(lam-gamma)-p*(2*p-1)*lam*s

def moments(s, lam, gamma, D, p):
    vals=[F(1)]
    for j in range(1,p+1):
        d=deltas(s,lam,gamma,j)
        if d<=0:
            return vals, j
        vals.append(2*D*j*vals[-1]/d)
    return vals,None

# Direct polynomial generator, independently of the closed product formula.
for den in range(3,13):
    for num in range(1,den):
        s=F(num,den); lam=F(den+2,den); gamma=lam*F(1,5); D=F(3,7)
        M, bad=moments(s,lam,gamma,D,9)
        for p in range(1,len(M)):
            rate=lam/s
            # Reconstruct the continuous drift and the jump contribution.
            generator=2*gamma*p*M[p]+2*D*p*M[p-1]+rate*((1-s)**(2*p)-1)*M[p]
            ok(generator==0, ('generator',den,num,p))
            ok(M[p]>0,('positivity',den,num,p))
        if bad is not None:
            ok(deltas(s,lam,gamma,bad)<=0,('first divergence',den,num,bad))

# Check exact covariance by two independently obtained expressions.
for den in range(3,15):
    for num in range(1,den):
        s=F(num,den); lam=F(3,2); gamma=F(1,3); D=F(7,5)
        A1=deltas(s,lam,gamma,1);A2=deltas(s,lam,gamma,2)
        if A1>0 and A2>0:
            M1=2*D/A1;M2=8*D**2/(A1*A2)
            covariance=M2-M1**2
            alternate=4*D**2*(lam/s)*(1-(1-s)**2)**2/(A1**2*A2)
            ok(covariance==alternate, ('covariance',den,num))
            ok(covariance>0,('strict positive covariance',den,num))

s=F(1,2);lam=D=F(1);gamma=F(1,3)
A1=deltas(s,lam,gamma,1);A2=deltas(s,lam,gamma,2)
M1=2*D/A1;M2=8*D**2/(A1*A2)
ok((A1,A2,M1,M2,M2-M1*M1)==(F(5,6),F(13,24),F(12,5),F(1152,65),F(3888,325)),'rational example')
ok(gaussian_delta(s,lam,gamma,1)==A1,'matching second moment')
ok(gaussian_delta(s,lam,gamma,2)<0<A2,'false fourth-moment divergence')

# Polynomial Taylor inequality is strict at order >= 2.
for den in range(3,26):
    for num in range(1,den):
        s=F(num,den)
        for p in range(2,17):
            exact=(1-(1-s)**(2*p))/(2*p*s)
            surrogate=1-F(2*p-1,2)*s
            ok(exact>surrogate,('strict threshold gap',den,num,p))

# High-order phase window at fixed gamma/lambda.
def F_limit(z):
    return -__import__('math').expm1(-2*z)/(2*z) if z else 1.0

def root(c):
    lo,hi=0.0,1.0
    while F_limit(hi)>c:
        hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if F_limit(mid)>c: lo=mid
        else: hi=mid
    return (lo+hi)/2

for c in (.1,.2,.5,.7,.9):
    z=root(c)
    ok(z>1-c,('strict high-order gap',c,z))
    for s in (.02,.01,.005,.002):
        # Continuous-order zero of the exact rate.
        lo,hi=0.000001,10/s
        for _ in range(90):
            p=(lo+hi)/2
            if (1-(1-s)**(2*p))/(2*p*s)>c:lo=p
            else:hi=p
        ok(abs(s*(lo+hi)/2-z)<2.0*s,('critical scaling',c,s,z,s*(lo+hi)/2))
        # A definite interior misclassification point.
        p=int((1-c)/s+0.5)+1
        if p>=2 and p*s<z-0.001:
            ok(deltas(F(str(s)),F(1),F(str(c)),p)>0,('exact finite',c,s,p))
            ok(gaussian_delta(F(str(s)),F(1),F(str(c)),p)<0,('surrogate infinite',c,s,p))

# Independent path-integral sampling at a benign parameter point.
rng=random.Random(55117)
s=.5; lam=1.;gamma=0.1;D=1.;rate=lam/s;a=1-s
m1=2*D/(rate*(1-a*a)-2*gamma)
m2=8*D*D/((rate*(1-a*a)-2*gamma)*(rate*(1-a**4)-4*gamma))
total1=total2=0.
nsim=12000
for _ in range(nsim):
    t=0.; v=0.; scale=1.
    while t<25 and scale>1e-13:
        wait=rng.expovariate(rate)
        h=min(wait,25-t)
        if gamma:
            v+=2*D*scale*exp(2*gamma*t)*__import__('math').expm1(2*gamma*h)/(2*gamma)
        else:v+=2*D*scale*h
        t+=h
        scale*=a*a
    total1+=v;total2+=v*v
ok(abs(total1/nsim/m1-1)<.04,('path mean',total1/nsim,m1))
ok(abs(total2/nsim/m2-1)<.07,('path square',total2/nsim,m2))
print('PASS:',checks,'checks; exact example E[V]=',M1,'E[V^2]=',M2,'Cov=',M2-M1*M1)
print('critical z(c=1/2)=',root(.5),'gaussian z=',.5)
print('Monte Carlo mean and square:',total1/nsim,total2/nsim,'theory:',m1,m2)
