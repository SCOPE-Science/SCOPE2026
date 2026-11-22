"""Independent exact checks for ternary surjection universal cycles (standard library)."""
from collections import Counter
from itertools import permutations, product

ALPHABET = '012'
WINDOWS = {''.join(x) for x in product(ALPHABET, repeat=4) if len(set(x)) == 3}
VERTICES = sorted({w[:3] for w in WINDOWS} | {w[1:] for w in WINDOWS})
ADJ = {v: tuple(sorted(w for w in WINDOWS if w[:3] == v)) for v in VERTICES}
BRANCH = tuple(v for v in VERTICES if len(ADJ[v]) == 3)
assert len(WINDOWS) == 36 and len(VERTICES) == 24 and len(BRANCH) == 6
assert all(len(ADJ[v]) in (1, 3) for v in VERTICES)
assert all(sum(w[1:] == v for w in WINDOWS) == len(ADJ[v]) for v in VERTICES)

# Independently form the six-vertex directed contraction and its Laplacian.
CONTRACT = {v: [] for v in BRANCH}
for v in BRANCH:
    for e in ADJ[v]:
        u = e[1:]
        steps = 0
        while u not in CONTRACT:
            assert len(ADJ[u]) == 1
            u = ADJ[u][0][1:]
            steps += 1
            assert steps <= 2
        CONTRACT[v].append(u)
assert all(len(set(CONTRACT[v])) == 3 and v not in CONTRACT[v] for v in BRANCH)
assert all(v in CONTRACT[u] for v in BRANCH for u in CONTRACT[v])

# Determinant by exact Leibniz expansion: 5! terms, no numerical approximation.
L = [[(3 if i == j else 0) - (BRANCH[j] in CONTRACT[BRANCH[i]])
      for j in range(6)] for i in range(6)]
M = [r[:5] for r in L[:5]]
def det5(m):
    d = 0
    for p in permutations(range(5)):
        inversions = sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5))
        t = 1
        for i in range(5):
            t *= m[i][p[i]]
        d += (-1 if inversions % 2 else 1) * t
    return d
assert det5(M) == 75
assert det5(M) * (2 ** 6) == 4800

# An exhaustive, independent rotor-order enumeration, rooted at the unique 0120 edge.
ROOT_EDGE = '0120'
ROOT = ROOT_EDGE[:3]
VARIABLE = {v: tuple(permutations(ADJ[v])) for v in BRANCH}
FORCED = {v: ADJ[v] for v in VERTICES if v not in BRANCH}
choices = []
for v in BRANCH:
    if v == ROOT:
        choices.append(tuple(p for p in VARIABLE[v] if p[0] == ROOT_EDGE))
    else:
        choices.append(VARIABLE[v])
assert len(choices[0]) == 2 and all(len(p) == 6 for p in choices[1:])
CYCLES = set()
for selected in product(*choices):
    rotor = dict(FORCED)
    rotor.update(zip(BRANCH, selected))
    pos = Counter()
    cur = ROOT
    edges = []
    for _ in range(36):
        if pos[cur] == len(rotor[cur]):
            break
        edge = rotor[cur][pos[cur]]
        pos[cur] += 1
        edges.append(edge)
        cur = edge[1:]
    if len(edges) != 36 or cur != ROOT:
        continue
    s = ''.join(e[0] for e in edges)
    assert s[:4] == ROOT_EDGE
    observed = {''.join(s[(i + j) % 36] for j in range(4)) for i in range(36)}
    assert observed == WINDOWS and s not in CYCLES
    CYCLES.add(s)
assert len(CYCLES) == 4800

def canonical(s):
    assert len(s) == 36
    positions = [i for i in range(36) if ''.join(s[(i+j)%36] for j in range(4)) == ROOT_EDGE]
    assert len(positions) == 1
    i = positions[0]
    return s[i:] + s[:i]

perms = tuple(permutations(ALPHABET))
actions = Counter()
for p in perms:
    table = str.maketrans(ALPHABET, ''.join(p))
    for reverse in (False, True):
        fixed = 0
        for s in CYCLES:
            transformed = s.translate(table)
            if reverse:
                transformed = transformed[::-1]
            if canonical(transformed) == s:
                fixed += 1
        actions[(''.join(p), reverse)] = fixed
assert actions[('012',False)] == 4800
assert all(actions[(''.join(p),False)] == (40 if p in [('0','2','1'),('1','0','2'),('2','1','0')] else 0)
           for p in perms if p != tuple(ALPHABET))
assert all(actions[(''.join(p),True)] == 0 for p in perms)
assert sum(actions.values()) == 4920 and sum(actions.values()) // 12 == 410

# Orbit sizes verify the entire symmetry classification, not merely Burnside's sum.
remaining = set(CYCLES)
orbits = Counter()
while remaining:
    s = next(iter(remaining))
    o = set()
    for p in perms:
        t = s.translate(str.maketrans(ALPHABET, ''.join(p)))
        o.add(canonical(t))
        o.add(canonical(t[::-1]))
    assert o <= CYCLES
    assert o <= remaining
    orbits[len(o)] += 1
    remaining -= o
assert orbits == Counter({6: 20, 12: 390})
print('VERIFY_OK', 'windows=36', 'contract_vertices=6', 'trees=75',
      'cycles=4800', 'symmetry_classes=410', 'orbits_6=20', 'orbits_12=390')
