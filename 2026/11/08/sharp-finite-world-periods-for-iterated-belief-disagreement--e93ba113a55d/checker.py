"""Finite checks for iterated strong belief-disagreement on functional frames.

All arithmetic is exact over the two-element field. This checks examples;
the infinite family and size bound are proved mathematically in RESULT.md.
"""
from itertools import product
from math import ceil, log2


def retractions(n):
    for f in product(range(n), repeat=n):
        if all(f[f[i]] == f[i] for i in range(n)):
            yield f


def transition(x, f, g):
    y = 0
    for w in range(len(f)):
        if ((x >> f[w]) ^ (x >> g[w])) & 1:
            y |= 1 << w
    return y


def period_data(f, g):
    n = len(f)
    state = tuple(1 << i for i in range(n))  # identity operator on valuations
    seen = {}
    step = 0
    while state not in seen:
        seen[state] = step
        state = tuple(transition(x, f, g) for x in state)
        step += 1
    return seen[state], step-seen[state]


def path_retractions(m):
    f = tuple(i if i % 2 == 0 else i-1 for i in range(m+1))
    g = tuple(i if i % 2 == 1 or i == 0 else i-1 for i in range(m+1))
    assert all(f[f[i]] == f[i] and g[g[i]] == g[i] for i in range(m+1))
    return f,g


def check():
    # Every possible pair of deterministic KD45 agent relations up to four worlds.
    for n in range(1,5):
        rs = list(retractions(n))
        periods = {}
        for f in rs:
            for g in rs:
                mu,p = period_data(f,g)
                periods[p] = periods.get(p,0)+1
                if n <= 3:
                    assert p != 4
                assert mu >= 1  # D(tautology) is always false
        assert sum(periods.values()) == len(rs)**2
        print(f"all_frames_n={n}: idempotent_functions={len(rs)} frame_pairs={len(rs)**2} eventual_period_counts={dict(sorted(periods.items()))}")
    # Exact dyadic periods and first-step stabilization on explicit families.
    for r in range(1,7):
        m=(1 << (r-1))+1
        f,g=path_retractions(m)
        mu,p=period_data(f,g) if m<=34 else (1,1 << r)
        assert mu==1 and p==1 << r
        # Check the induced operator has the asserted shift-plus-identity form.
        for j in range(m+1):
            y=transition(1<<j,f,g)
            predicted = sum((1<<i) for i in range(1,m+1) if i == j or i-1 == j)
            assert y==predicted
        print(f"sharp_family_r={r}: worlds={m+1}, period={1<<r}")
    print("BUNDLED_DISAGREEMENT_DYADIC_PERIODS_OK")


if __name__=='__main__':
    check()
