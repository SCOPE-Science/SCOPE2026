#!/usr/bin/env python3
"""Exact finite checks for minimum closed dominating walks and automorphism orbits.
Run: python3 check_watchman.py (Python 3.10+, standard library only).
"""
from collections import Counter, defaultdict, deque


def lcf_graph(n, pattern):
    edges = {(min(i, (i+1)%n), max(i, (i+1)%n)) for i in range(n)}
    for i in range(n):
        j = (i + pattern[i%len(pattern)])%n
        assert j!=i
        edges.add((min(i,j),max(i,j)))
    return adjacency(n, edges)


def gp_graph(n,k):
    edges = []
    for i in range(n):
        edges += [(i,(i+1)%n),(i,i+n),(n+i,n+(i+k)%n)]
    return adjacency(2*n,edges)


def adjacency(n, edges):
    sets=[set() for i in range(n)]
    for u,v in edges:
        assert 0<=u<n and 0<=v<n and u!=v
        sets[u].add(v);sets[v].add(u)
    assert all(len(S)==3 for S in sets)
    return tuple(tuple(sorted(S)) for S in sets)


def graphs():
    return {
        'Heawood': lcf_graph(14,[5,-5]),
        'Mobius-Kantor': gp_graph(8,3),
        'Pappus': lcf_graph(18,[5,7,-7,7,-7,-5]),
        'Desargues': gp_graph(10,3),
    }


def closedneighborhoods(adj):
    return [(1<<i)|sum((1<<j) for j in adj[i]) for i in range(len(adj))]


def dynamic_certificate(adj, max_steps):
    n=len(adj); nb=closedneighborhoods(adj); full=(1<<n)-1
    count={}; coverage={}; per_vertex=[]
    for s in range(n):
        states={(s,nb[s]):1}
        sc={}; cv={}
        for d in range(1,max_steps+1):
            new=defaultdict(int)
            for (v,vis),c in states.items():
                for u in adj[v]:new[(u,vis|nb[u])]+=c
            states=new
            if d%2==0:
                val=[(vis,c) for (v,vis),c in states.items() if v==s]
                sc[d]=sum(c for vis,c in val if vis==full)
                cv[d]=max(vis.bit_count() for vis,c in val)
        per_vertex.append(sc)
        for d in sc:
            count[d]=count.get(d,0)+sc[d]
            coverage[d]=max(coverage.get(d,0),cv[d])
    # Vertex-transitivity is independently checked below using automorphisms.
    return count,coverage,per_vertex


def canon(path):
    """A closed walk's dihedral orbit: no distinguished start or direction."""
    a=tuple(path[:-1]);r=a[::-1];n=len(a)
    return min([a[i:]+a[:i] for i in range(n)] +
               [r[i:]+r[:i] for i in range(n)])


def direct_minimum_walks(adj,L):
    n=len(adj); nb=closedneighborhoods(adj);full=(1<<n)-1
    unique=set(); root_count=0
    for s in range(n):
        path=[s]
        def rec(v,vis,depth):
            nonlocal root_count
            if depth==L:
                if v==s and vis==full:
                    root_count+=1
                    unique.add(canon(path))
                return
            for u in adj[v]:
                path.append(u)
                rec(u,vis|nb[u],depth+1)
                path.pop()
        rec(s,nb[s],0)
    return root_count,unique


def distances(adj):
    n=len(adj);out=[]
    for src in range(n):
        ds=[-1]*n;ds[src]=0;q=deque([src])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if ds[w]==-1:ds[w]=ds[v]+1;q.append(w)
        assert all(x>=0 for x in ds)
        out.append(ds)
    return out


def automorphisms(adj):
    n=len(adj); ds=distances(adj); mapping=[-1]*n; found=[]
    def recurse(used, assigned):
        if assigned==n:
            found.append(tuple(mapping));return
        # Choose the next original vertex with the most mapped neighbors;
        # distance constraints provide a second, independent pruning test.
        v=max((v for v in range(n) if mapping[v]==-1),
               key=lambda v:sum(mapping[w]!=-1 for w in adj[v]))
        for w in range(n):
            if (used>>w)&1:continue
            if any(ds[v][u]!=ds[w][mapping[u]] for u in range(n) if mapping[u]!=-1):continue
            mapping[v]=w;recurse(used|(1<<w),assigned+1);mapping[v]=-1
    recurse(0,0)
    for p in found:
        assert {tuple(sorted((p[i],p[j]))) for i in range(n) for j in adj[i] if i<j} == \
               {tuple(sorted((i,j))) for i in range(n) for j in adj[i] if i<j}
    return found


def support_type(path):
    L=len(path)
    edges={tuple(sorted((path[i],path[(i+1)%L]))) for i in range(L)}
    return len(set(path)),len(edges)


def orbit_certificate(walks,perms):
    remaining=set(walks);output=[]
    while remaining:
        path=min(remaining)
        orbit={canon([p[v] for v in path]+[p[path[0]]]) for p in perms}
        assert orbit<=walks
        remaining-=orbit
        output.append({'size':len(orbit),'support':support_type(path),'representative':path})
    return sorted(output,key=lambda x:(x['support'],x['size'],x['representative']))


def main():
    expected={
      'Heawood':(10,10920,546,336,[(42,(6,5)),(84,(8,8)),(168,(8,8)),(168,(8,8)),(84,(10,10))]),
      'Mobius-Kantor':(8,96,6,96,[(6,(8,8))]),
      'Pappus':(12,5400,225,216,[(108,(10,10)),(9,(12,12)),(108,(12,12))]),
      'Desargues':(10,240,12,240,[(12,(10,10))]),
    }
    for name,adj in graphs().items():
        L,N,W,A,types=expected[name]
        cnt,cov,perv=dynamic_certificate(adj,L)
        minL=min(d for d,v in cnt.items() if v>0)
        direct,walks=direct_minimum_walks(adj,L)
        perms=automorphisms(adj)
        orbits=orbit_certificate(walks,perms)
        assert (minL,cnt[L],len(walks),len(perms))==(L,N,W,A)
        assert direct==N
        assert all(v[L]==N//len(adj) for v in perv)
        assert sorted((o['size'],o['support']) for o in orbits)==sorted(types)
        print(name,'vertices',len(adj),'minimum',minL,'rooted',N,'dihedral',W,'automorphisms',A)
        print('max dominated by length:', ' '.join(f'{d}:{cov[d]}' for d in sorted(cov)))
        print('orbits (size, support vertices/edges, representative)')
        for o in orbits:print(o['size'],o['support'],o['representative'])
    print('ALL PASS')

if __name__=='__main__':main()
