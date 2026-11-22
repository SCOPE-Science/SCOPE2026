#!/usr/bin/env python3
"""Exact finite and interval-rational certificate for path parking site comparison."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

checks = 0

def demand(flag, what):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(what)

def padovan(n):
    s=[1,1,2]
    for m in range(3,n+1):
        s.append(s[m-2]+s[m-3])
    return s[:n+1]

def exact_seq(n,j):
    return sum((F((-1)**(r+t),factorial(r)*factorial(t)*(r+t+1))
               for r in range(j) for t in range(n-j+1)),F(0))

def exact_stat(n,j,s):
    return F(s[max(0,j-2)]*s[max(0,n-j-1)],s[n])

S=padovan(25)
for n in range(14,23):
    for j in range(1,n+1):
        sign=exact_seq(n,j)-exact_stat(n,j,S)
        exceptional=j in (2,4,n-3,n-1)
        demand(sign < 0 if exceptional else sign > 0,f'finite sign n={n},j={j}: {sign}')
for j in range(1,14):
    if j==7:
        demand(exact_seq(13,j)-exact_stat(13,j,S)<0,'sharp onset n13 center')

# independent branch-first recursion for greedy random-priority occupancy
@lru_cache(None)
def recurse(n):
    if n==0: return ()
    out=[F(0)]*n
    for r in range(n):
        out[r]+=F(1,n)
        left=recurse(max(0,r-1))
        right=recurse(max(0,n-r-2))
        for j in range(r-1): out[j]+=left[j]/n
        for j in range(r+2,n): out[j]+=right[j-(r+2)]/n
    return tuple(out)
for n in range(1,10):
    for j in range(1,n+1):
        demand(recurse(n)[j-1] == exact_seq(n,j),f'independent recursion {n},{j}')

# all interval bounds are exact rational, not floating-point evidence
plo=F(1324717957,10**9)
phi=F(1324717958,10**9)
f=lambda p:p**3-p-1
demand(f(plo)<0 and f(phi)>0,'plastic root bracket')

r_lower=F(95,100)
r_upper=F(97,100)
for m in (10,11,12):
    # S[m] / p^m; lower bound uses upper p
    demand(r_lower<S[m]/(phi**m),f'R_{m} lower')
    demand(S[m]/(plo**m)<r_upper,f'R_{m} upper')

def B_bounds(j):
    z=S[max(0,j-2)]
    return F(z,phi**(j+1)),F(z,plo**(j+1))
B7lo,B7hi=B_bounds(7)
for j in (6,8):
    demand(B_bounds(j)[1]<B7lo,f'B_{j} vs B_7')

el=sum((F((-1)**k, factorial(k)) for k in range(16)),F(0))
eu=el+F(1,factorial(16))
# alternate-series brackets exp(-1)
demand(F(367879,10**6)<el<eu<F(367880,10**6),'exp bracket')

# mean infinite-line occupancy rho - rigorous integrated Taylor remainders
rho_lower=(1-eu**2)/2
demand(rho_lower-F(2,factorial(7))>F(97,95)*B7hi,'uniform interior sign n>=23')

# boundary sites j<=5; exact A_j = a + b exp(-1)
Acoeff={1:(F(1),F(-1)),2:(F(0),F(1)),3:(F(1),F(-3,2)),
        4:(F(0),F(7,6)),5:(F(1),F(-37,24))}
for j,(a,b) in Acoeff.items():
    Alo=a+b*(el if b>0 else eu)
    Ahi=a+b*(eu if b>0 else el)
    Blo,Bhi=B_bounds(j)
    tail=F(1,factorial(20))
    if j in (2,4):
        demand(Ahi+tail < F(95,97)*Blo,f'boundary negative j={j}')
    else:
        demand(Alo-tail > F(97,95)*Bhi,f'boundary positive j={j}')

print(f'PASS: {checks} exact rational assertions')
print('Finite path sign classification: n=14..22, all vertices; n=13 counterthreshold')
print('Independent first-arrival recursion versus integral: n=1..9')
print('Infinite-n region: verified plastic-root bracket, Padovan ratio invariant,')
print('interior uniform gap and five boundary gaps, using exact rational intervals')
print('Note: infinite proof also uses explicitly stated recurrence and alternating-series inequalities.')
# Independent exhaustive static enumeration of maximal independent sets for small paths
for n in range(1,11):
    masks=[]
    for mask in range(1<<n):
        occupied=lambda j: 0<=j<n and ((mask>>j)&1)
        if all(not(occupied(j) and occupied(j+1)) for j in range(n-1)) and all(occupied(j) or occupied(j-1) or occupied(j+1) for j in range(n)):
            masks.append(mask)
    demand(len(masks)==S[n],f'static total n={n}')
    for j in range(1,n+1):
        real=F(sum(bool((m>>(j-1))&1) for m in masks),len(masks))
        demand(real==exact_stat(n,j,S),f'static formula n={n},j={j}')
print(f'PASS: {checks} total exact assertions including independent static enumeration')
