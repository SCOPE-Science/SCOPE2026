"""Exhaustive certificate for single-edge four-colouring dynamics of the Petersen graph.

Run with Python 3.10 or later. No external packages or downloaded data are needed.
The graph is KG(5,2), with 10 sorted two-subsets as vertices and 15
lexicographically sorted disjoint pairs as edges. Named colours are 0,1,2,3.
"""
from collections import Counter
from itertools import combinations

P = list(combinations(range(5), 2))
E = [(i,j) for i,j in combinations(range(10),2) if set(P[i]).isdisjoint(P[j])]
assert len(P)==10 and len(E)==15
incident = [[j for j,(a,b) in enumerate(E) if v in (a,b)] for v in range(10)]
assert all(len(z)==3 for z in incident)

colors=[-1]*15
states=[]
def extend(e):
    if e==15:
        states.append(tuple(colors))
        return
    a,b=E[e]
    forbidden={colors[k] for k in incident[a]+incident[b] if colors[k]>=0}
    for col in range(4):
        if col not in forbidden:
            colors[e]=col
            extend(e+1)
    colors[e]=-1
extend(0)
assert len(states)==49920
index={c:i for i,c in enumerate(states)}
assert len(index)==len(states)

adj=[[] for _ in states]
for i,c in enumerate(states):
    for e,(a,b) in enumerate(E):
        forbidden={c[k] for k in incident[a]+incident[b] if k!=e}
        for d in range(4):
            if d!=c[e] and d not in forbidden:
                changed=list(c)
                changed[e]=d
                adj[i].append(index[tuple(changed)])
assert all(len(row)==len(set(row)) for row in adj)
assert sum(map(len,adj))==218880
assert Counter(map(len,adj))=={0:960,1:1440,2:2880,3:10560,4:8640,5:12960,6:6720,7:5760}

component=[-1]*len(states)
comps=[]
for s in range(len(states)):
    if component[s]>=0:
        continue
    n=len(comps)
    component[s]=n
    q=[s]
    for a in q:
        for b in adj[a]:
            if component[b]<0:
                component[b]=n
                q.append(b)
    comps.append(q)
assert Counter(map(len,comps))=={1:960,24480:2}
large=[i for i,c in enumerate(comps) if len(c)>1]

def perm_sign(p):
    inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    return -1 if inversions%2 else 1

def missing_vertex(c,v):
    return next(i for i in range(4) if all(c[e]!=i for e in incident[v]))

sign=[]
for c in states:
    sig=1
    for v in range(10):
        local=[c[e] for e in incident[v]]+[missing_vertex(c,v)]
        sig*=perm_sign(local)
    sign.append(sig)
assert all(sign[a]==sign[b] for a,neighbors in enumerate(adj) for b in neighbors)
assert {sign[a] for a in comps[large[0]]}!={sign[a] for a in comps[large[1]]}
assert all(len(set(sign[a] for a in comps[i]))==1 for i in large)
assert Counter(sign[a] for a in range(len(states)) if len(adj[a])==0)=={-1:480,1:480}

# Every frozen coloring has exactly one missing-colour class of size four.
# Its four vertices are one of the five stars of KG(5,2), the remaining
# six vertices being split into three edges.
frozen=[i for i,a in enumerate(adj) if not a]
frozen_maps={tuple(missing_vertex(states[i],v) for v in range(10)) for i in frozen}
assert len(frozen_maps)==960
for i in frozen:
    missing=[missing_vertex(states[i],v) for v in range(10)]
    assert sorted(Counter(missing).values())==[2,2,2,4]
    star_col=next(col for col in range(4) if missing.count(col)==4)
    stars=[tuple(j for j,v in enumerate(P) if a in v) for a in range(5)]
    assert tuple(v for v in range(10) if missing[v]==star_col) in stars
    assert all(missing[a]!=missing[b] for a,b in E)

# Generate A5 x S4 from a 3-cycle, a 5-cycle, and colour transpositions.
# Each is a graph automorphism and therefore preserves graph distances.
vertex_index={v:i for i,v in enumerate(P)}
edge_index={e:i for i,e in enumerate(E)}
base_perms=[(1,2,0,3,4),(1,2,3,4,0)]
edge_perms=[]
for p in base_perms:
    vertex_perm=[vertex_index[tuple(sorted(p[t] for t in v))] for v in P]
    edge_perms.append([edge_index[tuple(sorted((vertex_perm[a],vertex_perm[b])))] for a,b in E])
color_perms=[(1,0,2,3),(0,2,1,3),(0,1,3,2)]
seen=bytearray(len(states));orbits=[]
for s in range(len(states)):
    if seen[s]:continue
    seen[s]=1
    q=[s]
    for i in q:
        w=states[i]
        for edge_perm in edge_perms:
            new=[0]*15
            for j,k in enumerate(edge_perm):new[k]=w[j]
            t=index[tuple(new)]
            if not seen[t]:seen[t]=1;q.append(t)
        for p in color_perms:
            t=index[tuple(p[x] for x in w)]
            if not seen[t]:seen[t]=1;q.append(t)
    orbits.append(q)
assert len(orbits)==42
assert Counter(map(len,orbits))=={240:2,480:4,720:6,1440:30}
assert sum(len(q) for q in orbits)==len(states)
assert all((len({component[v] for v in orbit})==1 if adj[orbit[0]] else all(not adj[v] for v in orbit)) for orbit in orbits)

# BFS from one representative per A5 x S4 orbit gives every eccentricity.
# The two large components each have 24480 states.
ecc_counts=Counter()
for orbit in orbits:
    s=orbit[0]
    if len(adj[s])==0:continue
    dist=[-1]*len(states)
    dist[s]=0
    q=[s]
    for a in q:
        for b in adj[a]:
            if dist[b]<0:
                dist[b]=dist[a]+1
                q.append(b)
    assert len(q)==24480
    ecc=max(dist[a] for a in q)
    assert ecc in (24,25)
    ecc_counts[ecc]+=len(orbit)
assert ecc_counts=={24:38880,25:10080}

# A transposition on the five underlying symbols interchanges the parity sectors.
p=(1,0,2,3,4)
vperm=[vertex_index[tuple(sorted(p[t] for t in v))] for v in P]
eperm=[edge_index[tuple(sorted((vperm[a],vperm[b])))] for a,b in E]
for s in [comps[k][0] for k in large]:
    transformed=[0]*15
    for j,k in enumerate(eperm):transformed[k]=states[s][j]
    assert sign[index[tuple(transformed)]]==-sign[s]
print('PASS: 49920 states, 109440 edges, 960 isolated, two 24480-state components')
print('PASS: conserved local permutation sign and exact frozen missing-color census')
print('PASS: 42 symmetry orbits, mobile radius 24, diameter 25')
print('PASS: eccentricity counts 38880 at 24 and 10080 at 25')
