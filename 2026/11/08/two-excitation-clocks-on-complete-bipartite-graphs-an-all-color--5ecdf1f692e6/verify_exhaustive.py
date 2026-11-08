#!/usr/bin/env python3
"""Exact enumeration of finite labelled Greenberg-Hastings state graphs."""
from collections import Counter, deque
from math import factorial


def onto(m,s):
    return sum((-1)**j * __import__('math').comb(s,j)*(s-j)**m for j in range(s+1))


def predicted(m,n,k):
    s=(k+1)//2
    d=Counter({1:1})
    f=onto(m,k)*onto(n,k)
    a=2*onto(m,s)*onto(n,s)
    d[k]+=f
    d[2*s]+=a
    return {p:c for p,c in d.items() if c}


def actual(m,n,k):
    powk=[k**i for i in range(m+n)]
    states=k**(m+n)
    dest=[0]*states
    indeg=[0]*states
    for x in range(states):
        z=x; cols=[]
        for _ in range(m+n):
            z,v=divmod(z,k);cols.append(v)
        left_has_1=1 in cols[:m]
        right_has_1=1 in cols[m:]
        y=0
        for i,c in enumerate(cols):
            if c: new=(c+1)%k
            elif i<m: new=int(right_has_1)
            else:new=int(left_has_1)
            y+=new*powk[i]
        dest[x]=y;indeg[y]+=1
    q=deque(i for i in range(states) if not indeg[i])
    while q:
        u=q.popleft();indeg[dest[u]]-=1
        if indeg[dest[u]]==0:q.append(dest[u])
    seen=set();counts=Counter()
    for x in range(states):
        if indeg[x] and x not in seen:
            length=0;z=x
            while z not in seen:
                seen.add(z);length+=1;z=dest[z]
            counts[length]+=length
    return dict(sorted(counts.items()))

cases=0;states=0
for k in range(3,9):
    for m in range(1,5):
        for n in range(1,5):
            if k**(m+n)>250000:continue
            a=actual(m,n,k); p=predicted(m,n,k)
            assert a==p, (m,n,k,a,p)
            cases+=1;states+=k**(m+n)
            if (m,n,k) in [(2,2,3),(3,3,3),(3,3,4),(3,3,5),(3,3,6)]:
                print('example',m,n,k,a)
print('PASS labelled-state exhaustive comparisons:',cases,'cases;',states,'states')
