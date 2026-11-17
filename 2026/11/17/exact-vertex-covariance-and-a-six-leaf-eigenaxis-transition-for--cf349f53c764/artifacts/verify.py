"""Exact-rational, standalone checks for the two-hub bipartite zonotope theorem.

Run: python3 artifacts/verify.py (Python >=3.9; standard library only).
The finite checks supplement, rather than replace, the general proof.
"""
from fractions import Fraction as F
from itertools import permutations, product


def closed_spectrum(q):
    assert q >= 3
    d = 2 * 3**q - 2**q
    return (d, F(q * (q + 2) * 3**(q - 2), d),
            F(4 * 3**(q - 1) - 2**q, d),
            F(q + 2, 2) * F(4 * 3**(q - 1) - 2**q, d))


def coordinate_vector(s, q):
    return ([F(sum(s[a*q + j] for j in range(q)), 2) for a in range(2)]
            + [F(-s[j] - s[q + j], 2) for j in range(q)])


def independent_permutation_vertices(q):
    # Acyclic orientations are obtained as signs of edges under total orders.
    signs = set()
    for pi in permutations(range(q + 2)):
        pos = {v: i for i, v in enumerate(pi)}
        signs.add(tuple(1 if pos[a] < pos[j+2] else -1
                        for a in range(2) for j in range(q)))
    return signs


def direct_ternary_vertices(q):
    # Distinct construction: two product alphabets minus their intersection.
    alternatives = (((-1, -1), (-1, 1), (1, 1)),
                    ((-1, -1), (1, -1), (1, 1)))
    out = set()
    for alphabet in alternatives:
        for colpairs in product(alphabet, repeat=q):
            out.add(tuple(t[a] for a in range(2) for t in colpairs))
    return out


def compute_matrix(signs, q):
    n = len(signs)
    rows = [coordinate_vector(s, q) for s in signs]
    assert all(sum(z) == 0 for z in rows)
    mean = [sum((z[i] for z in rows), F(0))/n for i in range(q+2)]
    assert mean == [0]*(q+2)
    return [[sum((z[i]*z[j] for z in rows), F(0))/n
             for j in range(q+2)] for i in range(q+2)]


def matrix_eigen_check(m, q, A, B, C):
    # Test full operator equality on spanning eigenbasis, not just trace.
    basis = [([1, -1] + [0]*q, A)]
    basis += [([0, 0] + [1 if j==0 else (-1 if j==k else 0)
                            for j in range(q)], B) for k in range(1,q)]
    basis += [([q, q] + [-2]*q, C)]
    for vector, eig in basis:
        lhs = [sum((m[i][j]*vector[j] for j in range(q+2)),F(0))
               for i in range(q+2)]
        assert lhs == [eig*x for x in vector], (q, vector, lhs, eig)
    ones=[1]*(q+2)
    assert all(sum((m[i][j]*ones[j] for j in range(q+2)), F(0)) == 0
               for i in range(q+2))


checked=0
for q in range(3,7):
    s=independent_permutation_vertices(q)
    d, A, B, C=closed_spectrum(q)
    assert len(s)==d
    assert s==direct_ternary_vertices(q)
    m=compute_matrix(s,q)
    matrix_eigen_check(m,q,A,B,C)
    checked+=1

# Larger independent ternary enumerations (without total permutations).
for q in range(7,10):
    s=direct_ternary_vertices(q)
    d,A,B,C=closed_spectrum(q)
    assert len(s)==d
    m=compute_matrix(s,q)
    matrix_eigen_check(m,q,A,B,C)
    checked+=1

for q in range(3,101):
    d,A,B,C=closed_spectrum(q)
    assert 0 < B < A
    assert C > B
    assert (C>A)==(q <= 5)
    gap = F(q+2,d)*((6-q)*3**(q-2)-2**(q-1))
    assert C-A == gap
    assert max(A,C)/B == (F(q+2,2) if q<=5
                           else F(q*(q+2)*3**(q-2),12*3**(q-2)-2**q))
print('TWO_HUB_VERTEX_COVARIANCE_CHECKS_PASSED full_matrices=%d q_inequalities=98' % checked)
