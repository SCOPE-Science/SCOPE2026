"""Exact exhaustive reverse-complement five-mer decycling census.

Python 3, standard library only. Enumerates all possible invariant sets of at most 12 vertices.
"""
from itertools import combinations
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache

K = 5
SIZE = 1 << K

def rc(v):
    return int(''.join('1' if c == '0' else '0' for c in f'{v:05b}'[::-1]), 2)

orbits = sorted({tuple(sorted((x, rc(x)))) for x in range(SIZE)})
assert len(orbits) == 16 and all(len(o) == 2 for o in orbits)
edges = [((2*x) & 31, ((2*x) & 31) | 1) for x in range(SIZE)]

def residual(s):
    survivor = set(range(SIZE)) - s
    incoming = {v: 0 for v in survivor}
    for x in survivor:
        for y in edges[x]:
            if y in survivor:
                incoming[y] += 1
    q = deque(v for v in survivor if incoming[v] == 0)
    longest = {v: 1 for v in survivor}
    processed = 0
    while q:
        x = q.popleft()
        processed += 1
        for y in edges[x]:
            if y in survivor:
                longest[y] = max(longest[y], longest[x] + 1)
                incoming[y] -= 1
                if incoming[y] == 0:
                    q.append(y)
    if processed < len(survivor):
        return None
    return max(longest.values(), default=0)

def expected_steps(s):
    @lru_cache(None)
    def steps(x):
        return Fraction(0) if x in s else 1 + (steps(edges[x][0]) + steps(edges[x][1])) / 2
    return sum((steps(x) for x in range(SIZE)), Fraction(0)) / SIZE

survivors = []
tested = Counter()
for n in range(7):
    for chosen in combinations(range(16), n):
        s = {w for i in chosen for w in orbits[i]}
        ell = residual(s)
        tested[(n, ell is not None)] += 1
        if ell is not None:
            assert n == 6
            survivors.append((chosen, ell, expected_steps(s)))

assert len(survivors) == 10
assert Counter(ell for _, ell, _ in survivors) == {6: 4, 8: 4, 10: 2}
assert Counter(e for _, _, e in survivors) == {
    Fraction(1189, 1024): 2, Fraction(1201, 1024): 2,
    Fraction(5125, 4096): 2, Fraction(5341, 4096): 2,
    Fraction(25253, 16384): 2,
}
assert all(0 in ix and 9 in ix for ix, _, _ in survivors)
assert [sum(tested[(n, success)] for success in (True, False)) for n in range(7)] == [1, 16, 120, 560, 1820, 4368, 8008]
print('VERIFY_OK_1')
print('tested',sum(tested.values()),'optimal',len(survivors))
for ix, ell, ex in survivors:
    print(','.join(map(str,ix)),ell,str(ex))
