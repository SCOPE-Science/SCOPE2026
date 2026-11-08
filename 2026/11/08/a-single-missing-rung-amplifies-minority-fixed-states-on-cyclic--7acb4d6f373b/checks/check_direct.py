"""Exhaustive spin-by-spin minority fixed-point verification with one rung deleted.
Standard Python only. Usage: python3 checks/check_direct.py
"""
from collections import Counter

def graph(n,twist):
    adj=[set() for _ in range(2*n)]
    def edge(u,v):
        assert u!=v and v not in adj[u]
        adj[u].add(v);adj[v].add(u)
    for i in range(1,n):edge(i,n+i) # one absent rung, precisely at column 0
    for i in range(n-1):
        edge(i,i+1);edge(n+i,n+i+1)
    if twist:
        edge(n-1,n);edge(2*n-1,0)
    else:
        edge(n-1,0);edge(2*n-1,n)
    assert [len(v) for v in adj]==[2]+[3]*(n-1)+[2]+[3]*(n-1)
    return [tuple(a) for a in adj]

def fib(n):
    x,y=0,1
    for _ in range(n):x,y=y,x+y
    return x
C=(6,-3,1,4,-1,-1)
M=(-2,3,3,-4,5,1)

checked=0
for n in range(3,10):
    for twist in (0,1):
        neighbors=graph(n,twist)
        stable=0
        for mask in range(1<<(2*n)):
            good=True
            for u,ns in enumerate(neighbors):
                bit=(mask>>u)&1
                opposite=sum(((mask>>v)&1)!=bit for v in ns)
                # Strict minority at degree 3; tie retention at degree 2.
                if 2*opposite<len(ns): good=False;break
            stable+=good
        target=3*fib(n)+(M if twist else C)[n%6]
        assert stable==target,(n,twist,stable,target)
        checked+=1<<(2*n)
        print(f'n={n:2d} twist={twist} fixed={stable:5d} expected={target:5d} OK')
print('PASS exhaustive labelled simulations; configurations=',checked)
