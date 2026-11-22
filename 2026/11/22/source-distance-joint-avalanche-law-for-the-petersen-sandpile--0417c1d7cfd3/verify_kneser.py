"""Exact stationary avalanche census for Petersen's sandpile via Kneser labels.

Run in the directory containing JOINT_COUNTS.csv. Python 3 standard library only.
"""
from collections import Counter
from itertools import combinations, product
from csv import DictReader
from pathlib import Path

V = list(combinations(range(5), 2))
assert len(V) == 10
E = [(i, j) for i in range(10) for j in range(i + 1, 10)
     if set(V[i]).isdisjoint(V[j])]
assert len(E) == 15
N = [set() for _ in V]
for i, j in E:
    N[i].add(j)
    N[j].add(i)
assert all(len(n) == 3 for n in N)
sink = 0
boundary = tuple(int(i in N[sink]) for i in range(1, 10))


def stabilize(initial):
    h = list(initial)
    firings = [0] * 9
    while True:
        at = next((i for i, a in enumerate(h) if a >= 3), None)
        if at is None:
            return tuple(h), tuple(firings)
        h[at] -= 3
        firings[at] += 1
        for v in N[at + 1]:
            if v != sink:
                h[v - 1] += 1


def is_recurrent(c):
    # Dhar's burning criterion, via addition of one grain per sink edge.
    burned, fired = stabilize([c[i] + boundary[i] for i in range(9)])
    assert burned == c if fired == (1,) * 9 else True
    return fired == (1,) * 9


states = [c for c in product(range(3), repeat=9) if is_recurrent(c)]
assert len(states) == 2000
joint = Counter()
for d, src in [('near', 7), ('far', 1)]:
    assert (src in N[0]) == (d == 'near')
    for c in states:
        a = list(c)
        a[src - 1] += 1
        final, fired = stabilize(a)
        mass = sum(fired)
        loss = sum(fired[v - 1] for v in N[0])
        assert sum(final) == sum(c) + 1 - loss
        joint[d, mass, loss] += 1
expected = Counter()
with Path('JOINT_COUNTS.csv').open(newline='', encoding='utf-8') as f:
    for r in DictReader(f):
        key = (r['source'], int(r['topplings']), int(r['sink_loss']))
        expected[key] = int(r['count'])
assert joint == expected, (joint - expected, expected - joint)
for d in ('near', 'far'):
    assert sum(v for (t, _, _), v in joint.items() if t == d) == 2000
    assert sum(k * v for (t, _, k), v in joint.items() if t == d) == 2000
assert max(m for (d, m, _), c in joint.items() if d == 'near') == 9
assert max(m for (d, m, _), c in joint.items() if d == 'far') == 24
print('PETERSEN_KNESER_EXACT_PASS recurrent=2000 joint_terms=' + str(len(joint)))
