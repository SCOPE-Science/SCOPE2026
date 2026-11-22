#!/usr/bin/env python3
"""Reproduction checks for canonical two-capacity exclusion singleton correlations.
Only Python standard library is required. No external data is downloaded.
"""
from fractions import Fraction
from itertools import product
from math import comb, sqrt

count = 0

def claim(condition, message):
    global count
    count += 1
    if not condition:
        raise AssertionError(message)

def weights(L, n, t):
    states = [s for s in product(range(3), repeat=L) if sum(s)==n]
    w = {s:t**s.count(0)*(t+1)**s.count(1) for s in states}
    return states, w

def stationary_balance(L,n,t,q):
    sts, w = weights(L,n,t)
    incoming = {s:Fraction(0) for s in sts}
    outgoing = {s:Fraction(0) for s in sts}
    bracket = (0,1,1+t)
    for s in sts:
        for i in range(L):
            j=(i+1)%L
            a,b=s[i],s[j]
            forward=Fraction(bracket[a]*(bracket[2]-bracket[b]))
            reverse=Fraction(q*bracket[b]*(bracket[2]-bracket[a]))
            for rate,delta in ((forward,-1),(reverse,1)):
                if rate==0: continue
                z=list(s); z[i]+=delta; z[j]-=delta; z=tuple(z)
                claim(z in w, 'transition does not preserve allowed states')
                outgoing[s]+=w[s]*rate
                incoming[z]+=w[s]*rate
    for s in sts:
        claim(incoming[s]==outgoing[s],f'balance failed {L,n,t,q,s}')

def Z(L,n,t):
    if n<0 or n>2*L: return 0
    # product (t+(1+t)*z+z*z)^L, integer dynamic program
    coeff=[1]
    for _ in range(L):
        new=[0]*(len(coeff)+2)
        for i,x in enumerate(coeff):
            new[i] += t*x
            new[i+1] += (t+1)*x
            new[i+2] += x
        coeff=new
    return coeff[n]

def cov(L,n,t):
    a=Z(L,n,t); b=Z(L-1,n-1,t); c=Z(L-2,n-2,t)
    return Fraction((t+1)**2*(a*c-b*b),a*a)

for L in range(3,6):
    for n in range(1,2*L):
        for t,q in [(1,Fraction(0)),(2,Fraction(1,2)),(4,Fraction(2))]:
            stationary_balance(L,n,t,q)
            sts,w=weights(L,n,t)
            total=sum(w.values())
            p1=Fraction(sum(v for s,v in w.items() if s[0]==1),total)
            p11=Fraction(sum(v for s,v in w.items() if s[0]==s[1]==1),total)
            claim(cov(L,n,t)==p11-p1**2, f'pair covariance mismatch L={L},n={n},t={t}')
            if n==L: claim(cov(L,n,t)>0,'half-filling strict positivity')

for L in range(3,42):
    for n in range(0,2*L+1):
        lhs=cov(L,n,1)
        rhs=Fraction(n*(2*L-n)*(L*(L-1)-(4*L-3)*(n-L)**2), L**2*(L-1)*(2*L-3)*(2*L-1)**2)
        claim(lhs==rhs, f't=1 sharp window formula L={L}, n={n}')
        if 0<n<2*L:
            claim((lhs>0)==(L*(L-1)>(4*L-3)*(n-L)**2), 'incorrect strict sign phase')

for t in (1,4,9):
    w=Fraction(t+1, int(sqrt(t)))
    p=Fraction(1,w+2)
    p1=Fraction(w,w+2)
    for L in (50, 100, 200, 400):
        # Near-central positive and negative sequences; exact arithmetic
        for c in (0, Fraction(1,4), Fraction(3,4)):
            d=round(float(c)*sqrt(L))
            C=cov(L,L+d,t)
            scaled=float(L*L*C)
            predicted=float(p1*p1*(1-Fraction(d*d,L)/p)/2)
            # Loose numerical convergence check, not a certificate of an infinite limit
            claim(abs(scaled-predicted)<0.18, f'central scaling disagreement t={t},L={L},d={d}')
        claim(cov(L,L,t)>0, 'half-filling positivity failed')

print(f'PASS: {count} deterministic exact-balance, coefficient, phase-window and asymptotic spot checks')
