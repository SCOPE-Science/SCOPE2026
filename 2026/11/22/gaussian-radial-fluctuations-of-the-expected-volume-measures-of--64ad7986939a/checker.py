#!/usr/bin/env python3
"""Exact-rational checks of two Laplace-transform Taylor coefficients.
Scientific scope: independent finite-dimensional identities and asymptotic arithmetic.
Not a substitute for the analytic central limit proof in RESULT.md.
"""
from fractions import Fraction as F
from math import prod

checks = 0

def eq(a, b, what):
    global checks
    checks += 1
    if a != b:
        raise AssertionError(f'{what}: got {a}, expected {b}')

def a1(n):
    return -F(n, 6) - F(1, 2)

def a2(n):
    return F(3*n, 40) + F(n*(n-1), 72) + F(n, 12) + F(3, 8)

def beta_u(d, k):
    # U ~ Beta((d+1)/2,1/2). Its kth moment is rational.
    a = F(1)
    for j in range(k):
        a *= F(d+1+2*j,d+2+2*j)
    return a

def b_moments(d):
    den2 = (d+1)*(d+2)
    den4 = den2*(d+3)*(d+4)
    c1 = beta_u(d,1)*(a1(d)+F(1,den2))
    c2 = beta_u(d,2)*(a2(d)+a1(d+2)/den2+F(1,den4))
    return -2*c1, 8*c2

def a_moments(d):
    den2=(d+2)*(d+3)
    den4=den2*(d+4)*(d+5)
    c1 = a1(d+1)/4+F(1,den2)
    c2 = a2(d+1)/16+a1(d+3)/(4*den2)+F(1,den4)
    return -2*c1, 8*c2

def source_b(d):
    return (F(d*(d*d+6*d+11),3*(d+2)**2),
            F(d*(5*d**4+92*d**3+646*d*d+2068*d+2589),45*(d+2)*(d+4)**2))

def source_a(d):
    return (F(d*(d*d+9*d+26),12*(d+2)*(d+3)),
            F(d*(5*d**4+122*d**3+1171*d*d+5278*d+9624),720*(d+3)*(d+4)*(d+5)))

for d in range(1,257):
    mb, sb=b_moments(d)
    ma, sa=a_moments(d)
    x,y=source_b(d)
    eq(mb,x,f'B mean d={d}')
    eq(sb,y,f'B second moment d={d}')
    x,y=source_a(d)
    eq(ma,x,f'A mean d={d}')
    eq(sa,y,f'A second moment d={d}')
    assert sb-mb**2 > 0 and sa-ma**2 > 0
    checks += 2

# First coefficients and asymptotic centered variance. These evaluate exact
# finite-dimensional formulas, independently of any simulation.
for d in (500,1000,2000,4000,8000,16000):
    mb,sb=b_moments(d)
    ma,sa=a_moments(d)
    vb=(sb-mb*mb)/d
    va=(sa-ma*ma)/d
    # Exact one-sided residuals from the rational expressions.
    eq(vb > F(22,45),True,f'B variance excess d={d}')
    eq(va > F(11,360),True,f'A variance excess d={d}')
    eq(abs(vb-F(22,45)) < F(2,d),True,f'B variance rate d={d}')
    eq(abs(va-F(11,360)) < F(1,d),True,f'A variance rate d={d}')

# The limiting relative variance to the Gaussian time-average's squared
# radius is the same for motion and bridge.
eq(F(22,45)/(2*F(1,3)**2),F(11,5),'B relative variance')
eq(F(11,360)/(2*F(1,12)**2),F(11,5),'A relative variance')

print(f'PASS: {checks} independent exact rational assertions')
