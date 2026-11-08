#!/usr/bin/env python3
"""Independent exact verification of four-colour recolouring distances on M(C5).

Only Python standard library. States use (v0,...,v4,u0,...,u4,w),
colours 0,1,2,3, and a move recolours one vertex.
"""
from collections import Counter, deque, defaultdict
from itertools import permutations, product

K = 4
adj = [set() for _ in range(11)]
def edge(i, j):
    adj[i].add(j); adj[j].add(i)
for i in range(5):
    edge(i, (i + 1) % 5)
    edge(5+i, (i-1) % 5)
    edge(5+i, (i+1) % 5)
    edge(5+i, 10)

# Construct from pentagon assignments and the apex, selecting shadows independently.
states=[]
for vs in product(range(K),repeat=5):
    if any(vs[i]==vs[(i+1)%5] for i in range(5)):
        continue
    for apex in range(K):
        shadow_choices=[tuple(c for c in range(K) if c not in
                             (apex,vs[(i-1)%5],vs[(i+1)%5])) for i in range(5)]
        for us in product(*shadow_choices):
            states.append(vs+us+(apex,))
assert len(states)==12480 and len(set(states))==12480
index={s:i for i,s in enumerate(states)}
assert all(s[i]!=s[j] for s in states for i in range(11) for j in adj[i])
# Independently generate edges from the colours absent from each closed neighbourhood.
neighbors=[]
for s in states:
    targets=[]
    for v in range(11):
        forbidden={s[v]} | {s[u] for u in adj[v]}
        for c in range(K):
            if c not in forbidden:
                targets.append(index[s[:v]+(c,)+s[v+1:]])
    neighbors.append(targets)
assert sum(map(len,neighbors))==2*45240
assert all(i in neighbors[j] for i,row in enumerate(neighbors) for j in row)

# Complete components, without assuming any symmetry.
components=[-1]*len(states); sizes=[]
for i in range(len(states)):
    if components[i]>=0: continue
    cid=len(sizes); q=deque([i]);components[i]=cid;size=0
    while q:
        x=q.popleft();size+=1
        for y in neighbors[x]:
            if components[y]<0:components[y]=cid;q.append(y)
    sizes.append(size)
assert sizes==[6240,6240]

# Full action S4 x D5; each acts by genuine graph automorphisms.
color_perms=list(permutations(range(K)))
def transform(s,cp,sign,shift):
    t=[0]*11;t[10]=cp[s[10]]
    for i in range(5):
        j=(sign*i+shift)%5
        t[j]=cp[s[i]]
        t[j+5]=cp[s[i+5]]
    return tuple(t)
visited=set();orbits=[]
for i,s in enumerate(states):
    if i in visited:continue
    orb={index[transform(s,cp,sign,shift)] for cp in color_perms
         for sign in (-1,1) for shift in range(5)}
    assert i in orb and len(orb) in (120,240)
    assert not (orb & visited)
    visited.update(orb);orbits.append(orb)
assert len(visited)==len(states) and len(orbits)==56

def breadth_first(start,parents=False):
    ds=[-1]*len(states);ds[start]=0;q=deque([start]);prev={}
    while q:
        x=q.popleft()
        for y in neighbors[x]:
            if ds[y]<0:
                ds[y]=ds[x]+1;q.append(y)
                if parents:prev[y]=x
    return ds,prev

# Reconstruct all eccentricities and unordered-pair counts from orbit representatives.
ecc_count=Counter();pair_count=Counter();extreme_orbits=[]
for orb in orbits:
    root=next(iter(orb));ds,_=breadth_first(root)
    hist=Counter(d for d in ds if d>=0)
    eccentricity=max(hist)
    ecc_count[eccentricity]+=len(orb)
    for d,ct in hist.items():
        if d: pair_count[d]+=len(orb)*ct
    if eccentricity==17:
        assert hist[17]==1
        extreme_orbits.append(orb)
for d in pair_count:
    assert pair_count[d]%2==0
    pair_count[d]//=2
assert ecc_count=={15:2160,16:10200,17:120}
assert len(extreme_orbits)==1 and len(extreme_orbits[0])==120
assert pair_count[17]==60
assert sum(pair_count.values())==2*(6240*6239//2)
assert pair_count=={
 1:45240, 2:164280, 3:409080, 4:807600, 5:1371600,
 6:2103600, 7:2978040, 8:3904800, 9:4766640,
 10:5471760,11:5871600,12:5428440,13:3680400,
 14:1552080,15:346200,16:29940,17:60}

# Named extremal pair and a shortest transformation witness.
start=(3,2,0,3,2,3,1,1,1,2,0)
finish=(2,3,1,2,3,2,0,0,0,3,1)
a=index[start];b=index[finish];ds,prev=breadth_first(a,True)
assert ds[b]==17 and sum(d==17 for d in ds)==1
path=[];p=b
while p!=a:path.append(p);p=prev[p]
path.append(a);path.reverse()
moves=[]
for x,y in zip(path,path[1:]):
    changes=[v for v in range(11) if states[x][v]!=states[y][v]]
    assert len(changes)==1 and y in neighbors[x]
    v=changes[0]; moves.append((v,states[y][v]))
assert len(moves)==17
print('PYTHON_INDEPENDENT_PASS')
print('states',len(states),'edges',sum(map(len,neighbors))//2,'components',sizes)
print('symmetry_orbits',len(orbits),'eccentricity_counts',sorted(ecc_count.items()))
print('pair_distance_counts',sorted(pair_count.items()))
print('unique_antipode_orbit_size',len(extreme_orbits[0]))
print('extremal_pair',start,finish,'distance',ds[b])
print('witness_moves_vertex_new_colour',moves)
