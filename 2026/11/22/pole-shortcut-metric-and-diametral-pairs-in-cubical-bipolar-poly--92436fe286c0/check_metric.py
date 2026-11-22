#!/usr/bin/env python3
"""Check cubical bipolar graph metric against independent shortest paths."""
from collections import defaultdict, deque, Counter
from itertools import product
from math import factorial


def predicted(u, v):
    if u is None and v is None:
        return 0
    if u is None:
        return sum(x==0 for x in v)+1
    if v is None:
        return sum(x==0 for x in u)+1
    a=sum(x==-y and x!=0 for x,y in zip(u,v))
    b=sum((x==0)!=(y==0) for x,y in zip(u,v))
    c=sum(x==y==0 for x,y in zip(u,v))
    return b+min(2*a,2*c+2)


def graph(n):
    words=list(product((-1,0,1), repeat=n))
    vertices=[None]+words
    adj={u:set() for u in vertices}
    for w in words:
        for i,x in enumerate(w):
            if x:
                u=w[:i]+(0,)+w[i+1:]
                adj[w].add(u);adj[u].add(w)
            else:
                for y in (-1,1):
                    u=w[:i]+(y,)+w[i+1:]
                    adj[w].add(u);adj[u].add(w)
        if all(x!=0 for x in w):
            adj[None].add(w);adj[w].add(None)
    return vertices,adj


def diametral_formula(n):
    total=1
    for c in range((n-1)//2+1):
        a=c+1; b=n-a-c
        ordered=factorial(n)//(factorial(a)*factorial(b)*factorial(c))*2**a*4**b
        assert ordered%2==0
        total+=ordered//2
    return total


def shell_formula_exact(n):
    ordered=Counter()
    fac=factorial(n)
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                coeff=fac//(factorial(a)*factorial(b)*factorial(c)*factorial(d))*2**(a+d)*4**b
                ordered[b+min(2*a,2*c+2)]+=coeff
    ordered[0]-=3**n
    assert all(v%2==0 for v in ordered.values())
    out=Counter({k:v//2 for k,v in ordered.items()})
    for f in range(n+1):
        out[f+1]+=fac//(factorial(f)*factorial(n-f))*2**(n-f)
    return +out


def check(n):
    vertices,adj=graph(n)
    assert len(vertices)==3**n+1
    edg=sum(map(len, adj.values()))//2
    assert edg==2*n*3**(n-1)+2**n
    distances=Counter()
    ecc={}
    for s in vertices:
        steps={s:0}
        todo=deque([s])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if w not in steps:
                    steps[w]=steps[v]+1; todo.append(w)
        assert len(steps)==len(vertices)
        for t,actual in steps.items():
            assert actual==predicted(s,t),(n,s,t,actual,predicted(s,t))
        ecc[s]=max(steps.values())
        for t,actual in steps.items():
            distances[actual]+=1
    assert set(ecc.values())=={n+1}
    distances[0]-=len(vertices)
    assert all(v%2==0 for v in distances.values())
    actual_shell=+Counter({k:v//2 for k,v in distances.items()})
    algebraic_shell=shell_formula_exact(n)
    assert actual_shell==algebraic_shell,(n,actual_shell,algebraic_shell)
    assert actual_shell[n+1]==diametral_formula(n)
    print(f'n={n}: vertices={len(vertices)} edges={edg} diameter={n+1} diametral_pairs={actual_shell[n+1]} distance_sum={sum(k*v for k,v in actual_shell.items())} shells={dict(sorted(actual_shell.items()))}')

if __name__=='__main__':
    for n in range(1,7): check(n)
