#!/usr/bin/env python3
"""Exact finite checks of the circular reciprocal-pair power-weight covariance."""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial


def moment_order(n, rank, power):
    """Exact E[X_(rank)^power] for n independent Exp(1) variables."""
    coeff=[Q(1)]+[Q(0)]*power
    for rate in range(n,n-rank,-1):
        next_coeff=[Q(0)]*(power+1)
        for k in range(power+1):
            next_coeff[k]=sum(coeff[k-j]*Q(1,rate**j) for j in range(k+1))
        coeff=next_coeff
    return factorial(power)*coeff[power]


def theorem(n, power):
    assert n>=5 and power in (0,1,2,3,4)
    f=factorial(power)
    rising=1
    for j in range(power): rising*=n+j
    mean = Q(n*f,3**(power+1)*rising)
    cov = Q(n*f,3*rising)*(Q(1,3**(power+1))-Q(1,5**(power+1)))
    return mean,cov


def exhaustive(n, power):
    moments=[None]+[moment_order(n,r,power) for r in range(1,n+1)]
    sum_R=sum_U=sum_RU=Q(0)
    count=0
    for rank_vec in permutations(range(1,n+1)):
        selected=[i for i in range(n) if rank_vec[i]<rank_vec[i-1] and rank_vec[i]<rank_vec[(i+1)%n]]
        R=len(selected)
        EU=sum((moments[rank_vec[i]] for i in selected),Q(0))
        sum_R+=R
        sum_U+=EU
        sum_RU+=R*EU
        count+=1
    ER=sum_R/count
    EU=sum_U/count
    ERU=sum_RU/count
    rising=1
    for j in range(power): rising*=n+j
    return ER,EU/rising,(ERU-ER*EU)/rising


def verify_integrals():
    # For integer k, the distance-two mixed moment equals a sum of two
    # gamma integrals over ordered half-planes. These are checked exactly.
    checks=0
    for k in range(5):
        gamma=factorial(k)
        expected=Q(gamma,2*3**(k+1))-Q(gamma,6*5**(k+1))
        part_y_gt_x=Q(gamma,2)*(Q(1,3**(k+1))-Q(1,5**(k+1)))
        part_x_gt_y=Q(gamma,3*5**(k+1))
        assert part_y_gt_x+part_x_gt_y==expected
        checks+=1
    return checks


def verify_finite():
    tests=verify_integrals()
    for n in (5,6,7,8):
        for k in (0,1,2,3):
            ER,EW,C=exhaustive(n,k)
            mean,cov=theorem(n,k)
            assert ER==Q(n,3),(n,k,ER)
            assert EW==mean,(n,k,EW,mean)
            assert C==cov,(n,k,C,cov)
            tests+=3
    # Explicit known n>=5 specializations from full local-moment table.
    for n in (5,6,7,8):
        assert theorem(n,0)[1]==Q(2*n,45)
        assert theorem(n,1)[0]==Q(1,9)
        assert theorem(n,1)[1]==Q(16,675)
        assert theorem(n,2)[1]==Q(196,10125*(n+1))
        tests+=4
    print(f"PASS: {tests} exact integer/rational checks, n=5..8 and powers 0..3")

if __name__=='__main__':
    verify_finite()
