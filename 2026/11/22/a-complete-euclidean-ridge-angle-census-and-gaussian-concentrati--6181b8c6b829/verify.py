"""Exact finite checks of the simplex-sum stellohedron ridge-angle census.
Run: python3 verify.py (standard library only)."""
from fractions import Fraction
from itertools import permutations, combinations
from math import comb, acos, pi, sqrt


def tubes(m):
    leaves = [frozenset([i]) for i in range(1, m + 1)]
    hubs = [frozenset([0] + [i + 1 for i in range(m) if mask & (1 << i)])
            for mask in range(1 << m)]
    return leaves + hubs


def vertices(m):
    ts = tubes(m)
    out = set()
    for order in permutations(range(m + 1)):
        rank = {j: k for k, j in enumerate(order)}
        v = [0] * (m + 1)
        for tube in ts:
            v[min(tube, key=rank.__getitem__)] += 1
        out.add(tuple(v))
    return sorted(out)


def rank_over_q(rows):
    basis = {}
    for row in rows:
        v = [Fraction(x) for x in row]
        for p, b in basis.items():
            if v[p]:
                coeff = v[p]
                v = [a - coeff * z for a, z in zip(v, b)]
        p = next((i for i, x in enumerate(v) if x), None)
        if p is not None:
            coeff = v[p]
            basis[p] = [a / coeff for a in v]
    return len(basis)


def compatible(a, b):
    return a < b or b < a or (a.isdisjoint(b) and 0 not in (a | b))


def normal_cosine(a, b, m):
    N = m + 1
    dot_scaled = N * len(a & b) - len(a) * len(b)
    sq = Fraction(dot_scaled * dot_scaled,
                  len(a) * (N - len(a)) * len(b) * (N - len(b)))
    return (1 if dot_scaled > 0 else -1 if dot_scaled < 0 else 0), sq


def predicted_counts(m):
    A = comb(m, 2)
    B = sum(s * comb(m, s) for s in range(1, m))
    C = sum(comb(m, t) * (2**t - 1) for t in range(1, m))
    return A, B, C


for m in range(2, 7):
    ts = [a for a in tubes(m) if len(a) < m + 1]
    predicted = predicted_counts(m)
    observed = [0, 0, 0]
    for a, b in combinations(ts, 2):
        if not compatible(a, b):
            continue
        if 0 not in a and 0 not in b:
            kind = 0
        elif (0 in a) != (0 in b):
            kind = 1
        else:
            kind = 2
        observed[kind] += 1
        sign, cos2 = normal_cosine(a, b, m)
        assert 0 < cos2 < 1
        assert sign == (-1 if kind == 0 else 1)
        if kind == 1:
            s = len(a) - 1 if 0 in a else len(b) - 1
            assert cos2 == Fraction(m - s, m * (s + 1))
        if kind == 2:
            s, t = sorted((len(a) - 1, len(b) - 1))
            assert cos2 == Fraction((s + 1) * (m - t), (t + 1) * (m - s))
    assert tuple(observed) == predicted
    assert sum(predicted) == 3**m + (m - 4) * 2**(m-1) + comb(m-1, 2)
    if m <= 5:
        vv = vertices(m)
        support = {a: min(sum(v[i] for i in a) for v in vv) for a in ts}
        active = {a: {j for j, v in enumerate(vv)
                      if sum(v[i] for i in a) == support[a]} for a in ts}
        for a, b in combinations(ts, 2):
            ix = active[a] & active[b]
            if not ix:
                observed_ridge = False
            else:
                v = [vv[j] for j in sorted(ix)]
                observed_ridge = rank_over_q(
                    [[v1-v0 for v1,v0 in zip(w, v[0])] for w in v[1:]]) == m-2
            assert observed_ridge == compatible(a,b), (m,a,b)
    print('m=',m,'vertices=',len(vertices(m)) if m<=5 else 'not enumerated',
          'classes=',predicted,'face_ranks_checked=',m<=5)

for m in range(4, 101):
    bs = [Fraction(m-s, m*(s+1)) for s in range(1,m)]
    cs = [Fraction((s+1)*(m-t),(t+1)*(m-s))
          for t in range(1,m) for s in range(t)]
    optimum = max(bs+cs)
    if m % 2 == 0:
        k=m//2
        assert optimum == Fraction(k*k,(k+1)**2)
    else:
        k=(m-1)//2
        assert optimum == Fraction(k,k+2)
print('STELLOHEDRON_RIDGE_SPECTRUM_PASS')
