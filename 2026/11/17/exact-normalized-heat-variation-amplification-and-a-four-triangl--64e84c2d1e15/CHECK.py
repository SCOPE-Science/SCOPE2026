#!/usr/bin/env python3
"""Exact-rational independent diagnostics for normalized heat variation on friendship graphs.
Uses only Python standard library. Finite checks corroborate, not replace, all-size proofs.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def graph(m):
    n = 1 + 2*m
    edges=[]
    for j in range(m):
        a,b=1+2*j,2+2*j
        edges.extend([(0,a),(0,b),(a,b)])
    return n,edges

def generator(m):
    n,edges=graph(m)
    deg=[0]*n
    for a,b in edges: deg[a]+=1;deg[b]+=1
    Q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n): Q[i][i]=-F(1)
    for a,b in edges:
        Q[a][b]+=F(1,deg[a]); Q[b][a]+=F(1,deg[b])
    return Q

def coefficients(m,x):
    # E(q)x = constant + q*slow + q**3*fast.
    h=x[0]
    s=[(x[1+2*j]+x[2+2*j])/2 for j in range(m)]
    a=[(x[1+2*j]-x[2+2*j])/2 for j in range(m)]
    mean=sum(s,F(0))/m
    avg=(h+2*mean)/3
    delta=mean-h
    C=[avg]*(2*m+1)
    U=[F(0)]*(2*m+1)
    V=[-2*delta/3]+[F(0)]*(2*m)
    for j in range(m):
        U[1+2*j]=U[2+2*j]=s[j]-mean
        V[1+2*j]=delta/3+a[j]
        V[2+2*j]=delta/3-a[j]
    return C,U,V

def apply(m,q,x):
    C,U,V=coefficients(m,x)
    return [C[i]+q*U[i]+q*q*q*V[i] for i in range(len(x))]

def tv(m,x):
    return sum((abs(x[i]-x[j]) for i,j in graph(m)[1]),F(0))

def matvec(M,v):
    return [sum((a*b for a,b in zip(row,v)),F(0)) for row in M]

def predicted(m,q):
    return F(2*(m-1),m)*q-F(m-2,m)*q**3

def test():
    ode=0; cuts=0; witness=0; signed=0; thresholds=0
    for m in range(1,7):
        Q=generator(m)
        n=2*m+1
        # Algebraic differential-system check, for each standard basis.
        for j in range(n):
            x=[F(0)]*n;x[j]=F(1)
            C,U,V=coefficients(m,x)
            assert [C[i]+U[i]+V[i] for i in range(n)]==x
            assert matvec(Q,C)==[F(0)]*n
            assert matvec(Q,U)==[-z/2 for z in U]
            assert matvec(Q,V)==[-3*z/2 for z in V]
            ode+=1
        for q in [F(1),F(1,2),F(3,4),F(9,10),F(1,4),F(15,16)]:
            k=predicted(m,q)
            assert k>=0
            for bits in product([0,1], repeat=2*m):
                x=[F(0)]+list(map(F,bits))
                j=tv(m,x)
                if j:
                    assert tv(m,apply(m,q,x))<=k*j,(m,q,bits)
                    cuts+=1
            if m>=1:
                x=[F(0)]*(2*m+1)
                x[1]=x[2]=F(1)
                assert tv(m,apply(m,q,x))==k*tv(m,x)
                witness+=1
        rng=Random(100+m)
        q=F(17,19)
        k=predicted(m,q)
        for _ in range(300):
            x=[F(rng.randint(-20,20)) for _ in range(n)]
            if tv(m,x):
                assert tv(m,apply(m,q,x))<=k*tv(m,x)
                signed+=1
    # Check initial derivative and strict threshold as exact rational inequalities.
    for m in range(1,30):
        derivative=F(m-4,2*m) if m>=2 else -F(3,2)
        if m>=2:
            assert derivative == -F(m-1,m)+F(3*(m-2),2*m)
        if m>=5:
            assert predicted(m,F(999,1000))>1
        else:
            assert predicted(m,F(999,1000))<1
        thresholds+=1
    print('GENERATOR_POLYNOMIAL_IDENTITIES_PASSED',ode)
    print('EXHAUSTIVE_BINARY_CUT_INEQUALITIES_PASSED',cuts)
    print('EXACT_PAIR_WITNESS_ATTAINMENT_PASSED',witness)
    print('ARBITRARY_SIGNED_INPUT_INEQUALITIES_PASSED',signed)
    print('AMPLIFICATION_THRESHOLD_COMPARISONS_PASSED',thresholds)
    print('ALL_NORMALIZED_FRIENDSHIP_GRAPH_HEAT_TESTS_PASSED')

if __name__=='__main__':
    test()
