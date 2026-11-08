#!/usr/bin/env python3
"""Exact finite checks for optimal reciprocal Lucas first-crossing indices.

Run with Python 3.11 or later: python verify_lucas_reciprocal.py
The infinite-frequency theorem is proved analytically, not by this finite test.
"""
from decimal import Decimal, localcontext, getcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from collections import Counter


def lucas(p, q, end):
    f = [0, 1]
    for i in range(2, end + 1):
        f.append(p * f[-1] + q * f[-2])
    return f


def params(p, q, prec=110):
    with localcontext() as ctx:
        ctx.prec = prec
        P, Q = Decimal(p), Decimal(q)
        A = (P + (P * P + 4 * Q).sqrt()) / 2
        s = Q / A**3
        C = (1 + P*s - Q*s*s) / (1+s)
        ll = A.ln()
        lam = 3 - Q.ln() / ll
        gamma = Decimal(p+q-1).ln()/ll - 1
        beta = (Decimal(p+q-1) / ((A - 1)*C)).ln()/ll
        delta = beta - gamma
        assert Decimal(0) < delta < Decimal(1)
        return lam, gamma, beta, delta


def floor(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))


def ceil(x):
    return int(x.to_integral_value(rounding=ROUND_CEILING))


def exact_crossing(p, q, k, Jmax):
    f = lucas(p, q, Jmax)
    s = Fraction(p-1, f[k+1]) - Fraction(1, f[k])
    for J in range(k+2, Jmax+1):
        s += Fraction(p+q-1, f[J])
        if s > 0:
            return J
    raise AssertionError(('No crossing in supplied range',p,q,k,Jmax))


def main():
    getcontext().prec=110
    checked=0
    fully_predicted=0
    first_stage_exceptions=[]
    gap_count=Counter()
    for p in range(2, 11):
        for q in range(2, p+1):
            lam, gamma, beta, delta = params(p,q)
            for k in range(1, 92, 2):
                k1=floor(lam*k+gamma)
                k2=ceil(lam*k+gamma-4+2*lam)
                j=exact_crossing(p,q,k,max(k2+2,k+4))
                assert k1<j<=k2,(p,q,k,j,k1,k2)
                predicted=floor(lam*k+beta)+1
                if j != predicted:
                    first_stage_exceptions.append((p,q,k,j,predicted))
                else:
                    fully_predicted += 1
                gap_count[j-k1]+=1
                checked += 1
    # The strict inequality produces one special small-index boundary
    # already documented by the source paper at p=q=2, k=1.
    assert (2,2,1,4,3) in first_stage_exceptions
    assert checked==sum(gap_count.values())
    print('VERIFY_OK exact_fraction_comparisons=%d formula_matches=%d finite_exceptions=%d gaps=%s' % (
        checked,fully_predicted,len(first_stage_exceptions),dict(sorted(gap_count.items()))))
    print('EXCEPTIONS',first_stage_exceptions[:25])
    for p,q in [(2,2),(3,2),(3,3),(5,5),(10,9)]:
        lam,gamma,beta,delta=params(p,q)
        print('DENSITY_PARAMETER p=%d q=%d predicted_plus_two=%.12f' % (p,q,delta))

if __name__ == '__main__':
    main()
