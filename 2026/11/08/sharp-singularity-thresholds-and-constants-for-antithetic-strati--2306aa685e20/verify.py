#!/usr/bin/env python3
"""Independent algebraic and numerical checks for antithetic power quadrature.
Run: python3 verify.py (Python standard library only).
These are finite checks; they do not replace the asymptotic proof.
"""
from fractions import Fraction as F
from math import comb, expm1, log1p

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def poly_g(power, k):
    return [F(comb(power, j) * (k ** (power-j) + (-1)**j * (k+1)**(power-j)), 2)
            for j in range(power+1)]

def integral(poly):
    return sum((a/F(j+1) for j, a in enumerate(poly)),F(0))

def variance_poly(poly):
    mean = integral(poly)
    second = sum((a*b/F(i+j+1) for i,a in enumerate(poly)
                  for j,b in enumerate(poly)), F(0))
    return second-mean*mean

def iid_pair_variance_linear(k):
    # Two independent uniform within-cell values of a linear function.
    return F(1,24)

for k in range(50):
    check(variance_poly(poly_g(0,k)) == 0, 'constant exactness')
    check(variance_poly(poly_g(1,k)) == 0, 'affine exactness')
    check(variance_poly(poly_g(2,k)) == F(1,180), 'quadratic variance')
    check(variance_poly(poly_g(3,k)) == F((2*k+1)**2, 80), 'cubic variance')
    for p in range(2, 7):
        check(variance_poly(poly_g(p,k)) > 0, 'non-affine positivity')
for n in range(1, 31):
    q2 = sum((variance_poly(poly_g(2,k)) for k in range(n)),F(0)) / n**6
    q3 = sum((variance_poly(poly_g(3,k)) for k in range(n)),F(0)) / n**8
    check(q2 == F(1,180*n**5),'quadratic finite n')
    check(q3 == F(4*n*n-1,240*n**7),'cubic finite n')
    check(sum(iid_pair_variance_linear(k) for k in range(n))/n**4 == F(1,24*n**3),
          'independent pair linear finite n')

# Directly integrate (via deterministic midpoint quadrature) the centered
# complementary pair, avoiding subtracting enormous raw moments.
def numeric_cell_var(beta,k,nodes=4096):
    c=k+.5
    hs=[]
    for j in range(nodes):
        u=(j+.5)/nodes
        t=(u-.5)/c
        hs.append(c**beta * (expm1(beta*log1p(t)) + expm1(beta*log1p(-t)))/2)
    mean=sum(hs)/nodes
    return sum((h-mean)**2 for h in hs)/nodes

for beta in (1.25,1.5,1.75,2.0,3.0):
    predicted=beta**2*(beta-1)**2/720
    for k in (1000,5000):
        val=numeric_cell_var(beta,k)
        scaled=val*k**(4-2*beta)
        check(abs(scaled/predicted - 1) < .008,
              f'power asymptotic {beta} {k}: {scaled}/{predicted}')
check(abs((1.5**2*.5**2/720)-1/1280)<1e-15,'critical coefficient')
check(abs((2**2*1**2/(720*(4-3)))-1/180)<1e-15,'quadratic coefficient')
print(f'PASS: {checks} exact-rational/deterministic assertions.')
print('Exact cases: beta=0,1,2,3; finite-n formulas for beta=2,3;')
print('large-cell power asymptotics, beta=5/4,3/2,7/4,2,3.')
