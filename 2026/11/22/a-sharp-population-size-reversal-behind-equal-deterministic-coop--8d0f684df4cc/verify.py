#!/usr/bin/env python3
"""Standalone exact/floating corroboration for the all-strength feedback fixation theorem.

Only Python standard-library components are needed. Proof of universal assertions is
analytical in RESULT.md; these tests do not certify infinitely many parameter values.
"""
from fractions import Fraction as F
from math import exp, isclose


def difference(n, i, t):
    x = F(i, n)
    r, s, p = F(3), F(1), F(0)
    a = (1-x)*t + x*r
    b = (1-x)*p + x*s
    c = (1-x)*r + x*t
    d = (1-x)*s + x*p
    cp = ((i-1)*a + (n-i)*b)/F(n-1)
    dp = (i*c + (n-i-1)*d)/F(n-1)
    return cp-dp


def predicted(n, t):
    return ((2-t)*(n-5)-6*t)/6, -(n*n+(2*t-1)*n-t+4)/6


def solve_absorption_probabilities(n, t, beta):
    # Solve h_i = up_i*h_{i+1} + dn_i*h_{i-1} + stay_i*h_i,
    # h_0=0,h_n=1 using a Thomas elimination, independent of fixation sums.
    a=[]; b=[]; c=[]; rhs=[]
    for i in range(1,n):
        d=float(difference(n,i,t))
        up=(i*(n-i)/n**2)/(1+exp(-beta*d))
        dn=(i*(n-i)/n**2)/(1+exp(beta*d))
        a.append(-dn)
        b.append(up+dn)
        c.append(-up)
        rhs.append(up if i==n-1 else 0.0)
    for j in range(1,n-1):
        fac=a[j]/b[j-1]
        b[j]-=fac*c[j-1]
        rhs[j]-=fac*rhs[j-1]
    ans=[0.0]*(n-1)
    ans[-1]=rhs[-1]/b[-1]
    for j in range(n-3,-1,-1):
        ans[j]=(rhs[j]-c[j]*ans[j+1])/b[j]
    return ans[0], 1.0-ans[-1]


def check():
    tested=0
    for t in (F(11,10),F(3,2),F(19,10)):
        for n in range(2,61):
            ds=[difference(n,i,t) for i in range(1,n)]
            sn=sum(ds,F(0))
            w=sum(((n-i)*ds[i-1] for i in range(1,n)),F(0))
            ps,pw=predicted(n,t)
            assert (sn,w)==(ps,pw),(n,t,sn,ps,w,pw)
            assert w<0
            tested+=1
    for t in (F(11,10),F(3,2),F(19,10)):
        for n in (2,3,4,12,22,23,24,31,50):
            for beta in (0.03,0.1,0.2):
                rho_c,rho_d=solve_absorption_probabilities(n,t,beta)
                odds=exp(beta*float(predicted(n,t)[0]))
                assert isclose(rho_c/rho_d,odds,rel_tol=3e-9,abs_tol=3e-9),(t,n,beta,rho_c,rho_d,odds)
                assert rho_c<1/n,(t,n,beta,rho_c)
    assert predicted(23,F(3,2))[0]==0
    assert predicted(22,F(3,2))[0]<0 and predicted(24,F(3,2))[0]>0
    print(f"PASS: {tested} exact-rational sum cases and 81 tridiagonal fixation checks; sharp N=23 verified.")

if __name__=='__main__':
    check()
