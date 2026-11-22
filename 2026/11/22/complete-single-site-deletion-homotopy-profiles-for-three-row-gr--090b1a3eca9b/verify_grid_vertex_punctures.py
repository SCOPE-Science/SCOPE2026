"""Integral homotopy of matching complexes after one grid vertex deletion.
All finite cases (3 by n, 4<=n<=6) and all symmetry orbits.
Standalone, standard library only.
"""
from collections import Counter, defaultdict, deque
import heapq

EXPECTED={
    4:{(0,0):(3,3),(0,1):(3,1),(1,0):(2,1),(1,1):(3,2)},
    5:{(0,0):(4,6),(0,1):(4,4),(0,2):(4,4),(1,0):(4,2),(1,1):(4,4),(1,2):(4,4)},
    6:{(0,0):(5,14),(0,1):(5,9),(0,2):(5,11),(1,0):(5,6),(1,1):(5,11),(1,2):(5,8)}
}

def graph_edges(n,omitted):
    vertices=[(r,c) for r in range(3) for c in range(n) if (r,c)!=omitted]
    return [(u,v) for u in vertices for v in vertices if u<v and abs(u[0]-v[0])+abs(u[1]-v[1])==1]

def enumerate_faces(edges):
    buckets=defaultdict(list)
    def descend(start,mask,occupied,card):
        if card:buckets[card-1].append(mask)
        for j in range(start,len(edges)):
            u,v=edges[j]
            if u not in occupied and v not in occupied:
                descend(j+1,mask|(1<<j),occupied|{u,v},card+1)
    descend(0,0,set(),0)
    return dict(buckets)

def reduction(buckets):
    dimension={f:d for d,faces in buckets.items() for f in faces}
    current=set(dimension)
    lower={f:[f^(1<<k) for k in range(f.bit_length()) if (f>>k)&1] if f.bit_count()>1 else [] for f in current}
    cofaces=defaultdict(list)
    for f,subs in lower.items():
        for s in subs: cofaces[s].append(f)
    remaining={f:len(lower[f]) for f in current}
    ready=[]
    for f,c in remaining.items():
        if c==1:heapq.heappush(ready,(dimension[f],f))
    critical=[];pairs=[]
    def discard(f):
        current.remove(f)
        for g in cofaces[f]:
            if g in current:
                remaining[g]-=1
                if remaining[g]==1:heapq.heappush(ready,(dimension[g],g))
    while current:
        while ready and (ready[0][1] not in current or remaining[ready[0][1]]!=1):heapq.heappop(ready)
        if ready:
            _,upper=heapq.heappop(ready)
            ll=[s for s in lower[upper] if s in current]
            assert len(ll)==1
            down=ll[0]
            pairs.append((down,upper))
            discard(upper);discard(down)
        else:
            cr=min(current,key=lambda x:(dimension[x],x))
            critical.append(cr)
            discard(cr)
    return dimension,lower,critical,pairs

def verify_dag(dimension,lower,pairs):
    matched=set(pairs)
    indegree={f:0 for f in dimension}
    out=defaultdict(list)
    covers=0
    for upper,lows in lower.items():
        for down in lows:
            assert dimension[upper]==dimension[down]+1
            if (down,upper) in matched:
                a,b=down,upper
            else:
                a,b=upper,down
            out[a].append(b); indegree[b]+=1; covers+=1
    que=deque(f for f,d in indegree.items() if d==0)
    count=0
    while que:
        f=que.popleft();count+=1
        for g in out[f]:
            indegree[g]-=1
            if indegree[g]==0:que.append(g)
    assert count==len(dimension),(count,len(dimension))
    return covers

def binary_rank(col):
    pivots={}
    for v in col:
        while v:
            t=v.bit_length()-1
            if t in pivots:v^=pivots[t]
            else:pivots[t]=v;break
    return len(pivots)

def mod2_betti(buckets):
    ranks={}
    for dim in sorted(buckets):
        if dim==0:continue
        row_index={f:j for j,f in enumerate(buckets[dim-1])}
        cols=[]
        for face in buckets[dim]:
            col=0
            for k in range(face.bit_length()):
                if (face>>k)&1: col ^= 1<<row_index[face^(1<<k)]
            cols.append(col)
        ranks[dim]=binary_rank(cols)
    return {dim:len(vals)-ranks.get(dim,0)-ranks.get(dim+1,0)-(1 if dim==0 else 0)
            for dim,vals in buckets.items() if len(vals)-ranks.get(dim,0)-ranks.get(dim+1,0)-(1 if dim==0 else 0)}

def main():
    total_faces=total_covers=total_pairs=0
    for n, profiles in EXPECTED.items():
        for v,(dim,rank) in profiles.items():
            es=graph_edges(n,v); fs=enumerate_faces(es)
            dimensions,lows,critical,pairs=reduction(fs)
            assert len(dimensions)==len(critical)+2*len(pairs)
            assert len(critical)==len(set(critical))
            assert len(pairs)==len(set(pairs))
            assert not (set(critical)&set(x for pair in pairs for x in pair))
            assert Counter(dimensions[x] for x in critical)==Counter({0:1,dim:rank})
            covers=verify_dag(dimensions,lows,pairs)
            assert mod2_betti(fs)=={dim:rank}
            # Exact reduced Euler characteristic, computed independently from all faces
            reduced_euler=-1+sum((-1)**d*len(fs[d]) for d in fs)
            assert reduced_euler==(-1)**dim*rank
            total_faces+=len(dimensions)
            total_covers+=covers
            total_pairs+=len(pairs)
            print(f'n={n} removed={v} edges={len(es)} faces={len(dimensions)} critical=1+{rank}x{dim} pairs={len(pairs)} covers={covers} PASS')
        # every graph vertex is represented by a (row reversal,column reversal) symmetry orbit
        seen={(r,c) for r in range(3) for c in range(n)}
        orbits=[{(r,c),(2-r,c),(r,n-1-c),(2-r,n-1-c)} for (r,c) in profiles]
        assert set.union(*orbits)==seen
        assert sum(map(len,orbits))==len(seen)
    print(f'PASS cases=16 faces={total_faces} covers={total_covers} pairs={total_pairs}')
if __name__=='__main__':main()
