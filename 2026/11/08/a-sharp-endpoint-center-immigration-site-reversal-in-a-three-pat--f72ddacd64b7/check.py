"""Exact certificate for the three-site source-location stationary comparison.

Requires Python >=3.10 and sympy >=1.10. Run: python check.py
No external data, network services, or numerical solvers are needed.
"""
from fractions import Fraction
import sympy as sp

x = sp.symbols('x', positive=True)


def generator(source):
    """Row-generator indexed by occupancy bitmask 0,...,7."""
    q = sp.zeros(8)
    for state in range(8):
        for v in range(3):
            if state & (1 << v):
                to = state ^ (1 << v)
                rate = sp.Integer(1)
            else:
                to = state | (1 << v)
                neighbours = sum(
                    int(abs(u-v) == 1 and bool(state & (1 << u)))
                    for u in range(3)
                )
                rate = sp.Integer(v == source) + x * neighbours
            q[state, to] += rate
            q[state, state] -= rate
    return q


def stationary(q):
    a = q.T.copy()
    a[7, :] = sp.ones(1, 8)
    b = sp.zeros(8, 1)
    b[7] = 1
    pi = a.inv(method='DM') * b
    assert all(sp.cancel(v) == 0 for v in q.T*pi)
    assert sp.cancel(sum(pi)-1) == 0
    return pi

q_end, q_mid = generator(0), generator(1)
pi_end, pi_mid = stationary(q_end), stationary(q_mid)
DE = 4*x**6 + 34*x**5 + 150*x**4 + 371*x**3 + 548*x**2 + 450*x + 144
DC = 2*(x+1)*(x**3 + 5*x**2 + 15*x + 12)
N_E_all = x**2*(4*x**4 + 24*x**3 + 60*x**2 + 64*x + 21)
N_M_all = x**2*(x+2)*(2*x+3)
N_E_empty = 16*x**4 + 86*x**3 + 194*x**2 + 201*x + 72
N_M_empty = 8*x**2 + 19*x + 12

for actual, expected in [
    (pi_end[7], N_E_all/DE),
    (pi_mid[7], N_M_all/DC),
    (pi_end[0], N_E_empty/DE),
    (pi_mid[0], N_M_empty/DC),
]:
    assert sp.cancel(actual-expected) == 0

S = 6*x**6 + 28*x**5 + 9*x**4 - 334*x**3 - 990*x**2 - 1038*x - 360
T = 16*x**6 + 166*x**5 + 808*x**4 + 2111*x**3 + 2980*x**2 + 2112*x + 576
assert sp.cancel(pi_end[7]-pi_mid[7] - x**2*S/(DC*DE)) == 0
assert sp.cancel(pi_end[0]-pi_mid[0] - x*T/(DC*DE)) == 0

# All denominator coefficients and all coefficients of T are positive.
assert all(v > 0 for v in sp.Poly(DE, x).all_coeffs())
assert all(v > 0 for v in sp.Poly(DC, x).all_coeffs())
assert all(v > 0 for v in sp.Poly(T, x).all_coeffs())

# Descartes' rule: S has exactly one positive root because its
# coefficient signs, from descending powers, have one sign change.
coeffs = sp.Poly(S,x).all_coeffs()
signs = [sp.sign(v) for v in coeffs]
assert sum(signs[i] != signs[i+1] for i in range(len(signs)-1)) == 1
assert S.subs(x, 0) < 0
assert sp.LC(sp.Poly(S,x)) > 0
left, right = sp.Rational(3637677,1000000), sp.Rational(3637678,1000000)
assert S.subs(x,left) < 0 < S.subs(x,right)

# Check normalization/stationarity after exact rational substitutions
# using the distinct cofactor / Markov-chain tree method.
def tree_stationary(q):
    weights = [sp.det((-q).minor_submatrix(i,i)) for i in range(8)]
    den = sum(weights)
    return [sp.cancel(w/den) for w in weights]

checks = 0
for val in [sp.Rational(1,10), sp.Rational(1,2), sp.Integer(1),
            sp.Integer(2), sp.Integer(3), sp.Integer(4), sp.Integer(10)]:
    for q, pi in [(q_end,pi_end),(q_mid,pi_mid)]:
        exact = tree_stationary(q.subs(x,val))
        assert all(exact[i] == pi[i].subs(x,val) for i in range(8))
        checks += 8

print('PASS: symbolic stationarity, four closed-form marginals, two exact')
print('      difference identities, positive coefficients, unique root,')
print('      112 independent exact spanning-tree/cofactor comparisons.')
print('Root bracket:',left,right)
print('All c>0: center probability of >=1 patch occupied is larger.')
print('Full occupancy: center superior below root, endpoint above root.')
