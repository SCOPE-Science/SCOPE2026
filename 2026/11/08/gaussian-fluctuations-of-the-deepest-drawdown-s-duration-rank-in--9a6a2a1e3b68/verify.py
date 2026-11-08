#!/usr/bin/env python3
"""Finite exact checks for a biased simple-walk excursion calculation.
Not a proof of the limiting rank theorem.
"""
from fractions import Fraction
from math import sqrt, log, comb, isclose

COUNT = 0

def check(condition, label):
    global COUNT
    if not condition:
        raise AssertionError(label)
    COUNT += 1

def rational_hitting(p, z, h):
    """Independent tridiagonal first-hit computation E_1[z^T; T0<T_(h+1)]."""
    if h==0: return Fraction(0)
    q=1-p
    # f_i - z*p*f_(i-1) - z*q*f_(i+1)=0, f0=1, f_(h+1)=0
    A=[[Fraction(0) for _ in range(h+1)] for __ in range(h)]
    for i in range(1,h+1):
        A[i-1][i-1]=Fraction(1)
        if i>1: A[i-1][i-2]=-z*p
        if i<h: A[i-1][i]=-z*q
        A[i-1][h]=(z*p) if i==1 else Fraction(0)
    for k in range(h):
        idx=next(i for i in range(k,h) if A[i][k])
        A[k],A[idx]=A[idx],A[k]
        piv=A[k][k]
        for j in range(k,h+1): A[k][j]/=piv
        for i in range(h):
            if i==k: continue
            v=A[i][k]
            for j in range(k,h+1): A[i][j]-=v*A[k][j]
    return A[0][h]

def closed_f(p,z,h):
    if h==0: return 0.0
    q=1-p
    rad=sqrt(1-4*p*q*z*z)
    rminus=(1-rad)/(2*q*z)
    rplus=(1+rad)/(2*q*z)
    u=rminus/rplus
    return rminus*(1-u**h)/(1-u**(h+1))

def closed_D(p,z,h):
    q=1-p
    rad=sqrt(1-4*p*q*z*z)
    rminus=(1-rad)/(2*q*z)
    rplus=(1+rad)/(2*q*z)
    u=rminus/rplus
    return z*rminus*u**(h-1)*(1-u)**2/((1-u**h)*(1-u**(h+1)))

def height_mass(p,h):
    r=(1-p)/p
    return r**(h-1)*(1-r)**2/((1-r**h)*(1-r**(h+1)))

def first_return_mass(p,m):
    # Exact dynamic programming: path starts at +1 with probability 1.
    q=1-p
    states={1:Fraction(1)}
    answer=Fraction(0)
    for step in range(2,2*m+1):
        nxt={}
        answer=Fraction(0)
        for level, prob in states.items():
            if level==1:
                answer+=prob*p
            else:
                nxt[level-1]=nxt.get(level-1,Fraction(0))+prob*p
            nxt[level+1]=nxt.get(level+1,Fraction(0))+prob*q
        states=nxt
    return answer

for p in [Fraction(3,5),Fraction(2,3),Fraction(3,4),Fraction(4,5)]:
    q=1-p
    for z in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]:
        prev=Fraction(0)
        for h in range(1,10):
            f=rational_hitting(p,z,h)
            check(abs(float(f)-closed_f(float(p),float(z),h))<1e-11,("f",p,z,h))
            d=float(z*(f-prev))
            check(abs(d-closed_D(float(p),float(z),h))<1e-11,("D",p,z,h))
            if z==1:
                check(abs(float(f-prev)-height_mass(float(p),h))<1e-11,("height",p,z,h))
            prev=f
    for m in range(1,13):
        actual=first_return_mass(p,m)
        expected=Fraction(comb(2*m-2,m-1),m)*p**m*q**(m-1)
        check(actual==expected,("Catalan",p,m))
    for h in range(1,10):
        ratio=q/p
        exact=ratio**(h-1)*(1-ratio)/(1-ratio**h)
        check(abs(float(1-rational_hitting(p,Fraction(1),h-1))-float(exact))<1e-11,("tail",p,h))

for p in [0.55,0.65,0.7,0.85]:
    q=1-p;delta=p-q; a=log(p/q); b=-log(2*sqrt(p*q))
    rho=2*b/(delta*a)
    check(0<rho<1,("rho",p))
    check(8*p*q*b*b/(delta**3*a)>0,("variance",p))
    def K(s):
        d=sqrt(1-4*p*q*__import__('math').exp(2*s))
        return log((1-d)/(1+d))
    eps=1e-5
    d1=(K(eps)-K(-eps))/(2*eps)
    d2=(K(eps)-2*K(0)+K(-eps))/(eps*eps)
    check(abs(d1-2/delta)<3e-5,("K prime",p,d1))
    check(abs(d2-8*p*q/delta**3)<0.02,("K double prime",p,d2))
print(f"PASS: {COUNT} exact-rational / independent-recurrence / numerical diagnostic assertions")
print("Not an infinite-asymptotic proof.")
