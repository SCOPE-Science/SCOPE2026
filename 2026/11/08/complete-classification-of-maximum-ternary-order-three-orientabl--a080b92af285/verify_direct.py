"""Separate exhaustive length-nine orientable-cycle and symmetry census.

All computations are over the labeled alphabet 0,1,2; only rotations
are identified before the separate permutation/reversal quotient.
"""
from itertools import product, permutations

ALPHABET = '012'
N = 9

def rotations(s):
    return {s[i:] + s[:i] for i in range(len(s))}

def windows(s):
    return [''.join(s[(i+j) % N] for j in range(3)) for i in range(N)]

def admissible(s):
    observed = windows(s)
    if any(t == t[::-1] for t in observed):
        return False
    return len({min(t, t[::-1]) for t in observed}) == N

cycles = set()
for letters in product(ALPHABET, repeat=N):
    s = ''.join(letters)
    if admissible(s):
        cycles.add(min(rotations(s)))

expected = {
    '001120122', '001122012', '001201122', '001220112',
    '002102211', '002110221', '002210211', '002211021',
}
assert cycles == expected, (len(cycles), sorted(cycles))
assert len(cycles) == 8
assert all(len(rotations(s)) == N for s in cycles)

def symmetry_images(s):
    for p in permutations(ALPHABET):
        tr = str.maketrans(ALPHABET, ''.join(p))
        t = s.translate(tr)
        yield min(rotations(t))
        yield min(rotations(t[::-1]))

remaining = set(cycles)
orbits = {}
while remaining:
    representative = min(remaining)
    orbit = set(symmetry_images(representative))
    assert orbit <= cycles, (representative, orbit-cycles)
    orbits[representative] = len(orbit)
    remaining -= orbit
assert orbits == {'001120122': 6, '001220112': 2}, orbits
print('DIRECT_VERIFY_OK', len(cycles), sorted(orbits.items()))
