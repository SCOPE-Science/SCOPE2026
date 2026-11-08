#!/usr/bin/env python3
"""Exact checks for sliding-window entry flux and the binary optimizer theorem.
Standard library only. Finite checks complement, not replace, the proofs.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, comb, sqrt

CHECKS = 0

def ck(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)

def flux_formula(weights, m):
    n = len(weights)
    ans = F(0)
    for i in range(n):
        rest = [j for j in range(n) if i != j]
        cover = F(0)
        for mask in range(1 << (n-1)):
            b = [rest[k] for k in range(n-1) if mask >> k & 1]
            ps = sum((weights[j] for j in b), F(0))
            cover += (-1) ** (n-1-len(b)) * ps ** (m-1)
        ans += weights[i] * (1-weights[i]) * cover
    return ans

def flux_brute(weights, m):
    n = len(weights)
    ans = F(0)
    for word in product(range(n), repeat=m+1):
        if len(set(word[1:])) == n and len(set(word[:-1])) < n:
            prob = F(1)
            for j in word:
                prob *= weights[j]
            ans += prob
    return ans

def stirling_2(a,b):
    arr = [[0]*(b+1) for _ in range(a+1)]
    arr[0][0] = 1
    for j in range(1,a+1):
        for k in range(1,min(j,b)+1):
            arr[j][k] = k*arr[j-1][k]+arr[j-1][k-1]
    return arr[a][b]

def two_flux(p,m):
    q=1-p
    return p*q**m+q*p**m

for w in [[F(1,2),F(1,2)], [F(1,3),F(2,3)], [F(1,4),F(3,4)],
          [F(2,9),F(3,9),F(4,9)], [F(1,10),F(3,10),F(6,10)],
          [F(1,2),F(1,3),F(1,6)], [F(1,4)]*4]:
    n=len(w)
    for m in range(n,n+4 if n<4 else n+2):
        ck(flux_formula(w,m)==flux_brute(w,m), ("enumeration",w,m))
        if n==2:
            ck(flux_formula(w,m)==two_flux(w[0],m), ("binary",w,m))
        if m==n:
            ck(flux_formula(w,m)==(n-1)*factorial(n-1)*__import__('math').prod(w),
               ("endpoint",w,m))

for n in range(2,7):
    w=[F(1,n)]*n
    for m in range(n,n+8):
        ck(flux_formula(w,m)==F((n-1)*factorial(n-1)*stirling_2(m-1,n-1),n**m),
           ("uniform",n,m))

p4=F(1,2)
ck(two_flux(p4,4)==F(1,16), "uniform M4")
# The maximum is attained at (1+-1/sqrt(3))/2.
# At that quadratic root, the exact f4 value is 1/12 (by reduction).
# Use polynomial arithmetic modulo 6p^2-6p+1.
def poly_mod_quadratic(coeffs):
    # Residue of sum coeffs[k]*p^k mod (6p^2-6p+1).
    a,b=F(0),F(0)
    power=(F(1),F(0))
    for c in coeffs:
        a += c*power[0]
        b += c*power[1]
        power=(power[1]*F(-1,6),power[0]+power[1])
    return a,b
# p(1-p)^4 +(1-p)p^4 = p-4p^2+6p^3-3p^4.
ck(poly_mod_quadratic([0,1,-4,6,-3])==(F(1,12),F(0)),"M4 exact algebra")

# Exact endpoint and derivative signs at rational trial points certify shape examples.
for m in range(4,80):
    def f_deriv_numerator(t):
        return 1-m*t + m*t**(m-1)-t**m
    ck(f_deriv_numerator(F(1,m))>0,('derivative lower',m))
    ck(f_deriv_numerator(F(2,m))<0,('derivative upper',m))
    ck(f_deriv_numerator(F(1))==0,('derivative symmetry',m))

# Asymptotic rare-vs-uniform strict dominance already at modest M for n = 2..5.
for n in range(2,6):
    for m in (40, 80):
        rare=F(1,m)
        w=[rare]+[(1-rare)/F(n-1)]*(n-1)
        u=[F(1,n)]*n
        ck(flux_formula(w,m)>flux_formula(u,m),('rare beating uniform',n,m))


# Independent polynomial coefficient extraction for the tangent-space Hessian.
# The analytic expression uses covering-word counts with prescribed letters.
def cover_words(s,k,h):
    return sum((-1)**j*comb(h,j)*(k-j)**s for j in range(h+1))

def local_curvature_formula(n,m):
    u=F(1,n);r=m-1;k=n-1
    q=F(cover_words(r,k,k),n**r)
    a=F(r*cover_words(r-1,k,k-1),n**(r-1))
    c=F(r*(r-1)*cover_words(r-2,k,k-1),n**(r-2))
    d=F(r*(r-1)*cover_words(r-2,k,k-2),n**(r-2))
    return -2*q+u*(1-u)*((n-1)*c-(n-2)*d)-2*(1-2*u)*a

def local_curvature_independent(n,m):
    u=F(1,n);r=m-1
    shifts=[1,-1]+[0]*(n-2)
    result=F(0)
    for i in range(n):
        f0=u*(1-u)
        f1=shifts[i]*(1-2*u)
        f2=-shifts[i]**2
        rest=[j for j in range(n) if j!=i]
        for mask in range(1<<(n-1)):
            b=[rest[j] for j in range(n-1) if mask>>j & 1]
            a=F(len(b),n)
            delta=sum(shifts[j] for j in b)
            q0=a**r
            q1=r*a**(r-1)*delta
            q2=comb(r,2)*a**(r-2)*delta**2
            result+=(-1)**(n-1-len(b))*(f0*q2+f1*q1+f2*q0)
    return result

for n in range(2,8):
    for m in range(max(n,3),max(n,3)+15):
        ck(local_curvature_formula(n,m)==local_curvature_independent(n,m),
           ('local curvature',n,m))
for n,m in [(2,4),(3,6),(4,9),(5,12),(6,16),(7,19)]:
    ck(local_curvature_formula(n,m)>0,('local instability',n,m))
for n in range(2,8):
    ck(local_curvature_formula(n,4*n)>0,('eventual local minimum',n))

print(f'PASS {CHECKS} exact arithmetic assertions')
