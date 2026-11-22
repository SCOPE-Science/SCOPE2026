#!/usr/bin/env python3
"""Independent direct ternary-word and bitmask census for [1,14] Schur triples."""
import csv
from collections import Counter

n = 14
triples = [(a, b, a + b) for a in range(1, n + 1)
           for b in range(a, n + 1) if a + b <= n]
assert len(triples) == 49
needed = [sum(1 << (v - 1) for v in set(t)) for t in triples]
counts = Counter()
zero = 0
for word in range(3 ** (n - 1)):
    masks = [1, 0, 0]  # normalize the color of integer 1 to zero
    number = word
    for vertex in range(2, n + 1):
        hue = number % 3
        number //= 3
        masks[hue] |= 1 << (vertex - 1)
    bad = []
    for i, triple_mask in enumerate(needed):
        if any(mask & triple_mask == triple_mask for mask in masks):
            bad.append(i)
            if len(bad) == 2:
                break
    if len(bad) == 0:
        zero += 1
    elif len(bad) == 1:
        counts[bad[0]] += 1

with open("critical_triples.csv", encoding="utf-8", newline="") as handle:
    table = list(csv.DictReader(handle))
assert len(table) == 49
for i, (row, (a,b,c)) in enumerate(zip(table, triples)):
    assert (int(row["x"]),int(row["y"]),int(row["z"])) == (a,b,c)
    assert int(row["normalized_colorings"]) == counts[i]
    assert int(row["named_colorings"]) == 3 * counts[i]
    assert int(row["critical"]) == (counts[i] > 0)
assert zero == 0
assert sum(counts.values()) == 1350
assert sum(value > 0 for value in counts.values()) == 29
assert sum(int(row["critical"]) for row in table) == 29
assert all(int(row["critical"]) == 0 for row in table if int(row["z"]) == 14)
print("PASS Python direct: normalized zero=0, one=1350, named one=4050, "
      "critical=29/49, no sum-14 equation critical")
