"""Reproducibility diagnostics for tri-direction Poisson zero-cell sidedness."""
from fractions import Fraction
from itertools import combinations
import math

import numpy as np


def predictions(rates):
    rates = tuple(rates)
    b = {}
    for size in (1, 2, 3):
        for I in combinations(range(3), size):
            L = sum(rates[i] for i in I)
            val = 1
            for j, rate in enumerate(rates):
                val *= rate / (L if j in I else L + rate)
            b[I] = val
    u = {k: sum(v for I, v in b.items() if len(I) == k) for k in (1, 2, 3)}
    S = sum(b[(i,)] ** 2 for i in range(3))
    return (2 * u[3], 2*u[2] - 6*u[3] + S,
            2*u[1]-4*u[2]+6*u[3]-2*S,
            1-2*u[1]+2*u[2]-2*u[3]+S)


def redundant_count(A, B):
    return int(np.count_nonzero(A > B.sum() - B) +
               np.count_nonzero(B > A.sum() - A))


def geometric_vertices(A, B):
    h = math.sqrt(3) / 2
    normals = np.array([[1, 0], [-.5, h], [-.5, -h]], dtype=float)
    G = np.vstack([normals, -normals])
    bounds = np.r_[A, B]
    vertices = []
    for i, j in combinations(range(6), 2):
        M = G[[i, j]]
        if abs(np.linalg.det(M)) < 1e-12:
            continue
        v = np.linalg.solve(M, bounds[[i, j]])
        if (np.all(G @ v <= bounds + 1e-9) and
                all(np.linalg.norm(v-w) > 1e-8 for w in vertices)):
            vertices.append(v)
    return len(vertices)


def main():
    R = Fraction
    assert predictions([R(1)] * 3) == (R(2,27),R(67,144),R(25,72),R(49,432))
    assert sum(predictions([R(1)] * 3)) == 1
    print('EXACT_FOUR_TYPE_PROBABILITIES_OK')
    rng = np.random.default_rng(21058)
    for rates in [(1.,1.,1.),(.3,1.2,2.4),(.5,.5,4.)]:
        n = 300000
        A = rng.exponential(size=(n,3)) / rates
        B = rng.exponential(size=(n,3)) / rates
        K = np.sum(A > B.sum(axis=1,keepdims=True)-B,axis=1) + \
            np.sum(B > A.sum(axis=1,keepdims=True)-A,axis=1)
        assert np.all((K >= 0) & (K <= 3))
        actual = np.array([np.mean(K == 6-i) for i in range(3,7)])
        expected = np.asarray(predictions(rates),float)
        assert np.max(np.abs(actual-expected)) < .006, (rates,actual,expected)
        for a,b in zip(A[:5000],B[:5000]):
            count = geometric_vertices(a,b)
            assert count == 6-redundant_count(a,b), (rates,count,a,b)
        print('RATES',rates,'PREDICTED',expected,'SAMPLED',actual)
    print('DIRECT_GEOMETRIC_15000_SAMPLES_OK')
    print('ALL_ZERO_CELL_DIAGNOSTICS_OK')

if __name__ == '__main__':
    main()
