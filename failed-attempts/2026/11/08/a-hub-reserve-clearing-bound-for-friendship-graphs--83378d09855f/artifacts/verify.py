"""Finite checks for a friendship-graph pebbling bound; no external packages."""
from functools import lru_cache
from itertools import combinations

def compositions(t, n):
    for cuts in combinations(range(t + n - 1), n - 1):
        before = -1
        v = []
        for p in cuts:
            v.append(p - before - 1)
            before = p
        v.append(t + n - 2 - before)
        yield tuple(v)

def graph(r):
    n = 2*r + 1
    return (tuple(range(1, n)),) + tuple(
        (0, i + 1 if i % 2 else i - 1) for i in range(1, n)
    )

def probe(r):
    n = 2*r + 1
    adj = graph(r)
    @lru_cache(None)
    def clearable(c):
        if sum(c) == 1:
            return True
        for i in range(n):
            if c[i] >= 2:
                for j in adj[i]:
                    d = list(c)
                    d[i] -= 2
                    d[j] += 1
                    if clearable(tuple(d)):
                        return True
        return False
    @lru_cache(None)
    def stackable(c):
        if sum(v > 0 for v in c) == 1:
            return True
        for i in range(n):
            if c[i] >= 2:
                for j in adj[i]:
                    d = list(c)
                    d[i] -= 2
                    d[j] += 1
                    if stackable(tuple(d)):
                        return True
        return False
    bad_t_minus_one = []
    for c in compositions(4*r - 1, n):
        if c[0] > 0:
            assert clearable(c), (r, 'hub positive', c)
        if not stackable(c):
            bad_t_minus_one.append(c)
    for c in compositions(4*r, n):
        assert clearable(c), (r, 'clearable', c)
    expected = [((0,) + tuple(
        2*r+1 if j == i else 0 if j == (i ^ 1) else 1
        for j in range(2*r)
    )) for i in range(2*r)]
    # The displayed obstructions have one large leaf, its mate zero, other leaves one.
    assert sorted(bad_t_minus_one) == sorted(expected), (r, bad_t_minus_one)
    print('EXHAUSTIVE_FRIENDSHIP_OK', r, 'upper', 4*r,
          'nonstackable_at_previous_weight', len(bad_t_minus_one),
          'cache', clearable.cache_info().currsize)

for r in (2, 3):
    probe(r)
print('VERIFY_OK')
