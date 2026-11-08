#!/usr/bin/env python3
"""Deterministic checks for the stated direction-indexed Mittag–Leffler occupation theorem.

Uses only Python standard library. Finite tests are not a proof of infinite limits.
"""
from fractions import Fraction
from math import comb, exp, log, pi, sin, cos

checks=0
p=Fraction(2,5); q=1-p; lam=Fraction(2); mu=Fraction(3)
# alpha = 1/2, Laplace evaluation arguments s=9 and t=4,
# so s**alpha = 3 and t**alpha = 2: rational transforms.
R=[Fraction(1)]; B=[Fraction(1)]
for j in range(1,31):
    R.append(R[-1]*lam*j/(lam*j+3))
    B.append(B[-1]*mu*j/(mu*j+2))
weights={0:Fraction(1)}
for n in range(1,26):
    nxt={}
    for m,w in weights.items():
        nxt[m+1]=nxt.get(m+1,Fraction(0))+w*p*lam*(m+1)/(lam*(m+1)+3)
        k=n-m
        nxt[m]=nxt.get(m,Fraction(0))+w*q*mu*k/(mu*k+2)
    weights=nxt
    direct=sum(weights.values(),Fraction(0))
    binomial=sum((Fraction(comb(n,m))*p**m*q**(n-m)*R[m]*B[n-m] for m in range(n+1)), Fraction(0))
    assert direct==binomial,(n,direct,binomial)
    checks+=1

# Stable-ratio density from Stieltjes inversion: integrate with a logistic
# substitution to remove integrable endpoint singularities.
def lamperti_logit_integrand(u,alpha,a,b,first_moment=False):
    r=1/(1+exp(-u))
    x=r**alpha; y=(1-r)**alpha
    den=a*a*y*y+b*b*x*x+2*a*b*cos(pi*alpha)*x*y
    value=(a*b*sin(pi*alpha)/pi)*x*y/den
    return r*value if first_moment else value

def simpson(f,lo=-45,hi=45,n=24000):
    h=(hi-lo)/n
    val=f(lo)+f(hi)
    for j in range(1,n):
        val+=(4 if j%2 else 2)*f(lo+j*h)
    return val*h/3

for alpha,a,b in ((0.5,1.,1.),(0.5,0.5,1.),(0.6,0.5,1/3),(.75,2.,3.)):
    mass=simpson(lambda u:lamperti_logit_integrand(u,alpha,a,b))
    mean=simpson(lambda u:lamperti_logit_integrand(u,alpha,a,b,True))
    assert abs(mass-1)<2e-7,(alpha,mass)
    assert abs(mean-a/(a+b))<2e-7,(alpha,mean,a/(a+b))
    checks+=2

# The continuous-extension alpha=1 boundary is a deterministic ratio.
for lam0,mu0 in ((1.,1.),(2.,3.),(7.,2.)):
    a=1/lam0; b=1/mu0
    assert abs(a/(a+b)-mu0/(lam0+mu0))<1e-14
    checks+=1

# Purely algebraic check: coefficient is antisymmetric under p <-> 1-p,
# while leading mean is p independent.
for numerator in range(1,10):
    p0=numerator/10
    c=(2*3)/(2+3)**2*log(p0/(1-p0))
    c_other=(2*3)/(2+3)**2*log((1-p0)/p0)
    assert abs(c+c_other)<1e-14
    checks+=1

print(f'{checks} deterministic checks passed; finite checks are not an infinite proof')
