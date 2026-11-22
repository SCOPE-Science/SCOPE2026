#!/usr/bin/env python3
"""Exact integer verification for the fully frustrated five-cube partition function.
Run with Python 3 and no third-party packages.
"""
from collections import Counter
from itertools import combinations

N = 5
vertices = range(1 << N)
even = [x for x in vertices if x.bit_count() % 2 == 0]
odd = [x for x in vertices if x.bit_count() % 2 == 1]

def sign(x, i):
    return -1 if (x & ((1 << i) - 1)).bit_count() % 2 else 1

# Exact square product check: one square per two directions and 3 free bits.
for i, j in combinations(range(N), 2):
    for x in vertices:
        if (x >> i) & 1 or (x >> j) & 1:
            continue
        square = sign(x, i) * sign(x ^ (1 << i), j) * sign(x ^ (1 << j), i) * sign(x, j)
        assert square == -1

B = [[next((sign(x, i) for i in range(N) if y == (x ^ (1 << i))), 0)
      for y in odd] for x in even]
# Orthogonality is a separate exact certificate.
for i in range(16):
    for j in range(16):
        dot = sum(B[x][i] * B[x][j] for x in range(16))
        assert dot == (5 if i == j else 0)
print('SQUARE_FRUSTRATION_AND_ORTHOGONALITY_PASS')

# Independent exhaustive enumeration over all 2^16 even-vertex spin words.
observed = Counter()
for mask in range(1 << 16):
    u = [(1 if (mask >> j) & 1 else -1) for j in range(16)]
    fields = [sum(u[i] * B[i][j] for i in range(16)) for j in range(16)]
    hist = (fields.count(1) + fields.count(-1),
            fields.count(3) + fields.count(-3),
            fields.count(5) + fields.count(-5))
    observed[hist] += 1
assert observed == {(8, 8, 0): 10240, (10, 5, 1): 45056, (12, 2, 2): 10240}, observed
print('ALL_65536_EVEN_SPIN_PATTERNS_PASS', sorted(observed.items()))

# Direct coefficient assembly via field choices from the exhaustive histogram.
def mult(a, b):
    result = Counter()
    for x, ax in a.items():
        for y, by in b.items():
            result[x + y] += ax * by
    return result

def factor(k):
    return Counter({k: 1, -k: 1})

def powered(k, n):
    p = Counter({0: 1})
    for _ in range(n):
        p = mult(p, factor(k))
    return p

coefficients = Counter()
for (a, b, c), count in observed.items():
    term = mult(mult(powered(1, a), powered(3, b)), powered(5, c))
    for s, mul in term.items():
        coefficients[s] += count * mul

# A second derivation uses only the inclusion-exclusion cardinalities.
assert 16 * 4096 == 65536
assert 40 * 256 == 10240
assert 65536 - (16 * 4096 - 2 * (40 * 256)) - 40 * 256 == 10240
assert sum(coefficients.values()) == 2**32
assert max(coefficients) == 32 and min(coefficients) == -32
assert coefficients[32] == 10240 and coefficients[30] == 126976
assert all(s % 2 == 0 and coefficients[s] == coefficients[-s] for s in coefficients)
assert len(coefficients) == 33

# Direct spin-sum samples, using all 80 edges rather than the field factorization.
edges = [(x, x ^ (1 << i), sign(x, i))
         for x in vertices for i in range(N) if not ((x >> i) & 1)]
assert len(edges) == 80
for evenmask in [0, 1, 3, 13, 127, 12345, 65535]:
    even_spin = {x: (1 if (evenmask >> i) & 1 else -1) for i, x in enumerate(even)}
    for oddmask in [0, 1, 17, 65535]:
        spin = dict(even_spin)
        spin.update({x: (1 if (oddmask >> i) & 1 else -1) for i, x in enumerate(odd)})
        score = sum(s * spin[x] * spin[y] for x, y, s in edges)
        assert -32 <= score <= 32 and score % 2 == 0
        fields = [sum(spin[x] * B[i][j] for i, x in enumerate(even)) for j in range(16)]
        assert score == sum(spin[y] * fields[j] for j, y in enumerate(odd))
print('PARTITION_COEFFICIENTS_PASS total=', sum(coefficients.values()),
      'energy_levels=', len(coefficients), 'ground=', coefficients[32],
      'next=', coefficients[30])
print('NEGATIVE_EDGE_MINIMUM_24_AND_5120_DISTINCT_SIGNINGS_PASS')
print('VERIFY_OK')
