#!/usr/bin/env python3
"""Exact four-cube Hamiltonian-cycle Walsh coefficients through degree three.
Runs an exhaustive anchored depth-first search and a full cube symmetry audit.
No external modules are needed.
"""
from itertools import combinations, permutations
from collections import Counter

N = 16
EDGES = [(u,v) for u in range(N) for v in range(u+1,N) if (u^v).bit_count()==1]
assert len(EDGES)==32
INDEX = {e:i for i,e in enumerate(EDGES)}
ADJ = [[] for _ in range(N)]
for i,(u,v) in enumerate(EDGES):
    ADJ[u].append((v,i)); ADJ[v].append((u,i))

# Each undirected spanning cycle is counted twice, once in each direction.
rooted=[]
def walk(u,visited,edge_mask):
    if visited==(1<<N)-1:
        for v,j in ADJ[u]:
            if v==0: rooted.append(edge_mask | (1<<j))
        return
    for v,j in ADJ[u]:
        if not (visited & (1<<v)):
            walk(v, visited | (1<<v), edge_mask | (1<<j))
walk(0,1,0)
cycles=set(rooted)
assert len(rooted)==2688 and len(cycles)==1344
assert all(rooted.count(c)==2 for c in cycles)

def coeff(inds):
    bitmask=sum(1<<i for i in inds)
    return sum(1-2*((x&bitmask).bit_count()%2) for x in cycles)

STATS={k:Counter() for k in (1,2,3)}
COEFF={k:{} for k in (1,2,3)}
for k in (1,2,3):
    for inds in combinations(range(len(EDGES)),k):
        w=coeff(inds)
        STATS[k][w]+=1
        COEFF[k][inds]=w
assert STATS[1]=={0:32}
assert STATS[2]=={-448:96,-216:48,-56:96,136:192,168:16,176:48}
assert STATS[3]=={-120:64,-56:96,-40:192,-32:384,-24:32,
                  -16:1152,0:1120,16:1152,24:192,32:384,88:192}

# Automorphism group: translations and coordinate permutations.
MAPPINGS=[]
for p in permutations(range(4)):
    for t in range(N):
        def mapped(u):
            return t ^ sum(((u>>j)&1)<<p[j] for j in range(4))
        MAPPINGS.append(tuple(INDEX[tuple(sorted((mapped(u),mapped(v))))] for u,v in EDGES))
assert len(set(MAPPINGS))==384

def get_orbits(k):
    unseen=set(COEFF[k]); out=[]
    while unseen:
        rep=min(unseen)
        orbit={tuple(sorted(g[i] for i in rep)) for g in MAPPINGS}
        assert orbit<=set(COEFF[k])
        assert len({COEFF[k][x] for x in orbit})==1
        unseen.difference_update(orbit)
        out.append((len(orbit),COEFF[k][rep],rep))
    return sorted(out,key=lambda a:(a[1],a[0],a[2]))

pair_orbits=get_orbits(2)
triple_orbits=get_orbits(3)
zero_triples=[z for z in triple_orbits if z[1]==0]
assert len(pair_orbits)==6
assert len(triple_orbits)==24
assert sorted(z[0] for z in zero_triples)==[64,96,192,192,192,384]
assert sum(z[0] for z in zero_triples)==1120
# Every Hamiltonian cycle crosses each vertex cut an even number of
# times. Exhaust all proper vertex sets to identify the minimum cuts.
cut_masks=set()
for u_set in range(1,(1<<N)-1):
    crossing=sum(1<<i for i,(u,v) in enumerate(EDGES)
                 if ((u_set>>u)^(u_set>>v))&1)
    if crossing.bit_count()==4:
        cut_masks.add(crossing)
vertex_stars={sum(1<<i for i,(u,v) in enumerate(EDGES) if x==u or x==v)
              for x in range(N)}
assert len(cut_masks)==16 and cut_masks==vertex_stars
star_forced=set()
for cut in vertex_stars:
    star_edges=[i for i in range(len(EDGES)) if (cut>>i)&1]
    for omitted in star_edges:
        star_forced.add(tuple(sorted(i for i in star_edges if i!=omitted)))
assert len(star_forced)==64
assert all(COEFF[3][S]==0 for S in star_forced)
assert len([S for S,val in COEFF[3].items() if val==0 and S not in star_forced])==1056
print('DFS_PASS cycles=1344 one=32_zero two=0_zero three=1120_zero')
print('MINCUT_PASS edge_connectivity=4 vertex_stars=16 forced_zero_triples=64 other_zero_triples=1056')
print('PAIR_HIST', sorted(STATS[2].items()))
print('TRIPLE_HIST', sorted(STATS[3].items()))
print('PAIR_ORBITS', pair_orbits)
print('ZERO_TRIPLE_ORBITS')
for length,value,rep in zero_triples:
    print('size=',length,'edge_ids=',','.join(map(str,rep)),
          'edges=',','.join(f'{EDGES[i][0]}-{EDGES[i][1]}' for i in rep))
print('FULL_TRIPLE_ORBIT_COUNT',len(triple_orbits))
