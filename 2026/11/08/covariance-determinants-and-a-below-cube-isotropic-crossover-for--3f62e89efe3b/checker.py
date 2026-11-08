"""Exact moment and isotropic checks for maximal-ranked chain polytopes.
Python 3 standard library only. No third-party papers or data are embedded.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

def formula(ms):
    d=sum(ms); D=(d+1)*(d+2)
    means=[F(m+1,2*(d+1)) for m in ms]
    lam=[F((m+1)*(m+2),12*D) for m in ms]
    a=[F((m+1)*(2*m+1),6*D) for m in ms]
    R=F(1)-F(3,2*(d+1))*sum((F(m*(m+1),2*m+1) for m in ms),F(0))
    det=R
    for m,aa,ll in zip(ms,a,lam): det*=aa*ll**(m-1)
    vol=F(1,factorial(d))
    for m in ms: vol*=factorial(m)
    return means,det,vol

def moment_formula(ms):
    d=sum(ms); D=(d+1)*(d+2)
    mean=[]; raw=[]; groups=[]
    for i,m in enumerate(ms):
        for r in range(m):
            groups.append(i); mean.append(F(m+1,2*(d+1)))
    for a,i in enumerate(groups):
        row=[]
        for b,j in enumerate(groups):
            mi,mj=ms[i],ms[j]
            if a==b: z=F((mi+1)*(mi+2),3*D)
            elif i==j: z=F((mi+1)*(mi+2),4*D)
            else: z=F((mi+1)*(mj+1),4*D)
            row.append(z)
        raw.append(row)
    return mean, [[raw[i][j]-mean[i]*mean[j] for j in range(d)] for i in range(d)]

def independent_chamber_moments(ms):
    # Average over all within-layer ordering permutations. In each chamber,
    # consecutive order-statistic gaps are standard-simplex Dirichlet(1,...,1).
    d=sum(ms);D=(d+1)*(d+2)
    means=[];second=[]; groups=[]; coords=[]
    for i,m in enumerate(ms):
        for c in range(m): groups.append(i);coords.append(c)
    for i in range(d):
        m=ms[groups[i]]
        means.append(sum((F(r,d+1) for r in range(1,m+1)),F(0))/m)
    for i in range(d):
        arr=[];m=ms[groups[i]]
        for j in range(d):
            n=ms[groups[j]]
            if i==j:
                val=sum((F(r*(r+1),D) for r in range(1,m+1)),F(0))/m
            elif groups[i]==groups[j]:
                val=sum((F(r*s+min(r,s),D) for r in range(1,m+1) for s in range(1,m+1) if r!=s),F(0))/(m*(m-1))
            else:
                val=sum((F(r*s,D) for r in range(1,m+1) for s in range(1,n+1)),F(0))/(m*n)
            arr.append(val)
        second.append(arr)
    return means,[[second[i][j]-means[i]*means[j] for j in range(d)] for i in range(d)]

def determinant(M):
    a=[row[:] for row in M]; n=len(a); det=F(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        assert pivot is not None
        if pivot!=i:a[i],a[pivot]=a[pivot],a[i];det=-det
        p=a[i][i];det*=p
        for j in range(i+1,n):
            if a[j][i]:
                f=a[j][i]/p
                for h in range(i+1,n):a[j][h]-=f*a[i][h]
                a[j][i]=F(0)
    return det

if __name__=='__main__':
    trials=[(m,) for m in range(1,7)]+[(2,2),(1,3),(3,2),(2,3,1),(1,1,1),(2,2,2),(3,1,2),(2,1,1,1),(4,2,1)]
    for ms in trials:
        mean,det,volume=formula(ms)
        m1,cov=moment_formula(ms)
        m2,cov2=independent_chamber_moments(ms)
        assert mean==[m1[sum(ms[:i])] for i in range(len(ms))]
        assert m1==m2 and cov==cov2 and determinant(cov)==det
        assert det>0 and volume>0
    # Compare the squared affine isotropic constant with the cube value 1/12.
    # L(C)^2=(det(Cov)/Vol(C)^2)^(1/d).
    ms=(1,1);d=sum(ms);_,det,vol=formula(ms)
    assert 12**d*det>vol**2
    ms=(30,30);d=sum(ms);_,det,vol=formula(ms)
    assert 12**d*det<vol**2
    print('RANKED_CHAIN_COVARIANCE_EXACT_CHECKS_PASSED',len(trials),'cases; two-sided cube comparisons PASS')
