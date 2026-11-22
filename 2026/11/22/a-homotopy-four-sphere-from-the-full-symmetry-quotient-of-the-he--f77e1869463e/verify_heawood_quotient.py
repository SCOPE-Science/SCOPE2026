"""Rebuild the Heawood ordinary matching quotient and its integral cellular chain complex.

Python 3, standard library only. Every finite object is enumerated from the
seven nonzero vectors of F_2^3. No precomputed chain matrix is imported.
"""
from itertools import product
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

V = tuple(range(1, 8))
def dot(a, b):
    return (a & b).bit_count() % 2

# A point p and line a are incident when their standard scalar product is 0.
E = tuple(sorted((p, a) for p in V for a in V if dot(p, a) == 0))
assert len(E) == 21
Eidx = {e:i for i,e in enumerate(E)}
G0 = []
for col in product(V, repeat=3):
    def lin(x):
        return (col[0] if x & 1 else 0) ^ (col[1] if x & 2 else 0) ^ (col[2] if x & 4 else 0)
    if len({lin(x) for x in V}) != 7:
        continue
    def dual(a):
        return next(b for b in V if all(dot(a,x) == dot(b,lin(x)) for x in V))
    G0.append(tuple(Eidx[lin(p),dual(a)] for p,a in E))
assert len(G0) == 168
G = G0 + [tuple(Eidx[E[perm[i]][1], E[perm[i]][0]] for i in range(21)) for perm in G0]
assert len(G) == len(set(G)) == 336
identity = tuple(range(21))
assert identity in G

compat = [0] * 21
for i, (p,a) in enumerate(E):
    for j, (q,b) in enumerate(E):
        if p != q and a != b:
            compat[i] |= 1<<j

faces=[]
def enumerate_matchings(mask,candidate):
    if mask:
        faces.append(mask)
    while candidate:
        bit = candidate & -candidate
        candidate -= bit
        i = bit.bit_length()-1
        enumerate_matchings(mask|bit, candidate & compat[i])
enumerate_matchings(0,(1<<21)-1)
faces.sort(key=lambda m:(m.bit_count(),m))
assert Counter(m.bit_count()-1 for m in faces) == dict(enumerate((21,168,644,1218,1050,336,24)))

@lru_cache(maxsize=None)
def image(mask, g):
    p = G[g]
    out=0
    while mask:
        bit=mask & -mask
        mask-=bit
        out |= 1<<p[bit.bit_length()-1]
    return out

canon={}
reps=[]
for m in faces:
    if m not in canon:
        orb={image(m,g) for g in range(336)}
        reps.append(m)
        for f in orb:
            canon[f]=m
assert len(canon)==len(faces) and len(reps)==29
stabs={r:[G[g] for g in range(336) if image(r,g)==r] for r in reps}
map_to_rep={}
for m in faces:
    if m == canon[m]:
        map_to_rep[m]=identity
    else:
        map_to_rep[m]=G[next(g for g in range(336) if image(m,g)==canon[m])]

def translate(blocks,p):
    result=[]
    for mask in blocks:
        out=0
        while mask:
            bit=mask & -mask
            mask-=bit
            out |= 1<<p[bit.bit_length()-1]
        result.append(out)
    return tuple(result)

def partitions(items):
    """Every ordered partition of items exactly once, as nonempty bit-mask blocks."""
    if not items:
        yield ()
        return
    first=1<<items[0]
    for part in partitions(items[1:]):
        for k in range(len(part)+1):
            yield part[:k]+(first,)+part[k:]
        for k in range(len(part)):
            yield part[:k]+(part[k]|first,)+part[k+1:]

cells=defaultdict(list)
lookup={}
for rep in reps:
    items=tuple(i for i in range(21) if rep>>i & 1)
    seen=set()
    for blocks in partitions(items):
        if blocks in seen:
            continue
        orbit={translate(blocks,g) for g in stabs[rep]}
        seen.update(orbit)
        representative=min(orbit)
        d=len(blocks)-1
        assert representative not in lookup
        lookup[representative]=len(cells[d])
        cells[d].append(representative)
assert tuple(len(cells[d]) for d in range(7)) == (29,311,1400,3051,3375,1800,360)

def canonical_flag(blocks):
    m=0
    for b in blocks:
        m |= b
    rep=canon[m]
    aligned=translate(blocks,map_to_rep[m])
    return min(translate(aligned,g) for g in stabs[rep])

# The quotient of barycentric subdivision is a genuine delta-complex: group
# automorphisms preserve all ranks in a flag, hence act without inversions.
# The alternating face-deletion boundary is therefore integral and exact.
B={}
for d in range(1,7):
    columns=[]
    for block in cells[d]:
        col={}
        for j in range(d+1):
            if j < d:
                deleted=block[:j]+(block[j]|block[j+1],)+block[j+2:]
            else:
                deleted=block[:d]
            i=lookup[canonical_flag(deleted)]
            col[i]=col.get(i,0)+(-1)**j
        columns.append({i:a for i,a in col.items() if a})
    B[d]=columns
for d in range(2,7):
    for col in B[d]:
        bd=defaultdict(int)
        for j,a in col.items():
            for i,b in B[d-1][j].items():
                bd[i] += a*b
        assert all(a==0 for a in bd.values())
assert Counter(sum(len(col) for col in B[d]) for d in range(1,7)) == Counter((622,4200,12204,16875,10800,2520))

# Sparse unimodular cancellations: at a unit pivot, eliminate its row in all
# other columns of the same matrix. Delete the paired column/row in adjacent
# matrices as forced by d^2=0. Every operation uses integer elementary basis
# changes, so Smith invariants and integral homology are preserved.
cols={d:{j:dict(c) for j,c in enumerate(B[d])} for d in range(1,7)}
rows={d:defaultdict(dict) for d in range(1,7)}
for d,C in cols.items():
    for c,entry in C.items():
        for r,v in entry.items():
            rows[d][r][c]=v
active={d:set(range(len(cells[d]))) for d in range(7)}
steps={}
for d in range(1,7):
    heap=[]
    nonce=0
    def queue(r,c):
        nonlocal_dummy = None
        if c not in cols[d] or r not in rows[d]:
            return
        if cols[d][c].get(r) not in (-1,1):
            return
        cost=(len(rows[d][r])-1)*(len(cols[d][c])-1)
        return cost
    for r,neighbours in rows[d].items():
        for c,v in neighbours.items():
            if abs(v)==1:
                nonce+=1
                heapq.heappush(heap,(queue(r,c),nonce,r,c))
    done=0
    while heap:
        cost,_,r,c=heapq.heappop(heap)
        if r not in rows[d] or c not in cols[d]:
            continue
        v=cols[d][c].get(r)
        if v not in (-1,1):
            continue
        newcost=(len(rows[d][r])-1)*(len(cols[d][c])-1)
        if newcost>cost:
            nonce+=1
            heapq.heappush(heap,(newcost,nonce,r,c))
            continue
        pivotcol=cols[d][c]
        pivotrow=rows[d][r]
        changes=set()
        for j,vrj in list(pivotrow.items()):
            if j == c:
                continue
            fac=-vrj//v
            assert fac*v == -vrj
            for i,vic in pivotcol.items():
                old=cols[d][j].get(i,0)
                new=old+fac*vic
                if new:
                    cols[d][j][i]=new
                    rows[d][i][j]=new
                else:
                    cols[d][j].pop(i,None)
                    rows[d][i].pop(j,None)
                changes.add(i)
        for i in pivotcol:
            rows[d][i].pop(c,None)
            changes.add(i)
            if not rows[d][i]:
                rows[d].pop(i,None)
        cols[d].pop(c)
        rows[d].pop(r,None)
        active[d].remove(c)
        active[d-1].remove(r)
        if d>1:
            old=cols[d-1].pop(r)
            for i in old:
                rows[d-1][i].pop(r,None)
                if not rows[d-1][i]:
                    rows[d-1].pop(i,None)
        if d<6:
            old=rows[d+1].pop(c,{})
            for j in old:
                cols[d+1][j].pop(c,None)
        for i in changes:
            if i in rows[d]:
                for j,w in rows[d][i].items():
                    if w in (-1,1):
                        nonce+=1
                        co=(len(rows[d][i])-1)*(len(cols[d][j])-1)
                        heapq.heappush(heap,(co,nonce,i,j))
        done += 1
    steps[d]=done
    # Verify the new reduced integral boundaries still form a chain complex.
    for q in range(2,7):
        if q not in cols or q-1 not in cols:
            continue
        for entry in cols[q].values():
            result=defaultdict(int)
            for j,a in entry.items():
                if j not in cols[q-1]:
                    continue
                for i,b in cols[q-1][j].items():
                    result[i]+=a*b
            assert all(x==0 for x in result.values())
assert tuple(len(active[d]) for d in range(7)) == (1,0,0,0,1,0,0)
assert all(not any(c.values()) for C in cols.values() for c in C.values())
assert sum(steps.values()) == (sum(map(len,cells.values()))-2)//2

# Separately prove original matching complex simply connected: its 1-skeleton
# has 21 vertices, 168 edges, and the 644 triangles give relators. A spanning
# tree kills 20 edges. Iterated single-generator triangular relators kill all
# remaining 148 generators, so no nontrivial pi_1 survives.
pairs=[];triples=[]
for f in faces:
    if f.bit_count() in (2,3):
        vertices=tuple(i for i in range(21) if f>>i&1)
        (pairs if len(vertices)==2 else triples).append(vertices)
adj={i:set() for i in range(21)}
for i,j in pairs:
    adj[i].add(j);adj[j].add(i)
parent={0:0};todo=deque((0,));tree=set()
while todo:
    i=todo.popleft()
    for j in sorted(adj[i]):
        if j not in parent:
            parent[j]=i;todo.append(j)
            tree.add((min(i,j),max(i,j)))
assert len(parent)==21
variables={e:k for k,e in enumerate(sorted(set(pairs)-tree))}
assert len(variables)==148
relations=[]
for a,b,c in triples:
    relations.append({variables[e] for e in ((a,b),(a,c),(b,c)) if e in variables})
alive=set(range(148));waves=[]
while True:
    killed={next(iter(r & alive)) for r in relations if len(r & alive)==1}
    if not killed:
        break
    alive-=killed
    waves.append(len(killed))
assert not alive

# All 336 symmetry elements are generated by stabilizers of the 21 matching
# vertices (individual graph incidences): a directly reproducible Armstrong
# normal-generation test. Since the original matching complex is simply
# connected, Armstrong's orbit pi_1 theorem gives quotient pi_1=1.
fixers={g for g in G if any(g[i]==i for i in range(21))}
def compose(p,q):
    return tuple(p[q[i]] for i in range(21))
subgroup={identity};todo=deque([identity])
while todo:
    h=todo.popleft()
    for g in fixers:
        p=compose(g,h)
        if p not in subgroup:
            subgroup.add(p);todo.append(p)
assert len(subgroup)==336
print('FACES',tuple(sum(f.bit_count()==d+1 for f in faces) for d in range(7)))
print('QUOTIENT_CELLS',tuple(len(cells[d]) for d in range(7)))
print('UNIT_PIVOTS',tuple(steps[d] for d in range(1,7)))
print('PI1_PRESENTATION_WAVES',tuple(waves))
print('FIXER_GENERATED_SYMMETRIES',len(subgroup))
print('HEAWOOD_MATCHING_FULL_AUT_QUOTIENT_S4_OK')
