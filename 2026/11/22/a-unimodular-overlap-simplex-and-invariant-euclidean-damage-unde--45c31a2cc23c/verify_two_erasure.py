"""Numerical cross-check of the two-deletion theorem for hypersimplices.

Dependencies: Python 3, NumPy, SciPy and SymPy. Finite tests do not replace the proof.
"""
from itertools import combinations
from math import comb, factorial
import numpy as np
from scipy.spatial import ConvexHull
from sympy import Matrix


def eulerian_hypersimplex(n, k):
    return sum((-1)**j * comb(n,j) * (k-j)**(n-1) for j in range(k+1))


def normalized_volume(verts):
    n = verts.shape[1]
    projected = verts[:,:-1]
    if np.linalg.matrix_rank(projected-projected[0], tol=1e-9) < n-1:
        return 0.0
    # Projection to the first n-1 coordinates has Jacobian 1/sqrt(n).
    return factorial(n-1) * ConvexHull(projected).volume


def main():
    cases = 0
    for n in range(4,9):
        for k in range(2,n-1):
            supports = list(combinations(range(n), k))
            vertices = np.array([[int(x in h) for x in range(n)] for h in supports], dtype=float)
            full = eulerian_hypersimplex(n,k)
            assert abs(normalized_volume(vertices)-full) < 2e-5
            first = tuple(range(k))
            i = supports.index(first)
            for t in range(1,min(k,n-k)+1):
                second = tuple(list(range(k-t)) + list(range(k,k+t)))
                j = supports.index(second)
                truncated = np.delete(vertices,[i,j],axis=0)
                target = full-2*comb(n-2,k-1)+int(t==1)
                observed = normalized_volume(truncated)
                assert abs(observed-target) < 2e-5, (n,k,t,observed,target)
                for h in (first,second):
                    w = np.ones(n) / (n-k)
                    w[list(h)] = 1-1/k
                    assert abs(w.sum()-k) < 1e-11
                    assert sum(w[x] for x in first) <= k-1+1e-11
                    assert sum(w[x] for x in second) <= k-1+1e-11
                    v = np.array([int(x in h) for x in range(n)],dtype=float)
                    assert abs(np.dot(v-w,v-w) - n/(k*(n-k))) < 1e-11
                cases += 1
        print('n=%d checked all ranks and two-deletion intersection types' % n)
    det_cases = 0
    for n in range(4,11):
        for k in range(2,n-1):
            common = tuple(range(k-1))
            i,j = k-1,k
            outer = tuple(range(k+1,n))
            supports = [common+(i,), common+(j,)]
            supports.extend(tuple(a for a in common if a!=q)+(i,j) for q in common)
            supports.extend(common+(b,) for b in outer)
            assert len(supports)==n
            rows = [[int(c in s)-int(c in supports[0]) for c in range(n-1)] for s in supports[1:]]
            assert abs(Matrix(rows).det())==1, (n,k)
            det_cases+=1
    print('PASS:', cases,'rank/intersection profiles; volume and Euclidean nearest-foot identities; ', det_cases, 'exact unimodular determinant tests')

if __name__ == '__main__':
    main()
