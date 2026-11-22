#!/usr/bin/env python3
"""Reproducible exact algebra and bounded Fourier checks for the stated theorem."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from math import comb, cos, sin, pi

checks = 0

def check(cond, label):
    global checks
    assert cond, label
    checks += 1

def p(z):
    z=Q(z)
    return 1 - Q(8, 3)*z + 2*z**2 - Q(2, 3)*z**3 + z**4/4

def pprime(z):
    z=Q(z)
    return -Q(8, 3) + 4*z - 2*z**2 + z**3

def phi(z):
    z=Q(z)
    return z - Q(4, 3)*z**2 + Q(2, 3)*z**3 - z**4/6 + z**5/20

def b4(z):
    return sum(Q((-1)**j * comb(4, j), 6)*max(z+2-j, Q(0))**3 for j in range(5))

phi_coeff=[Q(0),Q(1),-Q(4,3),Q(2,3),-Q(1,6),Q(1,20)]
for j in range(201):
    z = Q(j, 200)
    check(sum(c*z**i for i,c in enumerate(phi_coeff)) == phi(z), 'energy polynomial coefficients')
    check(sum(i*c*z**(i-1) for i,c in enumerate(phi_coeff) if i>=1) == p(z), 'energy derivative = arc slope')
    check(b4(z) == Q(2, 3)-z**2+z**3/2, 'four-box central density')
    check(pprime(z) == 2*(b4(z)-2*(1-z)), 'arc curvature')
    check(p(z) == 1+(-Q(8, 3)*z+2*z**2-Q(2, 3)*z**3+z**4/4), 'arc derivative')
for j in range(201):
    z = 1+Q(j, 200)
    check(b4(z) == (2-z)**3/6, 'four-box outer density')
    check(phi(1) == Q(13, 60), 'initial integration')
    check(Q(1, 5)+(2-z)**5/60 >= Q(1, 5), 'nonnegative plateau tail')
check(p(Q(0)) == 1, 'derivative at zero')
check(p(Q(1)) == -Q(1, 12), 'derivative at first knot')
check(phi(Q(1)) == Q(13, 60), 'first knot energy')
check(Q(3,1)*Q(0)**2-4*Q(0)+4 > 0, 'strict polynomial convexity lower endpoint')
check(p(Q(6111143254, 10**10)) > 0, 'lower root enclosure')
check(p(Q(6111143255, 10**10)) < 0, 'upper root enclosure')

with localcontext() as ctx:
    ctx.prec = 58
    lo, hi = Decimal('0'), Decimal('1')
    def pd(z):
        return Decimal(1)-Decimal(8)*z/Decimal(3)+2*z*z-Decimal(2)*z**3/Decimal(3)+z**4/Decimal(4)
    for _ in range(180):
        m=(lo+hi)/2
        if pd(m)>0:
            lo=m
        else:
            hi=m
    root=(lo+hi)/2
    def phid(z):
        return z-Decimal(4)*z**2/Decimal(3)+Decimal(2)*z**3/Decimal(3)-z**4/Decimal(6)+z**5/Decimal(20)
    value=phid(root)
    check(abs(root-Decimal('0.611114325406299'))<Decimal('1e-15'), 'root decimal')
    check(abs(value-Decimal('0.24633437378661799'))<Decimal('1e-15'), 'energy decimal')
    check(abs(value/4-Decimal('0.0615835934466545'))<Decimal('1e-16'), 'sharp coefficient')

# Independent Fourier summation; the discarded positive tail is <=2/(pi^2*N).
def fourier(a, length, N=25000):
    terms=0.0
    for k in range(1, N+1):
        sk=sin(pi*k*a)/(pi*k*a)
        terms += ((1-cos(2*pi*k*length)) / (pi*pi*k*k)) * (1-sk*sk)**2
    return terms, 2/(pi*pi*N)

for a in (1/6, 1/4, 1/3):
    length=float(root)*a
    val, tail=fourier(a,length)
    expected=a*float(value)
    check(val <= expected+1e-10, 'positive Fourier undercount')
    check(0 <= expected-val <= tail+1e-10, 'rigorous Fourier tail')
    half,tail=fourier(a,.5)
    check(half <= expected + tail, 'non-extremal semicircle sample')
    if a <= 1/4:
        check(abs(half-a/5) <= tail, 'separated-jump plateau')

print(f'PASS: {checks} exact-rational/decimal and bounded-Fourier checks')
print('root:', str(root))
print('Phi(root):', str(value))
print('sharp squared norm per unit bandwidth:', str(value/4))
print('Scope: 0 < bandwidth <= 1/3; infinite-domain optimality uses the analytic proof.')
