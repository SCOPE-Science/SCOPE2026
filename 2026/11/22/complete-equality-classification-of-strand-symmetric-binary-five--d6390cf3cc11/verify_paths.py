"""Independent exhaustive DFS verifier of reverse-complement invariant five-mer sets.

Uses a recursive three-color directed cycle test; checks all 65536 orbit masks.
"""
from collections import Counter
from fractions import Fraction

N = 32

def complement_reversal(v):
    ans = 0
    for i in range(5):
        ans |= (1 - ((v >> i) & 1)) << (4 - i)
    return ans

orbits = sorted({tuple(sorted((v, complement_reversal(v)))) for v in range(N)})
assert len(orbits) == 16
arcs = {v: (2 * v % 32, (2 * v + 1) % 32) for v in range(N)}

def classify(removed):
    state = [0] * 32
    depth = [-1] * 32
    def dfs(x):
        if x in removed:
            return 0
        if state[x] == 1:
            raise ValueError('cycle')
        if state[x] == 2:
            return depth[x]
        state[x] = 1
        depth[x] = 1 + max(dfs(v) for v in arcs[x])
        state[x] = 2
        return depth[x]
    try:
        return max(dfs(v) for v in range(N))
    except ValueError:
        return None

valid = {}
for mask in range(1<<16):
    count = mask.bit_count()
    if count > 6:
        continue
    removed = {v for i, orb in enumerate(orbits) if (mask >> i)&1 for v in orb}
    length = classify(removed)
    if length is not None:
        valid[mask] = length

assert len(valid) == 10
assert Counter(mask.bit_count() for mask in valid) == {6:10}
assert Counter(valid.values()) == {6:4, 8:4, 10:2}

# Complement swaps the reverse-complement orbit pairs, check five distinct orbits.
def comp(x):
    return x ^ 31

def canonical(mask):
    words = frozenset(v for i, orb in enumerate(orbits) if (mask >> i)&1 for v in orb)
    other = frozenset(comp(v) for v in words)
    assert other in [frozenset(v for i, orb in enumerate(orbits) if (mm >> i)&1 for v in orb) for mm in valid]
    return min(tuple(sorted(words)), tuple(sorted(other)))
assert len({canonical(mask) for mask in valid}) == 5
assert {tuple(i for i in range(16) if mask & (1<<i)) for mask in valid} == {
  (0,1,6,9,11,13), (0,1,8,9,10,11), (0,2,3,6,9,13),
  (0,2,3,8,9,10), (0,3,4,5,6,9), (0,4,9,10,14,15),
  (0,6,7,9,13,15), (0,6,9,11,12,13), (0,7,8,9,10,15),
  (0,8,9,10,11,12)
}
# Independent rational hitting-time evaluation by inverse topological recursion.
def mean_hits(mask):
    from functools import lru_cache
    removed = {v for i, orb in enumerate(orbits) if (mask >> i) & 1 for v in orb}
    @lru_cache(None)
    def e(v):
        if v in removed:
            return Fraction(0)
        left, right = arcs[v]
        return Fraction(1) + (e(left) + e(right)) / 2
    return sum((e(v) for v in range(N)), Fraction(0)) / N

assert Counter(mean_hits(mask) for mask in valid) == {
    Fraction(1189,1024):2, Fraction(1201,1024):2,
    Fraction(5125,4096):2, Fraction(5341,4096):2,
    Fraction(25253,16384):2
}

print('VERIFY_OK_2')
print('candidates_leq_six',sum(1 for m in range(1<<16) if m.bit_count()<=6))
print('min_orbit_count',min(mask.bit_count() for mask in valid))
print('number_optima',len(valid),'complement_classes',5)
