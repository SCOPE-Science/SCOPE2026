#!/usr/bin/env python3
"""Independent finite checks for clique-cycle independent-set covariance."""
from itertools import combinations
from fractions import Fraction
from math import sqrt, cos, pi

def is_stable(bits, n, h):
    if sum(bits[:h]) > 1 or (any(bits[:h]) and any(bits[h:])): return False
    return all(not(bits[h+i] and bits[h+(i+1)%n]) for i in range(n))

def covariance_rows(n, h):
    states = [bits for k in range(n+h+1) for idx in combinations(range(n+h), k)
        for bits in [tuple(int(i in idx) for i in range(n+h))] if is_stable(bits,n,h)]
    z=len(states); means=[Fraction(sum(x[i] for x in states),z) for i in range(n+h)]
    cov=[[sum(Fraction(x[i]*x[j],z) for x in states)-means[i]*means[j] for j in range(n+h)] for i in range(n+h)]
    return z,cov

def cycle_counts(n):
    return [tuple(int(i in s) for i in range(n)) for k in range(n+1)
     for s in combinations(range(n),k)
     if all(not(i in s and (i+1)%n in s) for i in range(n))]

def test():
    for n in range(3,9):
        Y=cycle_counts(n); L=len(Y); p=Fraction(sum(y[0] for y in Y),L)
        cyc=[[sum(Fraction(y[i]*y[j],L) for y in Y)-p*p for j in range(n)] for i in range(n)]
        v=sum(cyc[0])/1
        r=(sqrt(5)-3)/2; w=r**n
        v2=(1-w)/(5*sqrt(5)*(1+w))+n*w/(5*(1+w)**2)
        assert abs(float(v)-v2)<1e-10,(n,v,v2)
        for k in range(1,n):
            exact=sum(float(cyc[0][d])*cos(2*pi*k*d/n) for d in range(n))
            formula=(1-r*r)*(1-w)/(5*(1+w)*(1-2*r*cos(2*pi*k/n)+r*r))
            assert abs(exact-formula)<1e-10,(n,k,exact,formula)
        for h in range(1,5):
            Z,cov=covariance_rows(n,h); assert Z==L+h
            for i in range(h):
                for j in range(h):
                    expected=Fraction(int(i==j),Z)-Fraction(1,Z*Z)
                    assert cov[i][j]==expected,(n,h,i,j)
            for i in range(h):
                for j in range(n):
                    assert cov[i][h+j]==-Fraction(L,Z*Z)*p
            for i in range(n):
                for j in range(n):
                    expected=Fraction(L,Z)*cyc[i][j]+Fraction(L*h,Z*Z)*p*p
                    assert cov[h+i][h+j]==expected
    p=(1-1/sqrt(5))/2;v=1/(5*sqrt(5)); S=1/sqrt(5)
    assert abs((S-v)/(p*p)-(2+6/sqrt(5)))<1e-12
    for n in (16,24,40,56):
        r=(sqrt(5)-3)/2; w=r**n
        phi=(1+sqrt(5))/2;psi=(1-sqrt(5))/2; L=round(phi**n+psi**n)
        F=round((phi**(n-1)-psi**(n-1))/sqrt(5)); q=F/L
        vn=(1-w)/(5*sqrt(5)*(1+w))+n*w/(5*(1+w)**2)
        gammax=max((1-r*r)*(1-w)/(5*(1+w)*(1-2*r*cos(2*pi*k/n)+r*r)) for k in range(1,n))
        for c in (2,7):
            h=max(1,round(c*L/n));Z=L+h
            t=L/Z**2+L*vn/Z+n*h*L*q*q/Z**2
            det=L*L*vn/Z**3
            dis=sqrt(max(0,t*t-4*det))
            betamin=2*det/(t+dis); betamax=(t+dis)/2
            ratio=max(betamax,L*gammax/Z)/betamin/L
            target=(v+c*p*p)/v*max(S,v+c*p*p)
            assert abs(ratio-target)/target < 0.30,(n,c,ratio,target)
    print('UNIFORM_JOIN_FOURIER_CHECKS_PASSED')

if __name__=='__main__': test()
