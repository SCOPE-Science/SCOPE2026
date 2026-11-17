#!/usr/bin/env python3
"""Exact finite certificate for matching-complex topology and symmetry of C3 Cartesian C4.

Requires Python 3.10+ standard library only. Run: python torus_match_verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product
import json
import ast

N, M = 3, 4
VERTICES = list(product(range(N), range(M)))
EDGES = sorted({tuple(sorted(((i, j), ((i + 1) % N, j))))
                for i, j in VERTICES} |
               {tuple(sorted(((i, j), (i, (j + 1) % M))))
                for i, j in VERTICES})
VINDEX = {v: k for k, v in enumerate(VERTICES)}
EINDEX = {e: k for k, e in enumerate(EDGES)}
ENDPOINTS = [sum(1 << VINDEX[v] for v in e) for e in EDGES]
assert len(VERTICES) == 12 and len(EDGES) == 24

# Enumerate every matching in the original graph, not just maximal matchings.
FACES = [0]
def extend(face, covered_vertices, start):
    for e in range(start, len(EDGES)):
        if not ENDPOINTS[e] & covered_vertices:
            f2 = face | (1 << e)
            FACES.append(f2)
            extend(f2, covered_vertices | ENDPOINTS[e], e + 1)
extend(0, 0, 0)
FACESET = set(FACES)
assert len(FACES) == len(FACESET) == 2764
FCNT = {d - 1: v for d, v in Counter(f.bit_count() for f in FACES if f).items()}
assert FCNT == {0:24, 1:204, 2:748, 3:1149, 4:588, 5:50}

# Filtered matching on the nonempty face poset; order fixed in the certificate.
PIVOT_ORDER = [5,23,16,7,4,3,22,21,1,15,20,19,0,9,6,12,8,10,18,14,17,13,2,11]
assert sorted(PIVOT_ORDER) == list(range(24))
remaining = FACESET - {0}
PAIRS = []
for e in PIVOT_ORDER:
    v = 1 << e
    for a in sorted(f for f in remaining if not f & v and (f | v) in remaining):
        b = a | v
        assert a in remaining and b in remaining and b.bit_count() == a.bit_count() + 1
        PAIRS.append((a, b))
        remaining.remove(a)
        remaining.remove(b)
CRITICAL = remaining
assert len(PAIRS) == 1358 and len(CRITICAL) == 47
assert Counter(f.bit_count()-1 for f in CRITICAL) == {0:1, 3:45, 4:1}
LOWER_TO_UPPER = dict(PAIRS)
UPPER_TO_LOWER = {b:a for a,b in PAIRS}
assert len(LOWER_TO_UPPER) == len(UPPER_TO_LOWER) == len(PAIRS)

# Direct global DAG check, not merely a local assertion about pivot stages.
indeg = {f:0 for f in FACESET if f}
out = defaultdict(list)
incidences = 0
for b in indeg:
    for e in range(24):
        if not (b >> e) & 1: continue
        a = b ^ (1 << e)
        if not a: continue
        incidences += 1
        source,target = (a,b) if LOWER_TO_UPPER.get(a) == b else (b,a)
        out[source].append(target)
        indeg[target] += 1
q = deque(f for f,d in indeg.items() if d == 0)
visited = 0
while q:
    f=q.popleft(); visited += 1
    for h in out[f]:
        indeg[h] -= 1
        if indeg[h] == 0: q.append(h)
assert visited == 2763, (visited, len(indeg))

# Exact signed boundary on ordered edges.
def boundary(face):
    k = 0
    for e in range(24):
        if face & (1 << e):
            yield face ^ (1 << e), (1 if k % 2 == 0 else -1)
            k += 1

# Algebraic discrete Morse projection, obtained by eliminating each matched
# unit incidence. The dependency graph is acyclic by the checked Hasse DAG.
@lru_cache(None)
def projection(a):
    if a in CRITICAL:
        return {a:1}
    if a in UPPER_TO_LOWER:
        return {}
    b = LOWER_TO_UPPER[a]
    sign = next(s for c,s in boundary(b) if c == a)
    out = defaultdict(int)
    for c,s in boundary(b):
        if c != a:
            for crit,v in projection(c).items():
                out[crit] -= sign*s*v
    return {x:v for x,v in out.items() if v}

critical_3 = sorted(f for f in CRITICAL if f.bit_count() == 4)
critical_4 = [f for f in CRITICAL if f.bit_count() == 5]
assert len(critical_3) == 45 and len(critical_4) == 1
morse_boundary = defaultdict(int)
for a,s in boundary(critical_4[0]):
    for h,v in projection(a).items():
        morse_boundary[h] += s*v
morse_boundary = {k:v for k,v in morse_boundary.items() if v}
assert len(morse_boundary) == 7 and set(map(abs,morse_boundary.values())) == {1}
assert [(hex(k), morse_boundary[k]) for k in sorted(morse_boundary)] == [
    ('0x90102', -1), ('0x94002', 1), ('0x210500', -1),
    ('0x404410', -1), ('0x408401', -1), ('0x40c010', -1),
    ('0x480101', 1)]

# Independent check on original simplicial chain complex over F_2.
bydim = defaultdict(list)
for f in FACES:
    if f: bydim[f.bit_count()-1].append(f)
prev = None
ranks = {}
for d in range(6):
    curr = bydim[d]
    if prev is None:
        ranks[d] = 0
    else:
        pivots = {}
        pidx = {f:j for j,f in enumerate(prev)}
        for b in curr:
            col = 0
            for a,s in boundary(b): col ^= (1 << pidx[a])
            while col:
                p = col.bit_length()-1
                if p not in pivots:
                    pivots[p] = col
                    break
                col ^= pivots[p]
        ranks[d] = len(pivots)
    prev = curr
assert ranks == {0:0, 1:23, 2:181, 3:567, 4:538, 5:50}
mod2_betti = {d:len(bydim[d])-ranks[d]-ranks.get(d+1,0)
              for d in range(6)}
assert mod2_betti == {0:1,1:0,2:0,3:44,4:0,5:0}

# Natural S_3 x D_4 action. Compute characters two independent ways:
# (1) signed fixed-simplex Lefschetz sum and
# (2) evaluation I(-1) on the conflict graph of admissible edge orbits.
def graph_automorphism(rs,rt,cs,ct):
    p = []
    for edge in EDGES:
        image = tuple(sorted((((rs*i+rt) % 3), ((cs*j+ct) % 4))
                             for i,j in edge))
        p.append(EINDEX[image])
    assert sorted(p) == list(range(24))
    return tuple(p)

def signed_trace(p):
    lef = 0
    fixed = 0
    for f in FACES:
        if not f: continue
        ids = [j for j in range(24) if f & (1 << j)]
        images = [p[j] for j in ids]
        if sum(1 << j for j in images) != f: continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images)) for j in range(i+1,len(images)))
        lef += (-1 if len(ids) % 2 == 0 else 1) * (-1 if inversions%2 else 1)
        fixed += 1
    return 1 - lef, fixed

def orbit_trace(p):
    unseen = set(range(24))
    orbits = []
    while unseen:
        seed = min(unseen)
        cyc = []
        j=seed
        while j in unseen:
            unseen.remove(j)
            cyc.append(j)
            j=p[j]
        assert j == seed
        # An orbit can be included only if its edges themselves form a matching.
        covered=0
        for e in cyc:
            if ENDPOINTS[e]&covered:break
            covered |= ENDPOINTS[e]
        else:
            orbits.append(covered)
    k = len(orbits)
    closed = []
    for i in range(k):
        mask = 1 << i
        for j in range(k):
            if i != j and (orbits[i]&orbits[j]):mask |= 1 << j
        closed.append(mask)
    @lru_cache(None)
    def independence_at_minus_one(mask):
        if not mask:return 1
        j=(mask&-mask).bit_length()-1
        return independence_at_minus_one(mask ^ (1<<j)) - independence_at_minus_one(mask & ~closed[j])
    return independence_at_minus_one((1<<k)-1)

row_type = lambda s,t: ('id' if s==1 and t==0 else 'rot3' if s==1 else 'refl')
def col_type(s,t):
    if s == 1:return 'id' if t==0 else 'half' if t==2 else 'quarter'
    return 'vertex-ref' if t%2==0 else 'edge-ref'
classes = defaultdict(list)
perms = set()
for rs,rt,cs,ct in product((1,-1),range(3),(1,-1),range(4)):
    p=graph_automorphism(rs,rt,cs,ct)
    assert p not in perms
    perms.add(p)
    sign_trace,fixed = signed_trace(p)
    assert sign_trace == orbit_trace(p)
    classes[(row_type(rs,rt),col_type(cs,ct))].append((sign_trace,fixed))
assert len(perms) == 48 and len(classes) == 15
assert all(len({x[0] for x in observations}) == 1 for observations in classes.values())
char = {str(k):{'class_size':len(a),'trace':a[0][0], 'fixed_nonempty_faces':a[0][1]}
        for k,a in sorted(classes.items())}
full_fixed = sum(len(a)*a[0][0] for a in classes.values())
assert full_fixed == 48
rotation_fixed = sum(len(a)*a[0][0] for (r,c),a in classes.items()
                     if r in ('id','rot3') and c in ('id','half','quarter'))
assert rotation_fixed == 48 # dimension 4 under subgroup of size 12

def chi_s3(label,cl):
    return {'triv':{'id':1,'rot3':1,'refl':1},
            'sgn': {'id':1,'rot3':1,'refl':-1},
            'standard':{'id':2,'rot3':-1,'refl':0}}[label][cl]
def chi_d4(label,cl):
    if label=='E':return {'id':2,'half':-2,'quarter':0,'vertex-ref':0,'edge-ref':0}[cl]
    r,s=label
    return {'id':1,'half':1,'quarter':r,'vertex-ref':s,'edge-ref':r*s}[cl]
irreps = {}
for rl in ('triv','sgn','standard'):
    for cl in ((1,1),(1,-1),(-1,1),(-1,-1),'E'):
        numer = sum(len(a)*a[0][0]*chi_s3(rl,r)*chi_d4(cl,c)
                    for (r,c),a in classes.items())
        assert numer % 48 == 0 and numer >= 0
        irreps[(rl,str(cl))] = numer//48
assert sum(v*chi_s3(rl,'id')*chi_d4(ast.literal_eval(cl) if cl.startswith('(') else cl,'id')
           for (rl,cl),v in irreps.items()) == 44

summary = {'graph':'C3 Cartesian C4','graph_vertices':len(VERTICES),'graph_edges':len(EDGES),
           'matching_face_count_including_empty':len(FACES), 'face_counts_by_dimension':FCNT,
           'morse_pairs':len(PAIRS),'critical_cells_by_dimension':dict(Counter(f.bit_count()-1 for f in CRITICAL)),
           'hasse_incidences':incidences,'directed_acyclicity_nodes_visited':visited,
           'morse_integral_boundary':{hex(k):v for k,v in sorted(morse_boundary.items())},
           'mod2_original_boundary_ranks':ranks,'mod2_original_betti':mod2_betti,
           'third_integral_betti':44,'automorphism_group_order':len(perms),
           'conjugacy_class_traces':char,
           'rational_full_quotient_H3_rank':full_fixed//48,
           'rational_rotation_quotient_H3_rank':rotation_fixed//12,
           'irreducible_multiplicities':{str(k):v for k,v in irreps.items()}}
print(json.dumps(summary,sort_keys=True,indent=2))
print('TOROIDAL_C3xC4_MATCHING_INTEGRAL_SYMMETRY_PASS')
