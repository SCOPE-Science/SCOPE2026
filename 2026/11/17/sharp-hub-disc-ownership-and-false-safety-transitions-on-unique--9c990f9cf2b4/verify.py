"""Exact-arithmetic checks for the degree-similarity hub-disc theorem.

Requires sympy; checks finite examples only. Analytic proof is in RESULT.md.
"""
import sympy as sp


def check_adjacency(A, q):
    n = A.rows
    assert A.shape == (n, n) and A == A.T
    degrees = [sum(A[i, j] for j in range(n)) for i in range(n)]
    assert min(degrees) > 0
    D_q = sp.diag(*(d**q for d in degrees))
    J = -sp.eye(n) + D_q.inv()*A*D_q
    assert (D_q*J*D_q.inv() - (A - sp.eye(n))).is_zero_matrix
    assert sp.factor(J.charpoly().as_expr() - (A-sp.eye(n)).charpoly().as_expr()) == 0
    return J, degrees


def star(n):
    A = sp.zeros(n+1)
    for j in range(1, n+1):
        A[0, j] = A[j, 0] = 1
    return A


for n in (2, 3, 4, 8):
    A = star(n)
    for q in (sp.Rational(1,4), sp.Rational(1,2), sp.Rational(3,4), 1, 2, 3):
        J, ds = check_adjacency(A, q)
        expected = (sp.Symbol('lambda')+1)**(n-1)*((sp.Symbol('lambda')+1)**2-n)
        assert sp.expand(J.charpoly().as_expr()-expected) == 0
        hub_radius = sum(J[0, j] for j in range(1, n+1))
        leaf_radius = J[1, 0]
        assert sp.simplify(hub_radius - n**(1-q)) == 0
        assert sp.simplify(leaf_radius - n**q) == 0
        # The largest eigenvalue is sqrt(n)-1; test disc ownership.
        assert bool(sp.simplify(hub_radius >= sp.sqrt(n))) == bool(q <= sp.Rational(1,2))
        assert bool(sp.simplify(leaf_radius >= sp.sqrt(n))) == bool(q >= sp.Rational(1,2))
        assert bool(sp.simplify(hub_radius < 1)) == bool(q > 1)

# Non-star graph: one vertex of degree 4, an edge between two leaves.
A = star(4)
A[1,2] = A[2,1] = 1
for q in (2, 4, 8):
    J, ds = check_adjacency(A, q)
    assert ds == [4,2,2,1,1]
    assert sum(J[0,j] for j in range(1,A.rows)) < 1
    # Positive Rayleigh quotient for A-I on the star-supported vector.
    v = sp.Matrix([2,1,1,1,1])
    assert (v.T*(A-sp.eye(A.rows))*v)[0] > 0

print('VERIFY_OK similarity_cases=27 star_cases=24 nonstar_cases=3')

# Finite numerical threshold checks for the monotone hub radius.
# They support, but do not replace, the graph-uniform proof.
import numpy as np
from scipy.optimize import brentq
for A0 in (star(2), star(4), A):
    deg = np.asarray([sum(float(A0[i, j]) for j in range(A0.cols)) for i in range(A0.rows)])
    assert (deg == deg.max()).sum() == 1
    h = int(deg.argmax()); Delta = deg[h]
    nei = [int(j) for j in range(A0.cols) if A0[h,j] == 1]
    radius = lambda q: sum((deg[j]/Delta)**q for j in nei)
    rho = float(np.linalg.eigvalsh(np.asarray(A0.tolist(),dtype=float))[-1])
    assert 1 < rho < Delta
    qspec = brentq(lambda q: radius(q)-rho,0,50)
    qsafe = brentq(lambda q: radius(q)-1,0,50)
    assert 0 < qspec < qsafe
    assert abs(radius(qspec)-rho) < 1e-10
    assert abs(radius(qsafe)-1) < 1e-10
    if A0 == star(2) or A0 == star(4):
        assert abs(qspec-.5)<1e-10 and abs(qsafe-1)<1e-10
print('VERIFY_OK universal_threshold_examples=3')
