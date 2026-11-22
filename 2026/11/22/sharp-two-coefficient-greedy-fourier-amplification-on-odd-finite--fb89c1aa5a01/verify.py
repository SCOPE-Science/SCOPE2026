"""Independent finite checks of the analytic two-coefficient greedy theorem.
No external dependencies. Exact proofs are in RESULT.md; this checker probes only finite cases.
"""
import cmath
from math import pi, sin, isclose


def test_odd_order(q):
    omega = cmath.exp(2j * pi / q)
    phases = [(1 + omega**j) / abs(1 + omega**j) for j in range(q)]
    coeff = [sum(phases[j] * omega**(-j*k) for j in range(q)) / q
             for k in range(q)]
    expected = 2/(q*sin(pi/(2*q)))
    assert abs(coeff[0] + coeff[1] - expected) < 1e-9
    assert abs(abs(coeff[0])-abs(coeff[1])) < 1e-9
    assert min(abs(coeff[k]) for k in (0, 1)) > max(abs(c) for c in coeff[2:]) + 1e-8
    for k in range(q):
        formula = 1/(q*abs(sin(pi*(1-2*k)/(2*q))))
        assert abs(abs(coeff[k]) - formula) < 1e-9
    kernel_norm = sum(abs(1+omega**j) for j in range(q))/q
    assert abs(kernel_norm-expected) < 1e-9
    return expected


prev = 1e9
for q in range(3, 200, 2):
    c = test_odd_order(q)
    assert c < prev
    prev = c

# Product-quotient test: a function on Z_3 x Z_5 using only a Z_3 character.
q, r = 3, 5
omega = cmath.exp(2j*pi/q)
product_values = {(a,b): (1+omega**a)/abs(1+omega**a)
                  for a in range(q) for b in range(r)}
coeff = {}
for k in range(q):
    for ell in range(r):
        coeff[(k,ell)] = sum(product_values[(a,b)] *
                omega**(-a*k) * cmath.exp(-2j*pi*ell*b/r)
                for a in range(q) for b in range(r))/(q*r)
order = sorted(coeff, key=lambda k: abs(coeff[k]), reverse=True)
assert set(order[:2]) == {(0,0), (1,0)}
assert abs(coeff[(0,0)] + coeff[(1,0)] - 4/3) < 1e-10
print('VERIFY_OK: 99 odd orders and one noncyclic product quotient')
