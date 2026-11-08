"""Exact finite-state verification of the four-site, single-defect current theorem.
Run with Python 3 and SymPy. All identities use rational symbolic arithmetic.
"""
import sympy as sp

z = sp.symbols('z', positive=True)
N = 4
states = range(1 << N)
tau = (sp.Integer(1), z, sp.Integer(1), sp.Integer(1))
A0 = sp.zeros(16)
A1 = sp.zeros(16)

def put(A, old, new, rate):
    A[new, old] += rate
    A[old, old] -= rate

for state in states:
    for i in range(N - 1):
        occ_i = (state >> i) & 1
        occ_j = (state >> (i + 1)) & 1
        if occ_i != occ_j:
            departure = i if occ_i else i + 1
            new = state ^ (1 << i) ^ (1 << (i + 1))
            put(A0, state, new, 1 / tau[departure])
    for i, side in ((0, 1), (N - 1, -1)):
        new = state ^ (1 << i)
        occ = (state >> i) & 1
        put(A0, state, new, sp.Rational(1, 2))
        put(A1, state, new, side * (1 - 2 * occ) * sp.Rational(1, 2))

p0 = sp.Matrix([z ** ((state >> 1) & 1) / (8 * (1 + z)) for state in states])
assert all(sp.cancel(v) == 0 for v in A0 * p0)
assert sp.cancel(sum(p0) - 1) == 0
assert all(sum(A0[:, j]) == 0 and sum(A1[:, j]) == 0 for j in states)

# The linear response system has a unique normalized solution because the
# finite open chain is irreducible. The last row enforces zero total mass.
M = A0.copy()
for j in states:
    M[15, j] = 1
Minv = M.inv()

def solve_perturbation(rhs):
    rhs = rhs.copy()
    rhs[15] = 0
    return Minv * rhs

p1 = solve_perturbation(-A1 * p0)
p2 = solve_perturbation(-A1 * p1)
occup = sp.Matrix([[state & 1 for state in states]])
c2 = sp.cancel(-(occup * p2)[0])

P = (15612625*z**8 + 155893675*z**7 + 411771380*z**6 +
     510425170*z**5 + 351379457*z**4 + 142316303*z**3 +
     33739658*z**2 + 4331572*z + 232560)
Q = (27685*z**5 + 108535*z**4 + 149179*z**3 +
     90837*z**2 + 24584*z + 2380)
claimed = -2*z*(z-1)*P / ((z+1)*Q**2)
assert sp.cancel(c2 - claimed) == 0
assert all(v > 0 for v in sp.Poly(P, z).all_coeffs())
assert all(v > 0 for v in sp.Poly(Q, z).all_coeffs())
assert claimed.subs(z, 1) == 0
assert sp.cancel(c2.subs(z, 2) + sp.Rational(9192831529, 1678100281206)) == 0
assert sp.cancel(c2.subs(z, sp.Rational(1, 2)) - sp.Rational(76029578204, 12456309312723)) == 0
print('EXACT_IDENTITY_PASS')
print('SIGN_AND_HOMOGENEOUS_LIMIT_PASS')
print('TWO_EXACT_RATIONAL_SPOT_CHECKS_PASS')
