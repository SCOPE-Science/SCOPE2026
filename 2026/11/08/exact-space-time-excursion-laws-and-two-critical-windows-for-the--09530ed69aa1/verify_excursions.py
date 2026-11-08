#!/usr/bin/env python3
"""Arithmetic reproduction of the space-time excursion theorem.

Run: python3 verify_excursions.py
Only the Python standard library is required. Finite tests are not proofs of
infinite identities or asymptotic limits; those are proved in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb, sqrt, exp, erfc, pi


def alpha(l):
    return l**4 * (1+l*l-2*l**3) / (1-l**4)


def return_mass(l, n):
    a=alpha(l)
    if n==1:
        return 1-a
    m=n-1
    out=Q(0)
    for h in range(1,m+1):
        p=Q(h,m) * (1-l)**m * l**(m-h)*comb(2*m-h-1,m-h)
        out += (1-l)*l**(h-1)*p
    return a*out


def direct_return_masses(l, limit):
    states={j: Q(1-l)*l**(j-1)/(1-l**4) for j in range(1,5)}
    result=[]
    for step in range(1,limit+1):
        next_states={}
        for j,mass in states.items():
            first=1 if j<=3 else (2 if j==4 else j-1)
            for dest in range(first,limit+5):
                next_states[dest]=next_states.get(dest,Q(0)) + mass*(1-l)*l**(dest-first)
        result.append(sum((v for i,v in next_states.items() if i<=4),Q(0)))
        states={i:v for i,v in next_states.items() if i>4}
    return result


def solve(matrix, rhs):
    n=len(rhs)
    a=[list(row)+[rhs[i]] for i,row in enumerate(matrix)]
    for k in range(n):
        i=next(i for i in range(k,n) if a[i][k])
        a[k],a[i]=a[i],a[k]
        t=a[k][k]
        a[k]=[x/t for x in a[k]]
        for j in range(n):
            if j==k: continue
            t=a[j][k]
            a[j]=[a[j][v]-t*a[k][v] for v in range(n+1)]
    return [a[i][-1] for i in range(n)]


def direct_max_tail(l,L):
    A=[]
    b=[]
    for h in range(1,L):
        row=[]
        for j in range(1,L):
            k=j-h+1
            row.append(Q(int(j==h)) - ((1-l)*l**k if k>=0 else Q(0)))
        A.append(row)
        b.append(l**(L-h+1))
    p=solve(A,b)
    conditional=l**(L-1)
    for h in range(1,L):
        conditional+=(1-l)*l**(h-1)*p[h-1]
    return alpha(l)*conditional


def max_tail_formula(l,L):
    a=alpha(l)
    r=(1-l)/l
    return a*Q(2,L+1) if r==1 else a*(r*r-1)/(r**(L+1)-1)

for l in (Q(1,3), Q(1,2), Q(3,5), Q(3,4)):
    direct=direct_return_masses(l,9)
    assert direct==[return_mass(l,n) for n in range(1,10)]
    for L in range(2,8):
        assert direct_max_tail(l,L)==max_tail_formula(l,L)
    print('EXACT_RENEWAL_AND_MAXIMUM_OK', l)

assert alpha(Q(1,2))==Q(1,15)
for n in range(2,30):
    assert return_mass(Q(1,2),n)==Q(2,15)*Q(comb(2*n,n),4**n*(2*n-1))
for L in range(1,20):
    assert max_tail_formula(Q(1,2),L)==Q(2,15*(L+1))
print('CRITICAL_BINOMIAL_AND_SPATIAL_TAIL_OK')


def time_survival(n,u):
    l=.5+u/sqrt(n)
    s=0.
    for h in range(1,45):
        if h>n-1: break
        p=(1-l)**h
        cdf=0.
        for m in range(h,n):
            cdf+=p
            p*=l*(1-l)*(2*m-h+1)*(2*m-h)/((m+1)*(m-h+1))
        s+=(1-l)*l**(h-1)*(1-cdf)
    return alpha(l)*s

for u in (-0.6,0.0,0.6):
    n=20000
    value=sqrt(n)*time_survival(n,u)
    target=Q(2,15)*(exp(-4*u*u)/sqrt(pi)+2*u*erfc(-2*u))
    assert abs(value/target-1)<0.025
    print('TIME_WINDOW_TEST',u,'sample',round(value,9),'limit',round(target,9))

for u in (-1.0,-0.3,0.,0.3,1.0):
    L=20000
    l=.5+u/L
    r=(1-l)/l
    scaled=(L*alpha(l)*(r*r-1)/(r**(L+1)-1) if u else 2*L/(15*(L+1)))
    target=(8*u/15)/(1-exp(-4*u)) if u else 2/15
    assert abs(scaled/target-1)<.001
    print('SPACE_WINDOW_TEST',u,'sample',round(scaled,9),'limit',round(target,9))
print('SPACE_TIME_EXCURSION_VERIFICATION_OK')
