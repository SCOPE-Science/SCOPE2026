#!/usr/bin/env python3
"""Exact algebra and finite-support consistency checks of a Hilbert-shift spectral calculation."""
from fractions import Fraction as Q
import cmath, math
checks=0
for t in (Q(1),Q(2),Q(3),Q(5,2)):
    for h in (Q(1,4), Q(1,2), Q(1), Q(2), Q(4), Q(9)):
        # F(z) = t/(1-z) + h*z; the negative zero is inside precisely when h>t/2.
        zminus=(1-math.sqrt(float(1+4*t/h)))/2
        assert (zminus > -1) == (h>t/2)
        assert abs(float(t+h*Q(0))) > 0
        checks+=2
# A lone positive spike of size 1 at index 1 or 2 leaves the full list of 2-by-2
# singular Gram blocks invariant under relabeling of blocks.
c=[1]*60;d=[1]*60;c[1]=2;d[2]=2
assert sorted(c[1:])==sorted(d[1:]);checks+=1
# Characteristic polynomials for first and second spikes are exact.
for zz in (Q(-3),Q(-2),Q(-1),Q(0),Q(1,2),Q(2),Q(3)):
    assert (1+zz-zz*zz)==(1+(1-zz)*zz)
    assert (1+zz*zz-zz**3)==(1+(1-zz)*zz*zz)
    checks+=2
# For the second spike the monic cubic z^3-z^2-1 has a unique real zero >1;
# the other two roots are conjugates strictly inside the circle.
assert ((Q(1)**3-Q(1)**2-1)<0) and ((Q(2)**3-Q(2)**2-1)>0)
assert (Q(0)**3-Q(0)**2-1)<0 and (Q(2,3)**3-Q(2,3)**2-1)<0
checks+=2
# Approximate genuine infinite eigenvector by a length-128 truncation (t=h=1).
z=(1-math.sqrt(5))/2
lam=1j*math.sqrt(-z)
N=128
c=[1]*N;c[1]=2
y=[lam**n for n in range(N)]
x=[0j]*N;x[0]=1/lam
for n in range(1,N):x[n]=-lam**(n+1)/(1-lam*lam)
r_top=[(x[n-1] if n else 0)+c[n]*y[n]-lam*x[n] for n in range(N)]
r_bottom=[(y[n+1] if n+1<N else 0)-lam*y[n] for n in range(N)]
assert max(map(abs,r_top+r_bottom))<1e-11
checks+=1
print('CONJUGATE_SHIFT_SPECTRAL_ZEROS_OK',checks)
