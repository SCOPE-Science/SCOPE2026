"""Exact finite verification of the spin-one truncated-tetrahedron ground-state diagram.

Python 3.9+ standard library only. Run: python verify.py
"""
from collections import Counter
import csv
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
CERT = json.loads((ROOT / 'certificates/phase_polytope.json').read_text())
BASE = tuple((i, j) for i in range(4) for j in range(4) if i != j)
INDEX = {v: k for k, v in enumerate(BASE)}
EDGES = sorted({tuple(sorted((INDEX[(i, j)], INDEX[(i, k)])))
                for i in range(4) for j in range(4) for k in range(j + 1, 4)
                if j != i and k != i}
               | {tuple(sorted((INDEX[(i, j)], INDEX[(j, i)])))
                  for i in range(4) for j in range(4) if i != j})
assert len(BASE) == 12 and len(EDGES) == 18
assert all(sum(u in e for e in EDGES) == 3 for u in range(12))

# Route A: incrementally grow one vertex spin at a time.
LOWER = [tuple(v for v in range(k) if (v, k) in EDGES) for k in range(12)]
def vertex_recursion():
    hist = Counter()
    s = [0] * 12
    def visit(k, energy, mag, occ):
        if k == 12:
            hist[(energy, mag, occ)] += 1
            return
        for a in (-1, 0, 1):
            s[k] = a
            visit(k + 1, energy + a * sum(s[j] for j in LOWER[k]),
                  mag + a, occ + a * a)
    visit(0, 0, 0, 0)
    return hist

# Route B: sum over four triangle blocks, with the six matching edges
# connecting reversed ordered pairs. This factorization is distinct from
# Route A's vertex-by-vertex recursion.
LOCAL = []
for a, b, c in product((-1, 0, 1), repeat=3):
    LOCAL.append(((a, b, c), a*b + a*c + b*c,
                  a+b+c, a*a+b*b+c*c))
PAIR = [(i, j) for i in range(4) for j in range(i + 1, 4)]
BLOCKPOS = {i: {j: k for k, j in enumerate(t for t in range(4) if t != i)}
            for i in range(4)}
def block_contraction():
    hist = Counter()
    for picks in product(range(27), repeat=4):
        blocks = [LOCAL[t] for t in picks]
        e = sum(t[1] for t in blocks)
        m = sum(t[2] for t in blocks)
        q = sum(t[3] for t in blocks)
        for i,j in PAIR:
            e += blocks[i][0][BLOCKPOS[i][j]] * blocks[j][0][BLOCKPOS[j][i]]
        hist[(e,m,q)] += 1
    return hist

A = vertex_recursion()
B = block_contraction()
assert A == B
assert sum(A.values()) == 3**12 == 531441

sectors = {}
for (e, m, q), count in A.items():
    if (m,q) not in sectors or e < sectors[(m,q)][0]:
        sectors[(m,q)] = (e, count)
    elif e == sectors[(m,q)][0]:
        old_e, old_count = sectors[(m,q)]
        sectors[(m,q)] = (old_e, old_count + count)
assert len(sectors) == 91
with (ROOT / 'certificates/sector_minima.csv').open(newline='') as f:
    reader = csv.DictReader(f)
    table = {(int(r['magnetization']), int(r['occupied_sites'])):
             (int(r['minimum_exchange_energy']), int(r['degeneracy']))
             for r in reader}
assert table == sectors

V = {(m,q): (e,c) for m,q,e,c in CERT['vertices']}
assert len(V) == 17
for key,val in V.items():
    assert sectors[key] == tuple(val), (key, val, sectors[key])

# Rational convex-combination witnesses prove each omitted (m,q)
# sector is weakly dominated by the seventeen listed affine energies.
seen = set()
for row in CERT['domination']:
    m, q, e = row['m'], row['q'], row['e_min']
    assert (m,q) in sectors and (m,q) not in V
    assert sectors[(m,q)][0] == e
    assert (m,q) not in seen
    seen.add((m,q))
    weights = [Fraction(*src['weight']) for src in row['sources']]
    assert sum(weights) == 1 and all(w >= 0 for w in weights)
    assert sum(w*src['m'] for src,w in zip(row['sources'],weights)) == m
    assert sum(w*src['q'] for src,w in zip(row['sources'],weights)) == q
    assert sum(w*V[(src['m'],src['q'])][0]
               for src,w in zip(row['sources'],weights)) <= e
assert seen == set(sectors) - set(V)

# Strict rational supporting-field witnesses show that every listed sector
# is an open phase, not an inactive or merely boundary sector.
assert len(CERT['witnesses']) == 17
for row in CERT['witnesses']:
    m,q = row['m'],row['q']
    h,d = Fraction(*row['h']),Fraction(*row['d'])
    e = V[(m,q)][0]
    gap = min(Fraction(e2) - h*m2 + d*q2 - (e - h*m + d*q)
              for (m2,q2),(e2,c2) in sectors.items() if (m2,q2)!=(m,q))
    assert gap == Fraction(*row['gap']) and gap > 0

# At this exact two-field intersection, nonextremal sectors also contribute.
points = [(e-h*m+d*q, count) for (e,m,q),count in A.items()
          for h,d in [(1,1)]]
E0 = min(val for val,count in points)
deg = sum(count for val,count in points if val==E0)
assert E0 == 0 and deg == 1577
assert min(e for e,m,q in A) == -10
assert sum(count for (e,m,q),count in A.items() if e == -10) == 24

payload = '\n'.join(f'{e},{m},{q},{A[(e,m,q)]}' for e,m,q in sorted(A))
print('PASS | vertices=12 edges=18 microstates=531441 sectors=91')
print('PASS | independent complete microcanonical histograms equal')
print('PASS | exactly 17 generically exposed ground-state sectors')
print('PASS | 74 exact rational domination and 17 strict exposure certificates')
print('PASS | (h/J,D/J)=(1,1): energy/J=0, degeneracy=1577')
digest = hashlib.sha256(payload.encode()).hexdigest()
assert digest == '35dea54d5dddbc058df29197a4e4b33c552866fb96af0c481299873533db577d'
print('DOS SHA256:', digest)
