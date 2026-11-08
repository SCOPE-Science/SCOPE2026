"""Exact and numerical checks for normalized star–triad synchronization.

Usage: python verify_star_triad.py
Requires Python 3 and NumPy.  No external data files are needed.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import numpy as np


def matrices(n, triples, alpha):
    """Return normalized L1, L2 and their mixture, with hub n-1."""
    triples = [tuple(t) for t in triples]
    assert n >= 4 and triples
    assert all(len(set(t)) == 3 and all(0 <= i < n-1 for i in t)
               for t in triples)
    assert len(set(tuple(sorted(t)) for t in triples)) == len(triples)
    a = F(alpha)
    l1 = [[F(0) for _ in range(n)] for _ in range(n)]
    l2 = [[F(0) for _ in range(n)] for _ in range(n)]
    for u in range(n-1):
        h = n-1
        l1[u][u] += 1
        l1[h][h] += 1
        l1[u][h] -= 1
        l1[h][u] -= 1
    for t in triples:
        for u in t:
            l2[u][u] += 1
        for u, v in combinations(t, 2):
            l2[u][v] -= F(1,2)
            l2[v][u] -= F(1,2)
    d1 = F(2*(n-1), n)
    d2 = F(3*len(triples), n)
    mix = [[(1-a)*l1[i][j]/d1 + a*l2[i][j]/d2
            for j in range(n)] for i in range(n)]
    assert all(sum(row) == 0 for row in mix)
    assert sum(mix[i][i] for i in range(n)) == n
    return l1, l2, mix


def uniform_projection(n):
    return [[F(1) if i == j else -F(1,n-1)
             for j in range(n)] for i in range(n)]


def gap(m):
    eig = np.linalg.eigvalsh(np.asarray(m, dtype=float))
    return float(eig[1])


def pair_balanced(n, triples):
    from collections import Counter
    c = Counter()
    for triple in triples:
        c.update(tuple(sorted(p)) for p in combinations(triple, 2))
    values = [c[(u,v)] for u,v in combinations(range(n-1), 2)]
    return len(set(values)) == 1 and values[0] > 0


def test_balanced(n, triples):
    alpha = F(n-2,n)
    l1, l2, mix = matrices(n, triples, alpha)
    assert pair_balanced(n, triples)
    assert mix == uniform_projection(n)
    assert abs(gap(mix) - n/(n-1)) < 1e-10
    for a in [F(0), F(1,10), F(1,3), alpha, F(4,5), F(1)]:
        _, _, M = matrices(n, triples, a)
        A = F(n,2*(n-1))
        B = F(n,n-2)
        C = F(n*n,2*(n-1))
        formula = min(A*(1-a)+B*a, C*(1-a))
        assert abs(gap(M)-float(formula)) < 1e-10
    return True


def run():
    tested = 0
    for n in range(4,16):
        all_triples = list(combinations(range(n-1),3))
        test_balanced(n, all_triples)
        tested += 1
    fano = [
        (0,1,2), (0,3,4), (0,5,6), (1,3,5),
        (1,4,6), (2,3,6), (2,4,5)
    ]
    assert len(fano) == 7 and pair_balanced(8, fano)
    assert len(list(combinations(range(7),3))) == 35
    for a in (F(0), F(1,5), F(1,2), F(3,4), F(1)):
        _, _, sparse = matrices(8, fano, a)
        _, _, dense = matrices(8, list(combinations(range(7),3)), a)
        assert sparse == dense
    test_balanced(8, fano)
    tested += 1
    _, _, fano_m = matrices(8, fano, F(3,4))
    assert fano_m == uniform_projection(8)
    _, _, pure_star = matrices(8, fano, F(0))
    assert abs(gap(pure_star) - F(4,7)) < 1e-10
    assert abs(gap(fano_m) - F(8,7)) < 1e-10
    examined = 0
    equality_cases = 0
    for n in (4,5,6):
        ts = list(combinations(range(n-1), 3))
        alphas = [F(0),F(1,5),F(1,3),F(1,2),F(n-2,n),F(4,5),F(1)]
        for mask in range(1,1<<len(ts)):
            H = [t for j,t in enumerate(ts) if mask>>j & 1]
            for a in alphas:
                _, _, M = matrices(n,H,a)
                actual = gap(M)
                bound = n/(n-1)
                assert actual <= bound + 1e-10
                equality = abs(actual-bound) < 1e-10
                exact_characterization = (a == F(n-2,n) and pair_balanced(n,H))
                assert equality == exact_characterization
                equality_cases += int(equality)
                examined += 1
    print('PASS: %d pair-balanced design checks (including Fano)' % tested)
    print('PASS: %d exhaustive small-network/parameter comparisons' % examined)
    print('PASS: %d exact optimum comparisons, all equal to 2-design criterion' % equality_cases)
    print('PASS: for n=8, seven Fano triples attain exact 8/7 (vs star 4/7)')
    print('PASS: Fano seven-triple and complete 35-triple networks have identical matrices for all tested alpha')

if __name__ == '__main__':
    run()
