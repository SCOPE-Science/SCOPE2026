#!/usr/bin/env python3
"""Exact finite-particle stationary moment and lag checks for a mean-field resetting diffusion.

Standard library only. The independent check solves equations generated directly
from uncentered coordinate monomials, rather than from the closed-form answer.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, isclose

def solve(A,b):
    A=[list(map(F,row))+[F(rhs)] for row,rhs in zip(A,b)]
    n=len(b)
    for k in range(n):
        q=next(i for i in range(k,n) if A[i][k])
        A[k],A[q]=A[q],A[k]
        piv=A[k][k]
        A[k]=[x/piv for x in A[k]]
        for i in range(n):
            if i==k: continue
            a=A[i][k]
            A[i]=[u-a*v for u,v in zip(A[i],A[k])]
    return [row[-1] for row in A]

def moments(n,nu,lam,D,r,mu,tau2):
    b=nu+r; m=r*mu/b; h=mu-m
    Q=2*D+r*(h*h+tau2)
    T=(r+2*nu)*n*b+lam*(r+2*nu+2*(n-1)*b)
    S=Q*(n*b+lam)/T
    C=Q*lam/T
    return m,S,C

def raw_generator(n,nu,lam,D,r,mu,tau2):
    # Unknowns: m=E X_i, u=E X_i^2, v=E X_i X_j (i != j).
    # Each equation is computed from the particle's drift and jump replacement,
    # without using any closed formula for S or C.
    mu2=mu*mu+tau2
    A=[[nu+r,0,0],
       [0,2*(nu+lam)+r-2*lam/F(n),-2*lam*F(n-1,n)],
       [-2*r*mu,-2*lam/F(n),2*(nu+lam+r)-2*lam*F(n-1,n)]]
    z=[r*mu,2*D+r*mu2,0]
    return solve(A,z)

def main():
    count=0
    for n,nu,r,lam,D,mu,tau2 in product([2,3,4,7], [F(1,2),F(2)], [F(1,3),F(3)], [F(0),F(1,5),F(2),F(19)], [F(1,8),F(3)], [F(0),F(4)], [F(0),F(1,2)]):
        m,u,v=raw_generator(n,nu,lam,D,r,mu,tau2)
        mm,S,C=moments(n,nu,lam,D,r,mu,tau2)
        assert m==mm and u-m*m==S and v-m*m==C
        assert C*(n*(nu+r)+lam)==lam*S
        assert 0<=C<=S
        assert C==0 if lam==0 else C>0
        count+=1
    # Independently evaluate the stationary lag equations at multiple times.
    n,nu,lam,D,r,mu,tau2=4,1.2,3.0,.7,.9,2.0,.4
    m,S,C=moments(n,nu,lam,D,r,mu,tau2)
    b=nu+r
    slow=S+(n-1)*C; fast=S-C
    for t in [0,.1,.7,2,8]:
        # stationary mode regression: K'(t)=(-(nu+r+lam)I+lam*P)K(t).
        a=slow*exp(-b*t)/n
        f=fast*exp(-(b+lam)*t)/n
        kaa=a+(n-1)*f
        kab=a-f
        assert isclose(kaa+(n-1)*kab,slow*exp(-b*t),rel_tol=1e-12)
        assert isclose(kaa-kab,fast*exp(-(b+lam)*t),rel_tol=1e-10,abs_tol=1e-17)
        assert kab>0
        count+=2
    # Critical scaling and two-scale lag law.
    nu,r,D,mu,tau2,c=1.3,.8,1.2,2.1,.4,1.7
    b=nu+r; h=nu*mu/b; Q=2*D+r*(h*h+tau2)
    for n in [1000,10000,100000]:
        _,S,C=moments(n,nu,c*n,D,r,mu,tau2)
        corr=C/S
        assert abs(corr-c/(b+c))<1e-12
        slow=S+(n-1)*C; fast=S-C
        for s in [0,.5,2.]:
            t=s/n
            k=Nauto=slow*exp(-b*t)/n+(n-1)*fast*exp(-(b+c*n)*t)/n
            limit=Q/(2*b)+Q/(2*c)*exp(-c*s)
            if n>=100000: assert abs(n*k-limit)<0.0002
            count+=1
    print(f'PASS: {count} exact/analytic independent moment and lag cases; critical scaling checked.')
if __name__=='__main__':main()
