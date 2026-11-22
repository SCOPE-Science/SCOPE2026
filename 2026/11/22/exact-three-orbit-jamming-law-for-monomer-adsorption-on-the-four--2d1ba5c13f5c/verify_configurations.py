"""Independent exact check using accepted-set states and hypercube automorphisms."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations

DIM = 4
N = 1 << DIM
FULL = (1 << N) - 1
CLOSED = []
for vertex in range(N):
    neighbors = (1 << vertex)
    for other in range(N):
        if (vertex ^ other).bit_count() == 1:
            neighbors |= 1 << other
    CLOSED.append(neighbors)


def independent(subset):
    return all(not (subset & (1 << v)) or
               subset & CLOSED[v] == 1 << v for v in range(N))


def available(selected):
    rest = FULL
    for v in range(N):
        if selected & (1 << v):
            rest &= ~CLOSED[v]
    return rest


states = sorted((s for s in range(1 << N) if independent(s)), key=int.bit_count)
weights = defaultdict(Fraction)
weights[0] = Fraction(1)
for chosen in states:
    vacant = available(chosen)
    if not vacant:
        continue
    divisor = vacant.bit_count()
    for v in range(N):
        if vacant & (1 << v):
            weights[chosen | (1 << v)] += weights[chosen] / divisor

terminal = {s: weights[s] for s in states if not available(s)}
counts = Counter(s.bit_count() for s in terminal)
assert len(states) == 743
assert counts == {4: 24, 5: 16, 8: 2}, counts
assert sum(terminal.values()) == 1

# Independently enumerate the entire signed-coordinate permutation group.
seen = set()
orbits = []
for seed in terminal:
    if seed in seen:
        continue
    orbit = set()
    for perm in permutations(range(DIM)):
        for offset in range(N):
            mapped = 0
            for v in range(N):
                if seed & (1 << v):
                    target = offset
                    for j in range(DIM):
                        target ^= ((v >> j) & 1) << perm[j]
                    mapped |= 1 << target
            orbit.add(mapped)
    assert orbit <= terminal.keys()
    seen.update(orbit)
    same = {terminal[s] for s in orbit}
    assert len(same) == 1
    orbits.append((seed.bit_count(), len(orbit), same.pop()))
assert sorted(orbits) == sorted([(4, 24, Fraction(1, 144)),
                                (5, 16, Fraction(4, 165)),
                                (8, 2, Fraction(49, 220))]), orbits
assert sum(k * len_orbit * p for k, len_orbit, p in orbits) == Fraction(1018, 165)
assert sum(len_orbit * p for k, len_orbit, p in orbits) == 1
print('PASS accepted-state DP, maximal-set enumeration and 384 automorphisms')
print('PASS orbit list', sorted(orbits))
