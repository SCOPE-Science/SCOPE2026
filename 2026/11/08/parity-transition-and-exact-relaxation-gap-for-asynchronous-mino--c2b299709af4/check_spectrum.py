"""Independent spectral checks for the recurrent minority Markov chains.

Requires Python >=3.9 and NumPy. The Markov matrix is constructed by
selecting each graph vertex and counting its actual closed-neighborhood bits.
"""
from itertools import combinations
from math import comb, sqrt
import numpy as np


def recurrent_states(m):
    n = 2 * m
    ret = []
    for s in range(1 << n):
        S = s.bit_count()
        k = sum(((s >> (2 * i)) & 1) != ((s >> (2 * i + 1)) & 1) for i in range(m))
        if m % 2 == 0:
            keep = (S == m and k == 0)
        else:
            keep = (S == m and k == 1) or (abs(S - m) == 1 and k == 0)
        if keep:
            ret.append(s)
    return ret


def direct_transition(m):
    n = 2 * m
    ss = recurrent_states(m)
    idx = {s: i for i, s in enumerate(ss)}
    P = np.zeros((len(ss), len(ss)), dtype=float)
    for i, s in enumerate(ss):
        for v in range(n):
            ones = sum((s >> w) & 1 for w in range(n) if w != (v ^ 1))
            bit = 1 if ones < (n - 1) / 2 else 0
            t = (s & ~(1 << v)) | (bit << v)
            assert t in idx
            P[i, idx[t]] += 1 / n
    assert np.allclose(P, P.T, atol=1e-14)
    assert np.allclose(P.sum(axis=0), 1, atol=1e-14)
    assert np.allclose(P.sum(axis=1), 1, atol=1e-14)
    return ss, P


def middle_graph_eigs(m):
    r = (m - 1) // 2
    A = list(combinations(range(m), r))
    B = list(combinations(range(m), r + 1))
    small = np.zeros((len(A), len(B)), float)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if set(a).issubset(b):
                small[i, j] = 1
    H = np.block([[np.zeros((len(A), len(A))), small],
                  [small.T, np.zeros((len(B), len(B))) ]])
    vals = np.linalg.eigvalsh(H)
    predicted = []
    for j in range(r + 1):
        mult = comb(m, j) - (comb(m, j - 1) if j else 0)
        predicted += [r + 1 - j] * mult + [-r - 1 + j] * mult
    assert np.allclose(vals, sorted(predicted), atol=1e-9)
    return len(vals)


if __name__ == '__main__':
    for m in [3, 5, 7]:
        print('m=%d middle_base_vertices=%d' % (m, middle_graph_eigs(m)))
        ss, P = direct_transition(m)
        d = (m + 1) / 2
        exact_gap = (d + 1 - sqrt((d + 1) ** 2 - 2)) / (2 * m)
        eigs = np.linalg.eigvalsh(P)
        gap = 1 - eigs[-2]
        assert abs(gap - exact_gap) < 2e-12, (m, gap, exact_gap)
        print('m=%d recurrent=%d gap=%.14f predicted=%.14f' % (m, len(ss), gap, exact_gap))
    print('INDEPENDENT_SPECTRAL_CHECK_PASS')
