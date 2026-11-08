"""Finite checks of the component-cycle budget for progressive adoption.

Python 3 standard library only.  Run: python verify.py
The proof in RESULT.md handles arbitrary finite graphs; these checks are finite tests.
"""
from itertools import product
from random import Random


def subgraph_invariants(n, edges, mask):
    vertices = [v for v in range(n) if mask >> v & 1]
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    count = 0
    for u, v in edges:
        if (mask >> u & 1) and (mask >> v & 1):
            count += 1
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
    c = len({find(v) for v in vertices})
    return c, count-len(vertices)+c


def closure(n, edges, thresholds, seeds):
    nbr = [0]*n
    for u, v in edges:
        nbr[u] |= 1 << v
        nbr[v] |= 1 << u
    active = seeds
    while True:
        new = active
        for v in range(n):
            if not (active >> v & 1) and (nbr[v] & active).bit_count() >= thresholds[v]:
                new |= 1 << v
        if new == active:
            return active
        active = new


def connected(n, edges):
    return closure(n, edges, [1]*n, 1) == (1 << n)-1


def check(n, edges, tau, seeds):
    final = closure(n, edges, tau, seeds)
    c_s, b_s = subgraph_invariants(n, edges, seeds)
    c_f, b_f = subgraph_invariants(n, edges, final)
    cost = sum(tau[v]-1 for v in range(n) if (final >> v & 1) and not (seeds >> v & 1))
    assert cost <= c_s-c_f+b_f-b_s, (n, edges, tau, seeds, final, cost)
    c_g,b_g = subgraph_invariants(n,edges,(1<<n)-1)
    assert cost <= seeds.bit_count()-1+b_g
    return final


def all_terminal_states(n, edges, tau, seeds):
    """Exhaust all asynchronous legal activation orders, independently of closure()."""
    nbr = [0]*n
    for u,v in edges:
        nbr[u] |= 1<<v; nbr[v] |= 1<<u
    todo=[seeds]; seen={seeds}; terminal=set()
    while todo:
        x=todo.pop()
        enabled=[v for v in range(n) if not (x>>v&1) and (x&nbr[v]).bit_count()>=tau[v]]
        if not enabled:
            terminal.add(x)
        for v in enabled:
            y=x | 1<<v
            if y not in seen:
                seen.add(y); todo.append(y)
    return terminal


def gadget(r,k):
    """One seed, k reinforced adopters, exactly k(r-1) independent cycles."""
    edges=[]; hard=[]
    for i in range(k):
        leaves = list(range(1+i*r, 1+i*r+r-1))
        t = 1+i*r+r-1
        hard.append(t)
        for u in leaves:
            edges.extend([(0,u),(u,t)])
        edges.append((0,t))
    n=1+r*k
    thresholds=[1]*n
    for t in hard: thresholds[t]=r
    return n,edges,thresholds,hard


def main():
    count=0; terminal_checks=0
    for n in (2,3,4):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(pairs)):
            edges=[e for i,e in enumerate(pairs) if mask>>i&1]
            if not connected(n,edges):
                continue
            deg=[sum(v in e for e in edges) for v in range(n)]
            for tau in product(*[range(1,d+1) for d in deg]):
                for seeds in range(1,1<<n):
                    final=check(n,edges,tau,seeds);count+=1
                    if n<=4:
                        assert all_terminal_states(n,edges,tau,seeds)=={final}
                        terminal_checks+=1
    rng=Random(20261103)
    for n in range(5,9):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        for _ in range(250):
            # Random connected graph: spanning tree plus random chords.
            edges=[]
            for v in range(1,n): edges.append((rng.randrange(v),v))
            edge_set=set(edges)
            for e in pairs:
                if e not in edge_set and rng.random()<.35:
                    edges.append(e)
            deg=[sum(v in e for e in edges) for v in range(n)]
            for _ in range(20):
                tau=[rng.randint(1,d) for d in deg]
                seeds=rng.randrange(1,1<<n)
                check(n,edges,tau,seeds); count+=1
    for r in range(2,11):
        for k in range(1,12):
            n,edges,tau,hard=gadget(r,k)
            a=check(n,edges,tau,1)
            assert a==(1<<n)-1
            c,b=subgraph_invariants(n,edges,a)
            assert c==1 and b==k*(r-1)
            cost=sum(tau[v]-1 for v in range(1,n))
            assert cost==b==k*(r-1)
    print('PASS: component-cycle inequality',count,'independent finite instances')
    print('PASS: all asynchronous terminal states',terminal_checks,'instances')
    print('PASS: sharp constructions',9*11,'families, independent of activation rates')

if __name__=='__main__':
    main()
