#!/usr/bin/env python3
"""Exact-rational verification of a balanced multipartite leader-allocation theorem.

The symbolic proof for all graph sizes is in RESULT.md; these tests are finite crosschecks.
"""
from fractions import Fraction as Q
from itertools import product


def inverse_trace(a):
    size=len(a)
    if not size: return Q(0)
    mat=[[Q(v) for v in row]+[Q(i==j) for j in range(size)] for i,row in enumerate(a)]
    for t in range(size):
        p=next(j for j in range(t,size) if mat[j][t])
        mat[t],mat[p]=mat[p],mat[t]
        pivot=mat[t][t]
        mat[t]=[v/pivot for v in mat[t]]
        for i in range(size):
            if i!=t:
                c=mat[i][t]
                if c: mat[i]=[v-c*w for v,w in zip(mat[i],mat[t])]
    return sum((mat[i][size+i] for i in range(size)),Q(0))


def objective_direct(r,n,fs):
    d=(r-1)*n
    groups=[i for i,f in enumerate(fs) for _ in range(f)]
    m=len(groups)
    L=[[d if i==j else (-1 if groups[i]!=groups[j] else 0)
        for j in range(m)] for i in range(m)]
    return inverse_trace(L)


def objective_formula(r,n,fs):
    d=(r-1)*n
    m=sum(fs)
    S=sum((Q(f,d+f) for f in fs),Q(0))
    G=sum((Q(f,(d+f)**2) for f in fs),Q(0))
    assert S<1
    return Q(m-r,d)+sum((Q(1,d+f) for f in fs),Q(0))+G/(1-S)


def optimal_followers(r,n,F):
    q,t=divmod(F,n)
    return (n,)*q+(t,)*(t>0)+(0,)*(r-q-(t>0))


def pair_certificate(r,n,fs,i,j):
    d=(r-1)*n
    other=[f for u,f in enumerate(fs) if u!=i and u!=j]
    s=fs[i]+fs[j]
    S=sum((Q(f,d+f) for f in other),Q(0))
    G=sum((Q(f,(d+f)**2) for f in other),Q(0))
    c=1+S; T=2*d+s; U=4*d+s
    # derivative d(trace(L_F^-1))/d(f_i f_j) at fixed sum, including zero counts
    N=G*d*T+c*(U-c*T)
    assert U-c*T>=2*n
    assert N>0
    return N


def run():
    cases=0; matrix_checks=0; optimum_checks=0; pair_checks=0
    for r,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]:
        costs_by_F={}
        for fs in product(range(n+1),repeat=r):
            F=sum(fs)
            if not(1<=F<=r*n-1): continue
            cases+=1
            val=objective_formula(r,n,fs)
            assert val==objective_direct(r,n,fs),(r,n,fs,val)
            matrix_checks+=1
            for i in range(r):
                for j in range(i+1,r):
                    pair_certificate(r,n,fs,i,j)
                    pair_checks+=1
            costs_by_F.setdefault(F,[]).append((val,tuple(sorted(fs,reverse=True))))
        for F,opts in costs_by_F.items():
            target=optimal_followers(r,n,F)
            actual=min(v for v,fs in opts)
            assert actual==objective_formula(r,n,target)
            assert {fs for v,fs in opts if v==actual}=={target},(r,n,F)
            optimum_checks+=1
    # Empty and one-follower / one-leader boundaries
    assert objective_formula(3,2,(0,0,1))==Q(1,4)
    assert objective_formula(2,2,(2,1))==objective_direct(2,2,(2,1))
    print('VERIFY_OK allocations=%d exact_inverse=%d optimal_budgets=%d derivative_checks=%d' %
         (cases,matrix_checks,optimum_checks,pair_checks))

if __name__=='__main__':run()
