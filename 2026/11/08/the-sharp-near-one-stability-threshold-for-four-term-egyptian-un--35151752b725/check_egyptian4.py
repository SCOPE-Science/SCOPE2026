#!/usr/bin/env python3
"""Exact finite arithmetic for the four-unit-fraction boundary theorem."""
from fractions import Fraction as F
from collections import defaultdict

B = F(41, 42)
SECOND = F(599, 600)
CRITICAL = F(629, 630)
triples = []
node_counts = [0] * 4

def visit(prefix, value):
    j = len(prefix)
    node_counts[j] += 1
    if j == 3:
        x, y, z = prefix
        # Smallest fourth denominator giving a strict sum below one.
        fourth = max(z, (1 - value).denominator // (1 - value).numerator + 1)
        candidate = value + F(1, fourth)
        triples.append((prefix, fourth, candidate))
        return
    first = prefix[-1] if prefix else 2
    # Any completion above B requires (4-j)/next > B-value.
    bound = F(4-j, 1) / (B - value)
    for denominator in range(first, bound.numerator // bound.denominator + 1):
        new_value = value + F(1, denominator)
        if new_value >= 1:
            continue
        if new_value + F(3-j, denominator) <= B:
            continue
        visit(prefix + (denominator,), new_value)

visit((), F(0))
assert node_counts == [1, 3, 7, 21], node_counts
assert len(triples) == 21
special = [(x, m, s) for x, m, s in triples if x == (2, 3, 7)]
assert special == [((2, 3, 7), 43, F(1805, 1806))]
others = [(x, m, s) for x, m, s in triples if x != (2, 3, 7)]
assert max(v for x, m, v in others) == SECOND
assert [(x, m) for x, m, v in others if v == SECOND] == [((2, 3, 8), 25)]
by_first_two = defaultdict(list)
for x, m, v in others:
    by_first_two[x[:2]].append((x[2], m, v))
expected = {
    (2, 3): (tuple(range(8, 14)), F(599, 600)),
    (2, 4): (tuple(range(5, 9)), F(419, 420)),
    (2, 5): (tuple(range(5, 8)), F(119, 120)),
    (2, 6): ((6,), F(41, 42)),
    (3, 3): (tuple(range(4, 7)), F(155, 156)),
    (3, 4): ((4, 5), F(59, 60)),
    (4, 4): ((4,), F(19, 20)),
}
assert set(by_first_two) == set(expected)
for k, data in by_first_two.items():
    zrange, maximum = expected[k]
    assert tuple(x[0] for x in data) == zrange, (k, data)
    assert max(v for z, m, v in data) == maximum, (k, data)

# Independent four-coordinate branch census: every non-special quadruple
# with sum > B and < 1 is included by exact rational upper bounds.
quadruples = set()
def branch(prefix, value):
    j = len(prefix)
    if j == 4:
        if B < value < 1:
            quadruples.add(prefix)
        return
    first = prefix[-1] if prefix else 2
    if j == 3 and prefix == (2, 3, 7):
        return
    if value >= B:
        raise AssertionError((prefix, value))
    bound = F(4 - j, 1) / (B - value)
    for denominator in range(first, bound.numerator // bound.denominator + 1):
        nv = value + F(1, denominator)
        if nv < 1 and nv + F(3-j, denominator) > B:
            branch(prefix + (denominator,), nv)
branch((), F(0))
assert len(quadruples) == 103, len(quadruples)
assert max(sum((F(1, d) for d in x), F(0)) for x in quadruples) == SECOND
assert sum(1 for x in quadruples if sum((F(1, d) for d in x), F(0)) == SECOND) == 1

assert B + F(1, 45) == CRITICAL
assert B + F(1, 46) < SECOND
assert sum([F(1, 2), F(1, 3), F(1, 8), F(1, 25)]) == SECOND
for k in range(2, 60):
    good = CRITICAL + (F(1)-CRITICAL)/k
    a = 1 + int(1 / (good - B))
    assert B + F(1, a) < good
    assert B + F(1, a) >= CRITICAL > SECOND
    bad = SECOND + (CRITICAL-SECOND)/k
    a = 1 + int(1 / (bad - B))
    assert a == 46 and B + F(1, a) < SECOND < bad

print('VERIFY_OK exact_triple_nodes=' + str(node_counts))
print('VERIFY_OK complete_nonprefix_triples=20 complete_above_B_quadruples=103')
for prefix in sorted(by_first_two):
    zrange, maximum = expected[prefix]
    print('TABLE', prefix, 'third=',zrange,'max=',maximum)
print('VERIFY_OK maximum_nonprefix_4term_below_1=599/600 unique_witness=(2,3,8,25)')
print('VERIFY_OK sharp_threshold=629/630 upper_strict lower_counterexample_interval=(599/600,629/630]')
