"""Independent finite verifier with LCF graph encoding and bitmask dynamic enumerations.

The LCF presentation [2,6,-2]^4 gives a Hamiltonian 12-cycle plus chords.
This code uses Floyd-Warshall (not base-graph BFS), integer bitmasks (not
combinations of tuples), and all-pairs Floyd-Warshall (not configuration BFS).
"""
import collections
import itertools
import json

N = 12
LCF = [2,6,-2]*4
EDGE = {tuple(sorted((i,(i+1)%N))) for i in range(N)}
EDGE |= {tuple(sorted((i,(i+LCF[i])%N))) for i in range(N)}
assert len(EDGE) == 18
D = [[99]*N for _ in range(N)]
for i in range(N):D[i][i]=0
for u,v in EDGE:D[u][v]=D[v][u]=1
for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
assert max(map(max,D)) == 3

# Prove equivalence with the ordered-edge model by a concrete isomorphism.
P = (0,1,2,9,10,11,8,6,7,4,5,3)  # LCF vertex i -> ordered-edge vertex P[i]
OV = [(a,b) for a in range(4) for b in range(4) if a!=b]
OE = {tuple(sorted((i,j))) for i in range(12) for j in range(i+1,12)
      if OV[i][0]==OV[j][0] or OV[i]==OV[j][::-1]}
assert {tuple(sorted((P[u],P[v]))) for u,v in EDGE} == OE


def count_signatures(mask):
    loc = [i for i in range(N) if mask>>i & 1]
    return len({tuple(D[i][j] for j in loc) for i in range(N)})

MINS = [mask for mask in range(1<<N) if mask.bit_count()<3 and count_signatures(mask)==N]
assert not MINS
BASES = [mask for mask in range(1<<N) if mask.bit_count()==3 and count_signatures(mask)==N]
assert len(BASES)==156
ID = {mask:i for i,mask in enumerate(BASES)}
assert len(ID)==156


def graph_matrix(local):
    n=len(BASES)
    matrix=[[999]*n for _ in range(n)]
    for a in range(n):matrix[a][a]=0
    for i in range(n):
        m=BASES[i]
        for u in range(N):
            if not (m>>u)&1:continue
            for v in range(N):
                if (m>>v)&1:continue
                if local and tuple(sorted((u,v))) not in EDGE:continue
                mm=m^(1<<u)^(1<<v)
                j=ID.get(mm)
                if j is not None:matrix[i][j]=1
    edges=sum(sum(x==1 for x in row) for row in matrix)//2
    for k in range(n):
        for i in range(n):
            dik=matrix[i][k]
            if dik==999:continue
            for j in range(n):
                d=dik+matrix[k][j]
                if d<matrix[i][j]:matrix[i][j]=d
    assert all(x<999 for row in matrix for x in row)
    dist=collections.Counter()
    extra=collections.Counter()
    eccentric=collections.Counter()
    for i in range(n):
        eccentric[max(matrix[i])]+=1
        for j in range(i+1,n):
            d=matrix[i][j]
            lb=3-(BASES[i]&BASES[j]).bit_count()
            assert d>=lb
            dist[d]+=1
            extra[d-lb]+=1
    return edges,dict(sorted(dist.items())),dict(sorted(extra.items())),dict(sorted(eccentric.items()))

j_edges,j_dist,j_extra,j_ecc=graph_matrix(False)
s_edges,s_dist,s_extra,s_ecc=graph_matrix(True)
assert j_edges==1446 and j_dist=={1:1446,2:6000,3:4644}
assert j_extra=={0:12090} and j_ecc=={3:156}
assert s_edges==450 and s_dist=={1:450,2:1356,3:2812,4:3660,5:2964,6:812,7:36}
assert s_extra=={0:2050,1:3708,2:4104,3:2024,4:204}
assert s_ecc=={6:108,7:48}
print(json.dumps(dict(vertices=12,edges=18,metric_dimension=3,basis_count=156,
                      jump_edges=j_edges,jump_distance_hist=j_dist,
                      jump_excess_hist=j_extra,jump_eccentricities=j_ecc,
                      slide_edges=s_edges,slide_distance_hist=s_dist,
                      slide_excess_hist=s_extra,slide_eccentricities=s_ecc,
                      lcf_to_ordered_edge=list(P)),sort_keys=True))
