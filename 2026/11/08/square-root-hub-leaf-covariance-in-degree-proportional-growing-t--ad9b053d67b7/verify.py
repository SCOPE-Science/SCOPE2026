#!/usr/bin/env python3
"""Exact and asymptotic checks for a preferential-attachment tree covariance law."""
from fractions import Fraction
from math import comb, pi, sqrt
from collections import defaultdict

def closed(n):
    assert n >= 2
    q = Fraction(comb(2*n-4,n-2), 4**(n-2))
    a = (2*n-3)*q
    b = Fraction(2*(n-1),3)+Fraction(4,3)*q
    covariance = Fraction(0)
    for k in range(2,n):
        qk = Fraction(comb(2*k-4,k-2), 4**(k-2))
        covariance += Fraction(1,3)*qk*(Fraction(k-3,k-1)+Fraction(2*k-3,(k-1)**2)*qk)
    return a,b,q,covariance

def enumerated(n):
    # Independent enumeration over every labelled arrival-parent history.
    # Each state stores (degrees, exact probability); no moment recursion used.
    histories = [((1,1), Fraction(1))]
    for size in range(2,n):
        next_histories = []
        for degrees,prob in histories:
            for v,deg in enumerate(degrees):
                ds = list(degrees)
                ds[v] += 1
                ds.append(1)
                next_histories.append((tuple(ds), prob*Fraction(deg,2*(size-1))))
        histories = next_histories
    assert sum((weight for _,weight in histories), Fraction(0)) == 1
    a = sum((weight*degrees[0] for degrees,weight in histories),Fraction(0))
    b = sum((weight*sum(d==1 for d in degrees) for degrees,weight in histories),Fraction(0))
    q = sum((weight for degrees,weight in histories if degrees[0]==1),Fraction(0))
    cross = sum((weight*degrees[0]*sum(d==1 for d in degrees) for degrees,weight in histories),Fraction(0))
    return a,b,q,cross-a*b

def check():
    checks=0
    for n in range(2,10):
        obs=enumerated(n)
        exp=closed(n)
        for i in range(4):
            assert obs[i]==exp[i],(n,i,obs,exp)
            checks+=1
        if n<=3:
            assert exp[3]==0
        else:
            assert exp[3]>0
        checks+=1
    # Separate one-step exact conditional-moment recurrence check.
    a,b,q,c = Fraction(1),Fraction(2),Fraction(1),Fraction(0)
    for n in range(2,90):
        h=Fraction(1,2*(n-1))
        a,b,q,c=(1+h)*a, (1-h)*b+1, (1-h)*q, c+a*b*h*h-q*h
        assert (a,b,q,c)==closed(n+1),n
        checks+=1
    # Distinct floating-point computation for long-size asymptotics.
    a,b,q,c,v_l=1.,2.,1.,0.,0.
    last=None
    for n in range(2,100001):
        h=1/(2*(n-1))
        p=h*b
        next_v_l=(1-2*h)*v_l+p*(1-p)
        c += a*b*h*h-q*h
        a,b,q,v_l=(1+h)*a,(1-h)*b+1,(1-h)*q,next_v_l
        if n in (10000,100000):
            N=n+1
            var_d=2*(N-1)-a-a*a
            corr=c/sqrt(var_d*v_l)
            last=(N,c/sqrt(N),sqrt(N)*corr,v_l/N,var_d/N)
    n,scaled_cov,scaled_corr,scaled_var_l,scaled_var_d=last
    assert abs(scaled_cov-2/(3*sqrt(pi)))<.005
    assert abs(scaled_corr-sqrt(2/(pi-2)))<.05
    assert abs(scaled_var_l-1/9)<.003
    assert abs(scaled_var_d-(2-4/pi))<.02
    checks+=4
    print('PASS',checks,'assertions; n=',n,'asymptotic diagnostics',last)

if __name__=='__main__': check()
