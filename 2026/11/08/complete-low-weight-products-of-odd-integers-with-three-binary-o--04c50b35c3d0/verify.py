"""Exact exhaustive classification of odd 3-bit by 3-bit products of weight <=3."""
from itertools import combinations

# The two published global bounds for product weights 2 and 3
# are 2^14 and 2^23, respectively (Kaneko--Stoll, Theorems 2.1--2.2).
B2, B3 = 1 << 14, 1 << 23
# Every factor of a qualifying product is odd, has weight three, and is >=7.
# Every such factor is <B3, hence its two nonzero higher bit exponents
# belong to {1,...,22}; generating all of them is an overcount but exhaustive.
factors = sorted(1 + (1 << i) + (1 << j)
                 for i, j in combinations(range(1, 23), 2))
assert len(factors) == 231
observed = {2: [], 3: []}
admissible = 0
for idx, a in enumerate(factors):
    for b in factors[idx:]:
        z = a * b
        if z >= B3:
            break
        admissible += 1
        w = z.bit_count()
        if w in observed and (w == 3 or z < B2):
            observed[w].append((a, b, z))
expected = {
    2: [(25, 41, 1025)],
    3: [(7, 7, 49), (7, 19, 133), (7, 37, 259),
        (11, 35, 385), (13, 21, 273), (21, 49, 1029)]
}
for key in observed:
    observed[key].sort()
    assert observed[key] == expected[key], (key, observed[key])
assert admissible == 3672, admissible
for weight, rows in observed.items():
    for a, b, z in rows:
        assert a % 2 == b % 2 == 1 and a <= b
        assert a.bit_count() == b.bit_count() == 3 and z.bit_count() == weight
print('source-bound checks: k=2 -> product < 2^14; k=3 -> product < 2^23')
print(f'factor parametrizations: {len(factors)}; admissible unordered pairs: {admissible}')
for k in (2, 3):
    print(f'weight={k}: count={len(observed[k])}; solutions={observed[k]}')
print('VERIFY_OK')
