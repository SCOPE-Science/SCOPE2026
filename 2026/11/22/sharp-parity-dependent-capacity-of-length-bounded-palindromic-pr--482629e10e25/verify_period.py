#!/usr/bin/env python3
"""Independent union-find/inclusion-exclusion period calculation."""
from itertools import combinations,product

def components(m,periods):
    parent=list(range(m))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    def union(a,b):
        a,b=root(a),root(b)
        if a!=b: parent[a]=b
    for i in range(m): union(i,m-1-i)
    for t in periods:
        for i in range(m-t): union(i,i+t)
    return len({root(i) for i in range(m)})

def exact(q,n):
    acc=0
    for m in range(n//2+1,n+1):
        r=n-m
        for k in range(r+1):
            for S in combinations(range(1,r+1),k):
                acc+=(-1)**k*q**components(m,S)
    return acc

def direct_short_period(q,n):
    result=0
    for m in range(n//2+1,n+1):
        for u in product(range(q),repeat=(m+1)//2):
            w=u+u[-2::-1] if m%2 else u+u[::-1]
            if all(any(w[i]!=w[i+t] for i in range(m-t)) for t in range(1,n-m+1)):
                result+=1
    return result

if __name__=='__main__':
    for q,limit in ((2,14),(3,10),(4,8)):
        for n in range(1,limit+1):
            x=exact(q,n);y=direct_short_period(q,n)
            assert x==y,(q,n,x,y)
        print('IE vs direct periods q=',q,'to n=',limit,'PASS')
    print('Values q2:',[exact(2,n) for n in range(1,15)])
    print('Values q3:',[exact(3,n) for n in range(1,11)])
