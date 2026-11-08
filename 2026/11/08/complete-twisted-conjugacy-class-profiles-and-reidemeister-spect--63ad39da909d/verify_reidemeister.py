#!/usr/bin/env python3
"""Independent finite orbit check of the Reidemeister class-size theorem."""
from itertools import product
from collections import Counter

def rank(M,p):
    M=[list(row) for row in M]; n=len(M); m=len(M[0]) if n else 0
    r=0
    for c in range(m):
        k=next((i for i in range(r,n) if M[i][c]%p),None)
        if k is None:continue
        M[r],M[k]=M[k],M[r]; v=pow(M[r][c]%p,-1,p)
        M[r]=[(v*x)%p for x in M[r]]
        for i in range(n):
            if i!=r:
                t=M[i][c]; M[i]=[(x-t*y)%p for x,y in zip(M[i],M[r])]
        r+=1
        if r==n:break
    return r

def matmul(A,x,p):
    return tuple(sum(a*b for a,b in zip(row,x))%p for row in A)

def exact_profile(A,b,p):
    d=len(A); V=list(product(range(p),repeat=d)); index={x:i for i,x in enumerate(V)}
    parent=list(range(2*len(V)))
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def unite(x,y):
        x=root(x);y=root(y)
        if x!=y:parent[y]=x
    for ai,a in enumerate(V):
        for e in (0,1):
            ix=ai+e*len(V)
            for j in range(d):
                basis=tuple(int(k==j) for k in range(d))
                u=matmul(A,basis,p)
                x=tuple((a[k]+basis[k]-(1 if e==0 else -1)*u[k])%p for k in range(d))
                unite(ix,index[x]+e*len(V))
            x=tuple((-a[k]+(-1 if e else 1)*b[k])%p for k in range(d))
            unite(ix,index[x]+e*len(V))
    return [Counter(Counter(root(i) for i in range(e*len(V),(e+1)*len(V))).values()) for e in (0,1)]

def predicted_profile(A,p):
    d=len(A); profiles=[]
    for eps in (1,-1):
        r=rank([[(int(i==j)-eps*A[i][j])%p for j in range(d)] for i in range(d)],p)
        a=d-r
        c=Counter({p**r:1})
        if (p**a-1)//2:c[2*p**r]+=(p**a-1)//2
        profiles.append(c)
    return profiles

def all_gl(d,p):
    for entries in product(range(p),repeat=d*d):
        A=[entries[i*d:(i+1)*d] for i in range(d)]
        if rank(A,p)==d:yield A


def run():
    checks=0; groups=0
    for d,p in ((1,3),(1,5),(2,3),(2,5),(3,3)):
        rs=set()
        for i,A in enumerate(all_gl(d,p)):
            bs=[(0,)*d]
            if d==2:bs.append((1,)+(0,)*(d-1))
            for b in bs:
                got=exact_profile(A,b,p);exp=predicted_profile(A,p)
                assert got==exp,(d,p,A,b,got,exp)
                checks+=1
            pp=predicted_profile(A,p)
            rs.add(sum(sum(c.values()) for c in pp))
            groups+=1
        predicted=set()
        for a in range(d+1):
            for b in range(d-a+1):
                m=d-a-b
                if p==3 and d==1 and m==1:continue
                predicted.add(1+(p**a+p**b)//2)
        assert rs==predicted,(p,d,rs,predicted)
        print('case',d,p,'possible_R',sorted(rs),'GL_matrices',i+1)
    print('VERIFY_OK',checks,'orbit_profiles',groups,'automorphisms')
if __name__=='__main__':run()
