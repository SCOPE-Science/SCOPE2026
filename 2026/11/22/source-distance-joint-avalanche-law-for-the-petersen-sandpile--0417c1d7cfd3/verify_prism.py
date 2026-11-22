"""Independent exact Petersen avalanche check using generalized Petersen labels.

Run in the directory containing JOINT_COUNTS.csv. Python 3 standard library only.
"""
from collections import Counter
from csv import DictReader
from itertools import product
from pathlib import Path

# Generalized Petersen GP(5,2): outer cycle 0..4, inner star 5..9.
edges = [(i, (i + 1) % 5) for i in range(5)]
edges += [(i + 5, (i + 2) % 5 + 5) for i in range(5)]
edges += [(i, i + 5) for i in range(5)]
assert len(edges) == 15
neighbours = [set() for _ in range(10)]
for a, b in edges:
    neighbours[a].add(b)
    neighbours[b].add(a)
assert all(len(x) == 3 for x in neighbours)


def parallel_stabilize(h):
    state = list(h)
    fired = [0] * 9
    while True:
        unstable = [v for v in range(1, 10) if state[v - 1] >= 3]
        if not unstable:
            return tuple(state), tuple(fired)
        for v in unstable:
            state[v - 1] -= 3
            fired[v - 1] += 1
        for v in unstable:
            for w in neighbours[v]:
                if w:
                    state[w - 1] += 1


def no_forbidden_subconfiguration(c):
    # Equivalent forbidden-subconfiguration formulation of the burning test.
    remaining = set(range(1, 10))
    while remaining:
        removable = {i for i in remaining
                     if c[i - 1] >= len(neighbours[i] & remaining)}
        if not removable:
            return False
        remaining -= removable
    return True


states = [c for c in product(range(3), repeat=9)
          if no_forbidden_subconfiguration(c)]
assert len(states) == 2000
joint = Counter()
for source_type, source in [('near', 1), ('far', 2)]:
    assert (source in neighbours[0]) == (source_type == 'near')
    for c in states:
        inp = list(c)
        inp[source - 1] += 1
        fin, odometer = parallel_stabilize(inp)
        mass = sum(odometer)
        dissipation = sum(odometer[v - 1] for v in neighbours[0])
        assert sum(fin) + dissipation == sum(c) + 1
        joint[source_type, mass, dissipation] += 1

expected = Counter()
with Path('JOINT_COUNTS.csv').open(newline='', encoding='utf-8') as f:
    for row in DictReader(f):
        expected[row['source'], int(row['topplings']), int(row['sink_loss'])] = int(row['count'])
assert joint == expected, (joint - expected, expected - joint)
print('PETERSEN_GENERALIZED_PETERSEN_EXACT_PASS recurrent=2000 joint_terms=' + str(len(joint)))
