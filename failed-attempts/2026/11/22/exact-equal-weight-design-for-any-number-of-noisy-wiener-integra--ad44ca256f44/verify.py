#!/usr/bin/env python3
"""Supplemental rational checks for exact noisy-Wiener integral design.
No external packages; finite tests are not an infinite proof.
"""
from fractions import Fraction as F
from math import sqrt

def solve(A,b):
    n=len(b); X=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
    for k in range(n):
        p=next(i for i in range(k,n) if X[i][k]);X[k],X[p]=X[p],X[k]
        s=X[k][k];X[k]=[v/s for v in X[k]]
        for i in range(n):
            if i!=k:
                c=X[i][k];X[i]=[a-c*z for a,z in zip(X[i],X[k])]
    return [row[-1] for row in X]

def risk(t,eta):
    n=len(t);k=[x-x*x/2 for x in t]
    M=[[min(t[i],t[j])+(eta if i==j else 0) for j in range(n)] for i in range(n)]
    w=solve(M,k)
    return F(1,3)-sum(x*y for x,y in zip(k,w)),w

def analytic(n,eta):
    D=4*n*n-1
    # The rational cases are found by a quadratic discriminant square test.
    disc=4*(n+eta)**2-D
    if disc.denominator!=1 or int(sqrt(disc.numerator))**2!=disc.numerator:
        return None
    w=F(2,1)/(2*(n+eta)+F(int(sqrt(disc.numerator))))
    t=[1-(F(n-i,1)+F(1,2))*w for i in range(1,n+1)]
    R=F(1,3)-n*w/2+F(n*D,24)*w**3
    return w,t,R

def main():
    exact=0; competitors=0
    for n in range(1,7):
        for wden in range(1,30):
            # Pick a rational w inside the noiseless optimum and recover eta.
            w=F(2,2*n+1+wden)
            eta=F((4*n*n-1)*w*w+4,8*w)-n
            if eta<=0:continue
            ts=[1-(F(n-i,1)+F(1,2))*w for i in range(1,n+1)]
            R,v=risk(ts,eta)
            assert all(x==w for x in v)
            assert R==F(1,3)-F(n,2)*w+F(n*(4*n*n-1),24)*w**3
            assert all(0<t<1 for t in ts) and ts==sorted(set(ts))
            assert (4*n*n-1)*w*w-8*(n+eta)*w+4==0
            exact+=1
            if n<=4 and wden<=10:
                for shift in (-F(1,100),F(1,100)):
                    for j in range(n):
                        tt=ts[:];tt[j]=max(F(0),min(F(1),tt[j]+shift))
                        if len(tt)!=len(set(tt)):continue
                        rr,_=risk(sorted(tt),eta)
                        assert rr>=R
                        competitors+=1
    print('PASS',exact,'exact rational optimal designs;',competitors,'rational perturbation comparisons')
if __name__=='__main__':main()
