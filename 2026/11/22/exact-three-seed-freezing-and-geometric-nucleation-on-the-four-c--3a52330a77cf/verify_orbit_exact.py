"""Exact symmetry-reduced absorbing-probability certificate for the Q4 Glauber process.

Run: python3 verify_orbit_exact.py q4_certificate.json
Requires Python 3 and SymPy. No precomputed orbit data or saved intermediate is read.
"""
import collections
import itertools
import json
import math
import sys
from fractions import Fraction
import sympy as S

N = 16
FULL = (1 << N) - 1
NBR = [tuple(v ^ (1 << j) for j in range(4)) for v in range(N)]

# Generating coordinate reflections and adjacent coordinate permutations.
transforms = [[v ^ (1 << j) for v in range(N)] for j in range(4)]
for j in range(3):
    transforms.append([sum(((v >> k) & 1) << (k + 1 if k == j else k - 1 if k == j+1 else k)
                           for k in range(4)) for v in range(N)])

def apply(mask, perm):
    result = 0
    for vertex in range(N):
        if (mask >> vertex) & 1:
            result |= 1 << perm[vertex]
    return result

classes = [-1] * (1 << N)
orbits = []
for state in range(1 << N):
    if classes[state] >= 0:
        continue
    index = len(orbits)
    queue = [state]
    classes[state] = index
    for current in queue:
        for perm in transforms:
            other = apply(current, perm)
            if classes[other] < 0:
                classes[other] = index
                queue.append(other)
        other = current ^ FULL  # global spin reversal
        if classes[other] < 0:
            classes[other] = index
            queue.append(other)
    orbits.append((state, len(queue)))
assert len(orbits) == 222
assert sum(size for _,size in orbits) == 65536

# Twice the physical spin-flip rate is 2 for energy lowering, 1 for ties.
def weights(mask):
    for v in range(N):
        d = sum(((mask >> v) & 1) != ((mask >> u) & 1) for u in NBR[v])
        if d >= 2:
            yield mask ^ (1 << v), (2 if d > 2 else 1)

def cut(mask):
    return sum(((mask >> v) & 1) != ((mask >> (v ^ (1 << k))) & 1)
               for v in range(N) for k in range(4)) // 2

energies = [cut(state) for state,_ in orbits]
adj = []
for state,_ in orbits:
    row = collections.Counter()
    for other, weight in weights(state):
        row[classes[other]] += weight
    adj.append(row)

p = {}  # probability to reach unanimity
for energy in sorted(set(energies)):
    indices = [i for i in range(len(orbits)) if energies[i] == energy]
    rank = {i:j for j,i in enumerate(indices)}
    A = S.zeros(len(indices))
    b = S.zeros(len(indices),1)
    for i in indices:
        r = rank[i]
        if not adj[i]:
            A[r,r] = 1
            b[r] = int(orbits[i][0] == 0)
            continue
        A[r,r] += sum(adj[i].values())
        for j,weight in adj[i].items():
            assert energies[j] <= energy
            if energies[j] == energy:
                A[r, rank[j]] -= weight
            else:
                b[r] += weight*p[j]
    # An invertible finite M-matrix: eventual exit from each transient layer.
    values = A.inv() * b
    for i in indices:
        p[i] = values[rank[i]]

frozen = [1-p[i] for i in range(len(orbits))]
entries = [
    {'representative': state, 'orbit_size': size,
     'frozen_numerator': int(frozen[i].p), 'frozen_denominator': int(frozen[i].q)}
    for i,(state,size) in enumerate(orbits)
]
triple = {}
for state in range(1<<N):
    if state.bit_count() != 3:
        continue
    v = [j for j in range(N) if (state >> j) & 1]
    distances = tuple(sorted((a^b).bit_count() for a,b in itertools.combinations(v,2)))
    rate = frozen[classes[state]]
    if distances not in triple:
        triple[distances] = {'distances': list(distances), 'placements': 0,
                             'frozen_numerator': int(rate.p),
                             'frozen_denominator': int(rate.q)}
    triple[distances]['placements'] += 1
    assert S.Rational(triple[distances]['frozen_numerator'],triple[distances]['frozen_denominator']) == rate
assert sum(row['placements'] for row in triple.values()) == math.comb(16,3)

def mean_frozen(states):
    states = list(states)
    return sum((frozen[classes[s]] for s in states), S.Rational(0)) / len(states)

uniform = mean_frozen(range(65536))
balanced = mean_frozen(s for s in range(65536) if s.bit_count()==8)
absorb = [s for s in range(65536) if not list(weights(s))]
certificate = {
    'schema_version': 1,
    'model': 'standard fair-tie zero-temperature Glauber on the 4-cube',
    'normalization': 'rates 1 for energy-lowering flips, 1/2 for energy-neutral flips, 0 otherwise',
    'orbits': entries,
    'absorbing_states': absorb,
    'three_seed_classes': sorted(triple.values(),key=lambda row: row['distances']),
    'unbiased_frozen_fraction': [int(uniform.p),int(uniform.q)],
    'balanced_frozen_fraction': [int(balanced.p),int(balanced.q)]
}
if len(sys.argv)>1:
    with open(sys.argv[1], encoding='utf-8') as stream:
        expected = json.load(stream)
    assert certificate == expected, 'Exact orbit solution differs from certificate'
assert len(absorb)==10
assert len(triple)==6
assert frozen[classes[0]]==0
assert frozen[classes[255]]==1
print('PASS: independent exact 222-orbit solution matches all certificate fractions.')
print('Triple minority classes:')
for row in certificate['three_seed_classes']:
    print(row['distances'], row['placements'], str(S.Rational(row['frozen_numerator'],row['frozen_denominator'])))
print('Random three-minority frozen probability:',mean_frozen(s for s in range(65536) if s.bit_count()==3))
print('Unbiased finite-temperature-quench frozen probability: %.12f' % float(uniform))
print('Balanced-initial frozen probability: %.12f' % float(balanced))
