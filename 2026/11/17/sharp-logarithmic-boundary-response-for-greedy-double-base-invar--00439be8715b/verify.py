"""Finite-precision checks of the stated double-base boundary-response identities.
Uses only Python's decimal module. These tests do not prove the limit theorem.
"""
from decimal import Decimal, getcontext
getcontext().prec = 105
D = Decimal

def experiment(Btext, eps_text, count=400):
    B, e = D(Btext), D(eps_text)
    M = 1 / (B-1)
    q0 = B/(B-1)-e
    r = q0/B
    x = r
    w = D(1)
    orbit = []
    L = None
    for j in range(count):
        orbit.append((x, w))
        if x < 1/B:
            if L is None:
                L=j
            x = q0*x
            w = w/q0
        else:
            x = B*x-1
            w = w/B
        # numerical rounding can produce a negative value only if the iterate has
        # left the invariant domain; within 400 steps in high precision this
        # should not happen on the selected tests.
        assert x >= 0 and x <= M+D('1e-90')
    assert L is not None and 0 < L < count//2
    assert (D(1)/B)**L < 100*e
    for j in range(L+1):
        xx,ww = orbit[j]
        assert abs(xx-(M-e*B**(j-1))) < D('1e-70')
        assert abs(ww-B**(-j)) < D('1e-70')
        assert abs(ww*(M-xx)-e/B) < D('1e-70')
    Z = sum((x*w for x,w in orbit),D(0))
    mean = sum((x*x*w/2 for x,w in orbit),D(0))/Z
    points = sorted(set([D(0),M] + [p[0] for p in orbit]))
    L1 = D(0)
    for lo,hi in zip(points,points[1:]):
        z = (lo+hi)/2
        h = sum((w for x,w in orbit if x>=z),D(0))/Z
        L1 += abs(h-1/M)*(hi-lo)
    C = (B-1)**2 / (B**2*B.ln())
    leading = e*(1/e).ln()
    targetmean = -C*M/2
    meanratio = (mean-M/2)/leading
    l1ratio = L1/leading
    # The omitted tail is at most a geometric sum in the number of omitted
    # iterates, and is negligible relative to the selected test scale.
    assert abs(meanratio/targetmean - 1) < D('0.12'), (B,e,meanratio,targetmean)
    assert abs(l1ratio/(2*C) - 1) < D('0.12'), (B,e,l1ratio,2*C)
    return L, meanratio, l1ratio

if __name__=='__main__':
    cases=0; prefixes=0
    for B in ['1.5','2','3','5']:
        for eps in ['1e-12','1e-18','1e-24']:
            L, meanratio, l1ratio=experiment(B,eps)
            cases+=1; prefixes+=L+1
    print('VERIFY_OK base_epsilon_cases=%d exact_prefix_identities=%d weak_moment_and_L1_ratios=%d' % (cases,prefixes,2*cases))
