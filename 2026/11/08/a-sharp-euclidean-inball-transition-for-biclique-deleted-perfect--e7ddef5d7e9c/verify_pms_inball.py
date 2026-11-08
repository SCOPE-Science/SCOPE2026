"""Finite, independently reproducible tests for a bipartite subgraph-polytope inball theorem.

Requires Python 3, numpy and scipy. Finite checks support, but do not prove,
the theorem for all integer parameters.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog


def induced_perfect_matching(a, b, n, s):
    """Brute-force search, without using the Hall inequality being tested."""
    if len(a) != len(b):
        return False
    if not a:
        return True
    for perm in itertools.permutations(b):
        if all(not (i < s and j < s) for i, j in zip(a, perm)):
            return True
    return False


def check(n, s):
    assert 2 <= n and 1 <= s < n
    N = 2*n
    w = np.r_[np.ones(n), -np.ones(n)]
    projection = np.eye(N) - np.outer(w, w)/(2*n)
    g = np.r_[np.ones(s), np.zeros(n-s), np.zeros(s), -np.ones(n-s)]
    normals = np.concatenate([np.eye(N), -np.eye(N), g[None, :]])
    rhs = np.r_[np.ones(N), np.zeros(N), 0.]
    lengths = np.linalg.norm(normals @ projection, axis=1)
    ell = math.sqrt((2*n-1)/(2*n))
    eta = math.sqrt(n/2)
    assert np.allclose(lengths[:2*N], ell) and abs(lengths[-1]-eta) < 1e-12
    r_box = 1/(2*ell)
    r_hall = (n-s)/(n*ell+eta)
    r = min(r_box, r_hall)
    low = min(0.5, r*ell)
    high = 1-low
    center = np.r_[[low]*s, [high]*(n-s), [low]*s, [high]*(n-s)]
    if r_box < r_hall:
        center[:] = 0.5
    optimum = linprog(np.r_[np.zeros(N), -1.], A_ub=np.c_[normals, lengths],
                      b_ub=rhs, A_eq=np.c_[w[None, :], np.zeros((1, 1))],
                      b_eq=[0.], bounds=[(None, None)]*(N+1), method='highs')
    assert optimum.success and abs(optimum.x[-1]-r) < 2e-9
    assert np.linalg.norm(center @ w) < 2e-10
    assert np.max(normals @ center + lengths*r-rhs) < 2e-9
    active = np.abs(normals @ center + lengths*r-rhs) < 1e-8
    expected = 4*n if r_box < r_hall else 2*n+1
    assert int(active.sum()) == expected
    assert abs(r_box-r_hall) > 1e-8
    if n <= 5:
        vectors = []
        all_candidates = 0
        for a_bits in itertools.product((0,1), repeat=n):
            aa = tuple(i for i,x in enumerate(a_bits) if x)
            for b_bits in itertools.product((0,1),repeat=n):
                bb = tuple(j for j,x in enumerate(b_bits) if x)
                hall_ok = len(aa)==len(bb) and (len([i for i in aa if i<s]) <= len([j for j in bb if j>=s]))
                matching_ok = induced_perfect_matching(aa,bb,n,s)
                assert hall_ok == matching_ok, (n,s,aa,bb)
                all_candidates += 1
                if matching_ok:
                    vectors.append(a_bits + b_bits)
        vectors = np.array(vectors, dtype=float)
        assert np.linalg.matrix_rank(vectors - vectors[0]) == N-1
        for idx in np.where(active)[0]:
            face = vectors[np.abs(vectors @ normals[idx]-rhs[idx]) < 1e-8]
            assert face.shape[0] >= N-1
            assert np.linalg.matrix_rank(face - face[0]) == N-2, (n,s,idx)
        assert all_candidates == 2**N
    return expected


def main():
    tested = 0
    for n in range(2,7):
        for s in range(1,n):
            check(n,s)
            tested += 1
    assert tested == 15
    print('PMS_BICLIQUE_INBALL_HALL_AND_FACET_CHECKS_PASSED', tested)


if __name__ == '__main__':
    main()
