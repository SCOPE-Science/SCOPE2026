#!/usr/bin/env python3
"""Reproducible exact checks of covariance on rectangular rook graphs.
Only uses the Python standard library. Finite checks are supplementary to the proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def polynomial(m, n):
    return (2*m**3*n - m*m*n**3 - m*m*n*n + m*m*n + 2*m*m - m*n*n + 2*n*n)


def exact_formula(m, n):
    assert isinstance(m,int) and isinstance(n,int) and min(m,n)>=2
    return F(polynomial(m,n),m*m*n*n*(m+n)**2)


def g(x,y,m,n):
    a,b=x; c,d=y
    aa=F(int(a==c),1)-F(1,m)
    bb=F(int(b==d),1)-F(1,n)
    return aa/F(m*n)+bb/F(m*n)+aa*bb/F(m+n)


def k(e,f,m,n):
    x,y=e; v,z=f
    return g(x,v,m,n)-g(x,z,m,n)-g(y,v,m,n)+g(y,z,m,n)


def incidence(m,n,vertex):
    x,y=vertex
    return [((x,y),(i,y)) for i in range(m) if i!=x]+[((x,y),(x,j)) for j in range(n) if j!=y]


def direct_current_cov(m,n):
    u=(0,0);v=(0,1)
    ed_u=incidence(m,n,u)
    ed_v=incidence(m,n,v)
    return sum((k(e,e,m,n)-h*h if set(e)==set(f) else -h*h for e in ed_u for f in ed_v for h in [k(e,f,m,n)]),F(0))


def spanning_edges(m,n):
    return [((a,b),(c,b)) for a in range(m) for b in range(n) for c in range(a+1,m)]+[((a,b),(a,d)) for a in range(m) for b in range(n) for d in range(b+1,n)]


def enumerate_cov(m,n):
    nvert=m*n
    edges=[(a*n+b,c*n+d) for (a,b),(c,d) in spanning_edges(m,n)]
    count=su=sv=suv=0
    for block in combinations(edges,nvert-1):
        par=list(range(nvert))
        def root(i):
            while par[i]!=i:
                i=par[i]
            return i
        ok=True
        for i,j in block:
            a,b=root(i),root(j)
            if a==b:
                ok=False;break
            par[a]=b
        if not ok: continue
        # With N-1 acyclic edges the graph is connected.
        d_u=sum(i==0 or j==0 for i,j in block)
        d_v=sum(i==1 or j==1 for i,j in block)
        count+=1;su+=d_u;sv+=d_v;suv+=d_u*d_v
    assert count>0
    return F(suv,count)-F(su*sv,count*count), count


def run():
    checks=0
    for m in range(2,13):
        for n in range(2,13):
            got=direct_current_cov(m,n)
            assert got==exact_formula(m,n),(m,n,got,exact_formula(m,n))
            checks+=1
            t=n*(n+1)//2
            expected=0 if (m,n)==(2,2) else (1 if m>=t else -1)
            assert ((got>0)-(got<0))==expected,(m,n,got,expected)
            checks+=1
    for m,n in [(2,2),(2,3),(3,2),(2,4),(3,3)]:
        got,count=enumerate_cov(m,n)
        assert got==exact_formula(m,n),(m,n,got,exact_formula(m,n))
        print('exact spanning-tree enumeration',m,n,'count',count,'covariance',got)
        checks+=1
    # Verify symbolic threshold substitutions and the proof's polynomial identity at integer samples.
    for n in range(2,35):
        t=n*(n+1)//2
        left=F(-(n-2)*(n**4+4*n**3+3*n*n-4*n+4),4)
        right=F(n*n*(n**3+2*n*n+3*n+10),4)
        assert polynomial(t-1,n)==left
        assert polynomial(t,n)==right
        checks+=2
    print('VERIFY_OK', checks, 'exact assertions')

if __name__=='__main__':run()
