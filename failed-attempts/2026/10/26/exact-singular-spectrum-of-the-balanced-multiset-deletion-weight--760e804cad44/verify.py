"""Independent finite checks of a weighted multiset-deletion Gram spectrum.

Usage: python verify.py. Finite tests support, but do not establish, the theorem.
"""
from itertools import combinations_with_replacement
from math import comb
import numpy as np


def multisets(m, k):
    return list(combinations_with_replacement(range(m), k))


def deletion_matrix(m, k):
    rows = multisets(m, k-1)
    cols = multisets(m, k)
    index = {u: i for i, u in enumerate(rows)}
    e = np.zeros((len(rows), len(cols)), dtype=np.int64)
    for j, t in enumerate(cols):
        for h in range(k):
            s = t[:h] + t[h+1:]
            e[index[s], j] += 1
    return e


def predicted_gram(m, k):
    if m == 1:
        return [k*k]
    vals = []
    for j in range(k):
        vals.extend([(k-j)*(k+j+m-1)]*comb(m+j-2,j))
    return sorted(vals)


def run():
    count = 0
    for n in range(2, 11):
        for r in range(1, n+1):
            m = n-r+1
            e = deletion_matrix(m, r)
            assert e.shape == (comb(n-1,r-1), comb(n,r))
            assert np.all(e.sum(axis=1) == n), (n,r,"row")
            assert np.all(e.sum(axis=0) == r), (n,r,"column")
            gram = e@e.T
            predicted = predicted_gram(m,r)
            got = np.linalg.eigvalsh(gram.astype(float))
            assert len(got) == len(predicted)
            assert np.allclose(got,predicted,atol=2.e-9,rtol=2.e-10), (n,r,got,predicted)
            assert np.linalg.matrix_rank(e) == e.shape[0]
            assert sum(predicted) == int(np.trace(gram))
            if r >= 2:
                # Verify the adjacent-degree commutator with integer arithmetic.
                d0 = deletion_matrix(m,r-1)
                lhs = e@e.T - d0.T@d0
                assert np.array_equal(lhs,(2*(r-1)+m)*np.eye(e.shape[0],dtype=np.int64))
            count += 1
    print(f"VERIFY_OK cases={count} n_range=2..10 ranks=1..n exact_margins_commutators_trace plus_numeric_Gram_eigenvalues")

if __name__ == '__main__':
    run()
