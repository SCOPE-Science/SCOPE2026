#!/usr/bin/env python3
"""Exact integer matrix-tree and local-spectrum checks for two regular graphs.

Run: python3 verify.py (Python 3 standard library only).
"""
from fractions import Fraction
from math import comb


def rook_graph():
    V=[(i,j) for i in range(4) for j in range(4)]
    E={(min(a,b),max(a,b)) for a in V for b in V if a!=b and (a[0]==b[0] or a[1]==b[1])}
    return V,E


def shrikhande_graph():
    V=[(i,j) for i in range(4) for j in range(4)]
    S=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
    E=set()
    for x in V:
        for d in S:
            y=((x[0]+d[0])%4,(x[1]+d[1])%4)
            E.add((min(x,y),max(x,y)))
    return V,E


def bareiss(M):
    A=[row[:] for row in M]
    n=len(A)
    if n==0:return 1
    prev=1;sign=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None:return 0
            A[k],A[r]=A[r],A[k];sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*p-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=p
    return sign*A[-1][-1]


def tree_count(V,E,root,z):
    order={u:i for i,u in enumerate(V)}
    n=len(V)
    L=[[0]*n for _ in range(n)]
    for a,b in E:
        w=z if root in (a,b) else 1
        i,j=order[a],order[b]
        L[i][i]+=w;L[j][j]+=w
        L[i][j]-=w;L[j][i]-=w
    drop=order[V[-1]]
    return bareiss([[L[i][j] for j in range(n) if j!=drop] for i in range(n) if i!=drop])


def petersen_graph():
    from itertools import combinations
    V=list(combinations(range(5),2))
    E={(min(a,b),max(a,b)) for a in V for b in V if a!=b and set(a).isdisjoint(b)}
    return V,E


def adjacency_local(V,E,u):
    N=sorted(v for v in V if (min(u,v),max(u,v)) in E)
    return N,[[int((min(x,y),max(x,y)) in E and x!=y) for y in N] for x in N]


def matmul(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def charpoly(A):
    # Newton identities: coefficient of t^(n-j) is -(1/j)*sum_{i=1}^j coeff[j-i] trace(A^i).
    n=len(A);powers=[];B=[row[:] for row in A]
    for j in range(1,n+1):
        powers.append(sum(B[i][i] for i in range(n)))
        B=matmul(B,A)
    c=[1]
    for j in range(1,n+1):
        num=-sum(c[j-i]*powers[i-1] for i in range(1,j+1))
        assert num%j==0
        c.append(num//j)
    return tuple(c)


def poly_product(factors):
    out=[Fraction(1)]
    for p in factors:
        q=[Fraction(0)]*(len(out)+1)
        for j,v in enumerate(out):
            q[j]+=v*(1-p);q[j+1]+=v*p
        out=q
    return [Fraction(0)]+out


def verify():
    check=0
    for name,build,loc_char,ps in [
        ('rook',rook_graph,(1,0,-6,-4,9,12,4),[Fraction(1,4)]+[Fraction(5,32)]*4),
        ('shrikhande',shrikhande_graph,(1,0,-6,0,9,0,-4),[Fraction(7,32)]*2+[Fraction(5,32)]*2+[Fraction(1,8)])]:
        V,E=build();u=(0,0)
        assert len(V)==16 and len(E)==48;check+=2
        for v in V:
            neighbors={w for w in V if (min(v,w),max(v,w)) in E}
            assert len(neighbors)==6;check+=1
            for w in V:
                if w==v:continue
                count=len(neighbors & {x for x in V if (min(w,x),max(w,x)) in E})
                assert count==2;check+=1
        N,A=adjacency_local(V,E,u)
        assert len(N)==6 and all(sum(row)==2 for row in A);check+=2
        assert charpoly(A)==loc_char;check+=1
        # Check expected factorization in coefficient form separately below.
        coeff=poly_product(ps)
        assert sum(coeff)==1;check+=1
        base=tree_count(V,E,u,1)
        for z in range(7):
            eval_poly=sum(x*z**i for i,x in enumerate(coeff))
            value=Fraction(tree_count(V,E,u,z),base)
            assert value==eval_poly,(name,z,value,eval_poly)
            check+=1
        print(name,'spanning trees',base,'degree pgf',coeff)
    V,E=petersen_graph()
    assert len(V)==10 and len(E)==15;check+=2
    N,H=adjacency_local(V,E,V[0])
    assert len(N)==3 and all(sum(row)==0 for row in H);check+=2
    pg=poly_product([Fraction(2,5)]*2)
    b=tree_count(V,E,V[0],1)
    for z in range(4):
        assert Fraction(tree_count(V,E,V[0],z),b)==sum(c*z**i for i,c in enumerate(pg));check+=1
    R=poly_product([Fraction(1,4)]+[Fraction(5,32)]*4)
    S=poly_product([Fraction(7,32)]*2+[Fraction(5,32)]*2+[Fraction(1,8)])
    diff=[a-b for a,b in zip(R,S)]
    # Polynomial z(z-1)^3(5z+27)^2 / 2^23, coefficients via integer convolution.
    def multiply(A,B):
        C=[0]*(len(A)+len(B)-1)
        for i,a in enumerate(A):
            for j,b in enumerate(B):C[i+j]+=a*b
        return C
    want=multiply([0,1],multiply(multiply([-1,1],multiply([-1,1],[-1,1])),multiply([27,5],[27,5])))
    assert diff==[Fraction(c,2**23) for c in want];check+=1
    assert sum(i*diff[i] for i in range(7))==0;check+=1
    assert sum(i*(i-1)*diff[i] for i in range(7))==0;check+=1
    assert sum(i*(i-1)*(i-2)*diff[i] for i in range(7))==Fraction(3,4096);check+=1
    assert diff[1]==Fraction(-729,2**23);check+=1
    print('VERIFY_OK',check,'exact assertions; difference coefficients:',diff)

if __name__=='__main__':verify()
