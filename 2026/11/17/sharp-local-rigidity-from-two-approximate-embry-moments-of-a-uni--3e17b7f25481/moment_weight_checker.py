"""Exact rational checks for the sharp local two-moment weighted-shift estimate.
Run with python moment_weight_checker.py.  All checks are finite diagnostic tests;
the general theorem follows from the inequalities in RESULT.md.
"""
from fractions import Fraction as Q
from random import Random
from math import log, exp


def budget(d, n, j):
    return sum((n-1-h)*d[j+h] for h in range(n-1))


def witness(n, alpha, beta):
    """A finite log-increment pulse attaining the upper local bound."""
    k = beta/Q(n-1) + alpha*Q(n-2,2)
    j = n+2
    d = [Q(0)]*(4*n+6)
    for t in range(j-(n-1),j):
        d[t] = -alpha
    d[j] = k
    for t in range(j+1,j+n-1):
        d[t] = -alpha
    return d,j,k


def test():
    cases=0
    for n in range(3,51):
        for alpha in (Q(0),Q(1,7),Q(2,3),Q(4)):
            for beta in (Q(0),Q(1,5),Q(7,4)):
                d,j,k = witness(n,alpha,beta)
                assert d[j] == k
                assert min(d) >= -alpha
                assert budget(d,n,j) == beta
                for t in range(len(d)-n+1):
                    assert budget(d,n,t) <= beta, (n,alpha,beta,j,t)
                cases+=1
    # Independent finite log-increment tests for the derived upper estimate.
    rng=Random(20261114)
    random_cases=0
    for n in range(3,13):
        S=n*(n-1)//2
        for _ in range(1500):
            alpha=Q(rng.randint(0,5),4)
            beta=Q(rng.randint(0,5),3)
            # Generic admissible nonpositive increments. Includes nonperiodic steps.
            d=[-alpha*Q(rng.randint(0,6),6) for _ in range(40)]
            assert all(budget(d,n,t)<=beta for t in range(len(d)-n+1))
            assert max(d)<= beta/Q(n-1)+alpha*Q(n-2,2)
            random_cases+=1
    # A negative single step attains the lower bound.
    for n in range(3,30):
        a=Q(7,9); b=Q(2,5)
        d=[Q(0)]* (n+11);d[5]=-a
        assert all(budget(d,n,t)<=b for t in range(len(d)-n+1))
        assert min(d)==-a
    # Global contrast can persist at arbitrarily small relative moment defects.
    for n in (3,4,7,15):
        S=n*(n-1)//2
        for eps in (0.1,0.01,0.001):
            steps=max(1,int(S*log(4)/eps)+1)
            delta=log(4)/steps
            log_a=[-log(4)+delta*min(j,steps) for j in range(steps+n+5)]
            assert abs(log_a[-1])<1e-12
            assert max(log_a)-min(log_a)>log(4)-1e-12
            for j in range(len(log_a)-n+1):
                assert log_a[j+1]-log_a[j]>=-1e-12
                assert sum(log_a[j+r]-log_a[j] for r in range(1,n))<=eps+1e-11
    print('PASS: exact upper-constant pulses',cases,
          '; independent admissible sequences',random_cases,
          '; negative-step witnesses',27, '; global contrast probes',12)


if __name__=='__main__':
    test()
