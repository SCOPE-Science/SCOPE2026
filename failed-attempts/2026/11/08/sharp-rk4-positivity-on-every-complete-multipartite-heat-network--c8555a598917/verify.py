#!/usr/bin/env python3
"""Exact rational checks supporting a spectral positivity theorem for RK4 on multipartite heat networks."""
from fractions import Fraction as F
from itertools import combinations


def r(x):
    return 1-x+x*x/F(2)+x**3*(-F(1,6))+x**4/F(24)

def partitions(n):
    # nondecreasing integer partitions into at least two parts
    def rec(s, m):
        if s == 0:
            yield ()
            return
        for a in range(m,s+1):
            for tail in rec(s-a,a):
                yield (a,)+tail
    return [p for p in rec(n,1) if len(p)>=2]

def laplacian(part):
    n=sum(part)
    labels=[j for j,a in enumerate(part) for _ in range(a)]
    return [[F(n-part[labels[i]]) if i==j else (F(-1) if labels[i]!=labels[j] else F(0)) for j in range(n)] for i in range(n)],labels

def matmul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def direct(part,z):
    l,_=laplacian(part)
    n=len(l)
    p=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    power=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(1,5):
        power=matmul(power,l)
        for i in range(n):
            for j in range(n):
                p[i][j]+=(-z)**k*power[i][j]/[1,1,2,6,24][k]
    return p

def closed(part,z):
    n=sum(part)
    _,labels=laplacian(part)
    out=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if labels[i]!=labels[j]:
                val=(1-r(n*z))/n
            else:
                p=part[labels[i]];d=n-p
                off=(F(d)*z*z/F(24))*(12-4*(n+d)*z+(n*n+n*d+d*d)*z*z)
                val=off+(r(d*z) if i==j else 0)
            row.append(val)
        out.append(row)
    return out

def run():
    checks=0
    # Identity checks at rational step lengths; group all graph partitions up to order nine.
    for n in range(2,10):
        for part in partitions(n):
            for k in (0,1,2,4,7,10,11,12,15):
                z=F(k,4*n)
                actual=direct(part,z)
                formula=closed(part,z)
                assert actual==formula,(part,z)
                checks+=n*n
                assert all(sum(row)==1 for row in actual),(part,z)
                checks+=n
                truth=r(n*z)<=1
                assert (all(v>=0 for row in actual for v in row))==truth,(part,z)
                checks+=1
                if z>0 and r(n*z)>1:
                    assert actual[0][-1]<0,(part,z)
                    checks+=1
    # Positive quadratic discriminant certificate: Q(z)>0 for n>=2, 1<=d<n.
    for n in range(2,300):
        for d in range(1,n):
            discr=16*(n+d)**2-48*(n*n+n*d+d*d)
            assert discr == -32*n*n-16*n*d-32*d*d <0
            checks+=1
    # Cubic monotonicity discriminant and exact sign bracketing for RK4 real stability cutoff.
    assert 24-12*F(2785,1000)+4*F(2785,1000)**2-F(2785,1000)**3>0
    assert 24-12*F(2786,1000)+4*F(2786,1000)**2-F(2786,1000)**3<0
    checks+=2
    print(f'VERIFY_OK assertions={checks} numerical_domain=partitions_of_2_to_9 exact_fractions=True')
if __name__=='__main__':run()
