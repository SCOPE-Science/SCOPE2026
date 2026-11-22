"""Exhaustive coefficient census at one normal form per alternating rank.

Only the Python standard library is required.  The finite loop and the
normal-form argument together certify the complete five-stratum count.
"""
from collections import Counter
from itertools import combinations

N = 5
PAIRS = tuple(combinations(range(N), 2))


def rank(rows):
    pivots = [0] * N
    out = 0
    for entry in rows:
        while entry:
            p = entry.bit_length() - 1
            if pivots[p]:
                entry ^= pivots[p]
            else:
                pivots[p] = entry
                out += 1
                break
    return out


def profile(blocks):
    s = [0] * N
    for i, j in blocks:
        s[i] ^= 1 << j
        s[j] ^= 1 << i
    radical = [v for v in range(1, 1 << N)
               if all(((row & v).bit_count() & 1) == 0 for row in s)]
    counts = Counter()
    for h in range(1 << 15):
        a = [((h >> i) & 1) << i for i in range(N)]
        for j, (i, k) in enumerate(PAIRS):
            b = (h >> (N + j)) & 1
            a[i] |= b << k
            a[k] |= (b ^ ((s[i] >> k) & 1)) << i
        if rank(a) != N:
            continue
        e = sum(not (sum((a[i] & v).bit_count() & 1
                         for i in range(N) if (v >> i) & 1) & 1)
                for v in radical)
        counts[e] += 1
    return counts


EXPECTED = [({15: 13888}, 1),
            ({3: 8960, 7: 1344}, 155),
            ({0: 4864, 1: 4800}, 868)]
blocks = [[], [(0, 1)], [(0, 1), (2, 3)]]
whole = Counter()
for edges, (wanted, multiplicity) in zip(blocks, EXPECTED):
    found = profile(edges)
    assert found == wanted, (edges, found)
    whole.update({e: count * multiplicity for e, count in found.items()})
    print('alternating rank', len(edges) * 2, 'per-form', sorted(found.items()),
          'forms', multiplicity)
assert dict(whole) == {0: 4221952, 1: 4166400, 3: 1388800,
                       7: 208320, 15: 13888}
assert sum(whole.values()) == 9999360
print('FROBENIUS_CUBIC_ECKARDT_CENSUS_PASS', sorted(whole.items()))
