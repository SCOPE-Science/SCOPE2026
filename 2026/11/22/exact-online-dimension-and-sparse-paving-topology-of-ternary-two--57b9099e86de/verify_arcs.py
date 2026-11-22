"""Independent arc/incidence enumeration and adaptive witness verifier.

Run: python3 verify_arcs.py. This writes online_tree.json and checks every branch.
Only Python standard library is required.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

F = range(3)
points = set()
for x, y, z in itertools.product(F, repeat=3):
    if (x, y, z) == (0, 0, 0):
        continue
    first = next(t for t in (x, y, z) if t)
    scale = pow(first, -1, 3)
    points.add(tuple(scale*t % 3 for t in (x, y, z)))
points = sorted(points)
assert len(points) == 13
N = len(points)
lines = set()
for a, b, c in itertools.product(F, repeat=3):
    if (a, b, c) == (0, 0, 0):
        continue
    m = sum(1 << i for i, (x, y, z) in enumerate(points)
            if (a*x + b*y + c*z) % 3 == 0)
    lines.add(m)
assert len(lines) == 13
arcs = []
for inds in itertools.combinations(range(N), 4):
    m = sum(1 << i for i in inds)
    if all((m & line).bit_count() <= 2 for line in lines):
        arcs.append(m)
assert len(arcs) == 234
concepts = sorted({a | b for i, a in enumerate(arcs) for b in arcs[i+1:]})
assert len(concepts) == 4641
p = [3**i for i in range(N)]
total = 3**N
counts = [0] * total
for u in concepts:
    s = sum(p[i] * (2 if (u >> i) & 1 else 1) for i in range(N))
    counts[s] += 1
for i, step in enumerate(p):
    for s in range(total):
        if (s // step) % 3 == 0:
            counts[s] = counts[s+step] + counts[s+2*step]
assert counts[0] == len(concepts)
# Unrestricted choice of an as-yet-unqueried point, with adversary forcing both branches.
depths = bytearray(total)
for s in range(total-1, -1, -1):
    if counts[s] < 2:
        continue
    best = 0
    for i, step in enumerate(p):
        if (s // step) % 3 == 0 and counts[s+step] and counts[s+2*step]:
            best = max(best, 1 + min(depths[s+step], depths[s+2*step]))
    depths[s] = best
assert depths[0] == 8

# A complete, directly checkable 8-level tree; 0 = outside, 1 = inside.
def tree(s, remaining):
    if not remaining:
        assert counts[s] > 0
        return {"compatible_concepts": counts[s]}
    for i, step in enumerate(p):
        if (s // step) % 3 == 0 and counts[s+step] and counts[s+2*step] and \
             depths[s+step] >= remaining-1 and depths[s+2*step] >= remaining-1:
            return {"point_index": i,
                    "absent": tree(s+step, remaining-1),
                    "present": tree(s+2*step, remaining-1)}
    raise AssertionError('no tree branch')

witness = {"field": 3, "projective_points_lexicographic": points,
           "query_depth": 8, "branches": tree(0, 8)}

def check_tree(node, positive, negative, remaining):
    compatible = sum(1 for u in concepts if u & positive == positive and not (u & negative))
    assert compatible > 0
    if not remaining:
        assert node["compatible_concepts"] == compatible
        return 1
    i = node["point_index"]
    bit = 1 << i
    assert not (bit & (positive | negative))
    return (check_tree(node["absent"], positive, negative | bit, remaining-1)
            + check_tree(node["present"], positive | bit, negative, remaining-1))
assert check_tree(witness["branches"], 0, 0, 8) == 256
Path(__file__).with_name("online_tree.json").write_text(
    json.dumps(witness, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')

# Separate exhaustive ordinary shattering test, and the line-union obstruction.
f = Counter()
missing7 = set()
for s in range(1 << N):
    traces = {s & u for u in concepts}
    if len(traces) == (1 << s.bit_count()):
        f[s.bit_count()] += 1
    elif s.bit_count() == 7:
        missing7.add(s)
expected = [1,13,78,286,715,1287,1716,1638]+[0]*6
assert [f[k] for k in range(N+1)] == expected
assert missing7 == {a | b for a, b in itertools.combinations(lines, 2)}
assert max((a & b).bit_count() for a, b in itertools.combinations(missing7, 2)) <= 5
# Independent rank check for the top mod-two boundary (triangular incidence).
six = [m for m in range(1 << N) if m.bit_count() == 6]
index_six = {m: i for i, m in enumerate(six)}
seven = [m for m in range(1 << N) if m.bit_count() == 7 and m not in missing7]
pivots = {}
for m in seven:
    column = sum(1 << index_six[m ^ (1 << i)] for i in range(N) if (m >> i) & 1)
    while column:
        lead = column.bit_length() - 1
        if lead not in pivots:
            pivots[lead] = column
            break
        column ^= pivots[lead]
assert len(pivots) == 924 and len(seven) - len(pivots) == 714
assert -1 + 13 - 78 + 286 - 715 + 1287 - 1716 + 1638 == 714
print(json.dumps({"conics": len(arcs), "concepts": len(concepts),
                  "shattering_coefficients": expected[:8],
                  "circuit_hyperplanes": len(missing7),
                  "littlestone_dimension": depths[0],
                  "witness_leaves": 256, "boundary6_rank_mod2": 924,
                  "valid_partial_assignments": sum(c > 0 for c in counts)}, sort_keys=True))
