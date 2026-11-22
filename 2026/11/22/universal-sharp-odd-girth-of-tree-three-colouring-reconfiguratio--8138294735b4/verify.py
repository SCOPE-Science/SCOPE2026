#!/usr/bin/env python3
"""Exact small-tree checks for odd girth and cycle rank of three-colouring reconfiguration."""
from itertools import product
from collections import deque

def trees(n):
    if n==1:
        yield []
        return
    if n==2:
        yield [(0,1)]
        return
    for pr in product(range(n),repeat=n-2):
        deg=[1]*n
        for u in pr: deg[u]+=1
        edges=[]
        for u in pr:
            v=next(i for i in range(n) if deg[i]==1)
            edges.append((v,u)); deg[v]-=1;deg[u]-=1
        a,b=[i for i in range(n) if deg[i]==1]
        edges.append((a,b))
        yield edges

def run(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    colors=[c for c in product(range(3),repeat=n) if all(c[a]!=c[b] for a,b in edges)]
    ix={c:i for i,c in enumerate(colors)}
    links=[set() for c in colors]
    for i,c in enumerate(colors):
        for v in range(n):
            for newcolor in range(3):
                if newcolor ==c[v] or any(c[u]==newcolor for u in adj[v]):continue
                newc=c[:v]+(newcolor,)+c[v+1:]
                links[i].add(ix[newc])
    # Independently replay the 3n-step legal closed sweep from each coloring.
    for c in colors:
        lift=[None]*n
        lift[0]=c[0]
        queue=deque([0])
        while queue:
            u=queue.popleft()
            for w in adj[u]:
                if lift[w] is not None: continue
                lift[w]=lift[u]+(1 if (c[w]-c[u])%3 == 1 else -1)
                queue.append(w)
        original=lift[:]
        order=sorted(range(n),key=lambda v:-original[v])
        for _ in range(3):
            for v in order:
                lift[v]-=2
                assert all(abs(lift[v]-lift[u])==1 for u in adj[v])
        assert all((lift[v]-original[v])==-6 for v in range(n))
    vnum=len(colors); edgenum=sum(map(len, links))//2
    assert vnum == 3*2**(n-1)
    formula=sum(3*2**(n-1-len(adj[u])) for u in range(n))
    assert edgenum==formula,(n,edgenum,formula)
    visited={0};queue=deque([0])
    while queue:
        x=queue.popleft()
        for y in links[x]:
            if y not in visited: visited.add(y);queue.append(y)
    assert len(visited)==vnum
    # For each start, parity-expanded BFS finds the shortest odd closed walk
    # (its minimum equals the shortest simple odd cycle).
    girth=None
    if n<=6 or n==7:
        for s in range(vnum):
            distances={(s,0):0};queue=deque([(s,0)])
            while queue:
                x,p=queue.popleft()
                for y in links[x]:
                    next_state=(y,1-p)
                    if next_state not in distances:
                        distances[next_state]=distances[(x,p)]+1
                        if y==s and p==0:
                            girth = min(girth,distances[next_state]) if girth is not None else distances[next_state]
                            queue.clear();break
                        queue.append(next_state)
        assert girth == (3*n if n%2 else None),(n,edges,girth)
    return vnum, edgenum, girth

def main():
    count=0
    for n in range(1,6):
        for edges in trees(n):
            run(n,edges)
            count+=1
        print('ALL_LABELED_TREES_PASS',n,'count',n**(n-2) if n>=2 else 1)
    # Some nonisomorphic larger trees: paths, stars, brooms, double stars
    for n in (6,7):
        examples=[[(i,i+1) for i in range(n-1)],[(0,i) for i in range(1,n)],[(0,1),(0,2)]+[(i,i+1) for i in range(2,n-1)],[(0,1),(0,2),(0,3)]+[(3,i) for i in range(4,n)]]
        for edges in examples:
            assert len(edges)==n-1
            run(n,edges)
        print('FOUR_LARGER_TREE_SHAPES_PASS',n)
    print('TOTAL_SMALL_LABELED_TREE_CHECKS_PASS',count)
    print('VERIFY_OK')
if __name__ == '__main__':main()
