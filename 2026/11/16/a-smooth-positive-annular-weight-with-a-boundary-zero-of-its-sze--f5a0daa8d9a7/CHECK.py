"""Exact rational certificate for a boundary zero of a weighted annular Szego kernel.

Run: python CHECK.py
No third-party packages or external files are needed.
"""
from fractions import Fraction as Q

rho = Q(1, 4)
p = Q(2, 3)
N = 32
w_plus, w_minus = Q(-3, 8), Q(-3, 4)


def finite_kernel(s):
    assert s != 0
    return sum((s ** n) / (1 + rho ** (2 * n + 1))
               for n in range(-N, N + 1))


def finite_determinant(w):
    return (finite_kernel(w) * finite_kernel(p * p)
            - finite_kernel(p) * finite_kernel(p * w))


args = [w_plus, w_minus, p, p * p, p * w_plus, p * w_minus]
assert all(Q(1, 4) <= abs(s) <= Q(3, 4) for s in args)
assert rho < p < 1
assert w_minus < w_plus < -rho

E = 4 * Q(3, 4) ** (N + 1) + Q(16, 3) * Q(1, 4) ** (N + 1)
assert E < Q(1, 3000)
assert 24 * E < Q(1, 125)

Dp = finite_determinant(w_plus)
Dm = finite_determinant(w_minus)
assert Dp > Q(19, 100)
assert Dm < Q(-9, 100)
assert Dp - 24 * E > 0
assert Dm + 24 * E < 0

# These numbers are illustrations only; inequalities above use exact rationals.
print("PASS: exact annular Szego boundary-zero certificate")
print("D_32(-3/8) approx", format(float(Dp), '.15g'))
print("D_32(-3/4) approx", format(float(Dm), '.15g'))
print("Uniform Laurent tail E_32 approx", format(float(E), '.15g'))
print("Inferred: D(-3/8)>0>D(-3/4); root inside (-3/4,-3/8)")
