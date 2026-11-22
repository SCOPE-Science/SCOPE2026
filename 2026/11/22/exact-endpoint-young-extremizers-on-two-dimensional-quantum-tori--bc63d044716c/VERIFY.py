"""Finite diagnostics for a Weyl-cocycle equality classification.

These finite computations do not certify the infinite-dimensional theorem.
Run: python VERIFY.py
"""
from fractions import Fraction
from itertools import product
from math import cos, sin, pi, sqrt

checks = 0


def require(condition):
    global checks
    assert condition
    checks += 1


def determinant(h, k):
    return h[0]*k[1] - h[1]*k[0]

# The twisted-character law can be checked exactly modulo 2 in its
# rational-half-integer sign exponent for an isotropic rank-two lattice.
h1, h2 = (2, 0), (0, 1)
alpha = Fraction(1, 2)
area = determinant(h1, h2)
require(alpha*area == 1)

# Choosing both basis phases equal to 1 gives chi(k,l)=(-1)^(k*l).
def chi_sign(k, l):
    return -1 if k*l % 2 else 1

for k,l,kp,lp in product(range(-3, 4), repeat=4):
    lhs = chi_sign(k,l)*chi_sign(kp,lp)
    # exp(pi*i*alpha*area*(k*lp-l*kp)) is (-1)^(k*lp-l*kp).
    twisted = -1 if (k*lp-l*kp) % 2 else 1
    rhs = twisted*chi_sign(k+kp,l+lp)
    require(lhs == rhs)

for denominator in range(1, 13):
    for area in range(1, 41):
        for numerator in range(1, denominator+1):
            if __import__('math').gcd(numerator,denominator) == 1:
                require(((Fraction(numerator,denominator)*area).denominator == 1) == (area%denominator == 0))

# At theta=1/2, Pauli U,V furnish an exact unitary representation.
# Direct integer matrix arithmetic checks UV=-VU, U^2=I, and the
# characteristic polynomials of the two witnesses.
I=((1,0),(0,1))
U=((1,0),(0,-1))
V=((0,1),(1,0))

def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def matadd(a,b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def matscale(a,s):
    return tuple(tuple(s*a[i][j] for j in range(2)) for i in range(2))
def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def tr2(a):
    return a[0][0]+a[1][1]

require(matmul(U,U)==I)
require(matmul(V,V)==I)
require(matmul(U,V)==matscale(matmul(V,U),-1))
nonisotropic=matadd(matadd(I,U),V)
isotropic=matadd(matadd(I,matmul(U,U)),V)
require(nonisotropic==((2,1),(1,0)))
require(isotropic==((2,1),(1,2)))
require(tr2(nonisotropic)==2 and det2(nonisotropic)==-1)
require(tr2(isotropic)==4 and det2(isotropic)==3)
# The above integer characteristic-polynomial certificates imply the
# eigenvalues 1 +/- sqrt(2), and 3 and 1, respectively.
require(1+sqrt(2) < 3)
require(max(abs(1+sqrt(2)),abs(1-sqrt(2))) == 1+sqrt(2))
require(max(abs(3), abs(1)) == 3)

# Orthogonality and phase obstruction on a rank-one arithmetic triple:
# (1,1,i) cannot be aligned by a single character frequency.
phase0, phase1, phase2 = 1+0j, 1+0j, 1j
require(abs((phase0*phase2)/(phase1*phase1) - 1) > 1e-8)
# Conversely (1, exp(it), exp(2it)) is aligned.
for t in (0, pi/7, pi/4, 2*pi/3):
    c0=1+0j
    c1=complex(cos(t),sin(t))
    c2=complex(cos(2*t),sin(2*t))
    require(abs(c0*c2/(c1*c1)-1) < 1e-12)

print('VERIFY_OK', checks)
