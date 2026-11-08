"""Exact checks for a four-spine caterpillar principal-specialization theorem.

Run with Python 3.9+; requires only the standard library.
"""
from collections import defaultdict
from itertools import product
from math import comb


def clean(a):
    return {k: v for k, v in a.items() if v}


def add(a, b, sign=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + sign * v
    return clean(out)


def mul(a, b, cutoff=None):
    out = defaultdict(int)
    for i, ai in a.items():
        for j, bj in b.items():
            if cutoff is None or i + j <= cutoff:
                out[i + j] += ai * bj
    return clean(out)


def power(a, n, cutoff=None):
    out = {0: 1}
    while n:
        if n & 1:
            out = mul(out, a, cutoff)
        n //= 2
        if n:
            a = mul(a, a, cutoff)
    return out


def spine_polynomial(alpha, k, cutoff=None):
    """Ordinary principal specialization, by independent leaf choices."""
    cache = {}
    def weight(c, length):
        key = (c, length)
        if key not in cache:
            other = {j: 1 for j in range(k) if j != c}
            cache[key] = mul({c: 1}, power(other, length - 1, cutoff), cutoff)
        return cache[key]
    result = {}
    for s in product(range(k), repeat=4):
        if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
            continue
        term = {0: 1}
        for c, length in zip(s, alpha):
            term = mul(term, weight(c, length), cutoff)
        result = add(result, term)
    return result


def direct_actual_coloring(alpha, k=3):
    """Independent DFS on each of the vertices; records exponent and color set."""
    n = sum(alpha)
    parent = [-1, 0, 1, 2]
    for j, a in enumerate(alpha):
        parent.extend([j] * (a - 1))
    assert len(parent) == n
    colors = [-1] * n
    counts = defaultdict(int)
    def dfs(v, total, mask):
        if v == n:
            counts[(total, mask.bit_count())] += 1
            return
        for c in range(k):
            if parent[v] >= 0 and colors[parent[v]] == c:
                continue
            colors[v] = c
            dfs(v+1, total+c, mask | (1<<c))
    dfs(0, 0, 0)
    return dict(counts)


def main():
    q = {1: 1}; q2 = {2: 1}; one = {0: 1}
    L0 = add(q, q2)
    L1 = add(one, q2)
    L2 = add(one, q)
    D0 = mul(L0, L0)
    D2 = mul(q2, mul(L2, L2))
    assert D0 == D2
    K01 = mul(mul(L0, L1), add(L1, L0, -1))
    K12 = mul(mul(L1, L2), add(L2, L1, -1))
    assert K01 == K12
    print('FORMAL_THREE_COLOR_CANCELLATION_IDENTITY_OK')

    for h in range(13):
        a = (h+2, h+1, h+3, 3)
        b = (h+3, h+1, h+2, 3)
        assert spine_polynomial(a, 3) == spine_polynomial(b, 3)
        assert a != b and a != b[::-1]
        assert a[::-1] != b
    print('THREE_COLOR_SPINE_POLYNOMIAL_OK h=0..12')

    for h in range(3):
        a = (h+2, h+1, h+3, 3)
        b = (h+3, h+1, h+2, 3)
        da, db = direct_actual_coloring(a), direct_actual_coloring(b)
        assert da == db
        for alpha, d in ((a, da), (b, db)):
            s = defaultdict(int)
            for (exp, ncolors), count in d.items():
                assert ncolors in (2, 3)
                s[exp] += count
            assert dict(s) == spine_polynomial(alpha, 3)
    print('DIRECT_VERTEX_COLORING_AND_T_REFINEMENT_OK h=0..2')

    got = []
    for h in range(17):
        a = (h+2, h+1, h+3, 3)
        b = (h+3, h+1, h+2, 3)
        da = spine_polynomial(a, 4, cutoff=8).get(8, 0)
        db = spine_polynomial(b, 4, cutoff=8).get(8, 0)
        got.append(da-db)
    assert got == [14, 4] + [2]*15, got
    print('FOUR_COLOR_Q8_CERTIFICATE_OK h=0..16 values=' + str(got))
    for h in (19, 25, 40):
        a = (h+2, h+1, h+3, 3)
        b = (h+3, h+1, h+2, 3)
        assert spine_polynomial(a, 4, cutoff=8).get(8,0) - spine_polynomial(b, 4, cutoff=8).get(8,0) == 2
    print('FOUR_COLOR_ADDITIONAL_EXACT_CHECKS_OK h=19,25,40')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
