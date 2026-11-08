"""Exact standalone finite check of the six-point Walsh magnitude classification.

Run: python3 CHECK.py.  Uses only the Python standard library.
"""
from collections import Counter
from itertools import combinations
from math import comb


def rank(vectors):
    pivots = {}
    for value in vectors:
        x = value
        while x:
            bit = x.bit_length() - 1
            if bit in pivots:
                x ^= pivots[bit]
            else:
                pivots[bit] = x
                break
    return len(pivots)


def kind(points):
    r = rank([p ^ points[0] for p in points[1:]])
    if r == 3:
        return "rank3"
    if r == 5:
        return "rank5"
    assert r == 4
    four_dep = any(a ^ b ^ c ^ d == 0 for a, b, c, d in combinations(points, 4))
    return "rank4_circuit4" if four_dep else "rank4_circuit6"


def spectrum(points, d):
    return Counter(abs(sum(1 if (u & x).bit_count() % 2 == 0 else -1
                           for x in points)) for u in range(1 << d))


LOCAL = {
    "rank3": (3, {0: 4, 2: 3, 6: 1}),
    "rank4_circuit4": (4, {0: 6, 2: 7, 4: 2, 6: 1}),
    "rank4_circuit6": (4, {2: 15, 6: 1}),
    "rank5": (5, {0: 10, 2: 15, 4: 6, 6: 1}),
}


for dim, expected in [(3, {"rank3": comb(8, 6)}),
                      (4, {"rank3": 840, "rank4_circuit4": 6720,
                           "rank4_circuit6": 448})]:
    tally = Counter()
    for E in combinations(range(1 << dim), 6):
        label = kind(E)
        tally[label] += 1
        r, local = LOCAL[label]
        predicted = Counter({a: b * 2 ** (dim - r) for a, b in local.items()})
        assert spectrum(E, dim) == predicted, (dim, E, label)
    assert tally == expected, (dim, tally)
    print("DIMENSION", dim, "sets", sum(tally.values()), "types", dict(tally))

# Four canonical types in the first ambient dimension permitting all types.
canonical = {
    "rank3": [0, 1, 2, 3, 4, 5],
    "rank4_circuit4": [0, 1, 2, 4, 8, 1 ^ 2],
    "rank4_circuit6": [0, 1, 2, 4, 8, 1 ^ 2 ^ 4 ^ 8],
    "rank5": [0, 1, 2, 4, 8, 16],
}
for label, E in canonical.items():
    assert kind(E) == label, (label, E)
    r, local = LOCAL[label]
    assert spectrum(E, 5) == Counter({a: b * 2 ** (5 - r) for a, b in local.items()})
    print("CANONICAL", label, "nonzero", 2 ** (5 - r) * sum(v for k, v in local.items() if k != 0))
print("CHECK_OK exact_subsets_3d=28 exact_subsets_4d=8008 canonical_5d=4")
