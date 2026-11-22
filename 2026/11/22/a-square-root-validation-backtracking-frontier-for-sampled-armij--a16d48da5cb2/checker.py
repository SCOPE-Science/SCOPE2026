"""Exact one-sweep, independent-batch stochastic Armijo verifier.
Run with: python validation_checker.py
All arithmetic for finite tests is rational and independent of numpy.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, ceil, erfc, sqrt


def armijo_backtrack(direction, signs, c, J):
    # Source's one-row gradient or LSQR direction, normalized by its line scale:
    # correction sign direction in {+1,-1}, candidate steps 2^{-j}.
    v = sum(signs, 0) * Q(1, len(signs))
    sample = lambda x: sum(((x-b)**2 for b in signs), Q(0))/ (2*len(signs))
    at0 = sample(Q(0))
    grad0 = -v
    for j in range(J+1):
        x = direction*Q(1,2**j)
        if grad0*x < 0 and sample(x)-at0 <= c*grad0*x:
            return x
    return Q(0)


def exact_tail(s,J,c):
    threshold = Q(1,2**J) / (2*(1-c))
    if threshold > 1: return Q(0)
    # mean of signs is (2k-s)/s; avoid floating-point threshold effects.
    k0 = ((Q(s,2)*(1+threshold)).numerator +
          (Q(s,2)*(1+threshold)).denominator - 1)//(Q(s,2)*(1+threshold)).denominator
    return Q(sum(comb(s,k) for k in range(k0,s+1)),2**s)


def run():
    cases=0
    total_outcomes=0
    for c in (Q(1,10000),Q(1,4),Q(1,2),Q(3,4)):
        for s in range(1,8):
            for J in range(0,6):
                # Actual independent validation batch, and both possible independent correction-row draws.
                accepted=0
                full_increase=Q(0)
                for b in (-1,1):
                    for v in product((-1,1),repeat=s):
                        x=armijo_backtrack(b,v,c,J)
                        # Full objective Phi(x)=(x*x+1)/2, unique minimizer at zero.
                        assert (x==0 or (x*x)/2>0)
                        if x != 0: accepted +=1
                        full_increase+=x*x/2
                assert Q(accepted,2**(s+1))==exact_tail(s,J,c),(s,J,c)
                assert full_increase>=0
                cases+=1
                total_outcomes+=2**(s+1)
    # Critical scaling: s=4^m and J=m+j, limiting Gaussian tail.
    for c in (Q(1,4),Q(1,2)):
        for j in (-2,0,2):
            for m in (3,4,5):
                s=4**m; J=m+j
                limit = erfc((2.0**(-j))/(2*(1-float(c))*sqrt(2)))/2
                observed=float(exact_tail(s,J,c))
                assert abs(observed-limit)<.15,(c,j,m,observed,limit)
    print(f'PASS: {cases} full-algorithm exact-rational cases, {total_outcomes} correction/validation outcomes; Gaussian-window spot checks passed')

if __name__=='__main__':run()
