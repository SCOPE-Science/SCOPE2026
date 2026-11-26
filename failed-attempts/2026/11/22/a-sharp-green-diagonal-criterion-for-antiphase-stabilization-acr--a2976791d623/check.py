#!/usr/bin/env python3
"""Exact finite-graph checks for bridge antiphase stability in the mixed Kuramoto flow.

Python 3 with SymPy. Tests chosen finite cases only; the all-graph proof is mathematical.
"""
from itertools import combinations
from sympy import Matrix, Rational, eye, ones, zeros, simplify


def lap(m, edges):
    L=zeros(m)
    for i,j in edges:
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    return L


def connected(m,edges):
    adj=[set() for _ in range(m)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        for k in adj[stack.pop()]:
            if k not in seen:seen.add(k);stack.append(k)
    return len(seen)==m


def diagonal_resistance(m,edges,vertex):
    if m==1:return Rational(0)
    L=lap(m,edges)
    J=ones(m,m)/m
    Linv=(L+J).inv()-J  # Moore-Penrose pseudoinverse
    return simplify(Linv[vertex,vertex])


def inertia_pos(M):
    """Return number of positive eigenvalues using exact characteristic roots for test matrices."""
    vals=M.eigenvals()
    return len(vals), vals


def positive_definite(M):
    # Sylvester's criterion, no floating-point rounding.
    for k in range(1,M.rows+1):
        if M[:k,:k].det()<=0:return False
    return True


def antiphase_hessian(m,ea,eb,K1,K2):
    n=2*m
    edges=ea+[(i+m,j+m) for i,j in eb]+[(m-1,m)]
    s=Matrix([1]*m+[-1]*m)
    Ls=zeros(n)
    for i,j in edges:
        w=s[i]*s[j]
        Ls[i,i]+=w;Ls[j,j]+=w;Ls[i,j]-=w;Ls[j,i]-=w
    d=Rational(2*len(edges),n)
    H=K1/d*Ls+K2/n*(s*s.T)
    # Basis for mean-zero, not orthonormal: positive definiteness is preserved.
    B=Matrix.hstack(*[eye(n)[:,i]-eye(n)[:,n-1] for i in range(n-1)])
    return B.T*H*B, d, len(edges)


def path(m):return [(j,j+1) for j in range(m-1)]
def clique(m):return list(combinations(range(m),2))


def test(m,ea,eb):
    r=diagonal_resistance(m,ea,m-1)+diagonal_resistance(m,eb,0)
    total=len(ea)+len(eb)+1
    # K1=1, and K2 takes a few rational values, including exact threshold.
    threshold=Rational(2,total)/(1-r) if r<1 else None
    ks=[Rational(0),Rational(1,10),Rational(1),Rational(3),Rational(20)]
    if threshold is not None:ks += [threshold/2, threshold, threshold+Rational(1,100)]
    for k in ks:
        H,_,_=antiphase_hessian(m,ea,eb,Rational(1),k)
        observed=positive_definite(H)
        predicted=(r<1 and k>threshold)
        assert observed==predicted, (m,ea,eb,r,threshold,k,observed,predicted)
    if threshold is not None:
        H,_,_=antiphase_hessian(m,ea,eb,Rational(1),threshold)
        assert H.det()==0, (m,ea,eb,'border must be singular')
    return r, threshold


def main():
    count=0
    for m in range(1,6):
        e=path(m)
        r,threshold=test(m,e,e);count+=1
        expect=Rational((m-1)*(2*m-1),3*m)
        assert r==expect
        if m<=2:assert threshold==[None,Rational(2),Rational(4,3)][m]
        else:assert threshold is None
        print('path',2*m,'R=',r,'threshold=',threshold)
    for m in range(2,7):
        e=clique(m)
        r,threshold=test(m,e,e);count+=1
        assert r==Rational(2*(m-1),m*m)
        print('barbell',2*m,'R=',r,'threshold=',threshold)
    # All connected labelled 3-vertex components, plus 15 selected 4-vertex connected components.
    for m in [2,3,4]:
        allpairs=list(combinations(range(m),2))
        subsets=[]
        for mask in range(1<<len(allpairs)):
            es=[e for j,e in enumerate(allpairs) if mask>>j&1]
            if connected(m,es):subsets.append(es)
        if m==4:subsets=subsets[::max(1,len(subsets)//15)]
        for a in subsets:
            for b in subsets:
                test(m,a,b);count+=1
    print('PASS: exact positive-definiteness and threshold on',count,'bridge graph cases; finite tests only')

if __name__=='__main__':main()
