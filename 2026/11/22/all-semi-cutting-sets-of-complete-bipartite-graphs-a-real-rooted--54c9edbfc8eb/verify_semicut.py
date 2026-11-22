#!/usr/bin/env python3
"""Direct finite checks of the shortest-terminal-path semi-cutting polynomial."""
from collections import Counter,deque
from itertools import product
from math import comb

def graph(a,b):
    return a+b,[(i,a+j) for i in range(a) for j in range(b)]

def distances(n,edge_list,mask):
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(edge_list):
        if mask>>i&1:continue
        adj[u].append(v);adj[v].append(u)
    D=[]
    for s in range(n):
        d=[10**6]*n;d[s]=0; todo=deque([s])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if d[w]>d[v]+1:d[w]=d[v]+1;todo.append(w)
        D.append(d)
    return D

def direct(a,b,x,y):
    n,E=graph(a,b);term=list(range(x))+list(range(a,a+y))
    D=distances(n,E,0); p=Counter()
    for mask in range(1<<len(E)):
        dist=distances(n,E,mask)
        if all(dist[term[i]][term[j]]>D[term[i]][term[j]] for i in range(len(term)) for j in range(i+1,len(term))):
            p[mask.bit_count()]+=1
    return p

def poly(a,b,x,y):
    ans=[1]
    def mul(c):
        nonlocal ans
        out=[0]*(len(ans)+len(c)-1)
        for i,v in enumerate(ans):
            for j,w in enumerate(c):out[i+j]+=v*w
        ans=out
    for _ in range(x*y):mul([0,1])
    for _ in range(b-y):mul(([1] if x==0 else [0]*(x-1)+[x,1]))
    for _ in range(a-x):mul(([1] if y==0 else [0]*(y-1)+[y,1]))
    for _ in range((a-x)*(b-y)):mul([1,1])
    return Counter({i:v for i,v in enumerate(ans) if v})

def test():
    c=0
    for a in range(1,5):
        for b in range(1,5):
            if a*b>10:continue
            for x in range(a+1):
                for y in range(b+1):
                    if x+y<2:continue
                    actual=direct(a,b,x,y);exp=poly(a,b,x,y)
                    assert actual==exp,(a,b,x,y,actual,exp)
                    tau=x*y+(b-y)*max(0,x-1)+(a-x)*max(0,y-1)
                    assert min(actual)==tau
                    assert tau>=x+y-1
                    c+=1
    print('INDEPENDENT_TERMINAL_PAIR_BFS_AND_POLYNOMIAL_PASS cases=',c)
    c=0
    for a,b in ((4,4),(5,5),(4,7)):
        for x in range(a+1):
            for y in range(b+1):
                if x+y<2:continue
                coeff=poly(a,b,x,y)
                tau=x*y+(b-y)*max(0,x-1)+(a-x)*max(0,y-1)
                assert min(coeff)==tau
                assert tau>=x+y-1
                # Predicted all-minimal solutions count and exponents.
                n=((x if x else 1)**(b-y))*((y if y else 1)**(a-x))
                assert coeff[tau]==n
                c+=1
    print('EXTREMAL_POLYNOMIAL_AND_BOUND_PASS cases=',c)
    print('VERIFY_OK')
if __name__=='__main__':test()
