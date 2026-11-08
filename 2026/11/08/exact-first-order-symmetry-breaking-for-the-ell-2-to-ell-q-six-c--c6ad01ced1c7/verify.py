"""Finite checks of the C6 incidence-norm transition formulas.

This is corroboration, not an infinite proof. Uses only the Python standard library.
"""
from fractions import Fraction as F
from math import log, isclose, sqrt

checks = 0
q0 = log(4) / log(F(4, 3))
assert 4 < q0 < 5
checks += 1

def shell(t, q):
    return (2.0**q + 2.0 * (1.0 + t)**q) / (2.0 + t*t)**(q/2.0)

def ratio(t, q):
    return shell(t, q) / shell(1.0, q)

# Symbolic-polynomial identities replayed exactly at many rational values.
for i in range(0, 81):
    t = F(i, 27)
    q2_slack = 4*(t*t+2) - (4+2*(1+t)**2)
    assert q2_slack == 2*(t-1)**2
    checks += 1
    q4_slack = F(16, 3)*(t*t+2)**2 - (16+2*(1+t)**4)
    assert q4_slack == F(2, 3)*(t-1)**2*(5*t*t-2*t+5)
    checks += 1

# Critical exponent ties precisely the uniform and broken vectors.
assert isclose(ratio(0.5, q0), 1.0, rel_tol=3e-14, abs_tol=3e-14)
checks += 1
assert isclose(((4/3)**q0), 4.0, rel_tol=3e-14)
checks += 1
assert isclose((3/4)**(q0-1), F(1, 3), rel_tol=3e-14)
checks += 1

# Sampled global profiles; these are NOT exhaustive certificates.
for q in [2.0, 2.5, 3.0, 4.0, 4.5, 4.75, q0]:
    for i in range(1, 600):
        t = i / 200.0
        assert ratio(t, q) <= 1.0 + 5e-12, (t, q, ratio(t, q))
        checks += 1

for q in [q0 + 0.03, 5.0, 6.0, 7.0, 10.0, 20.0]:
    assert ratio(0.5, q) > 1.0 + 1e-5
    checks += 1

# The familiar nonuniform critical vector (1,2,2)/3.
u = [1 / sqrt(3)] * 3
v = [1 / 3, 2 / 3, 2 / 3]
def matvec(x):
    return [sum(x) - y for y in x]
def norm(x, q):
    return sum(y**q for y in x)**(1/q)
assert isclose(norm(matvec(u), q0), norm(matvec(v), q0), rel_tol=3e-14)
checks += 1
print('EXACT_C6_CHECK_OK', checks)
