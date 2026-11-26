"""Exact terminal law for uniform random sequential dimer adsorption on GP(10,2).

Standard-library-only proof checker: two finite, exact rational recursions.
The recurrence itself is justified by the exchangeable order of still
available edge arrival times. This program contains all graph data.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

N = 20
# Outer decagon: 0,...,9; inner vertices: 10,...,19.
# The latter form two 5-cycles, via a two-step jump.
def graph_edges():
    raw = []
    for j in range(10):
        raw.append((j, (j + 1) % 10))
        raw.append((10 + j, 10 + (j + 2) % 10))
        raw.append((j, 10 + j))
    return tuple(sorted({tuple(sorted(edge)) for edge in raw}))

E = graph_edges()
B = tuple((1 << u) | (1 << v) for (u, v) in E)
assert len(E) == 30 and N == 20
assert sorted(sum(v in e for e in E) for v in range(N)) == [3] * N

# Method A: recursive continuation distribution for every reachable mask.
@lru_cache(None)
def remaining(mask):
    available = [b for b in B if not (b & mask)]
    if not available:
        return (Fraction(1),)
    accum = [Fraction(0)] * 11
    for edge in available:
        for k, v in enumerate(remaining(mask | edge)):
            if k < 10: accum[k + 1] += v
    return tuple(x / len(available) for x in accum)

P = remaining(0)
P = tuple(P[k] if k < len(P) else Fraction(0) for k in range(11))

# Method B: forward transfer of probability mass through disjoint-pair masks.
# No use of the recursive cache or its outputs.
mass = {0: Fraction(1)}
terminal = [Fraction(0)] * 11
terminal_counts = [0] * 11
for count in range(11):
    following = {}
    for state, weight in mass.items():
        legal = [b for b in B if state & b == 0]
        if not legal:
            terminal[count] += weight
            terminal_counts[count] += 1
            continue
        for b in legal:
            new_state = state | b
            following[new_state] = following.get(new_state, Fraction(0)) + weight / len(legal)
    mass = following
assert not mass
assert tuple(terminal) == P
assert sum(P) == 1
assert all(v == 0 for v in P[:6])

# Reconstruct the exact target coefficients without decimal arithmetic.
EXPECTED = {
    6: Fraction(1, 3125),
    7: Fraction(91294494167, 2756754000000),
    8: Fraction(1796566904214749, 4862914056000000),
    9: Fraction(2544405065946811, 4862914056000000),
    10: Fraction(123231298227, 1667666000000),
}
assert {k: p for k, p in enumerate(P) if p} == EXPECTED

# The unoccupied vertices in a jammed matching form an independent set.
# Check the precise independence number and count of largest independent sets.
neighbor = [0] * 20
for u, v in E:
    neighbor[u] |= 1 << v
    neighbor[v] |= 1 << u

def is_independent(seq):
    mask = sum(1 << v for v in seq)
    return all(neighbor[v] & mask == 0 for v in seq)

max_independent_sets = [x for x in combinations(range(20), 8) if is_independent(x)]
assert len(max_independent_sets) == 5
assert not any(is_independent(x) for x in combinations(range(20), 9))
for independent_set in max_independent_sets:
    leftover = set(independent_set)
    core = [v for v in range(N) if v not in leftover]
    core_edges = [(u,v) for u,v in E if u in core and v in core]
    assert len(core_edges) == 6
    assert all(sum(v in e for e in core_edges) == 1 for v in core)
    # Each core edge has four incident edges crossing to the independent set.
    assert all(sum(bool((u in e) or (v in e)) for e in E) == 5
               for u,v in core_edges)
assert P[6] == Fraction(len(max_independent_sets), 5**6)
assert all(terminal_counts[k] > 0 for k in range(6, 11))

mean = sum(k * p for k, p in enumerate(P))
assert mean == Fraction(42002246692500247, 4862914056000000)
variance = sum((k - mean) ** 2 * p for k, p in enumerate(P))

if __name__ == '__main__':
    print('model: GP(10,2); vertices:', N, '; edges:', len(E))
    print('states in backward transfer:', remaining.cache_info().currsize)
    print('terminal occupied-mask counts by number of dimers:', [(k, c) for k, c in enumerate(terminal_counts) if c])
    print('max independent sets of size 8:', len(max_independent_sets))
    for k, p in enumerate(P):
        if p: print(f'P(K={k}) = {p} = {float(p):.12f}')
    print('E[K] =', mean, '=', float(mean))
    print('Var[K] =', variance, '=', float(variance))
    print('All exact-rational checks passed.')
