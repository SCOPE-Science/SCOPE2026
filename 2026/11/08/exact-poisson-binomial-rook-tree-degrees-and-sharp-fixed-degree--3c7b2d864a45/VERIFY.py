"""Independent finite checks for a single-vertex degree law on rook graphs."""
from fractions import Fraction
from itertools import combinations
from math import comb
from collections import Counter
import sympy as S


def data(m,n):
    vertices=[(i,j) for i in range(m) for j in range(n)]
    es=[(a,b) for a in range(m*n) for b in range(a+1,m*n)
        if (vertices[a][0]==vertices[b][0]) != (vertices[a][1]==vertices[b][1])]
    return es


def pgf_prediction(m,n,z):
    t=Fraction(z)
    s=m+n
    return (1+Fraction(2,s)*(t-1))*(1+Fraction(m+1,m*s)*(t-1))**(m-2)*(1+Fraction(n+1,n*s)*(t-1))**(n-2)


def tree_det(m,n,z):
    N=m*n
    L=S.zeros(N-1)
    for a,b in data(m,n):
        w=z if a==0 or b==0 else 1
        if a<N-1:L[a,a]+=w
        if b<N-1:L[b,b]+=w
        if a<N-1 and b<N-1:
            L[a,b]-=w;L[b,a]-=w
    return L.det(method='domain-ge')


def brute(m,n):
    N=m*n
    edges=data(m,n)
    counts=Counter()
    for subset in combinations(edges,N-1):
        parent=list(range(N))
        def root(i):
            while parent[i]!=i:
                i=parent[i]
            return i
        ok=True
        for a,b in subset:
            ra,rb=root(a),root(b)
            if ra==rb:ok=False;break
            parent[ra]=rb
        if ok:counts[sum(a==0 or b==0 for a,b in subset)]+=1
    return counts


def poly_prediction(m,n):
    z=S.symbols('z');s=m+n
    return S.Poly(S.expand(z*(1+S.Rational(2,s)*(z-1))*
        (1+S.Rational(m+1,m*s)*(z-1))**(m-2)*
        (1+S.Rational(n+1,n*s)*(z-1))**(n-2)),z)


def verify():
    c=0
    cases=[(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3)]
    for m,n in cases:
        norm=tree_det(m,n,1)
        for z in (0,2,3,4):
            lhs=Fraction(int(tree_det(m,n,z)),int(norm))
            rhs=Fraction(z)*pgf_prediction(m,n,z)
            assert lhs==rhs,(m,n,z,lhs,rhs)
            c+=1
    for m,n in ((2,2),(2,3),(2,4),(3,3)):
        counts=brute(m,n)
        norm=sum(counts.values());P=poly_prediction(m,n)
        for k in range(0,m+n):
            a=Fraction(counts.get(k,0),norm)
            b=Fraction(P.nth(k))
            assert a==b,(m,n,k,a,b)
            c+=1
    for s in range(4,70):
        ps=[]
        for m in range(2,s-1):
            n=s-m
            p=pgf_prediction(m,n,0)
            ps.append(p)
            assert p==pgf_prediction(n,m,0)
            c+=1
        assert ps==list(reversed(ps));c+=1
        assert ps[len(ps)//2]==min(ps);c+=1
        assert ps[0]==max(ps);c+=1
        if s>=6:
            assert ps[0]>ps[1];c+=1
    print('VERIFY_OK',c,'exact assertions')

if __name__=='__main__': verify()
