#!/usr/bin/env python3
"""Exact-integer checks for sharp robust Gini contraction on directed cycles.

The analytical result holds for every real input and every finite n>=4.
These finite checks independently test complete binary-cut families at selected
rational parameters; they do not replace the proof.
"""
from itertools import product


def gini(values):
    return sum(abs(a-b) for i, a in enumerate(values) for b in values[i+1:])


def profile(n, theta_quarters, eps_scale_num, eps_scale_den):
    mu_quarters = min(theta_quarters, 4-theta_quarters)
    den = 4*(n-2)*eps_scale_den
    center = theta_quarters*(n-2)*eps_scale_den
    rad = mu_quarters*eps_scale_num
    return den, center-rad, center+rad


def validate():
    inspected = 0
    for n in range(4, 8):
        for theta_quarters in (1, 2, 3):
            for eps_num, eps_den, is_contracting in ((1,1,True),(5,4,False)):
                den,low,high = profile(n,theta_quarters,eps_num,eps_den)
                assert 0 <= low <= high <= den
                worst_num = -1
                for bits in product((low,high),repeat=n):
                    for mask in range(1,(1<<n)-1):
                        cut=[(mask>>i)&1 for i in range(n)]
                        y=[den*cut[i]+bits[i]*(cut[(i+1)%n]-cut[i]) for i in range(n)]
                        observed=gini(y)
                        baseline=den*sum(cut)*(n-sum(cut))
                        worst_num=max(worst_num,observed-baseline)
                        if is_contracting:
                            assert observed<=baseline,(n,theta_quarters,eps_num,mask,bits)
                        inspected+=1
                if is_contracting:
                    assert worst_num==0,(n,theta_quarters,worst_num)
                else:
                    assert worst_num>0,(n,theta_quarters,worst_num)
    print('EXACT_CRITICAL_RADIUS_ALL_ENVIRONMENTS_AND_CUTS_PASSED',inspected)

    # An independent integer check of the key maximization inequality.
    count=0
    for n in range(4,200):
        for k in range(1,n):
            for r in range(1,min(k,n-k)+1):
                for d in range(-r,r+1):
                    lhs=r*r+(2*k-n)*d-d*d
                    assert lhs <= r*r*(n-2),(n,k,r,d,lhs)
                    count+=1
    print('EXACT_ALL_COMBINATORIAL_ROUNDNESS_CASES_PASSED',count)
    print('ROBUST_TWO_TAP_GINI_CHECKS_PASSED')


if __name__=='__main__':
    validate()
