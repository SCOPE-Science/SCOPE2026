"""Independent finite-dimensional checks of the orthant polynomial concentration theorem.

Requires Python >=3.9 and NumPy. The theorem for all dimensions is proved
by the accompanying representation argument, not by these finite checks.
"""
from functools import lru_cache
from itertools import combinations
from math import exp, lgamma, pi
import numpy as np


def poly(d, terms):
    """A polynomial as a sparse exponent-tuple -> coefficient dictionary."""
    out = {}
    for c, indices in terms:
        e = tuple(indices.count(i) for i in range(d))
        out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


@lru_cache(None)
def moment(exponents, restricted):
    """Normalized integral of one monomial over the unit ball/orthant."""
    if not restricted and any(e % 2 for e in exponents):
        return 0.0
    d = len(exponents)
    logvalue = (lgamma(d / 2 + 1)
                - lgamma((d + sum(exponents)) / 2 + 1)
                + sum(lgamma((e + 1) / 2) - lgamma(.5)
                      for e in exponents))
    return exp(logvalue) / (2 ** d if restricted else 1)


def form(p, q, restricted):
    return sum(a * b * moment(tuple(i + j for i, j in zip(e, f)), restricted)
               for e, a in p.items() for f, b in q.items())


def gram(polys, restricted):
    n = len(polys)
    ans = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            ans[i, j] = ans[j, i] = form(polys[i], polys[j], restricted)
    return ans


def generalized_eig(A, B):
    L = np.linalg.cholesky(B)
    C = np.linalg.solve(L, A)
    C = np.linalg.solve(L, C.T).T
    return np.linalg.eigvalsh((C + C.T) / 2)


def block_polys(d):
    ones = [(1, ())]
    linear = [(1, (i,)) for i in range(d)]
    diag = [(1, (i, i)) for i in range(d)]
    edge = [(1, (i, j)) for i, j in combinations(range(d), 2)]
    trivial = [poly(d, t) for t in (ones, linear, diag, edge)]
    std = [poly(d, [(1, (0,)), (-1, (1,))]),
           poly(d, [(1, (0, 0)), (-1, (1, 1))]),
           poly(d, [(1, (0, j)) for j in range(2, d)] +
                   [(-1, (1, j)) for j in range(2, d)])]
    second = [poly(d, [(1, (0, 1)), (-1, (0, 2)),
                       (-1, (3, 1)), (1, (3, 2))])]
    return trivial, std, second


def all_monomials(d):
    terms = [[(1, ())]]
    terms += [[(1, (i,))] for i in range(d)]
    terms += [[(1, (i, i))] for i in range(d)]
    terms += [[(1, (i, j))] for i, j in combinations(range(d), 2)]
    return [poly(d, t) for t in terms]


def verify(d):
    T0, T1, T2 = block_polys(d)
    reduced = [generalized_eig(gram(T, True), gram(T, False))
               for T in (T0, T1, T2)]
    expected = sorted(list(reduced[0]) + list(reduced[1]) * (d - 1) +
                      list(reduced[2]) * (d * (d - 3) // 2))
    full = generalized_eig(gram(all_monomials(d), True),
                           gram(all_monomials(d), False))
    assert len(full) == (d + 1) * (d + 2) // 2
    assert np.allclose(full, expected, rtol=3e-8, atol=2e-11)
    special = (1 - 2 / pi)**2 / 2**d
    assert abs(reduced[2][0] - special) < 1e-12
    assert abs(sum(full) - len(full) / 2**d) < 1e-10
    assert 0 < min(full) < max(full) < 1
    return float(full[0]), float(full[-1]), float(reduced[2][0]), len(full)


if __name__ == '__main__':
    for d in range(4, 9):
        a, b, c, N = verify(d)
        print(f'd={d} dimension={N} minimum={a:.12g} '
              f'maximum={b:.12g} special={c:.12g}: PASS')
    print('All checks passed.')
