"""Check the explicit power-domination sensor-slide / Johnson-subdivision map."""
from itertools import combinations
from collections import deque, Counter

def all_minimum(n):
    all_labels=set(range(n))
    nodes={}
    for u,v in combinations(range(n),2):
        key=('pair',(u,v))
        sensors=frozenset(all_labels-{u,v})
        nodes[key]=sensors
    for i,j,k in combinations(range(n),3):
        triple={i,j,k}
        for a,b in combinations((i,j,k),2):
            h=next(iter(triple-{a,b}))
            key=('edge',(tuple(sorted((a,h))),tuple(sorted((b,h)))))
            key=('edge',tuple(sorted(key[1])))
            sensor=('w',a,b)
            nodes[key]=frozenset(all_labels-triple)|{sensor}
    assert len(nodes)==n*(n-1)**2//2
    return nodes

def check(n):
    nodes=all_minimum(n)
    labels=list(nodes)
    edges=set()
    for i,j in combinations(range(n),2):
        edges.add(frozenset((i,('w',i,j))))
        edges.add(frozenset((j,('w',i,j))))
    computed=set()
    for a,b in combinations(labels,2):
        A=nodes[a];B=nodes[b]
        if len(A-B)==len(B-A)==1:
            u=next(iter(A-B));v=next(iter(B-A))
            if frozenset((u,v)) in edges:
                computed.add(frozenset((a,b)))
    expected={frozenset((('pair',p),('edge',e))) for kind,e in labels if kind=='edge' for p in e}
    assert expected==computed,(n, expected-computed,computed-expected)
    graph={k:[] for k in nodes}
    for a,b in expected:graph[a].append(b);graph[b].append(a)
    degrees=Counter(map(len,graph.values()))
    diameter=0
    for a in graph:
        dist={a:0};dq=deque([a])
        while dq:
            v=dq.popleft()
            for w in graph[v]:
                if w not in dist:
                    dist[w]=dist[v]+1;dq.append(w)
        assert len(dist)==len(graph)
        diameter=max(diameter,max(dist.values()))
    assert diameter==min(n,6)
    assert degrees[2]==3*__import__('math').comb(n,3)+( __import__('math').comb(n,2) if n==3 else 0)
    print('n=',n,'vertices=',len(nodes),'edges=',len(expected),'diameter=',diameter,'degrees=',dict(degrees))
for n in range(3,9):check(n)
print('SLIDES_OK')
