#!/usr/bin/env python3
"""Independent construction of predicted minimizers and exact arithmetic test.
Prints n, optimum r, exact weight, labelled matching count and a direct
check of the perfect Roman condition for each constructed optimum up to n=10.
"""
from itertools import combinations
from math import factorial

def pairings(vertices, k):
    if k == 0:
        yield ()
        return
    for used in combinations(vertices, 2*k):
        def rec(pool):
            if not pool:
                yield ()
            else:
                x=pool[0]
                for j in range(1,len(pool)):
                    y=pool[j]
                    for others in rec(pool[1:j]+pool[j+1:]):
                        yield ((x,y),)+others
        yield from rec(used)

def make_labels(n, matching):
    edge={tuple(sorted(p)) for p in matching}
    touched={v for e in matching for v in e}
    out={}
    for u in range(n):
        for v in range(u+1,n):
            if (u,v) in edge: out[(u,v)]=2
            elif (u in touched) != (v in touched):out[(u,v)]=0
            else:out[(u,v)]=1
    return out

def valid(labels):
    for (u,v),x in labels.items():
        if x==0 and sum(y==2 for (a,b),y in labels.items() if (a,b)!=(u,v) and (u==a or u==b or v==a or v==b))!=1:return False
    return True

for n in range(3,11):
    r=(2*n+3)//8
    count=0;correct=True
    for mat in pairings(tuple(range(n)),r):
        lab=make_labels(n,mat)
        correct &= valid(lab) and sum(lab.values())==n*(n-1)//2 +r-2*r*(n-2*r)
        count+=1
    expected=factorial(n)//(2**r*factorial(r)*factorial(n-2*r))
    assert correct and count==expected,(n,count,expected)
    print(f'n={n} r={r} minimum={n*(n-1)//2+r-2*r*(n-2*r)} count={count} passed={correct}')
