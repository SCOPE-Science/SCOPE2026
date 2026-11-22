"""Finite checks for the one-point-extension rank of partial-transversal equivalence structures.

Run with Python 3 (no external packages): python checker.py
"""
from functools import lru_cache
from math import isqrt
from random import Random


def component_profiles(n):
    """One copy of each unlabelled host of order n; (ordinary_count, root_flag) components."""
    arr = []

    def rec(low, left):
        if left == 0:
            yield tuple(arr)
        else:
            for k in range(1, left + 1):
                for root in (0, 1):
                    comp = (k - root, root)
                    if comp >= low:
                        arr.append(comp)
                        yield from rec(comp, left - k)
                        arr.pop()
    yield from rec((-1, -1), n)


def criterion(components, t):
    if t == 0:
        return True
    ordinary_roots = sorted((u for u, p in components if p), reverse=True)
    free_rootless = sum(u for u, p in components if not p)
    return (len(ordinary_roots) >= t
            and all(ordinary_roots[j] >= t - j for j in range(t - 1))
            and ordinary_roots[t - 1] + free_rootless >= 1)


def direct_ranks(components):
    """Game recursion on individual marked subsets, not component aggregates."""
    cls, col = [], []
    for j, (ordinary, root) in enumerate(components):
        cls.extend([j] * (ordinary + root))
        col.extend([0] * ordinary + [1] * root)
    n = len(cls)
    @lru_cache(None)
    def rank(mask):
        active = {cls[i] for i in range(n) if mask & (1 << i)}
        challenges = [(None, 0), (None, 1)]
        for c in active:
            challenges.append((c, 0))
            if not any((mask & (1 << i)) and cls[i] == c and col[i]
                       for i in range(n)):
                challenges.append((c, 1))
        worst = n + 2
        for c, color in challenges:
            eligible = [i for i in range(n) if not mask & (1 << i)
                        and col[i] == color
                        and ((cls[i] not in active) if c is None else (cls[i] == c))]
            if not eligible:
                return 0
            best = max(rank(mask | (1 << i)) for i in eligible)
            worst = min(worst, best)
        return worst + 1
    root = rank(0)
    return root, rank, cls, col


def profile_rank(components):
    """Independent component-multiplicity minimax implementation."""
    @lru_cache(None)
    def rec(states):
        active = [j for j, (x, y) in enumerate(states) if x + y]
        challenges = [(None, 0), (None, 1)]
        for j in active:
            challenges.append((j, 0))
            if states[j][1] == 0:
                challenges.append((j, 1))
        adversary = []
        for j, color in challenges:
            next_ranks = []
            for i, (u, root) in enumerate(components):
                if (j is None) != (i not in active):
                    continue
                if j is not None and j != i:
                    continue
                nordinary, nroot = states[i]
                if color == 0 and nordinary < u:
                    nxt = list(states)
                    nxt[i] = (nordinary + 1, nroot)
                    next_ranks.append(rec(tuple(nxt)))
                elif color == 1 and root and not nroot:
                    nxt = list(states)
                    nxt[i] = (nordinary, 1)
                    next_ranks.append(rec(tuple(nxt)))
            if not next_ranks:
                return 0
            adversary.append(max(next_ranks))
        return 1 + min(adversary)
    return rec(tuple((0, 0) for _ in components))


def relative_criterion(components, cls, col, mask, t):
    if t == 0:
        return True
    active = {cls[i] for i in range(len(cls)) if mask & (1 << i)}
    for j in active:
        if components[j][1] == 0:
            return False
        unmarked_ordinary = sum(1 for i, c in enumerate(cls)
                                if c == j and not col[i] and not mask & (1 << i))
        if unmarked_ordinary < t:
            return False
    leftover = tuple(components[i] for i in range(len(components)) if i not in active)
    return criterion(leftover, t)


def main():
    checked_hosts = 0
    checked_rel = 0
    checked_profile = 0
    for n in range(0, 11):
        witness = []
        for comp in component_profiles(n):
            r, R, cls, col = direct_ranks(comp)
            q = max((t for t in range(n + 1) if criterion(comp, t)), default=0)
            assert r == q, (comp, r, q)
            assert r == profile_rank(comp), ('profile', comp, r)
            checked_profile += 1
            for mask in range(1 << n):
                for t in range(r + 2):
                    # Universal rank at F cannot exceed unmarked host size.
                    got = R(mask) >= t
                    want = relative_criterion(comp, cls, col, mask, t)
                    assert got == want, (comp, mask, t, got, want)
                    checked_rel += 1
            if r == max((t for t in range(n + 1) if t * (t + 3) // 2 <= n), default=0):
                witness.append(comp)
            checked_hosts += 1
        print('size', n, 'hosts', checked_hosts, 'relative tests', checked_rel)
    # Component-level recursion extends to larger sizes without subset blowup.
    rng = Random(92374)
    for _ in range(300):
        k = rng.randint(1, 8)
        parts = tuple((rng.randint(0, 7), rng.randint(0, 1)) for j in range(k))
        if all(u + p for u, p in parts) and sum(u + p for u, p in parts) <= 26:
            r = profile_rank(parts)
            q = max((t for t in range(sum(u + p for u, p in parts) + 1)
                     if criterion(parts, t)), default=0)
            assert r == q, (parts, r, q)
            checked_profile += 1
    for t in range(1, 7):
        size = t * (t + 3) // 2
        base = tuple((u, 1) for u in range(2, t + 1))
        alpha = base + ((1, 1),)
        beta = base + ((0, 1), (1, 0))
        assert sum(u + p for u, p in alpha) == size
        assert sum(u + p for u, p in beta) == size
        assert criterion(alpha, t) and criterion(beta, t)
        assert not criterion(alpha, t + 1) and not criterion(beta, t + 1)
        assert all(not criterion(parts, t) for parts in component_profiles(size - 1))
    print('ALL_CHECKS_OK hosts=', checked_hosts, 'relative_tests=', checked_rel,
          'profile_checks=', checked_profile, 'thresholds=1..6')


if __name__ == '__main__':
    main()
