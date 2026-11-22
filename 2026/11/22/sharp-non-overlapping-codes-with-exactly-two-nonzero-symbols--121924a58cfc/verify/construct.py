#!/usr/bin/env python3
"""Construct optimal q-ary sparse synchronization codes and audit overlaps."""
from itertools import combinations,product

def output(n,q):
    m=q-1
    def word(t,a,b):
        x=[0]*n;x[0]=a;x[t]=b
        return tuple(x)
    X=[word(t,a,b) for t in range(1,(n+1)//2) for a,b in product(range(1,q),repeat=2)]
    if n%2==0:
        A=range(1,1+m//2)
        B=range(1+m//2,q)
        X.extend(word(n//2,a,b) for a in A for b in B)
    return X

def conflict(x,y):
    for k in range(1,len(x)):
        if x[:k]==y[-k:] or y[:k]==x[-k:]:return k
    return None

def primitive_count(n,q):
    W=[]
    for i,j in combinations(range(n),2):
        for a,b in product(range(1,q),repeat=2):
            t=[0]*n;t[i]=a;t[j]=b;W.append(tuple(t))
    orbits={}
    for w in W:
        rotations=[w[k:]+w[:k] for k in range(n)]
        if len(set(rotations))!=n:continue
        orbits[min(rotations)]=1
    return len(orbits)

if __name__=='__main__':
    seen=0
    for q in range(2,8):
        for n in range(3,17):
            X=output(n,q)
            m=q-1
            target=(n//2)*m*m if n%2 else (n//2-1)*m*m+(m*m)//4
            assert len(X)==target and len(set(X))==target,(q,n,len(X),target)
            for i,x in enumerate(X):
                assert conflict(x,x) is None,(q,n,i,'self')
                for j in range(i):
                    assert conflict(x,X[j]) is None,(q,n,i,j)
            seen+=1
    checks=0
    for q in range(2,7):
        for n in range(3,10):
            m=q-1
            all_prim=primitive_count(n,q)
            expected=m*m*((n-1)//2) + (m*(m-1)//2 if n%2==0 else 0)
            assert all_prim==expected,(q,n,all_prim,expected)
            checks+=1
    print('CONSTRUCTION_CASES',seen)
    print('NECKLACE_CENSUS_CASES',checks)
    print('PASS')
