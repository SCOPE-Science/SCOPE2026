"""Deterministic finite checks for correlated longest Bernoulli runs."""
from fractions import Fraction
from itertools import product
from math import factorial, exp, log


def formula(n,k,eps):
    p=Fraction(1,2**(k+1))
    q=p*(1-eps/2)**(k+1)
    m=n-k
    cross=lambda d: eps*Fraction(1,2**(k+d+2))*(1-eps/2)**(k-d)
    cov=m*(q-p*p)+2*sum((m-d)*(cross(d)-p*p) for d in range(1,min(k,m-1)+1))
    return p,q,cov,cross

def exact(n,k,eps):
    prob=[(2-eps)/4,eps/4,eps/4,(2-eps)/4] # 00 01 10 11
    m=n-k
    sx=sy=sb=sxy=Fraction(0)
    for vals in product(range(4),repeat=n):
        weight=Fraction(1)
        for a in vals:weight*=prob[a]
        if not weight:continue
        X=[a>>1 for a in vals]
        Y=[a&1 for a in vals]
        IsX=[int(X[i-1]==0 and all(X[j]==1 for j in range(i,i+k))) for i in range(1,n-k+1)]
        IsY=[int(Y[i-1]==0 and all(Y[j]==1 for j in range(i,i+k))) for i in range(1,n-k+1)]
        nx=sum(IsX);ny=sum(IsY)
        sx+=weight*nx;sy+=weight*ny;sb+=weight*sum(a*b for a,b in zip(IsX,IsY));sxy+=weight*nx*ny
    return sx,sy,sb,sxy-sx*sy

def check():
    checks=0
    for n in range(3,8):
        for k in range(1,min(n,4)):
            for eps in (Fraction(0),Fraction(1,2),Fraction(1)):
                p,q,cov,cross=formula(n,k,eps)
                ex,ey,eb,ecov=exact(n,k,eps)
                m=n-k
                assert ex==ey==m*p,(n,k,eps,ex,m*p);checks+=1
                assert eb==m*q,(n,k,eps,eb,m*q);checks+=1
                assert ecov==cov,(n,k,eps,ecov,cov);checks+=1
                for d in range(1,min(k,m-1)+1):
                    # exact cross event from local overlap enumeration
                    i=1;j=i+d
                    if j>n-k:continue
                    local=Fraction(0)
                    for vals in product(range(4),repeat=j+k):
                        weight=Fraction(1)
                        for a in vals:weight*=((2-eps)/4 if a in (0,3) else eps/4)
                        X=[a>>1 for a in vals];Y=[a&1 for a in vals]
                        if X[i-1]==0 and all(X[h] for h in range(i,i+k)) and Y[j-1]==0 and all(Y[h] for h in range(j,j+k)):
                            local+=weight
                    assert local==cross(d),(n,k,d,eps,local,cross(d));checks+=1
    assert Fraction(0)==formula(9,3,Fraction(0))[3](1)
    checks+=1
    print(f'PASS {checks} exact rational formula assertions')

if __name__=='__main__':check()
