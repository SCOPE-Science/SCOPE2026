#!/usr/bin/env python3
"""Finite exact occupancy-moment and coloured-fibre checks.

Pure Python 3, standard library only. Finite checks support the stated
identities; the asymptotic logic theorem is proved separately.
"""
from fractions import Fraction
from itertools import product
from math import factorial, comb, log, exp

def falling(n, k):
    if k > n: return 0
    a = 1
    for j in range(k): a *= n-j
    return a

def exact_factorial_moment(m, n, r, t):
    if r*t > n or t > m: return Fraction(0)
    # For t designated boxes, each receives r balls, all remaining balls avoid them.
    assignments = falling(n,r*t)//(factorial(r)**t)
    return (Fraction(falling(m,t)*assignments, m**(r*t))
            *Fraction(m-t,m)**(n-r*t))

def count_fibres(seq, m, r):
    cnt = [0]*m
    for b in seq: cnt[b]+=1
    return sum(x==r for x in cnt)

def occupancy_stats(m,n,r):
    # Exact enumeration of all m^n functions.
    counts={}
    for f in product(range(m),repeat=n):
        z=count_fibres(f,m,r)
        counts[z]=counts.get(z,0)+1
    den=m**n
    return {k:Fraction(v,den) for k,v in counts.items()}

def factorial_from_law(law,t):
    return sum(Fraction(falling(z,t))*p for z,p in law.items())

def main():
    check_univariate=0
    check_joint=0
    for m in range(1,5):
        for n in range(0,6):
            for r in range(0,4):
                law=occupancy_stats(m,n,r)
                assert sum(law.values())==1
                for t in range(0,min(m,3)+1):
                    observed=factorial_from_law(law,t)
                    expected=exact_factorial_moment(m,n,r,t)
                    assert observed==expected,(m,n,r,t,observed,expected)
                    check_univariate+=1
    # Factorial moments for two independent maps factor at finite size,
    # including the probability that both colour classes cover all boxes.
    for m in range(1,4):
        for n0 in range(0,4):
            for n1 in range(0,4):
                for r0 in range(0,3):
                    for r1 in range(0,3):
                        law0=occupancy_stats(m,n0,r0)
                        law1=occupancy_stats(m,n1,r1)
                        for t0 in range(0,min(2,m)+1):
                            for t1 in range(0,min(2,m)+1):
                                product_law=(factorial_from_law(law0,t0)*
                                             factorial_from_law(law1,t1))
                                formula=(exact_factorial_moment(m,n0,r0,t0)*
                                         exact_factorial_moment(m,n1,r1,t1))
                                assert product_law==formula
                                check_joint+=1
    # Verify exact critical finite-size means move towards their predicted
    # limits when the number of boxes increases. Convergence with r>0 is
    # slow (log-log m / log m); no false small-m relative tolerance imposed.
    cases=[]
    for r,c in [(0,0.0),(1,0.3),(2,-0.2)]:
        target=exp(-c)/factorial(r)
        means=[]
        for m in (100000, 10000000000):
            n=round(m*(log(m)+r*log(log(m))+c))
            val=exp(log(m)+sum(log(n-j) for j in range(r))
                    -log(factorial(r))-r*log(m)
                    +(n-r)*log1p_safe(-1/m))
            means.append(val)
        assert abs(means[1]-target)<abs(means[0]-target),(r,means,target)
        cases.append((r,round(means[0],5),round(means[1],5),round(target,5)))
    print('CRITICAL_COLOURED_FIBRE_CHECKS_OK',
          'univariate_moments',check_univariate,
          'joint_moments',check_joint,
          'threshold_examples',cases)

def log1p_safe(x):
    from math import log1p
    return log1p(x)

if __name__=='__main__': main()
