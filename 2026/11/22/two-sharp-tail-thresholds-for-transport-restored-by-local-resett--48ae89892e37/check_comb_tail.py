"""Exact checks for a random comb with tooth-local Poisson returns.

Run: python3 check_comb_tail.py
Only Python standard-library modules are required.
The infinite-volume and tail asymptotics are proved analytically, not by enumeration.
"""
from fractions import Fraction as F
from math import acosh, cosh, sqrt, isclose


def solve(A, b):
    """Exact rational Gauss-Jordan elimination."""
    n=len(b)
    A=[list(map(F,row))+[F(bi)] for row,bi in zip(A,b)]
    for j in range(n):
        k=next(i for i in range(j,n) if A[i][j])
        A[j],A[k]=A[k],A[j]
        z=A[j][j]
        A[j]=[a/z for a in A[j]]
        for i in range(n):
            if i!=j:
                z=A[i][j]
                A[i]=[a-z*b for a,b in zip(A[i],A[j])]
    return [row[-1] for row in A]


def tooth_time(L,r):
    """Independent exact first-passage-time Poisson equation."""
    A=[]
    for k in range(1,L+1):
        row=[F(0)]*L
        row[k-1]=r+(2 if k<L else 1)
        if k>1: row[k-2]-=1
        if k<L: row[k]-=1
        A.append(row)
    return solve(A,[1]*L)[0]


def closed_tooth(L,r):
    if r==0:return float(L)
    th=acosh(1+float(r)/2)
    return (1-cosh((L-.5)*th)/cosh((L+.5)*th))/float(r)


def stationary_ring(Ls,p,q,a,r):
    states=[]
    for i,L in enumerate(Ls):
        states += [(i,j) for j in range(L+1)]
    idx={state:k for k,state in enumerate(states)}
    Q=[[F(0) for _ in states] for _ in states]
    n=len(Ls)
    for t,(i,j) in enumerate(states):
        edges=[]
        if j==0:
            edges.extend([((i+1)%n,0,p),((i-1)%n,0,q),(i,1,a)])
        else:
            edges.append((i,j-1,F(1)))
            if j<Ls[i]:edges.append((i,j+1,F(1)))
            edges.append((i,0,r))
        for ii,jj,rate in edges:
            Q[t][idx[(ii,jj)]]+=rate
            Q[t][t]-=rate
    A=[[Q[k][j] for k in range(len(states))] for j in range(len(states)-1)]
    A.append([F(1)]*len(states))
    b=[F(0)]*(len(states)-1)+[F(1)]
    pi=solve(A,b)
    return (p-q)*sum(pi[idx[(i,0)]] for i in range(n))


def run():
    checks=0
    for r in [F(1,10),F(1,2),F(2,1),F(7,3)]:
        for L in range(1,11):
            x=tooth_time(L,r)
            assert isclose(float(x),closed_tooth(L,r),rel_tol=2e-12,abs_tol=2e-12)
            checks+=1
        for L in range(1,10):
            d=float(tooth_time(L,r)-tooth_time(L-1,r)) if L>1 else float(tooth_time(1,r))
            th=acosh(1+float(r)/2)
            d2=cosh(th/2)**2/(cosh((L-.5)*th)*cosh((L+.5)*th))
            assert isclose(d,d2,rel_tol=2e-12,abs_tol=2e-12)
            checks+=1
    for L in range(1,9):
        # The first derivative at r=0 follows exactly from second hitting-time moment.
        u=tooth_time(L,F(1,10000000))
        expected= L-F(1,10000000)*F(L*(L+1)*(2*L+1),6)
        assert abs(float(u-expected))<1e-9
        checks+=1
    for lengths in ([1,2,3],[2,1,4],[3,3,1]):
        for r in [F(1,3),F(3,5)]:
            p,q,a=F(3),F(1),F(1,2)
            observed=stationary_ring(lengths,p,q,a,r)
            expect=(p-q)/(1+a*sum(tooth_time(L,r) for L in lengths)/len(lengths))
            assert observed==expect,(lengths,r,observed,expect)
            checks+=1
    print('PASS',checks,'exact recurrence / incremental / finite-ring checks')

if __name__=='__main__':run()
