"""Finite checks for the heterogeneous action-copy realization theorem."""
from itertools import product, combinations
from math import prod


def color_array(m, r):
    assert len(m) >= 2 and all(t > 0 for t in m)
    assert r >= 1
    k = len(m)
    order = sorted(range(k), key=lambda i: (m[i], i))
    top = order[-1]
    others = order[:-1]
    M = prod(m[i] for i in others)
    assert r <= M
    def color(x):
        digits = [(x[i] + x[top]) % m[i] for i in others]
        idx = 0
        for i, d in zip(others, digits):
            idx = idx * m[i] + d
        return idx % r
    return color


def verify_slices(m, r):
    f = color_array(m, r)
    for i in range(len(m)):
        for a in range(m[i]):
            seen = {f(x) for x in product(*(range(t) for t in m)) if x[i] == a}
            assert seen == set(range(r)), (m, r, i, a, seen)


def build_outcome(m, families, r):
    f = color_array(m, r)
    for C in product(*families):
        assert set.intersection(*(set(z) for z in C))
    def step(actions):
        S = set.intersection(*(set(s) for s, a in actions))
        z = f(tuple(a for s, a in actions))
        return z if z in S else min(S)
    for i, fam in enumerate(families):
        for S in fam:
            for a in range(m[i]):
                seen = set()
                alternatives = [[(T, b) for T in fam_j for b in range(m[j])]
                                for j, fam_j in enumerate(families)]
                alternatives[i] = [(S, a)]
                for profile in product(*alternatives):
                    seen.add(step(profile))
                assert seen == set(S), (m, families, i, S, a, seen)


def verify():
    slice_checks = 0
    for k in (2, 3, 4):
        for m in product(range(1, 5), repeat=k):
            ceiling = min(prod(m[j] for j in range(k) if j != i) for i in range(k))
            for r in range(1, min(ceiling, 6) + 1):
                verify_slices(m, r)
                slice_checks += 1
    outcome_checks = 0
    for r in (1, 2, 3):
        O = frozenset(range(r))
        subset_pool = [frozenset(s) for t in range(1, r + 1) for s in combinations(range(r), t)]
        family_pool = []
        for mask in range(1, 1 << len(subset_pool)):
            fam = tuple(subset_pool[i] for i in range(len(subset_pool)) if mask >> i & 1)
            if set.union(*(set(z) for z in fam)) == set(O):
                family_pool.append(fam)
        # Every two-agent frame on one, two, or three outcomes with up to 3 neighborhoods per agent.
        for f1 in family_pool:
            for f2 in family_pool:
                if len(f1) > 3 or len(f2) > 3:
                    continue
                if not all(s1 & s2 for s1 in f1 for s2 in f2):
                    continue
                build_outcome((r, r), (f1, f2), r)
                outcome_checks += 1
    for m, r in [((2, 3, 3), 5), ((1, 2, 3, 3), 6), ((2, 2, 3, 3), 7), ((3, 4, 4), 10)]:
        verify_slices(m, r)
        O = frozenset(range(r))
        families = tuple((O, frozenset(range(r-1))) for _ in m)
        build_outcome(m, families, r)
        outcome_checks += 1
    for m, r in [((2, 2, 4), 5), ((1, 1, 5), 2), ((3, 3), 4)]:
        assert min(prod(m[j] for j in range(len(m)) if j != i) for i in range(len(m))) < r
    print('VERIFY_OK', 'slice_cases', slice_checks, 'frame_cases', outcome_checks)


if __name__ == '__main__':
    verify()
