"""Reproducible exact mod-two homology of a graph-metric Cech nerve.
Witnesses are all metric-graph vertices and edge midpoints; scale is 4.
"""
from collections import deque
from itertools import combinations


def graph():
    n=10
    arms=((0,1,2,3),(3,4,5,6,0),(3,7,8,9,0))
    edges=sorted(set(tuple(sorted((u,v))) for arm in arms for u,v in zip(arm,arm[1:])))
    return n,edges


def nerve(n,edges,scale=4):
    assert scale==4
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    dist=[]
    for v in range(n):
        row=[n+1]*n;row[v]=0;q=deque([v])
        while q:
            u=q.popleft()
            for w in adj[u]:
                if row[w]>row[u]+1:row[w]=row[u]+1;q.append(w)
        dist.append(row)
    witnesses=[]
    for w in range(n):
        witnesses.append(sum(1<<v for v in range(n) if 2*dist[v][w]<=scale))
    for u,w in edges:
        witnesses.append(sum(1<<v for v in range(n) if 2*min(dist[v][u],dist[v][w])+1<=scale))
    # The distance from a vertex to a point of an edge is min(d(v,u)+t,d(v,w)+1-t).
    # At radius two, maximal witness sets occur at vertices or edge midpoints.
    # Thus these maximal sets generate the full nerve.
    return sorted({s for s in witnesses if not any(s!=t and s&t==s for t in witnesses)})


def faces(facets):
    ans=set()
    for facet in facets:
        sub=facet
        while sub:
            ans.add(sub)
            sub=(sub-1)&facet
    return {k:sorted(f for f in ans if f.bit_count()==k+1) for k in range(max(x.bit_count() for x in ans))}


def rank(columns):
    pivots={}
    for word in columns:
        while word:
            i=word.bit_length()-1
            if i in pivots:word^=pivots[i]
            else:pivots[i]=word;break
    return len(pivots)


def betti(face_map):
    r=[]
    for dim in range(1,len(face_map)):
        lower={s:i for i,s in enumerate(face_map[dim-1])}
        cols=[]
        for s in face_map[dim]:
            bd=0
            for v in range(s.bit_length()):
                if s>>v&1:bd^=1<<lower[s^(1<<v)]
            cols.append(bd)
        rank_cols=rank(cols)
        # Independent rank by pivoting the transposed binary matrix.
        rows=[]
        for i in range(len(lower)):
            row=sum(1<<j for j,col in enumerate(cols) if col>>i&1)
            rows.append(row)
        assert rank_cols==rank(rows), (dim,rank_cols,rank(rows))
        r.append(rank_cols)
    ranks=[0]+r+[0]
    b={i:len(fs)-ranks[i]-ranks[i+1] for i,fs in face_map.items()}
    b[0]-=1
    return {i:v for i,v in b.items() if v},r


def cycle(m,mapping):
    n=10
    edges=[tuple(sorted((mapping[i],mapping[(i+1)%m]))) for i in range(m)]
    local_edges=[tuple(sorted((i,(i+1)%m))) for i in range(m)]
    fs=nerve(m,local_edges)
    return {sum(1<<mapping[v] for v in range(m) if f>>v&1) for f in fs}


def main():
    n,edges=graph()
    assert len(edges)==11
    facets=nerve(n,edges)
    f=faces(facets)
    b,r=betti(f)
    print('theta graph:',n,'vertices,',len(edges),'edges')
    print('facets:',[list(i for i in range(n) if a>>i&1) for a in facets])
    print('face numbers:',[len(f[i]) for i in sorted(f)])
    print('boundary ranks:',r)
    print('reduced mod-2 Betti:',b)
    assert [len(f[i]) for i in sorted(f)]==[10,45,114,134,74,20,2]
    assert r==[9,36,76,56,18,2]
    assert b=={2:2,3:2}
    ca=cycle(7,tuple(range(7)))
    cb=cycle(7,(0,1,2,3,7,8,9))
    wedge=faces(ca|cb)
    bw,rw=betti(wedge)
    print('union of intrinsic cycle nerves:',bw)
    assert bw=={3:2}
    for facet in ca|cb:
        assert any(facet&big==facet for big in facets), 'component nerve not a subcomplex'
    print('comparison: two new independent degree-two classes in the theta nerve')
    print('PASS')
if __name__=='__main__':main()
