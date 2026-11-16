#!/usr/bin/env python3
"""Exact inclusion-exclusion and S5-orbit certificate for triangle-free graph Walsh convolution."""
import itertools, collections, json, math, pathlib

def build(n):
    edges=list(itertools.combinations(range(n),2))
    triangles=[sum(1<<edges.index(edge) for edge in itertools.combinations(tri,2)) for tri in itertools.combinations(range(n),3)]
    return edges,triangles

def walsh(a):
    a=list(a); h=1; N=len(a)
    while h<N:
        for k in range(0,N,2*h):
            for j in range(k,k+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

E,T=build(5); m=len(E); N=1<<m
# Independent exact inclusion-exclusion over forbidden triangles.
W=[0]*N
for triangle_subset in range(1<<len(T)):
    covered=0
    for j,t in enumerate(T):
        if triangle_subset>>j&1: covered|=t
    sign=(-1 if triangle_subset.bit_count()%2 else 1)
    contribution=sign*(1<<(m-covered.bit_count()))
    sub=covered
    while True:
        W[sub] += (-contribution if sub.bit_count()%2 else contribution)
        if sub==0:break
        sub=(sub-1)&covered
assert W[0]==388
assert sum(v*v for v in W)==N*388
assert sum(v==0 for v in W)==150
assert min(abs(v) for v in W if v)!=0 and min(abs(v) for v in W if v)==2
assert len(set(W))==21
# S5-action on ten edges. Canonical orbit tables are complete.
edge_pos={e:i for i,e in enumerate(E)}
edge_maps=[]
for perm in itertools.permutations(range(5)):
    edge_maps.append([edge_pos[tuple(sorted((perm[u],perm[v])))] for u,v in E])
def reindex(s,emap):
    return sum(1<<emap[i] for i in range(m) if s>>i&1)
remaining=set(range(N)); orbit_table=[]
while remaining:
    rep=min(remaining)
    orbit={reindex(rep,emap) for emap in edge_maps}
    assert orbit<=remaining
    assert all(W[t]==W[rep] for t in orbit)
    remaining-=orbit
    orbit_table.append((rep,len(orbit),W[rep]))
assert len(orbit_table)==34
zero_orbits=[(a,b) for a,b,c in orbit_table if c==0]
assert zero_orbits==[(63,60),(221,60),(255,30)]
assert sum(b for a,b,c in orbit_table)==N
support=[int(v!=0) for v in W]
P=walsh(support)
assert sum(abs(v) for v in P)==7924
assert math.gcd(7924,N)==4
assert collections.Counter(s.bit_count() for s,v in enumerate(W) if v==0)=={6:120,8:30}
# Check 5-vertex triangle-free orbit multiplicities against the independent support table.
outfile=pathlib.Path(__file__).with_name('orbit_table.tsv')
expected=outfile.read_text(encoding='utf-8').strip().splitlines()
actual=['mask_decimal\torbit_size\tWalsh_multiplier']+['%d\t%d\t%d'%(a,b,c) for a,b,c in orbit_table]
assert expected==actual, (len(expected),len(actual))
print('PASS inclusion-exclusion: 1024 coefficients; 34 S5 orbits; zero orbits 60+60+30; P-norm 1981/256; Parseval.')
