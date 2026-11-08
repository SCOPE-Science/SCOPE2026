#!/usr/bin/env python3
"""Exact certificate for the first nonmonotone cyclotomic-binomial filter order.

For 2 <= d <= 36, completely evaluate C_t(d) for 1 <= t <= d
using elementary symmetric polynomials and p-adic integer arithmetic.
"""
from math import factorial
from fractions import Fraction

def factor(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p; e += 1
            out.append((p,e))
        p += 1
    if n>1: out.append((n,1))
    return out

def vp(n,p):
    if not n: return float('inf')
    z = 0
    while n % p == 0:
        n //=p; z+=1
    return z

def e_polynomials(cmax):
    # E[c][j] = e_j(1,2,...,c) as exact integers
    E = [[1]]
    for c in range(1,cmax+1):
        row=E[-1]+[0]
        for j in range(c,0,-1):
            row[j]+=c*E[-1][j-1] if j<=len(E[-1]) else 0
        E.append(row)
    return E

def numerator(d,t,c,E):
    return sum((-d)**(j*t)*E[c][c-j*t] for j in range(1,c//t+1))

def trial(d,t,E):
    factors=factor(d)
    fac=1
    for c in range(d):
        if c: fac*=c
        N=numerator(d,t,c,E)
        for p,a in factors:
            if vp(N,p)-vp(fac,p)<a:
                return False,(c,p,vp(N,p)-vp(fac,p),a)
    return True,None

E=e_polynomials(36)
mask={}
for d in range(2,37):
    mask[d]=[trial(d,t,E)[0] for t in range(1,d+1)]
threshold={d: next(t for t in range(1,d+1) if all(mask[d][t-1:])) for d in range(2,37)}
assert all(mask[d]==[False]*(threshold[d]-1)+[True]*(d-threshold[d]+1) for d in range(2,36))
assert [t for t,ok in enumerate(mask[36],1) if ok]==[15]+list(range(17,37))
assert threshold=={2:1,3:1,4:2,5:1,6:4,7:1,8:2,9:2,10:7,11:1,12:5,13:1,14:11,15:6,16:3,17:1,18:14,19:1,20:9,21:9,22:19,23:1,24:10,25:2,26:22,27:3,28:12,29:1,30:26,31:1,32:3,33:15,34:30,35:8,36:17}

# The single failure witness: reduced rational at n=-1,c=32,t=16,d=36.
N=numerator(36,16,32,E)
D=factorial(32)
q=Fraction(N,D)
assert q == Fraction(196839814746004676662011581276685234,1506938033147421875)
assert vp(q.numerator,2)-vp(q.denominator,2)==1
assert trial(36,16,E)[0] is False
assert trial(36,15,E)[0] is True

# Second independent formula, directly as symmetric polynomials in reciprocals.
# This is deliberately separate from integer E[c][j] recurrence.
for d in range(2,37):
    recip=[Fraction(1)]
    for c in range(d):
        if c:
            for j in range(c,0,-1):
                if j == len(recip):recip.append(Fraction(0))
                recip[j] += recip[j-1] / c
        for t in range(1,d+1):
            if c<t: continue
            q2=sum(((-d)**(j*t)*recip[j*t] for j in range(1,c//t+1)),Fraction(0))
            q1=Fraction((-1)**c*numerator(d,t,c,E),factorial(c))
            assert q1==(-1)**c*q2,(d,t,c,q1,q2)

print('VERIFY_OK moduli=35 filter_orders=665 finite_coefficient_cases='+str(sum(d*d for d in range(2,37))))
print('first_nonmonotone_modulus=36; valid_orders=15,17..infinity; invalid_orders=1..14,16')
print('counterexample d=36 t=16 c=32 valuation_2=1 required_2=2; rational=',q)
print('thresholds_d2_to_d35:', [threshold[d] for d in range(2,36)])
