#!/usr/bin/env python3
"""Exact-rational checks of cycle-resolvent probing formula and optimal partitions.
All computations use the Python standard library; finite checks supplement proof.
"""
from fractions import Fraction as F
from math import lcm
from itertools import product


def solve(A, b):
    n = len(A)
    rows = [[F(a) for a in row] + [F(v)] for row, v in zip(A,b)]
    for j in range(n):
        p = next(i for i in range(j,n) if rows[i][j])
        rows[j],rows[p] = rows[p],rows[j]
        piv = rows[j][j]
        rows[j] = [v/piv for v in rows[j]]
        for i in range(n):
            if i!=j and rows[i][j]:
                fac=rows[i][j]
                rows[i]=[x-fac*y for x,y in zip(rows[i],rows[j])]
    return [r[-1] for r in rows]


def resolvent(n,mu):
    A=[[F(2)+mu if i==j else F(-1) if (i-j)%n in (1,n-1) else F(0) for j in range(n)] for i in range(n)]
    g=solve(A,[F(int(i==0)) for i in range(n)])
    for i in range(n):
        assert sum(A[i][j]*g[j] for j in range(n))==int(i==0)
    assert all(g[j]==g[n-j] for j in range(1,n))
    return g


def test(n,k,mu):
    assert n%k==0 and 3<=k<n
    g=resolvent(n,mu)
    weights=[x*x for x in g]
    den=lcm(*(w.denominator for w in weights))
    weights=[int(w*den) for w in weights]
    colors=[0]*n
    best=None
    count=0
    winners=0
    exemplar=None
    def rec(i,top,energy):
        nonlocal best,count,winners,exemplar
        if i==n:
            if top+1!=k:return
            count+=1
            if best is None or energy<best:
                best=energy;winners=1;exemplar=tuple(colors)
            elif energy==best:winners+=1
            return
        for c in range(min(top+1,k-1)+1):
            colors[i]=c
            increment=sum(weights[i-j] for j in range(i) if colors[j]==c)
            rec(i+1,max(top,c),energy+increment)
    rec(1,0,0)
    m=n//k
    predicted=sum(weights[j*k] for j in range(1,m))*n//2
    assert 2*predicted==n*sum(weights[j*k] for j in range(1,m))
    assert best==predicted,(n,k,mu,best,predicted)
    assert winners==1,(n,k,mu,winners,exemplar)
    assert exemplar==tuple(i%k for i in range(n))
    print(f'n={n} k={k} shift={mu}, checked {count} partitions, unique unlabeled optimum, variance={4*F(best,den)}')
    return count


def check_estimator():
    n,k,mu=6,3,F(2,3)
    g=resolvent(n,mu)
    tr=n*g[0]
    vals=[]
    for signs in product((-1,1),repeat=n):
        stat=sum(signs[i]*signs[j]*g[(i-j)%n] for i in range(n) for j in range(n) if i%k==j%k)
        vals.append(stat)
    mean=sum(vals,F(0))/len(vals)
    variance=sum((s-mean)**2 for s in vals)/len(vals)
    predicted=4*sum((g[(i-j)%n]**2 for i in range(n) for j in range(i+1,n) if i%k==j%k),F(0))
    assert mean==tr and variance==predicted
    print('exhaustive 2^6 Rademacher-sign law: mean and exact variance verified')


if __name__=='__main__':
    check_estimator()
    total=0
    for n,k,mu in [(6,3,F(1,5)),(6,3,F(7,2)),(9,3,F(1,5)),(9,3,F(3,1)),(10,5,F(3,2)),(12,3,F(1,4)),(12,4,F(1,5)),(12,4,F(3,1))]:
        total+=test(n,k,mu)
    print(f'PASS: {total} exact partition comparisons; analytic theorem not inferred from finite checks')
