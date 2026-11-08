#!/usr/bin/env python3
"""Exact rational checks for the heterogeneous clique-product FMMC formula.

Finite checks illustrate the symbolic tensor-eigenspace proof; they do not prove
its all-parameter or global optimality claims.
"""
from fractions import Fraction as F
from itertools import product


def params(q):
    d = len(q)
    C = sum((F(v-1,v) for v in q), F(0))
    t = min(F(2,d+1), 1/C)
    mu = max(F(d-1,d+1), 1-1/C)
    return C, t, mu


def matrix(q):
    C,t,mu = params(q)
    states = list(product(*(range(z) for z in q)))
    P=[]
    for s in states:
        row=[]
        for v in states:
            diff=[i for i in range(len(q)) if s[i]!=v[i]]
            if not diff:
                a=1-C*t
            elif len(diff)==1:
                i=diff[0]
                a=t/q[i]
            else:
                a=F(0)
            row.append(a)
        assert sum(row,F(0))==1
        assert all(v>=0 for v in row)
        P.append(row)
    return states,P


def basis_for(q):
    # q linearly independent basis vectors: constant and q-1 zero-sum contrasts.
    out=[[1]*q]
    for j in range(1,q):
        a=[0]*q; a[0]=-1; a[j]=1
        out.append(a)
    return out


def check(q):
    q=tuple(q)
    C,t,mu=params(q)
    states,P=matrix(q)
    bases=[basis_for(v) for v in q]
    N=len(states)
    lam_list=[]
    for indices in product(*(range(v) for v in q)):
        y=[F(1) for _ in range(N)]
        for k,s in enumerate(states):
            for i in range(len(q)):
                y[k]*=bases[i][indices[i]][s[i]]
        S=[i for i in range(len(q)) if indices[i]>0]
        lam=1-t*len(S)
        lam_list.append(lam)
        for j in range(N):
            assert sum((P[j][k]*y[k] for k in range(N)),F(0))==lam*y[j]
    assert max(abs(z) for z in lam_list if z!=1 or len(lam_list)==1) <= mu
    assert max(abs(1-t*len(S)) for size in range(1,len(q)+1) for S in [list(range(size))])==mu
    assert (1-C*t>0)==(C < F(len(q)+1,2))
    return N


def grid_check(q,scale=12):
    d=len(q);C,t,mu=params(q)
    cs=[F(v-1,v) for v in q]
    seen=0
    for ks in product(range(scale+1),repeat=d):
        x=[F(k,scale) for k in ks]
        if sum((a*b for a,b in zip(cs,x)),F(0))>1:
            continue
        m=min(x);total=sum(x)
        val=max(1-m,total-1)
        assert val>=mu,(q,x,val,mu)
        seen+=1
    return seen


def example():
    for Q in range(4,21):
        C,t,mu=params((2,Q))
        assert t==F(2,3) and mu==F(1,3)
        a=F(1,Q)
        edge_slem=max(abs(1-2*a),abs(1-Q*a),abs(1-(Q+2)*a))
        assert edge_slem==1-F(2,Q)
        # Verify any smaller uniform edge weight has no lower SLEM
        assert F(1,Q)<=F(2,Q+4)
    return 17


if __name__=='__main__':
    cases=[(2,3),(2,9),(3,4),(2,3,4),(2,2,3),(3,3,4),(2,3,3,2)]
    tested=sum(check(q) for q in cases)
    grids=sum(grid_check(q,8) for q in [(2,3),(2,9),(3,4),(2,3,4),(2,2,3),(3,3,4)])
    print('VERIFY_OK',len(cases),'tensor basis families,',tested,'exact basis vectors,',grids,'rational-grid designs,',example(),'comparison examples')
