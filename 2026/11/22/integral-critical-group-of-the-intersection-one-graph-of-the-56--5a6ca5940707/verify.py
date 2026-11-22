#!/usr/bin/env python3
"""Exact integer check for the degree-two del Pezzo intersection-one graph.
No nonstandard packages or network access are required.
"""
from collections import Counter, deque
from itertools import combinations
from math import prod


def curves():
    # A divisor is written dH - sum(m_i E_i); an exceptional E_i has m_i=-1.
    result=[]
    for i in range(7):
        m=[0]*7; m[i]=-1
        result.append((0,tuple(m)))
    for I in combinations(range(7),2):
        result.append((1,tuple(int(j in I) for j in range(7))))
    for I in combinations(range(7),5):
        result.append((2,tuple(int(j in I) for j in range(7))))
    for i in range(7):
        m=[1]*7; m[i]=2
        result.append((3,tuple(m)))
    return result


def pairing(a,b):
    return a[0]*b[0] - sum(x*y for x,y in zip(a[1],b[1]))


def construct(sink=55):
    C=curves(); n=len(C)
    assert n==56 and len(set(C))==56
    assert all(pairing(c,c)==-1 and 3*c[0]-sum(c[1])==1 for c in C)
    incidence=Counter()
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                x=pairing(C[i],C[j]);incidence[x]+=1
                assert x in (0,1,2)
                A[i][j]=int(x==1)
    assert incidence=={0:56*27,1:56*27,2:56}
    assert all(sum(row)==27 for row in A)
    assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
    # The ordinary Gosset graph has adjacency precisely at intersection zero.
    G0=[[j for j in range(n) if j!=i and pairing(C[i],C[j])==0]
        for i in range(n)]
    for start in range(n):
        distances=[-1]*n
        distances[start]=0
        work=deque([start])
        while work:
            x=work.popleft()
            for y in G0[x]:
                if distances[y]<0:
                    distances[y]=distances[x]+1;work.append(y)
        assert Counter(distances)=={0:1,1:27,2:27,3:1}
        assert all((distances[j]==2)==bool(A[start][j]) for j in range(n))
    # The unique geometric mate of c is -K-c.
    indices={c:i for i,c in enumerate(C)}
    mate=[indices[(3-d, tuple(1-x for x in m))] for d,m in C]
    assert all(mate[mate[i]]==i and mate[i]!=i for i in range(n))
    # Direct Gram decomposition A = Gram + I - 2P.
    for i in range(n):
        for j in range(n):
            assert A[i][j] == pairing(C[i],C[j]) + int(i==j) - 2*int(j==mate[i])
    # The 8x8 matrix V^t V J has one eigenvalue 28 and seven -12.
    V=[[d]+[-x for x in m] for d,m in C]
    T=[[sum(V[i][r]*V[i][s] for i in range(n)) * (1 if s==0 else -1)
        for s in range(8)] for r in range(8)]
    assert T[0]==[168]+[60]*7
    assert all(T[i]==[-60]+[-20 if j!=i else -32 for j in range(1,8)]
               for i in range(1,8))
    assert all(sum(T[i][k]*T[k][j] for k in range(8)) - 16*T[i][j]
               - 336*int(i==j)==0 for i in range(8) for j in range(8))
    L=[[27*int(i==j)-A[i][j] for j in range(n) if j!=sink]
       for i in range(n) if i!=sink]
    return L


def bareiss_det(a):
    """Fraction-free exact determinant with integer divisions checked."""
    B=[row[:] for row in a]; n=len(B)
    sign=1;prev=1
    for k in range(n-1):
        if B[k][k]==0:
            m=next((i for i in range(k+1,n) if B[i][k]),None)
            if m is None: return 0
            B[k],B[m]=B[m],B[k];sign=-sign
        p=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=B[i][j]*p-B[i][k]*B[k][j]
                assert v%prev==0
                B[i][j]=v//prev
            B[i][k]=0
        prev=p
    return sign*B[-1][-1]


def local_valuations(a,p,precision):
    """Perform invertible row/column operations over Z/(p^precision)."""
    mod=p**precision;n=len(a)
    B=[[x%mod for x in row] for row in a]
    vals=[]
    def vp(x):
        if x==0:return precision
        v=0
        while x%p==0: x//=p;v+=1
        return v
    for k in range(n):
        v=precision;pos=None
        for i in range(k,n):
            for j in range(k,n):
                z=vp(B[i][j])
                if z<v: v=z;pos=(i,j)
        assert pos is not None, 'Precision too small for remaining invariant factors'
        i,j=pos
        B[k],B[i]=B[i],B[k]
        for row in B:row[k],row[j]=row[j],row[k]
        pv=p**v
        assert B[k][k]%pv==0
        unit=B[k][k]//pv
        inv=pow(unit,-1,mod)
        B[k]=[(inv*x)%mod for x in B[k]]
        assert B[k][k]==pv
        for i in range(k+1,n):
            assert B[i][k]%pv==0
            q=B[i][k]//pv
            if q: B[i]=[(x-q*y)%mod for x,y in zip(B[i],B[k])]
        for j in range(k+1,n):
            assert B[k][j]%pv==0
            q=B[k][j]//pv
            if q:
                for i in range(k,n):
                    B[i][j]=(B[i][j]-q*B[i][k])%mod
        assert all(B[i][k]==0 for i in range(k+1,n))
        assert all(B[k][j]==0 for j in range(k+1,n))
        vals.append(v)
    assert vals==sorted(vals)
    return vals


def verify():
    assert len(curves())==56
    tree=2**128*3**35*7**26
    a=construct()
    assert bareiss_det(a)==tree
    reference={
        2:{0:8,1:14,2:12,4:15,5:6},
        3:{0:34,1:14,3:7},
        7:{0:29,1:26}}
    valuations={}
    for p,k in [(2,12),(3,10),(7,8)]:
        vals=local_valuations(a,p,k)
        assert Counter(vals)==reference[p]
        assert sum(vals)=={2:128,3:35,7:26}[p]
        valuations[p]=vals
    factors=[prod(p**valuations[p][i] for p in (2,3,7)) for i in range(55)]
    expected=Counter({1:8,2:14,4:7,28:5,336:14,3024:1,6048:6})
    assert Counter(factors)==expected
    assert all(factors[i+1]%factors[i]==0 for i in range(54))
    assert prod(factors)==tree
    for sink in (0,17):
        other=construct(sink)
        for p,k in ((2,12),(3,10),(7,8)):
            assert local_valuations(other,p,k)==valuations[p]
    print('DEGREE_TWO_DEL_PEZZO_INTERSECTION_ONE_CRITICAL_GROUP_VERIFIED_OK')
    print('prime_local_valuations:',{p:dict(Counter(vals)) for p,vals in valuations.items()})
    print('invariant_factors:',dict(expected))
    print('spanning_trees:',tree)

if __name__=='__main__':
    verify()
