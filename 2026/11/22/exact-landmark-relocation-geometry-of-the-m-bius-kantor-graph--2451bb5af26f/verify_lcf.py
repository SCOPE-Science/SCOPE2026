#!/usr/bin/env python3
"""Independent finite verifier using the LCF [5,-5]^8 graph representation.

Uses distance signatures to classify resolving sets, direct set replacement,
Floyd-Warshall for optimum-placement distances, and backtracking symmetry checks.
Standard library only; no reliance on verify_gp.py.
"""
import itertools
import collections
import json

N=16
neighbors=[set() for i in range(N)]
for v in range(N):
    for w in ((v+1)%N, (v-1)%N, (v+(5 if v%2==0 else -5))%N):
        neighbors[v].add(w)
        neighbors[w].add(v)
assert all(len(s)==3 for s in neighbors)
assert sum(map(len,neighbors))//2 == 24
# Explicit 16-vertex certificate that this LCF encoding is GP(8,3).
lcf_to_gp=(0,1,2,10,13,8,11,3,4,5,6,14,9,12,15,7)
assert sorted(lcf_to_gp)==list(range(N))
gp_edges=set()
for t in range(8):
    for u,v in ((t,(t+1)%8),(t,t+8),(8+t,8+(t+3)%8)):
        gp_edges.add(tuple(sorted((u,v))))
transferred={tuple(sorted((lcf_to_gp[u],lcf_to_gp[v])))
             for u in range(N) for v in neighbors[u] if u<v}
assert transferred==gp_edges and len(gp_edges)==24
INF=1000
D=[[0 if v==w else (1 if w in neighbors[v] else INF) for w in range(N)] for v in range(N)]
for h in range(N):
    for u in range(N):
        for v in range(N):
            D[u][v]=min(D[u][v],D[u][h]+D[h][v])
assert max(x for row in D for x in row)==4

def resolves(B):
    signatures=[tuple(D[v][b] for b in B) for v in range(N)]
    return len(set(signatures))==N
assert all(not resolves(t) for k in range(4) for t in itertools.combinations(range(N),k))
bases=list(t for t in itertools.combinations(range(N),4) if resolves(t))
assert len(bases)==320
index={b:i for i,b in enumerate(bases)}

def prepare(local):
    edges=[]
    for i,b in enumerate(bases):
        ss=set(b)
        for old in b:
            for new in range(N):
                if new in ss or (local and new not in neighbors[old]):
                    continue
                target=tuple(sorted((ss-{old})|{new}))
                j=index.get(target)
                if j is not None and i<j:
                    edges.append((i,j))
    return edges

jump=prepare(False)
slide=prepare(True)
assert len(jump)==1984 and len(slide)==576

def allpairs(edges):
    # Floyd-Warshall, independent of the BFS method.
    n=len(bases)
    mat=[[0 if i==j else 999 for j in range(n)] for i in range(n)]
    for i,j in edges:
        mat[i][j]=mat[j][i]=1
    for k in range(n):
        row_k=mat[k]
        for row_i in mat:
            ik=row_i[k]
            for j in range(n):
                s=ik+row_k[j]
                if s<row_i[j]:row_i[j]=s
    assert all(d<999 for row in mat for d in row)
    return mat

A=allpairs(jump)
B=allpairs(slide)
summary={}
for name, mat, hist, ecc in [
    ('jump',A,{1:1984,2:9888,3:23008,4:16064,5:96},{4:128,5:192}),
    ('slide',B,{1:576,2:1440,3:3072,4:5744,5:7392,6:9192,7:8448,8:7584,9:4512,10:2344,11:576,12:160},{12:320})]:
    got=collections.Counter(mat[i][j] for i in range(320) for j in range(i+1,320))
    got_e=collections.Counter(max(row) for row in mat)
    assert got==hist and got_e==ecc
    summary[name]={'hist':dict(sorted(got.items())),'ecc':dict(sorted(got_e.items()))}

excess=collections.Counter(B[i][j]-A[i][j] for i in range(320) for j in range(i+1,320))
assert excess == {0:4480,1:5856,2:7200,3:10048,4:10152,5:7968,6:3984,7:1216,8:136}

# The order of the automorphism group is verified using an independent
# constraint-propagating backtracker, not a graph-isomorphism package.
aut=[]
mapping={}
used=set()
def recurse():
    if len(mapping)==N:
        aut.append(tuple(mapping[x] for x in range(N)))
        return
    # Choose the unassigned vertex with the most mapped neighbors.
    options=[v for v in range(N) if v not in mapping]
    v=max(options,key=lambda t:(sum(y in mapping for y in neighbors[t]),-t))
    for w in range(N):
        if w in used:continue
        # An isomorphism must respect adjacency AND nonadjacency with mapped vertices.
        if any((u in neighbors[v]) != (mapping[u] in neighbors[w]) for u in mapping):continue
        mapping[v]=w;used.add(w)
        recurse()
        used.remove(w);del mapping[v]
recurse()
assert len(aut)==96
base_set=set(bases)
seen=set();sizes=[];orbit_descriptions=[]
for b in bases:
    if b in seen:continue
    orbit={tuple(sorted(p[v] for v in b)) for p in aut}
    assert orbit <= base_set
    seen.update(orbit)
    sizes.append(len(orbit))
    i=index[b]
    orbit_descriptions.append({'size':len(orbit),'jump_degree':sum(i in e for e in jump),'slide_degree':sum(i in e for e in slide),'jump_ecc':max(A[i]),'slide_ecc':max(B[i])})
assert len(seen)==320
assert sorted(sizes)==[24,24,32,48,96,96]
assert collections.Counter(map(len,neighbors))=={3:16}
print(json.dumps({'graph':'LCF [5,-5]^8','bases':len(bases),'automorphisms':len(aut),
                  'orbits':sorted(orbit_descriptions,key=lambda x:(x['size'],x['slide_degree'])),
                  'jump':summary['jump'],'slide':summary['slide'],'slide_jump_penalty':dict(sorted(excess.items()))},sort_keys=True,separators=(',',':')))
print('VERIFIED_LCF_OK')
