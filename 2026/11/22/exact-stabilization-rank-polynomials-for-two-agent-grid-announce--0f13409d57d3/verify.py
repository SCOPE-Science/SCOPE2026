#!/usr/bin/env python3
"""Finite independent checks for a public-announcement rank theorem."""
from itertools import product, combinations
from collections import Counter
from math import factorial

def stirling(n,k):
    if k<0 or k>n: return 0
    a=[[0]*(k+1) for _ in range(n+1)]
    a[0][0]=1
    for t in range(1,n+1):
        for j in range(1,k+1):
            a[t][j]=a[t-1][j-1]+j*a[t-1][j]
    return a[n][k]

def Q(n,k):return factorial(k)*stirling(n,k)

def rank_direct(m,n,code):
    def p(i,j):return (code>>(i*n+j))&1
    w={(i,j) for i in range(m) for j in range(n)}
    t=0
    while True:
        wnew={(i,j) for i,j in w if
           any(p(i,b) for a,b in w if a==i) and
           any(not p(a,j) for a,b in w if b==j)}
        if wnew==w:return t
        w=wnew;t+=1

def rank_peeling(m,n,code):
    def p(i,j):return (code>>(i*n+j))&1
    rows=set(range(m));cols=set(range(n));t=0
    while True:
        newrows={i for i in rows if any(p(i,j) for j in cols)}
        newcols={j for j in cols if any(not p(i,j) for i in rows)}
        if not rows or not cols or (newrows==rows and newcols==cols):return t
        rows=newrows;cols=newcols;t+=1

def has_checkerboard(m,n,code):
    def p(i,j):return (code>>(i*n+j))&1
    return any(p(i,c)!=p(i,d) and p(k,c)!=p(k,d) and p(i,c)!=p(k,c)
           for i,k in combinations(range(m),2) for c,d in combinations(range(n),2))

def extremal(m,n):
    if m==n:return 2*factorial(m)**2
    x,y=sorted((m,n))
    return factorial(x)*factorial(x+1)*stirling(y,x+1)

def maximum(m,n):
    x=min(m,n)
    return 2*x-1 if m==n else 2*x


from functools import lru_cache
from math import comb

def add_poly(x,y,coeff=1,shift=0):
    out=Counter(x)
    for k,v in y.items():out[k+shift]+=coeff*v
    return dict(out)

def i_count(m,n):
    return (2**n-1)**m+(2**m-1)**n-2**(m*n)

@lru_cache(None)
def A(m,n):
    if m==0:return {0:1}
    if n==0:return {}
    out={0:i_count(m,n)}
    for c in range(1,n+1):
        out=add_poly(out,B(m,n-c),comb(n,c),1)
    return out

@lru_cache(None)
def B(m,n):
    if n==0:return {0:1}
    if m==0:return {}
    out={0:i_count(m,n)}
    for r in range(1,m+1):
        out=add_poly(out,A(m-r,n),comb(m,r),1)
    return out

def F(m,n):
    return add_poly(add_poly(A(m,n),B(m,n)),{0:i_count(m,n)},-1)

def terminal_worlds(m,n,code):
    def p(i,j):return (code>>(i*n+j))&1
    w={(i,j) for i in range(m) for j in range(n)}
    while True:
        wn={(i,j) for i,j in w if any(p(a,b) for a,b in w if a==i)
            and any(not p(a,b) for a,b in w if b==j)}
        if wn==w:return w
        w=wn

def run():
    total=0;reports=[]
    for m,n in [(1,n) for n in range(1,8)]+[(2,n) for n in range(1,8)]+[(3,n) for n in range(1,5)]+[(4,4)]:
        dist=Counter()
        for code in range(1<<(m*n)):
            a=rank_direct(m,n,code)
            b=rank_peeling(m,n,code)
            assert a==b,(m,n,code,a,b)
            assert a<=maximum(m,n),(m,n,a)
            assert bool(terminal_worlds(m,n,code))==has_checkerboard(m,n,code),(m,n,code)
            if not has_checkerboard(m,n,code):
                # In a finite acyclic orientation every vertex is eventually deleted.
                pass
            dist[a]+=1;total+=1
        assert max(dist)==maximum(m,n),(m,n,max(dist))
        assert dist[maximum(m,n)]==extremal(m,n),(m,n,dist)
        assert dist[0]==(2**n-1)**m+(2**m-1)**n-2**(m*n),(m,n,dist)
        if m==2:
            expected={0:Q(n,2)+Q(n,3),1:2*Q(n,1)+Q(n,3)+Q(n,4),2:2*Q(n,1)+Q(n,2),3:4*Q(n,2),4:2*Q(n,3)}
            assert all(dist[r]==v for r,v in expected.items()),(n,dist,expected)
        assert {k:v for k,v in F(m,n).items() if v}==dict(dist),(m,n,F(m,n),dist)
        reports.append((m,n,total,max(dist),dist[maximum(m,n)]))
    print('VERIFY_OK', 'models_checked=',total, 'cases=',len(reports))
    print('extreme',reports)
if __name__=='__main__':run()
