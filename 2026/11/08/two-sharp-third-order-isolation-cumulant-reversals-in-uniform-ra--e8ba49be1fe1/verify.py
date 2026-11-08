#!/usr/bin/env python3
"""Independent exact moment enumeration and high-precision asymptotic checks."""
from fractions import Fraction
from itertools import combinations, product
from math import comb, exp
from decimal import Decimal, localcontext

assertions=0

def check(condition, description):
    global assertions
    if not condition: raise AssertionError(description)
    assertions+=1

def qj(P,K,j):
    return Fraction(comb(P-j*K,K),comb(P,K))

def moments(P,K,n):
    q,r,u=(qj(P,K,j) for j in (1,2,3))
    p1=q**(n-1)
    p2=q*r**(n-2)
    p3=q*r*u**(n-3)
    return p1,p2,p3

def kappa(P,K,n):
    p1,p2,p3=moments(P,K,n)
    return p3-3*p1*p2+2*p1**3

def exhaustive(P,K,n):
    rings=[frozenset(z) for z in combinations(range(P),K)]
    den=len(rings)**n
    c1=c2=c3=0
    for choice in product(rings,repeat=n):
        isolated=[all(not(choice[i]&choice[j]) for j in range(n) if i!=j) for i in range(3)]
        c1+=isolated[0]
        c2+=isolated[0] and isolated[1]
        c3+=all(isolated)
    return Fraction(c1,den),Fraction(c2,den),Fraction(c3,den)

for P,K,n in [(4,1,3),(4,1,4),(4,1,5),(5,1,4),(6,1,5),(8,2,3),(8,2,4)]:
    brute=exhaustive(P,K,n)
    calc=moments(P,K,n)
    for j in range(3):check(brute[j]==calc[j],f'brute {P=} {K=} {n=} {j=}')
    check(brute[2]-3*brute[0]*brute[1]+2*brute[0]**3==kappa(P,K,n),'cumulant')

for K in range(1,5):
    for P in range(4*K,4*K+40):
        q,r,u=(qj(P,K,j) for j in (1,2,3))
        check(0<u<q*r<q**3<1,'strict ratios')
        check(q*q/r>1,'convex exponential base')

s=[kappa(8,2,n) for n in range(3,10)]
check(s[1]>0 and s[2]<0 and s[3]>0,'exact finite double sign reversal')

def scaled_numeric(P,K,c):
    n=round(c*P)
    with localcontext() as context:
        context.prec=90
        q,r,u=(Decimal(qj(P,K,j).numerator)/Decimal(qj(P,K,j).denominator) for j in (1,2,3))
        return float(P*P*(q*r*u**(n-3)-3*q**n*r**(n-2)+2*q**(3*n-3)))

for K in (1,2,3):
    for c in (.6/K,1/K+1/(3*K*K),1/K+1/K**2):
        limiting=exp(-3*c*K*K)*K**3*(c*K-1)*(3*c*K*K-3*K-2)
        for P in (1000,2000,4000):
            measured=scaled_numeric(P,K,c)
            check(abs(measured-limiting) < (0.065 if K==3 else 0.04)/P*1000,'asymptotic accuracy')
            check(measured*limiting>0,'asymptotic sign')

print('VERIFICATION_OK exact_assertions='+str(assertions))
