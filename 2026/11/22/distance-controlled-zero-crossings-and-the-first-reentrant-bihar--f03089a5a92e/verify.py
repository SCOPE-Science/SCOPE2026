#!/usr/bin/env python3
"""Exact, standalone checks for the Boolean-cube biharmonic kernel theorem.

Uses Python's standard library only. It checks algebraic identities, exact
rational brackets and independently built Walsh eigenvectors; the all-
dimension zero bound is proved in RESULT.md rather than by finite tests.
"""
from fractions import Fraction
from math import comb, exp, log

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def hd(a, b):
    return (a ^ b).bit_count()

def coeff(d, r, k):
    return sum((-1)**j * comb(r, j) * comb(d-r, k-j)
               for j in range(max(0, k-d+r), min(r, k)+1))

def polynomial(d, r):
    return {k*k: coeff(d,r,k) for k in range(d+1) if coeff(d,r,k) != 0}

def val(poly, x):
    return sum(c * x**k for k,c in poly.items())

def deriv(poly, a):
    return sum(c * k * a**(k-1) for k,c in poly.items() if k>=1)

def deriv2(poly, a):
    return sum(c * k*(k-1) * a**(k-2) for k,c in poly.items() if k>=2)

def variations(poly):
    cs=[c for k,c in sorted(poly.items()) if c]
    return sum(u*v<0 for u,v in zip(cs, cs[1:]))

# The five exact distance kernels of the four-cube.
expected4={
0:{0:1,1:4,4:6,9:4,16:1},
1:{0:1,1:2,9:-2,16:-1},
2:{0:1,4:-2,16:1},
3:{0:1,1:-2,9:2,16:-1},
4:{0:1,1:-4,4:6,9:-4,16:1}}
for r in range(5):
    check(polynomial(4,r)==expected4[r], f'Q4 polynomial r={r}')

for d in range(1,8):
    n=1<<d
    # Check graph Laplacian and its Walsh diagonalization independently.
    A=[[int(hd(i,j)==1) for j in range(n)] for i in range(n)]
    L=[[d*int(i==j)-A[i][j] for j in range(n)] for i in range(n)]
    for mask in range(n):
        char=[(-1)**((mask&i).bit_count()) for i in range(n)]
        ev=2*mask.bit_count()
        for i in range(n):
            check(sum(L[i][j]*char[j] for j in range(n))==ev*char[i],
                  f'Walsh eigenvector d={d},mask={mask},i={i}')
    # Verify coefficient formula both via combinatorics and Walsh projectors.
    for r in range(d+1):
        v=(1<<r)-1
        for k in range(d+1):
            count=sum((-1)**((mask&v).bit_count())
                      for mask in range(n) if mask.bit_count()==k)
            check(count==coeff(d,r,k), f'Krawtchouk d={d},r={r},k={k}')
        P=polynomial(d,r)
        check(val(P,Fraction(1))==(n if r==0 else 0), f'initial d={d},r={r}')
        check(P[0]==1, f'limit coefficient d={d},r={r}')
        if r:
            m=(r+1)//2
            check(variations(P)<=r, f'variation bound d={d},r={r}')
            # Direct exact Taylor support: the first nonzero coefficient
            # of e^{-t L^2} must appear at order ceil(r/2).
            U=[[int(i==j) for j in range(n)] for i in range(n)]
            L2=[[sum(L[i][a]*L[a][j] for a in range(n)) for j in range(n)] for i in range(n)]
            for j in range(m+1):
                check((U[0][v] == 0) if j<m else (U[0][v]!=0),
                      f'Taylor order d={d},r={r},j={j}')
                U=[[sum(U[i][a]*L2[a][b] for a in range(n)) for b in range(n)] for i in range(n)]

# Exact rational root isolations are not floating-point root searches.
intervals={
    (4,2):[(Fraction(85,100),Fraction(86,100))],
    (4,3):[(Fraction(50,100),Fraction(51,100))],
    (4,4):[(Fraction(25,100),Fraction(26,100)),
           (Fraction(93,100),Fraction(94,100))]
}
for (d,r), bounds in intervals.items():
    P=polynomial(d,r)
    for lo,hi in bounds:
        check(val(P,lo)*val(P,hi)<0, f'exact bracket d={d},r={r}')
    mult={2:1,3:2,4:2}[r]
    check(val(P,Fraction(1))==0, f'boundary root {r}')
    if mult>=2:
        check(deriv(P,Fraction(1))==0, f'double boundary root {r}')
    check((deriv(P,Fraction(1)) if mult==1 else deriv2(P,Fraction(1)))!=0,
          f'exact root multiplicity {r}')
    check(variations(P)==r, f'exact variation count r={r}')

# Verify sign directions, exact norm formula and mass conservation on a grid.
for ti in range(1,201):
    t=ti/400
    x=exp(-4*t)
    vals=[val(expected4[r],x)/16 for r in range(5)]
    check(abs(sum(comb(4,r)*vals[r] for r in range(5))-1)<1e-13,
          'row mass')
    norm=sum(comb(4,r)*abs(vals[r]) for r in range(5))
    formula=1+sum(comb(4,r)*max(0,-val(expected4[r],x))/8
                  for r in (2,3,4))
    check(abs(norm-formula)<1e-12, 'norm formula')

# A self-contained numerical comparison with direct sums over all Walsh modes.
for t in (0.001,0.02,0.05,0.20,0.34,0.50):
    x=exp(-4*t)
    for u in range(16):
        for v in range(16):
            h=sum((-1)**((m&(u^v)).bit_count()) * exp(-4*t*m.bit_count()**2)
                  for m in range(16))/16
            check(abs(h-val(expected4[hd(u,v)],x)/16)<4e-15,
                  f'kernel d4,t={t},u={u},v={v}')
print(f'VERIFY_OK {checks} exact and numerical checks')
