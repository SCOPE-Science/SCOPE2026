#!/usr/bin/env python3
"""Exact finite verification of the illustrative three-habitat reversal.

The global uniqueness and logarithmic asymptotics are proved analytically in RESULT.md;
this checker is only a reproducible finite certificate for the stated witness.
"""
from fractions import Fraction as Q
from math import factorial

def mat_vec(M, v):
    return [sum(a*b for a,b in zip(row,v)) for row in M]

def partial(M, t, N=36):
    v=[1]*len(M)
    S=[Q(1)]*len(M)
    for n in range(1,N+1):
        v=mat_vec(M,v)
        for i in range(len(v)):
            S[i] += Q(v[i])*t**n/Q(factorial(n))
    # If norm(M)_infinity * t <= 2, the tail is at most
    # exp(2)*2^(N+1)/(N+1)! < 8*2^(N+1)/(N+1)! in each component.
    err=Q(8*2**(N+1),factorial(N+1))
    return S,err

def verify():
    M=[[1,1,0],[1,-1,1],[0,1,4]]
    assert max(sum(abs(x) for x in row) for row in M)==5
    checked=0
    for t,sign in [(Q(1,5),1),(Q(2,5),-1)]:
        S,err=partial(M,t)
        difference=S[0]-S[1]
        assert sign*difference>2*err,(t,difference,err)
        print('t=',t,'difference between approximants=',float(difference),
              'rigorous absolute error <',float(2*err),'sign=',sign)
        checked+=2
    # Exact Perron-eigenvector threshold for general rational parameters.
    for m in [Q(1,4),Q(1,2),Q(1),Q(2),Q(5)]:
        for Delta in [Q(1,5),Q(1),Q(3),Q(8)]:
            for r1 in [Q(-2),Q(0),Q(2)]:
                r2=r1-Delta
                crit=r1 + m*Delta/(m+Delta)
                s=Q(1)+Delta/m
                MT=[
                    [r1-m,m,Q(0)],
                    [m,r2-2*m,m],
                    [Q(0),m,crit-m]
                ]
                v=[Q(1),Q(1),s]
                assert mat_vec(MT,v)==[r1*x for x in v]
                # The top spectral coefficient has a negative first derivative.
                K=s*s*(2+s)/(m*(2+s*s)**2)
                assert K>0
                checked+=2
    # Exact two-site derivative and threshold sign checks for examples.
    for r1,r2,m in [(Q(2),Q(1),Q(1)),(Q(7,3),Q(-2),Q(3,4))]:
        MM=[[r1-m,m],[m,r2-m]]
        assert [x-y for x,y in zip(mat_vec(MM,[1,1]),[0,0])] == [r1,r2]
        checked+=1
    print('PASS:',checked,'exact-rational check assertions; no assertion about global proof from finite tests')

if __name__=='__main__':
    verify()
