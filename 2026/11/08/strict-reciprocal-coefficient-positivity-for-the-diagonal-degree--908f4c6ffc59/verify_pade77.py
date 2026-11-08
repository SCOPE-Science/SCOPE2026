#!/usr/bin/env python3
"""Exact rational certificates for the seventh diagonal Pade reciprocal."""
from fractions import Fraction as F
from math import factorial, comb

Q = [F((-1)**j * comb(7,j) * factorial(14-j), factorial(14)) for j in range(8)]
assert Q == [F(1), -F(1,2), F(3,26), -F(5,312), F(5,3432), -F(1,11440), F(1,308880), -F(1,17297280)]

# A complex rational is represented by a pair of exact rational numbers.
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def evaluate(coeff,z):
    out=(F(0),F(0))
    for a in reversed(coeff):out=add(mul(out,z),(a,F(0)))
    return out

def deriv(coeff):return [j*coeff[j] for j in range(1,len(coeff))]
def L1(z):return abs(z[0])+abs(z[1])
def squares(z):return z[0]**2+z[1]**2

r=F(1,10**6)
M=F(15)
assert sum(j*(j-1)*abs(Q[j])*F(14)**(j-2) for j in range(2,8)) < M

centers=[(F('9.9435737'),F(0)),
         (F('9.5165811'),F('3.4785721')),
         (F('8.1402783'),F('7.0343481')),
         (F('5.3713538'),F('10.8413883'))]
# The remaining three roots are the conjugates of the nonreal centers.
D = deriv(Q)
for c in centers:
    assert squares(c) < (F(14)-r)**2
    p=evaluate(Q,c);d=evaluate(D,c)
    # Rouche: on |z-c|=r, q'(c)(z-c) dominates the constant
    # and the Taylor remainder. Every indicated disc has one zero.
    assert L1(p) + M*r*r/F(2) < r*max(abs(d[0]),abs(d[1]))

# Discs are disjoint by their real/imaginary coordinates.
roots_centers=centers+[(x,-y) for x,y in centers[1:]]
for i in range(7):
    for j in range(i):
        assert max(abs(roots_centers[i][0]-roots_centers[j][0]),abs(roots_centers[i][1]-roots_centers[j][1])) > 2*r

# Conservative modulus and derivative bounds at all enclosed zeros.
R0=F('9.944')
assert centers[0][0]+r < R0
assert evaluate(D,centers[0])[0]+M*r < 0
assert L1(evaluate(D,centers[0]))+M*r < F('0.0052')

bounds=[(F('10.132'),F('0.0071'),F(15)),
        (F('10.758'),F('0.0202'),F(5)),
        (F('12.098'),F('0.157'),F(1))]
for c,(lo,dp,cap) in zip(centers[1:],bounds):
    assert squares(c) > (lo+r)**2
    assert squares(evaluate(D,c)) > (dp+M*r)**2
    assert lo*dp*cap > 1
assert R0*F('0.0052')*19 < 1

# Taylor coefficients through 31 are strictly positive by exact recurrence.
coeffs=[F(1)]
for n in range(1,32):
    coeffs.append(-sum(Q[j]*coeffs[n-j] for j in range(1,min(7,n)+1)))
    assert coeffs[-1]>0, (n,coeffs[-1])

# Tail n>=32 by residue dominance; each conjugate pair counted twice.
N=32
majorant=2*sum(cap*(R0/lo)**N for lo,dp,cap in bounds)
assert majorant < 19
assert all(R0<lo for lo,_,_ in bounds)
print('VERIFY_OK q_7_7: 7 disjoint Rouche root discs; exact residues; n=0..31 positive; tail n>=32 positive')
print('tail_majorant_at_32_upper',float(majorant))
print('n31',float(coeffs[31]))
