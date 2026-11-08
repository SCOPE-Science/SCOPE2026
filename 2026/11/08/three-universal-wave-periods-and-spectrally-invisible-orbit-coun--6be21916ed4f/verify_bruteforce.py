#!/usr/bin/env python3
"""Independent elementary-state enumeration on three strongly regular examples.
No third-party modules are required."""
from itertools import combinations

def graph(n,edges):
    adj=[0]*n
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    return adj

def cycle5():return graph(5,[(i,(i+1)%5) for i in range(5)])
def complete_bipartite(a,b):return graph(a+b,[(i,a+j) for i in range(a) for j in range(b)])
def rk(rows):
    basis={}
    for r in rows:
        while r:
            p=r.bit_length()-1
            if p in basis:r^=basis[p]
            else:basis[p]=r;break
    return len(basis)

def update(A,s):
    n=len(A);u=s&((1<<n)-1);old=s>>n;fresh=old
    for i,r in enumerate(A):
        if (r&u).bit_count()%2:fresh^=1<<i
    return fresh|(u<<n)

def check(label,A,order):
    n=len(A);q=1<<n
    d0=n-rk(A);d1=n-rk([a^(1<<i) for i,a in enumerate(A)])
    expected={}
    if order==4:
        fixed={1:1<<d0,2:1<<(2*d0),4:1<<(2*n)}
    elif order==10:
        fixed={1:2,2:4,5:1<<(2*n-1),10:1<<(2*n)}
    else:
        fixed={1:1<<d0,2:1<<(2*d0),3:1<<(d0+2*d1),6:1<<(2*n)}
    actual={t:0 for t in fixed}
    orbit_pop={t:0 for t in fixed}
    for s in range(q*q):
        x=s;t=0
        while True:
            x=update(A,x);t+=1
            assert t<=order
            if x==s:break
        assert order%t==0
        orbit_pop[t]+=1
        for e in fixed:
            if e%t==0:actual[e]+=1
    assert actual==fixed,(label,fixed,actual)
    assert sum(orbit_pop.values())==q*q
    assert all(pop%t==0 for t,pop in orbit_pop.items())
    print(label,'states',q*q,'fixed',fixed,'primitive points',orbit_pop,
          'primitive cycles',{t:pop//t for t,pop in orbit_pop.items()})

if __name__=='__main__':
    check('C5',cycle5(),10)
    check('K2,2',complete_bipartite(2,2),4)
    check('K3,3',complete_bipartite(3,3),6)
    print('PASS: independent exhaustive state enumeration for orders 4,6,10.')
