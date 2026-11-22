#!/usr/bin/env python3
"""Exact finite verification of two-line symmetric-difference shattering in PG(2,3).
Run alongside certificate.json with Python 3.10+; no third-party packages.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

CFILE = Path(__file__).with_name('certificate.json')
certificate = json.loads(CFILE.read_text(encoding='utf-8'))
q = 3

def norm(x):
    first = next(y for y in x if y)
    inverse = pow(first, -1, q)
    return tuple((v*inverse)%q for v in x)

points = sorted({norm(t) for t in itertools.product(range(q), repeat=3) if any(t)})
assert len(points) == 13
assert [list(p) for p in points] == certificate['point_coordinates']
index = {p:i for i,p in enumerate(points)}
lines = [sum(1<<i for i,p in enumerate(points) if sum(x*y for x,y in zip(p,l))%q==0)
         for l in points]
assert all(v.bit_count() == 4 for v in lines)
assert lines == certificate['line_masks']
assert len(set(lines)) == 13
pairs = list(itertools.combinations(range(13),2))
concepts = [lines[a]^lines[b] for a,b in pairs]
assert len(set(concepts)) == 78
assert all(c.bit_count() == 6 for c in concepts)

# Every support is checked directly against all 78 traces.
shattered = {s for s in range(1<<13) if len({c&s for c in concepts}) == 1<<s.bit_count()}
counts = Counter(s.bit_count() for s in shattered)
assert [counts[k] for k in range(6)] == [1,13,78,286,702,0]
assert not any(s.bit_count()>=5 for s in shattered)
for s in range(1<<13):
    if s.bit_count()==4:
        assert (s in shattered) == (not any((s&l)==l for l in lines))
facets = [s for s in shattered if not any(s|1<<i in shattered for i in range(13) if not s>>i&1)]
assert len(facets)==702 and all(s.bit_count()==4 for s in facets)

# Enumerate the complete projective linear group and its action on supports.
perms = set()
for coeffs in itertools.product(range(3), repeat=9):
    a,b,c,d,e,f,g,h,i = coeffs
    det = (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3
    if not det:
        continue
    perm = tuple(index[norm(((a*x+b*y+c*z)%3,
                             (d*x+e*y+f*z)%3,
                             (g*x+h*y+i*z)%3))] for x,y,z in points)
    perms.add(perm)
assert len(perms)==5616

def group_orbit(mask):
    return {sum(1<<p[j] for j in range(13) if mask>>j&1) for p in perms}
for k,expected,representatives in [(4,[13,468,234],[(0,1,2,3),(0,1,2,4),(1,2,4,5)]),
                                   (5,[117,702,468],[(0,1,2,3,4),(0,1,2,4,5),(1,2,3,4,5)])]:
    orbits = [group_orbit(sum(1<<j for j in rep)) for rep in representatives]
    assert [len(O) for O in orbits]==expected
    assert len(set.union(*orbits)) == len(list(itertools.combinations(range(13),k)))
    for i,O in enumerate(orbits):
        assert not any(O & T for T in orbits[:i])

# Independent of global enumeration, the two complete 16-trace witness tables
# establish shattering of the two non-collinear quadruple orbit types.
for item in certificate['four_representatives']:
    support = item['support']
    assert len(support)==4
    assert len(item['witness_line_pairs_by_trace_bitmask'])==16
    for trace_code,pair in enumerate(item['witness_line_pairs_by_trace_bitmask']):
        a,b=pair
        assert 0<=a<b<13
        actual = sum(((lines[a]^lines[b])>>x&1)<<j for j,x in enumerate(support))
        assert actual == trace_code

for item in certificate['five_representatives']:
    s = sum(1<<j for j in item['support'])
    target = sum(1<<j for j in item['missing_trace_points'])
    assert target & s == target
    assert not any(c&s==target for c in concepts)

# The adaptive tree is a full binary tree indexed 1,...,63; leaf i=32,...,63
# has the witness at index i-32. A right edge means true, left means false.
tree = certificate['tree_depth_five']
queries = tree['internal_queries_heap_order']
leaves = tree['leaf_line_pairs_left_to_right']
assert len(queries)==31 and len(leaves)==32
assert all(0<=i<13 for i in queries)
assert len({tuple(x) for x in leaves})==32
for k,(a,b) in enumerate(leaves):
    assert 0<=a<b<13
    value=lines[a]^lines[b]
    i=32+k
    visited=[]
    while i>1:
        parent=i//2
        bit=i%2
        query=queries[parent-1]
        visited.append(query)
        assert (value>>query)&1 == bit
        i=parent
    assert len(set(visited))==5

# The design's 2-wise multiplicities exclude depth six without search:
# all coordinates have r=36 positives; every distinct pair has lambda=15.
for x in range(13):
    assert sum(bool(c>>x&1) for c in concepts)==36
    for y in range(x):
        assert sum(bool(c>>x&1) and bool(c>>y&1) for c in concepts)==15
print('TERNARY_TWO_LINE_XOR_PROJECTIVE_PASS concepts=78 faces=1080 facets=702 orbits=2 VC=4 Ldim=5')
