#!/usr/bin/env python3
"""Self-contained, standard-library exact checker for three unordered particles on the Petersen graph.
Run with python3 verify.py. All arithmetic integral except separately labeled field checks.
"""
from collections import defaultdict, deque
from itertools import combinations
from math import comb, gcd

# Canonical Petersen: outer pentagon, spokes, inner five-point star.
V0=range(10)
petersen_edges=set()
for i in range(5):
    petersen_edges.add(tuple(sorted((i,(i+1)%5))))
    petersen_edges.add((i,i+5))
    petersen_edges.add(tuple(sorted((i+5,5+(i+2)%5))))
petersen_edges=sorted(petersen_edges)
assert len(petersen_edges)==15 and len(set(petersen_edges))==15
assert all(sum(v in e for e in petersen_edges)==3 for v in V0)
# No triangles or quadrilaterals; the outer pentagon is a cycle.
nei={v:{w for x,y in petersen_edges for w in ([y] if x==v else ([x] if y==v else []))} for v in V0}
assert all(not nei[a].intersection(nei[b]) for a,b in petersen_edges)
assert all(len(nei[a].intersection(nei[b]))<=1 for a,b in combinations(V0,2) if b not in nei[a])

# Subdivide each original edge once. Original vertices are 0,...,9;
# the midpoint of the i-th sorted original edge is 10+i.
N=25
edges=sorted(tuple(sorted(e)) for k,(u,v) in enumerate(petersen_edges)
             for e in [(u,10+k),(v,10+k)])
assert len(edges)==30

# A k-cube is k mutually closure-disjoint open edges and 3-k distinct
# vertices outside the edge endpoints; two cubes use identical k-edge lists.
faces=[[] for _ in range(4)]
ix=[{} for _ in range(4)]
for k in range(4):
    for ee in combinations(range(30),k):
        ends={v for a in ee for v in edges[a]}
        if len(ends)!=2*k:
            continue
        for vv in combinations(sorted(set(range(N))-ends),3-k):
            key=(ee,vv)
            ix[k][key]=len(faces[k]);faces[k].append(key)
C=[len(x) for x in faces]
assert C==[2300,7590,8190,2880],C
print('cubical cells dimensions 0..3:',C)
# Completely separate count: 3 slots are chosen as distinct vertices or
# pairwise closed-disjoint open edges, and edge selections determine dimension.
count2=[]
for k in range(4):
    z=0
    for ee in combinations(range(30),k):
        ends={v for a in ee for v in edges[a]}
        if len(ends)==2*k:
            z+=comb(N-2*k,3-k)
    count2.append(z)
assert C==count2

# Product cubical orientations: increasing edge indices and increasing endpoint
# labels on each interval. The face at lower endpoint has coefficient (-1)^(i+1),
# and at upper endpoint (-1)^i, for 0-based edge-coordinate i.
boundaries=[None]
for k in range(1,4):
    cols=[]
    for ee,vv in faces[k]:
        col=[]
        for i,e in enumerate(ee):
            for t,x in enumerate(edges[e]):
                key=(ee[:i]+ee[i+1:],tuple(sorted(vv+(x,))))
                col.append((ix[k-1][key],(-1)**(i+t+1)))
        assert len({r for r,_ in col})==len(col)
        cols.append(tuple(col))
    boundaries.append(cols)
for k in (2,3):
    for c in boundaries[k]:
        v=defaultdict(int)
        for i,s in c:
            for j,t in boundaries[k-1][i]:v[j]+=s*t
        assert all(not a for a in v.values()),('boundary squared not zero',k)
print('boundary-square tests: PASS')

# Greedy *genuine elementary CW collapses*, not only a Morse rank guess.
# Each pair is chosen from a k-cell with exactly one (k+1)-coface.
co=[[set() for _ in f] for f in faces]
for k in range(1,4):
    for j,col in enumerate(boundaries[k]):
        for i,_ in col:co[k-1][i].add(j)
active=[[True]*c for c in C]
left=C[:]
queue=deque((k,i) for k in (2,1,0) for i in range(C[k]) if len(co[k][i])==1)
pairs=0
while queue:
    k,i=queue.popleft()
    if not active[k][i] or len(co[k][i])!=1:continue
    j=next(iter(co[k][i]))
    assert active[k+1][j]
    # A free k-face and its unique k+1-coface are removed together.
    active[k][i]=active[k+1][j]=False
    left[k]-=1;left[k+1]-=1;pairs+=1
    for a,_ in boundaries[k+1][j]:
        if a==i:continue
        co[k][a].remove(j)
        if len(co[k][a])==1:queue.append((k,a))
    if k>0:
        for a,_ in boundaries[k][i]:
            co[k-1][a].remove(i)
            if len(co[k-1][a])==1:queue.append((k-1,a))
assert left==[1297,3210,1933,0],left
assert pairs==7260 and 2*pairs+sum(left)==sum(C)
for k in (1,2,3):
    for j,col in enumerate(boundaries[k]):
        if active[k][j]:assert all(active[k-1][i] for i,_ in col)
print('elementary collapse pairs:',pairs,'remaining CW cells:',left)

# Connected 1-skeleton, choose spanning tree. Contracting the embedded tree
# is a homotopy equivalence for a connected CW complex. In the quotient,
# each tree edge is zero and each non-tree edge a loop.
parent=list(range(C[0]))
def root(i):
    while i!=parent[i]:parent[i]=parent[parent[i]];i=parent[i]
    return i
edge_ids=[];T=set()
for i,a in enumerate(active[1]):
    if not a:continue
    u,v=[x for x,s in boundaries[1][i]]
    assert active[0][u] and active[0][v]
    edge_ids.append(i)
    x,y=root(u),root(v)
    if x!=y:parent[x]=y;T.add(i)
assert len(T)==left[0]-1
loop_ids=[e for e in edge_ids if e not in T]
assert len(loop_ids)==1914
loop_idx={e:i for i,e in enumerate(loop_ids)}
cols={};rows={i:{} for i in range(len(loop_ids))}
ct=0
for j,a in enumerate(active[2]):
    if not a:continue
    d={loop_idx[e]:s for e,s in boundaries[2][j] if e in loop_idx}
    assert all(abs(s)==1 for s in d.values())
    cols[ct]=d
    for r,v in d.items():rows[r][ct]=v
    ct+=1
assert ct==1933
assert sum(map(len,cols.values()))==4605
print('spanning tree edges:',len(T),'quotient boundary rows/cols: 1914/1933; entries:',4605)

# Integer Smith reduction using only elementary unimodular row/column
# operations at units. At a unit at (r,c), replace rows i by
# row_i - (a_ic/a_rc)*row_r, then clear pivot row by column operations.
# This isolates a diagonal unit and leaves its cokernel/kernel unchanged.
# Sparse bidirectional maps keep the exact *integer* Schur complement.
units=0
while True:
    pivot=None
    for c,col in cols.items():
        if len(col)==1:
            r,s=next(iter(col.items()))
            if abs(s)==1:pivot=(r,c,s);break
    if pivot is None:
        for r,row in rows.items():
            if len(row)==1:
                c,s=next(iter(row.items()))
                if abs(s)==1:pivot=(r,c,s);break
    if pivot is None:
        best=10**10
        for c,col in cols.items():
            for r,s in col.items():
                if abs(s)==1:
                    score=(len(rows[r])-1)*(len(col)-1)
                    if score<best:best=score;pivot=(r,c,s)
    if pivot is None:break
    r,c,s=pivot
    col=cols[c].copy();row=rows[r].copy()
    for i,v in col.items():
        if i==r:continue
        for j,w in row.items():
            if j==c:continue
            new=rows[i].get(j,0)-v*w*s
            if new:
                rows[i][j]=new;cols[j][i]=new
            else:
                rows[i].pop(j,None);cols[j].pop(i,None)
    for i in col:
        if i!=r:rows[i].pop(c,None)
    for j in row:
        if j!=c:cols[j].pop(r,None)
    del rows[r];del cols[c]
    units+=1
assert units==1907,units
assert len(rows)==7 and len(cols)==26
assert all(cols[c].get(r)==a for r,row in rows.items() for c,a in row.items())
assert all(rows[r].get(c)==a for c,col in cols.items() for r,a in col.items())
remaining=[(r,c,a) for r,row in rows.items() for c,a in row.items()]
assert len({r for r,c,a in remaining})==1
assert len(remaining)==8 and all(abs(a)==2 for r,c,a in remaining)
assert len({c for r,c,a in remaining})==8
assert gcd(*(abs(a) for r,c,a in remaining))==2
print('integral boundary Smith nonzeros: 1 repeated',units,'times, then 2 once')
print('terminal residual: 7 rows, 26 columns, 8 nonzero coefficients, all +/-2 in one row')
assert len(loop_ids)-(units+1)==6
assert ct-(units+1)==25
assert sum(((-1)**k)*C[k] for k in range(4))==20
assert 1-6+25==20
print('H0=Z; H1=Z^6 + Z/2; H2=Z^25; higher homology zero')
print('ALL_CHECKS_PASS')
