"""Independent full-state check of a spin-one model on the cuboctahedron.

Run with Python 3 (standard library only).  Each of the 3**12 states is
explicitly visited; only sector compression occurs after enumeration.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

cube_edges = tuple((v, v ^ (1 << k)) for v in range(8)
                   for k in range(3) if v < (v ^ (1 << k)))
assert len(cube_edges) == 12
adjacency = tuple((i, j) for i in range(12) for j in range(i + 1, 12)
                  if len(set(cube_edges[i] + cube_edges[j])) == 3)
assert len(adjacency) == 24

sectors = Counter()
for spins in product((-1, 0, 1), repeat=12):
    interaction = sum(spins[i] * spins[j] for i, j in adjacency)
    occupation = sum(s * s for s in spins)
    magnetization = sum(spins)
    sectors[interaction, occupation, magnetization] += 1
assert sum(sectors.values()) == 3**12

samples = [
    ("vacuum", Fraction(2), Fraction(1, 4), 1),
    ("one_positive_per_triangle", Fraction(3, 2), Fraction(5, 2), 9),
    ("three_distinct", Fraction(1, 2), Fraction(1, 4), 24),
    ("two_positive_one_empty", Fraction(1), Fraction(4), 9),
    ("two_positive_one_negative", Fraction(-1), Fraction(1), 9),
    ("fully_polarized", Fraction(-1), Fraction(8), 1),
    ("even_cycle_coexistence", Fraction(1), Fraction(0), 69),
    ("matching_coexistence", Fraction(-1), Fraction(4), 108),
]
for title, delta, field, multiplicity in samples:
    energies = {c + delta*q - field*m: 0 for c, q, m in sectors}
    minimum = min(energies)
    count = sum(cnt for (c,q,m),cnt in sectors.items()
                if c + delta*q - field*m == minimum)
    tri_options = []
    for a,b,c in product((-1,0,1),repeat=3):
        tri_options.append(a*b + a*c + b*c
                           + delta*(a*a+b*b+c*c)/2 - field*(a+b+c)/2)
    local_minimum = min(tri_options)
    assert minimum == 8*local_minimum, (title, minimum, local_minimum)
    assert count == multiplicity, (title, count, multiplicity)
    print(title, "energy/J", minimum, "degeneracy", count)
print("EXHAUSTIVE_CUBE_OK", sum(sectors.values()), "states", len(sectors), "sectors")
