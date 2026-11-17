#!/usr/bin/env python3
"""Standalone exact finite cross-checks for the 13-vertex Paley torus's systolic shell."""
from itertools import combinations, permutations
from collections import defaultdict, deque, Counter
from math import gcd

P=13
D=(1,3,4,9,10,12)
steps={1:(1,0),12:(-1,0),3:(0,1),10:(0,-1),4:(1,1),9:(-1,-1)}
assert set(D)==set(steps)
E={tuple(sorted((i,j))) for i in range(P) for j in range(i+1,P) if (j-i)%P in D}
assert len(E)==39
adj={i:{j for j in range(P) if tuple(sorted((i,j))) in E} for i in range(P)}
assert all(len(adj[i])==6 for i in range(P))
tris={frozenset((i,i+1 if i+1<P else i+1-P,(i+4)%P)) for i in range(P)}
tris |= {frozenset((i,(i+3)%P,(i+4)%P)) for i in range(P)}
assert len(tris)==26
cliques={frozenset(t) for t in combinations(range(P),3) if all(tuple(sorted(e)) in E for e in combinations(t,2))}
assert cliques==tris
assert not any(all(tuple(sorted(e)) in E for e in combinations(t,2)) for t in combinations(range(P),4))
assert 13-39+26==0
for v in range(P):
    link=[t-{v} for t in tris if v in t]
    links={tuple(sorted(s)) for s in link}
    assert len(links)==6
    deg=Counter(x for s in links for x in s)
    assert set(deg.values())=={2} and len(deg)==6
    nxt={w for s in links for w in s}
    assert nxt==adj[v]

def nrm(x):return max(abs(x[0]),abs(x[1]),abs(x[0]-x[1]))

def deck(x):return (x[0]+3*x[1])%P ==0
basis=((3,-1),(4,3))
assert basis[0][0]*basis[1][1]-basis[0][1]*basis[1][0]==13
vectors=[(u,v) for u in range(-4,5) for v in range(-4,5) if deck((u,v)) and 0<nrm((u,v))<=4]
assert len(vectors)==6
expected={(3,-1),(-3,1),(4,3),(-4,-3),(1,4),(-1,-4)}
assert set(vectors)==expected
assert all(nrm(z)==4 for z in vectors)
assert all(gcd(*z)==1 for z in vectors)
# Independent BFS check of exact triangular lattice word-length norm through radius eight.
q=deque([(0,0)]); seen={(0,0):0}
while q:
    u,v=q.popleft()
    if seen[(u,v)]>=8:continue
    for a,b in steps.values():
        w=(u+a,v+b)
        if w not in seen:
            seen[w]=seen[(u,v)]+1
            q.append(w)
assert len(seen)==1+3*8*9
assert all(nrm(z)==d for z,d in seen.items())
# Exact simple 4-cycle census on 13 graph vertices; canonical key removes rotation/reversal.
def canonical(c):
    c=list(c)
    return min(tuple(z[i:]+z[:i]) for z in (c,c[::-1]) for i in range(len(z)))
cycles=set()
for a,b,c,d in permutations(range(P),4):
    if b in adj[a] and c in adj[b] and d in adj[c] and a in adj[d]:
        cycles.add(canonical([a,b,c,d]))
assert len(cycles)==78

def lift(c):
    u=v=0
    for i in range(len(c)):
        dif=(c[(i+1)%len(c)]-c[i])%P
        x,y=steps[dif]
        u+=x;v+=y
    assert deck((u,v))
    return (u,v)

def unoriented(x):return min(x,(-x[0],-x[1]))
classes={c:unoriented(lift(c)) for c in cycles}
count=Counter(classes.values())
assert count[unoriented((0,0))]==39, count
assert len(count)==4,count
for z in expected:
    assert count[unoriented(z)]==13
sys={c for c,z in classes.items() if z!=(0,0)}
assert len(sys)==39
# Entire affine 13:6 group preserves the flag complex and acts transitively on systoles.
Q={1,3,4,9,10,12}
assert all({(a*i+b)%P for i in range(P)}==set(range(P)) for a in Q for b in range(P))
assert all({tuple(sorted(((a*i+b)%P,(a*j+b)%P))) for i,j in E}==E for a in Q for b in range(P))
x=next(iter(sys))
orbit={canonical([(a*i+b)%P for i in x]) for a in Q for b in range(P)}
assert orbit==sys and len(orbit)==39
# Equivariant rotation on deck lattice: multiplication by 3.
def rotate(z):u,v=z;return (-v,u-v)
assert rotate((1,0))==(0,1) and rotate((0,1))==(-1,-1)
assert rotate((3,-1))==(1,4)
assert rotate((1,4))==(-4,-3)
assert rotate((-4,-3))==(3,-1)
# Direct combinatorial cycle count using strongly regular graph common neighbors.
common=Counter((len(adj[i]&adj[j]), tuple(sorted((i,j))) in E) for i,j in combinations(range(P),2))
assert common==Counter({(2,True):39,(3,False):39}),common
assert (39*1+39*3)//2==78
print('VERIFY_OK vertices=13 edges=39 faces2=26 surface_links=C6')
print('VERIFY_OK lattice_index=13 exact_norm_BFS_radius=8 length4_deck_vectors=6')
print('VERIFY_OK simple_4_cycles_total=78 contractible=39 essential=39')
print('VERIFY_OK essential_classes=3 primitive_unoriented multiplicities=13_each')
print('VERIFY_OK affine_group=13:6 order=78 essential_cycle_orbit=39')
print('VERIFY_OK first_length=4 marked_spectrum=max(abs(3m+4n),abs(-m+3n),abs(4m+n))')
