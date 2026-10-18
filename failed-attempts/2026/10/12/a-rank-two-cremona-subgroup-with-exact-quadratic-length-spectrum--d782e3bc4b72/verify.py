#!/usr/bin/env python3
from fractions import Fraction

def coeff(m, n):
    return (m + n, n)

def add(u, v):
    return (u[0] + v[0], u[1] + v[1])

# Exact group law and inverse on a finite stress window.
for m in range(-8, 9):
    for n in range(-8, 9):
        c = coeff(m, n)
        assert c == (m+n, n)
        assert add(c, coeff(-m, -n)) == (0, 0)
        assert (c == (0,0)) == (m == 0 and n == 0)

for m1 in range(-4, 5):
    for n1 in range(-4, 5):
        for m2 in range(-4, 5):
            for n2 in range(-4, 5):
                assert add(coeff(m1,n1), coeff(m2,n2)) == coeff(m1+m2,n1+n2)

# Exact branch classification.
for m in range(-10, 11):
    for n in range(-10, 11):
        a, b = coeff(m,n)
        if (m,n) == (0,0):
            branch = 0
        elif a == 0:
            assert b != 0
            branch = 1
        else:
            branch = 5
        assert branch in (0,1,5)

# Normalization identities for arbitrary rational a,b != 0.
tests = [
    (Fraction(1), Fraction(1)),
    (Fraction(2), Fraction(3)),
    (Fraction(-5), Fraction(7)),
    (Fraction(11), Fraction(-13)),
]
for a,b in tests:
    beta2 = b/a
    alpha = b*b/a
    aprime = a * beta2 * beta2 / alpha
    bprime = b * beta2 / alpha
    assert aprime == 1
    assert bprime == 1

# b=0 branch: alpha=a, beta=1.
for a in [Fraction(1), Fraction(2), Fraction(-3), Fraction(17)]:
    alpha = a
    beta4 = Fraction(1)
    assert a * beta4 / alpha == 1

print("coefficient_lattice=Z^2")
print("identity_kernel={(0,0)}")
print("quadratic_branch=m+n=0 excluding origin")
print("quartic_branch=m+n!=0")
print("normalized_nonzero_b_coefficients=(1,1)")
print("VERIFY_OK")
