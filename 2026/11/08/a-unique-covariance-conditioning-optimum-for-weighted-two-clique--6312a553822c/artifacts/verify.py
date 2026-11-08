#!/usr/bin/env python3
"""Exact finite checks of two-clique graphical zonotope vertex covariances."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def graph(a,b):
    n=a+b-1
    A=tuple(range(a));B=(0,)+tuple(range(a,n))
    return n,A,B


def full_vertices(a,b,t,s):
    """Direct construction: induce acyclic orientations from global orders."""
    n,A,B=graph(a,b)
    edge=[]
    for block,w in ((A,t),(B,s)):
        edge.extend((i,j,w) for ii,i in enumerate(block) for j in block[ii+1:])
    ans=set()
    for p in permutations(range(n)):
        pos=[0]*n
        for j,v in enumerate(p):pos[v]=j
        x=[0]*n # twice a centered zonotope vertex
        for i,j,w in edge:
            z=w if pos[i]>pos[j] else -w
            x[i]+=z;x[j]-=z
        ans.add(tuple(x))
    return ans


def predicted(a,b,t,s):
    n,A,B=graph(a,b)
    u=F((a+1)*t*t,12);v=F((b+1)*s*s,12)
    C=[[F(0) for _ in range(n)] for _ in range(n)]
    for block,w in ((A,u),(B,v)):
        for i in block:
            for j in block:
                C[i][j]+=w*(len(block)-1 if i==j else -1)
    return C,u,v


def observed(vertices):
    N=len(vertices);n=len(next(iter(vertices)))
    # integer vectors represent 2X
    E=[F(sum(x[i] for x in vertices),2*N) for i in range(n)]
    assert E==[0]*n
    C=[[F(sum(x[i]*x[j] for x in vertices),4*N) for j in range(n)] for i in range(n)]
    return C


def minor_det(M):
    A=[[F(v) for v in row] for row in M]
    n=len(A);d=F(1)
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        assert k is not None
        if k!=j:A[j],A[k]=A[k],A[j];d=-d
        pivot=A[j][j];d*=pivot
        for k in range(j+1,n):
            f=A[k][j]/pivot
            for z in range(j,n):A[k][z]-=f*A[j][z]
    return d


def check(a,b,t,s):
    n,_,_=graph(a,b)
    V=full_vertices(a,b,t,s)
    assert len(V)==factorial(a)*factorial(b),(a,b,t,s,len(V))
    C,u,v=predicted(a,b,t,s)
    assert observed(V)==C,(a,b,t,s)
    assert all(sum(row)==0 for row in C)
    pdet=F(n)*minor_det([row[:-1] for row in C[:-1]])
    assert pdet==(a*u)**(a-2)*(b*v)**(b-2)*n*u*v
    # Test group-contrast eigenvectors, plus quotient trace/product.
    for block,w in ((range(1,a),a*u),(range(a,n),b*v)):
        if len(block)<2:continue
        i,j=list(block)[:2]
        z=[0]*n;z[i]=1;z[j]=-1
        assert [sum(C[ii][jj]*z[jj] for jj in range(n)) for ii in range(n)]==[w*zz for zz in z]
    return len(V),n*n


def main():
    samples=[(2,2,1,1),(2,4,2,1),(3,4,1,2),(4,4,2,3),(3,5,1,1),(4,4,1,1)]
    N=entries=0
    for a,b,t,s in samples:
        n,e=check(a,b,t,s);N+=n;entries+=e
    # Purely rational global inequalities supporting tuning, not the infinite proof.
    for a in range(2,15):
        for b in range(2,15):
            n=a+b-1
            for yy in [F(1,9),F(1,2),F(1),F(3,2),F(4),F(13)]:
                R=(a*yy+b)**2/(n*yy)
                gap=(a*yy-b)**2/(n*yy)
                assert R==F(4*a*b,n)+gap
                assert R>=F(4*a*b,n)
    print(f'TWO_CLIQUE_WEIGHTED_COVARIANCE_CHECKS_PASSED profiles={len(samples)} vertices={N} covariance_entries={entries} tuning_profiles={13*13*6}')

if __name__=='__main__':main()
