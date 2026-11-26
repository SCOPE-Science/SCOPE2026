"""Standalone exhaustive checks for the one-descent adjacent-swap graph.

Run: python3 checker.py
No third-party modules or external files are required.
"""
from itertools import permutations
from collections import Counter, deque


def desc(p):
    return sum(a > b for a, b in zip(p, p[1:]))


def mobile_path(n, j):
    """Construct the proposed path for value-boundary j, 1<=j<n."""
    result = []
    for t in range(1, n):
        if t <= j:
            q = list(range(1,t)) + [j+1] + list(range(t,j+1)) + list(range(j+2,n+1))
        else:
            q = list(range(1,j)) + list(range(j+1,t+2)) + [j] + list(range(t+2,n+1))
        result.append(tuple(q))
    return result


def adjacent(n, p):
    for k in range(n-1):
        q=list(p)
        q[k],q[k+1]=q[k+1],q[k]
        if desc(q)==1:
            yield tuple(q)


def run():
    total_pairs=0
    for n in range(3, 10):
        states={p for p in permutations(range(1,n+1)) if desc(p)==1}
        assert len(states)==2**n-n-1,(n,len(states))
        paths=[mobile_path(n,j) for j in range(1,n)]
        paths_union=set(q for path in paths for q in path)
        assert len(paths_union)==(n-1)**2
        assert all(q in states for q in paths_union)
        expected_edges=set()
        for path in paths:
            for a,b in zip(path,path[1:]):
                expected_edges.add(frozenset((a,b)))
        edges=set()
        adjacency={p:list(adjacent(n,p)) for p in states}
        for p,neigh in adjacency.items():
            for q in neigh:
                assert q in states
                edges.add(frozenset((p,q)))
        assert expected_edges==edges,(n,len(expected_edges),len(edges),len(expected_edges^edges))
        isolated=[p for p in states if not adjacency[p]]
        assert len(isolated)==2**n-n*n+n-2
        assert len(edges)==(n-1)*(n-2)
        expected_degree_counts=Counter({0:len(isolated),1:2*(n-1),2:(n-1)*(n-3)})
        assert Counter(map(len,adjacency.values()))==expected_degree_counts
        seen=set(); sizes=[]
        for p in states:
            if p in seen:continue
            q=deque([p]); seen.add(p); component=[]
            while q:
                v=q.popleft(); component.append(v)
                for u in adjacency[v]:
                    if u not in seen:seen.add(u);q.append(u)
            sizes.append(len(component))
        assert Counter(sizes)==Counter({1:len(isolated),n-1:n-1})
        if n<=8:
            for path in paths:
                for t,p in enumerate(path):
                    queue=deque([p]);dist={p:0}
                    while queue:
                        v=queue.popleft()
                        for u in adjacency[v]:
                            if u not in dist:dist[u]=dist[v]+1;queue.append(u)
                    assert len(dist)==n-1
                    assert all(dist[q]==abs(t-s) for s,q in enumerate(path))
                    total_pairs +=len(path)
        print(f'n={n}: vertices={len(states)}, paths={n-1}, isolated={len(isolated)}, edges={len(edges)}, OK')
    for n in [2,3,4,5,10,50,100,500]:
        mobile=(n-1)**2
        total=2**n-n-1
        assert 0<=mobile<=total
    print(f'PASS: exact graph/component/degree/edge agreement for n=3..9; all-pairs distances n=3..8 ({total_pairs} ordered checks)')


if __name__=='__main__':
    run()
