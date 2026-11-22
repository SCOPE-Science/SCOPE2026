"""Supplementary numerical and exact checks for two circular tent covariances.

No finite computation is used as a proof of the infinite positivity criterion.
"""
from fractions import Fraction
from math import cos, pi, sin
from math import gcd
import numpy as np
import sympy as sp
import mpmath as mp


def coeff(width, n):
    if n == 0:
        return width/(2*pi)
    return (1-cos(n*width))/(pi*width*n*n)


def finite_threshold(A, B, Q):
    assert 0 < B < A and 2*A <= Q and gcd(A,Q)==1
    v = []
    for j in range(1, Q):
        u = mp.sin(mp.pi*j*A/Q)
        t = mp.sin(mp.pi*j*B/Q)
        v.append((t/u)**2)
    return (mp.mpf(B)/A)/max(v)


def tent(width, x):
    d = abs(((x+pi)%(2*pi))-pi)
    return max(0.0, 1.0 - d/width)

mp.mp.dps=70
count=0
# Every rational case has a finite exact test; sample many distinct primitive widths.
for Q in range(5, 34):
    for A in range(2, (Q//2)+1):
        if gcd(A,Q) != 1: continue
        for B in range(1,A):
            threshold = finite_threshold(A,B,Q)
            a,b=2*pi*A/Q,2*pi*B/Q
            lam=float(threshold)
            assert lam>0 and lam<1
            for n in range(0,3*Q+1):
                c=coeff(a,n)-lam*coeff(b,n)
                assert c>=-1e-10, (Q,A,B,n,c)
                count+=1
            # Violation at a minimizing residue above the threshold.
            ratios=[]
            for n in range(1,Q):
                cb=coeff(b,n)
                if cb>1e-12:
                    ratios.append((coeff(a,n)/cb,n))
            rmin,nmin=min(ratios)
            assert abs(rmin-lam)<2e-8
            assert coeff(a,nmin)-(lam+1e-6)*coeff(b,nmin)<0
            count+=2

# A rational base cannot be strictly positive definite: alternating vector kills its 2Q grid.
for Q,A,B in ((5,2,1),(7,2,1),(11,3,1),(13,4,3)):
    a,b=2*pi*A/Q,2*pi*B/Q
    lam=float(finite_threshold(A,B,Q))
    points=[2*pi*j/(2*Q) for j in range(2*Q)]
    gram=np.array([[tent(a,x-y)-lam*tent(b,x-y) for y in points] for x in points])
    v=np.array([(-1)**j for j in range(2*Q)])
    assert np.linalg.norm(gram @ v)<1e-10
    assert np.linalg.eigvalsh(gram).min()>-1e-10
    count+=2

# Closed form rational family q odd, (A,B)=(2,1).
for Q in range(5, 70, 2):
    v=finite_threshold(2,1,Q)
    t=1-mp.cos(mp.pi/Q)
    assert abs(v-t)<mp.mpf('1e-60')
    count+=1

# Irrational width and order-two winding: the ratio supremum tends to 2.
a=mp.pi/mp.sqrt(2)
b=2*mp.pi-2*a
lam=(mp.sqrt(2)-1)/2
assert abs(lam - b/(4*a)) < mp.mpf('1e-60')
maximum=mp.mpf(0)
for n in range(1,10001):
    u=mp.sin(n*a/2)
    v=mp.sin(n*b/2)
    ratio=abs(v/u)
    assert ratio<2
    maximum=max(maximum,ratio)
    diff=(1-mp.cos(n*a))/a-lam*(1-mp.cos(n*b))/b
    assert diff>0
    count+=2
assert maximum>mp.mpf('1.99999')
count+=1

# A generic irrational separation has arbitrarily small tested Fourier ratios, indicating failure.
a=float(mp.pi/mp.sqrt(2))
b=0.61*pi
ratios=[]
for n in range(1,100000):
    den=1-cos(n*b)
    if den>0.1:
        ratios.append((1-cos(n*a))/den)
assert min(ratios)<1e-7
count+=1

# Exact verification of a five-fold cyclotomic example.
x=(3-sp.sqrt(5))/4
assert sp.simplify(x-(1-sp.cos(sp.pi/5)))==0
print('PASS:',count,'supplementary checks; rational, irrational, exact and finite-grid cases.')
print('order-two irrational threshold:',mp.nstr(lam,18))
print('rational q=5 threshold:', sp.simplify(x))
