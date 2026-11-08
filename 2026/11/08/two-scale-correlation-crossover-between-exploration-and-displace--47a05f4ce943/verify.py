#!/usr/bin/env python3
"""Exact small-size enumeration and analytic formula checks for coordinate exploration and displacement."""
from fractions import Fraction as F
from itertools import product
from math import exp, log, sqrt

def formula(n,t):
    p=F(n-1,n)**t
    a=F(n-2,n)**t
    b=F(n-3,n-1)**t
    d=F(n-4,n)**t
    mean_D=n*(1-p)
    mean_H=F(n,2)*(1-a)
    cov=F(n,2)*p*(1+(n-1)*b-n*a)
    vD=n*(p+(n-1)*a-n*p*p)
    vH=F(n,4)*(1+(n-1)*d-n*a*a)
    return mean_D,mean_H,cov,vD,vH

def enumerate_exact(n,t):
    S=[0]*5
    for seq in product(range(n),repeat=t):
        counts=[0]*n
        for i in seq: counts[i]+=1
        D=sum(x!=0 for x in counts)
        H=sum(x%2 for x in counts)
        for j,v in enumerate((D,H,D*H,D*D,H*H)):S[j]+=v
    den=n**t
    ED,EH,EDH,ED2,EH2=[F(x,den) for x in S]
    return ED,EH,EDH-ED*EH,ED2-ED*ED,EH2-EH*EH

def main():
    cases=0
    for n in range(3,8):
        for t in range(2,8):
            if n**t>120000:continue
            exact=enumerate_exact(n,t)
            predicted=formula(n,t)
            assert exact==predicted,(n,t,exact,predicted)
            assert predicted[2]>0 and predicted[3]>0 and predicted[4]>0
            cases+=1
    # Direct high-dimension limit checks, without claiming to prove asymptotics numerically.
    for c in [0.2,0.6,1.,2.,5.]:
        z=exp(-c); u=exp(-2*c)
        fD=z-(1+c)*u
        fH=1-(1+4*c)*exp(-4*c)
        g=1-(1+2*c)*u
        assert fD>0 and fH>0 and g>0
        limit=z*g/sqrt(fD*fH)
        for n in [10000,100000]:
            t=round(c*n)
            # floats have cancellation ~n times, sufficient at 1e5 for this audit
            p=(1-1/n)**t
            a=(1-2/n)**t
            b=(1-2/(n-1))**t
            d=(1-4/n)**t
            vD=n*(p+(n-1)*a-n*p*p)
            vH=n/4*(1+(n-1)*d-n*a*a)
            cov=n*p/2*(1+(n-1)*b-n*a)
            assert abs(cov/sqrt(vD*vH)-limit)<.006,(c,n,limit,cov/sqrt(vD*vH))
    for beta in [0.4,1.,1.4]:
        n=100000; t=round(beta*n*log(n)); p=(1-1/n)**t
        a=(1-2/n)**t; b=(1-2/(n-1))**t; d=(1-4/n)**t
        vD=n*(p+(n-1)*a-n*p*p)
        vH=n/4*(1+(n-1)*d-n*a*a)
        cov=n*p/2*(1+(n-1)*b-n*a)
        ratio=cov/sqrt(vD*vH)/sqrt(p)
        assert abs(ratio-1)<.08,(beta,ratio)
    print('PASS exact finite cases',cases,'moment identities',cases*5,'positive covariance/variances',cases*3,'asymptotic numerical checks',10+3)
if __name__=='__main__':main()
