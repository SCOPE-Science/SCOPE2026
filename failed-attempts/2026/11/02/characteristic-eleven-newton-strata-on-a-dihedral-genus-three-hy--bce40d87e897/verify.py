#!/usr/bin/env python3
"""Exact certificate for a characteristic-11 genus-three dihedral locus.
No external packages. Polynomial coefficients are computed over F_11."""
from math import factorial
from itertools import product
P = 11

def poly_mul(A, B):
    C = {}
    for (xa, aa), ca in A.items():
        for (xb, ab), cb in B.items():
            z = (xa+xb, aa+ab)
            C[z] = (C.get(z,0)+ca*cb)%P
    return {z:v for z,v in C.items() if v}

def power(A,n):
    R={(0,0):1}
    for _ in range(n):
        R=poly_mul(R,A)
    return R

def in_x(POLY,k):
    return {ap:c for (xp,ap),c in POLY.items() if xp == k}

# h_C(x,a) = x^7+a*x^4+x.
h={(7,0):1,(4,1):1,(1,0):1}
h5=power(h,5)
H=[[in_x(h5, 11*i-j) for j in range(1,4)] for i in range(1,4)]
expected=[[{}, {}, {1:5}], [{}, {1:8,3:9,5:1}, {}], [{1:5}, {}, {}]]
assert H==expected, (H,expected)

# E0: V^2=u^3+a*u^2+u, E1:v^2=t^3-3*t+a.
e0={(3,0):1,(2,1):1,(1,0):1}
e1={(3,0):1,(1,0):8,(0,1):1}
assert in_x(power(e0,5),10)=={1:8,3:9,5:1}
assert in_x(power(e1,5),10)=={1:6}

# Hasse coefficient B(a) = a(a^2+1)(a^2-3).
for a in range(P):
    smooth = (a*a-4)%P != 0
    B=(a**5-2*a**3-3*a)%P
    assert B==(a*(a*a+1)*(a*a-3))%P
    rank = (2 if a else 0) + (1 if B else 0)
    if smooth:
        desired=0 if a==0 else (2 if (a*a+1)%P==0 or (a*a-3)%P==0 else 3)
        assert rank==desired, (a,rank,desired)
# Count: 9 smooth F11 a's: 1 p-rank 0, 2 p-rank 2, 6 ordinary.
counts={0:0,2:0,3:0}
for a in range(P):
    if (a*a-4)%P==0:continue
    B=(a**5-2*a**3-3*a)%P
    rank=(2 if a else 0)+(1 if B else 0)
    counts[rank]+=1
assert counts=={0:1,2:2,3:6},counts
# All geometric zeroes of the Hasse factors are distinct and avoid singular fibers.
assert ((0*0-4)%P)!=0
assert ((-1-4)%P)!=0
assert ((3-4)%P)!=0
# E1 has 1 supersingular parameter, E0 5 over the algebraic closure.
# The a !=0 roots of E0 are the four roots a^2= -1,3.
assert (5**2-3)%P==0 and ((-5)**2-3)%P==0
assert all((a*a+1)%P!=0 for a in range(P))
print('F11_HYPERELLIPTIC_SMOOTH_PARAMETERS=9')
print('H_C_ANTIDIAGONAL=(5a, a(a^2+1)(a^2-3), 5a)')
print('ELLIPTIC_HASSE_E0=a(a^2+1)(a^2-3); E1=6a')
print('F11_RANK_COUNTS={0: 1, 2: 2, 3: 6}')
print('GEOMETRIC_NP_STRATA=SUPERSPECIAL_AT_0; MIXED_AT_a^2=-1,3; ORDINARY_OTHERWISE')
print('VERIFY_OK')
