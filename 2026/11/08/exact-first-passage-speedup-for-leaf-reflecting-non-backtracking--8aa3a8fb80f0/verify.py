"""Exact arithmetic verification of a tree first-passage identity.

Only Python standard library. Every test solves independent first-step
linear equations for both walks, rather than using the claimed induction.
"""
from fractions import Fraction as Q
from itertools import product

def adjacency(n, edges):
    g = [set() for _ in range(n)]
    for a, b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b
        g[a].add(b)
        g[b].add(a)
    assert len(edges) == n - 1
    seen = {0}; stack = [0]
    while stack:
        v = stack.pop()
        for w in g[v]:
            if w not in seen:
                seen.add(w); stack.append(w)
    assert len(seen) == n
    return [sorted(z) for z in g]

def solve(a, b):
    n = len(a)
    tab = [list(a[i]) + [b[i]] for i in range(n)]
    for j in range(n):
        k = next((k for k in range(j, n) if tab[k][j]), None)
        assert k is not None, 'absorbing system is singular'
        tab[j], tab[k] = tab[k], tab[j]
        z = tab[j][j]
        tab[j] = [x / z for x in tab[j]]
        for i in range(n):
            if i != j:
                z = tab[i][j]
                if z:
                    tab[i] = [u - z*v for u, v in zip(tab[i], tab[j])]
    return [tab[i][-1] for i in range(n)]

def independent_hitting(g, s, t, persistent):
    n = len(g)
    if persistent:
        states = [(u,v) for u in range(n) for v in g[u] if v != t]
    else:
        states = [(None,v) for v in range(n) if v != t]
    index = {z:i for i,z in enumerate(states)}
    A = [[Q(int(i==j)) for j in range(len(states))] for i in range(len(states))]
    for i, (u,v) in enumerate(states):
        options = ([w for w in g[v] if w != u] if persistent and len(g[v])>1 else g[v])
        for w in options:
            if w != t:
                target_state = (v,w) if persistent else (None,w)
                A[i][index[target_state]] -= Q(1,len(options))
    h = solve(A,[Q(1)]*len(states))
    if not persistent:
        return h[index[(None,s)]]
    return Q(1) + sum((h[index[(s,w)]] for w in g[s] if w != t),Q(0))/len(g[s])

def predicted(g,s,t):
    n=len(g)
    parent=[-1]*n
    parent[t]=t
    order=[t]
    for v in order:
        for w in g[v]:
            if parent[w] == -1:
                parent[w]=v;order.append(w)
    sub=[1]*n
    for v in reversed(order):
        if v!=t:sub[parent[v]] += sub[v]
    p=[s]
    while p[-1] != t:p.append(parent[p[-1]])
    simple=sum((2*sub[v]-1 for v in p[:-1]),0)
    saving=Q(2)*(Q(sub[s]-1,len(g[s]))+
                 sum((Q(sub[v]-1+sub[p[i-1]],len(g[v])) for i,v in enumerate(p[1:-1],1)),Q(0)))
    return Q(simple), Q(simple)-saving, saving

def recursive_trees(n):
    if n == 2:
        yield [(0,1)];return
    for parents in product(*(range(j) for j in range(1,n))):
        yield [(i+1,p) for i,p in enumerate(parents)]

def run():
    count=0
    for n in range(2,7):
        for edges in recursive_trees(n):
            g=adjacency(n,edges)
            for s in range(n):
                for t in range(n):
                    if s==t:continue
                    simple,nb,saving=predicted(g,s,t)
                    assert simple==independent_hitting(g,s,t,False)
                    assert nb==independent_hitting(g,s,t,True)
                    assert saving>=0
                    assert (saving==0)==(len(g[s])==1 and t in g[s])
                    count+=1
        print('checked n =',n,'pairs so far =',count)
    for n in (7,8,10):
        patterns=[[(i-1,i) for i in range(1,n)], [(0,i) for i in range(1,n)],
                  [(i, (i-1)//2) for i in range(1,n)]]
        for edges in patterns:
            g=adjacency(n,edges)
            for s,t in ((0,n-1),(n-1,0),(n//2,0),(n//2,n-1)):
                if s==t:continue
                a,b,_=predicted(g,s,t)
                assert a==independent_hitting(g,s,t,False)
                assert b==independent_hitting(g,s,t,True)
                count+=1
    print('VERIFY_OK exact independent comparisons =',count)
if __name__=='__main__':run()
