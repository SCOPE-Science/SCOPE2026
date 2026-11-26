"""Independent finite certificate, via the 4-dimensional binary symplectic space.

A point is a nonzero vector in F_2^4.  A line is a totally isotropic
2-dimensional subspace, represented by its three nonzero vectors.
This implementation uses bit masks and integer thresholds, not duad syntax.
"""
from collections import Counter, deque
from itertools import combinations


def pairing(x,y):
    bx=lambda q,k:(q>>k)&1
    return (bx(x,0)*bx(y,2) + bx(x,2)*bx(y,0)
          + bx(x,1)*bx(y,3) + bx(x,3)*bx(y,1))%2

P = tuple(range(1,16))
LINE = tuple(sorted({tuple(sorted((x,y,x^y)))
                     for x,y in combinations(P,2) if pairing(x,y)==0}))
assert len(LINE)==15
edge_masks=[0]*30
for j, line in enumerate(LINE):
    for x in line:
        i=x-1
        edge_masks[i] |= 1<<(15+j)
        edge_masks[15+j] |= 1<<i
assert all(m.bit_count()==3 for m in edge_masks)

def bfs(src,block=0):
    d=[-1]*30
    d[src]=0
    q=deque([src])
    while q:
        u=q.popleft()
        unseen=edge_masks[u]&~block
        while unseen:
            lsb=unseen&-unseen
            v=lsb.bit_length()-1
            if d[v]<0:
                d[v]=d[u]+1
                q.append(v)
            unseen-=lsb
    return d

D=tuple(bfs(v) for v in range(30))
assert all(max(row)==4 for row in D)

def feasible_porous(S):
    selected=sum(1<<i for i in S)
    for u in range(30):
        if selected>>u&1:continue
        if sum(1 << (4-D[s][u]) for s in S) < 8:
            return False
    return True

def feasible_blocked(S):
    selected=sum(1<<i for i in S)
    distances=[bfs(s,selected^(1<<s)) for s in S]
    for u in range(30):
        if selected>>u&1:continue
        # Exact common-denominator integral comparison for the paths found.
        vals=[d[u] for d in distances if d[u]!=-1]
        if not vals:return False
        M=max(vals)
        if sum(1 << (M-d+1) for d in vals) < 1 << M:return False
    return True

counts={}
for k in range(1,5):
    good=[S for S in combinations(range(30),k) if feasible_porous(S)]
    counts[k]=len(good)
    if k==4:
        assert len(good)==45
        assert all(feasible_blocked(S) for S in good)
        assert all(sum(s<15 for s in S)==2 for S in good)
        MASKS=[sum(1<<s for s in S) for S in good]
        deg=[0]*45
        dist_counts=Counter()
        neighbors=[[] for _ in range(45)]
        for i,j in combinations(range(45),2):
            z=(MASKS[i]&MASKS[j]).bit_count()
            dist_counts[z]+=1
            if z==1:
                neighbors[i].append(j);neighbors[j].append(i)
                deg[i]+=1;deg[j]+=1
        assert dist_counts==Counter({0:540,1:450})
        assert set(deg)=={20}
        for r in range(45):
            reached={r};fr={r}
            for step in range(2):
                fr=set(v for u in fr for v in neighbors[u])-reached
                reached|=fr
            assert len(reached)==45
assert counts=={1:0,2:0,3:0,4:45}
print('symplectic GQ(2,2) points=15 lines=15 incidence_edges=45')
print('porous_exact_counts',counts)
print('blocked_all_45_feasible=True')
print('three_swap_graph degree=20 diameter=2 edges=450')
