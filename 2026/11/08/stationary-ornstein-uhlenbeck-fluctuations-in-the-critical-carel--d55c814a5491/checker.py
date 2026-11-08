#!/usr/bin/env python3
"""Exact finite-state checks for stationary occupancy of the post-loss coupon process.
No external libraries required. All equalities use Fraction, not floating-point tests.
"""
from fractions import Fraction as F
from math import comb

checks = 0

def confirm(a,b,label):
    global checks
    assert a == b, (label, a, b)
    checks += 1

def solve(a,b):
    n=len(b)
    a=[list(row)+[b[i]] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        scale=a[j][j]
        a[j]=[v/scale for v in a[j]]
        for i in range(n):
            if i != j:
                scale=a[i][j]
                if scale:
                    a[i]=[v-scale*w for v,w in zip(a[i],a[j])]
    return [row[-1] for row in a]

def matvec(v,P):
    return [sum(v[k]*P[k][j] for k in range(len(v))) for j in range(len(v))]

for n in range(2,9):
    for p in [F(1,2),F(1,3),F(2,5)]:
        q=1-p
        P=[]
        for k in range(n+1):
            row=[]
            for j in range(n+1):
                a=F(k,n)*comb(k,j)*q**j*p**(k-j) if j<=k else F(0)
                b=F(n-k,n)*comb(k+1,j)*q**j*p**(k+1-j) if j<=k+1 else F(0)
                row.append(a+b)
            confirm(sum(row),1,('row sum',n,p,k))
            P.append(row)
        A=[[P[i][j]-int(i==j) for i in range(n+1)] for j in range(n+1)]
        A[-1]=[F(1)]*(n+1)
        rhs=[F(0)]*n+[F(1)]
        stat=solve(A,rhs)
        confirm(matvec(stat,P),stat,('stationarity',n,p))
        confirm(sum(stat),1,('mass',n,p))
        for r in range(n+1):
            formula=F(1)
            for j in range(1,r+1):
                formula *= F(j,1)*q**j/(n*(1-q**j)+j*q**j)
            from_count=sum(stat[k]*F(comb(k,r),comb(n,r)) for k in range(r,n+1))
            confirm(formula,from_count,('factorial',n,p,r))
        mean=sum(k*stat[k] for k in range(n+1))
        alpha=q/(n*p+q)
        confirm(mean,n*alpha,('mean',n,p))
        second=sum(k*k*stat[k] for k in range(n+1))
        variance=second-mean*mean
        cov=-n*p*p*q*q/((n*p+q)**2*(n*p*(1+q)+2*q*q))
        predicted=n*alpha*(1-alpha)+n*(n-1)*cov
        confirm(variance,predicted,('variance',n,p))
        if n>=2:
            m2=F(2)*q*q*alpha/(n*(1-q*q)+2*q*q)
            confirm(m2-alpha*alpha,cov,('distinct marginal covariance',n,p))
        a=q*(1-F(1,n))
        for lag in range(1,5):
            # conditional mean of future count in the Markov chain, tested for each starting state
            for k in range(n+1):
                v=[F(0)]*(n+1);v[k]=1
                for _ in range(lag): v=matvec(v,P)
                cond=sum(j*v[j] for j in range(n+1))
                confirm(cond,mean+a**lag*(k-mean),('regression',n,p,lag,k))
            cxy=sum(stat[k]*k*(mean+a**lag*(k-mean)) for k in range(n+1))-mean**2
            confirm(cxy,a**lag*variance,('lag covariance',n,p,lag))
print('PASS',checks,'exact rational assertions')
