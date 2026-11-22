"""Exact rational-polynomial certificate for the trivariate power-ratio copula.

Requires Python 3 and SymPy. All comparisons are in exact rational arithmetic.
No numerical sampling is used to infer nonnegativity.
"""
from itertools import combinations_with_replacement, product
from sympy import (symbols, diff, together, cancel, Poly, binomial, expand,
                   fraction, Rational, factor)

X, Y, Z, p, t, s, r = symbols('X Y Z p t s r')
xyz = (X, Y, Z)
h = 1 - t*(1-X)*(1-Y)*(1-Z)
q = 1/h
for x in xyz:
    q = q + p*x*diff(q, x)
N = factor(q*h**4)
assert factor(N-h**4*q) == 0
assert Poly(N, X, Y, Z, t).total_degree() <= 12

# Boundary values of the mixed-density numerator.
for values, expected in [((0,0,0), (1-t)**3),
                         ((1,0,0), 1-p*t),
                         ((1,1,0), 1+p**2*t),
                         ((1,1,1), 1-p**3*t)]:
    assert factor(N.subs(dict(zip(xyz,values)))-expected)==0

Q = Poly(N, X, Y, Z)
power = {(i,j,k): Q.coeff_monomial(X**i*Y**j*Z**k)
         for i,j,k in product(range(4),repeat=3)}

def xyz_bernstein(i,j,k):
    return factor(sum(power[a,b,c]*binomial(i,a)*binomial(j,b)*binomial(k,c)
                      / (binomial(3,a)*binomial(3,b)*binomial(3,c))
                      for a in range(i+1) for b in range(j+1) for c in range(k+1)))

# At each fixed p>0, parametrize the entire proposed theta interval by s in [0,1].
# The numerator is a tensor Bernstein polynomial, degree at most 3 in each
# of X, Y, Z, s. Symmetry leaves 20*4=80 distinct coefficients per regime.
for label, upper, p_sub in [
    ('0<p<=1', 1, 1/(1+r)),
    ('p>=1', 1/p**3, 1+r)]:
    count = 0
    theta = -1/p**2 + s*(upper + 1/p**2)
    for i,j,k in combinations_with_replacement(range(4),3):
        P = Poly(cancel(xyz_bernstein(i,j,k).subs(t,theta)),s)
        assert P.degree() <= 3
        for m in range(4):
            z = sum(P.coeff_monomial(s**l)*binomial(m,l)/binomial(3,l)
                    for l in range(m+1))
            numerator, denominator = fraction(cancel(z.subs(p,p_sub)))
            # Each numerator and denominator has nonnegative rational
            # coefficients in r, and the denominator's constant is >0.
            a = Poly(expand(numerator),r).all_coeffs()
            b = Poly(expand(denominator),r).all_coeffs()
            assert all(c >= 0 for c in a), (label,i,j,k,m,'numerator',a)
            assert all(c >= 0 for c in b) and b[-1] > 0, (label,i,j,k,m,'denominator',b)
            count += 1
    assert count == 80
    print(label, '80 exact Bernstein coefficients verified')
print('PASS: corner necessities and all 160 positivity certificates')
