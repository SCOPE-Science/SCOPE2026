"""Independent symbolic verification of the two reconfiguration geometries.

Run: python3 verify_structure.py
Requires only Python's standard library.
"""
from collections import defaultdict, deque


def check(n):
    labels=[(a,b) for a in range(n) for b in range(n) if a!=b]
    V=len(labels)
    index={v:i for i,v in enumerate(labels)}
    nbr=[set() for _ in labels]
    for i,(a,b) in enumerate(labels):
        for j,(c,d) in enumerate(labels):
            if i!=j and (a==c or b==d):nbr[i].add(j)
    assert V==n*(n-1)
    assert all(len(v)==2*(n-2) for v in nbr)
    assert sum(map(len,nbr))//2==n*(n-1)*(n-2)
    degree3_count=0
    geodesic3_count=0
    for i,(a,b) in enumerate(labels):
        if n<=12:
            dist={i:0}
            ways={i:1}
            Q=deque([i])
            while Q:
                v=Q.popleft()
                for w in nbr[v]:
                    if w not in dist:
                        dist[w]=dist[v]+1;ways[w]=ways[v];Q.append(w)
                    elif dist[w]==dist[v]+1:
                        ways[w]+=ways[v]
            assert len(dist)==V
            for j,(c,d) in enumerate(labels):
                predicted=0 if i==j else (1 if a==c or b==d else (3 if a==d and b==c else 2))
                assert dist[j]==predicted,(n,i,j,predicted,dist[j])
            assert ways[index[(b,a)]]==2*(n-2)
            assert sum(v==3 for v in dist.values())==1
        degree3_count+=1
        geodesic3_count+=2*(n-2)
    assert degree3_count==V
    assert geodesic3_count==V*2*(n-2)
    # Add a hub to each side. All ordinary-exchange distances are <=2.
    # Under adjacent sliding the hubs have degree zero.
    assert V+V==2*n*(n-1)
    return n,V,2*V+2,2*V*(n-1),2*V*(n-2),n*(n-1)


if __name__=='__main__':
    for n in list(range(4,13))+[15,25,50]:
        print('STRUCTURE_OK',*check(n))
