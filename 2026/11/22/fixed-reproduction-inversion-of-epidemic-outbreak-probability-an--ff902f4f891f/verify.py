"""Independent finite diagnostics for a two-type fixed-product SIR theorem.

Run: python3 verify.py. Uses Python's standard library. Analytic proofs, not
numerical sampling, establish the uncountable-parameter theorem.
"""
from __future__ import annotations

import math
from fractions import Fraction

CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def f(x):
    return -math.expm1(-x) / x if x != 0 else 1.0


def bisect_decreasing(func, lo, hi):
    check(func(lo) > 0, 'wrong lower bracket')
    check(func(hi) < 0, 'wrong upper bracket')
    for _ in range(100):
        mid = (lo+hi)/2
        if func(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def values(p, A, R, c):
    d = A / c
    k = (1-p)+p*A
    if R*k<=1:
        raise ValueError('strict supercritical condition required')
    Q = bisect_decreasing(
        lambda q: R*((1-p)*f(q)+p*A*f(c*q))-1.0,
        0.0, 1.0+R*k)
    z = bisect_decreasing(
        lambda z: R*((1-p)/(1+z)+p*A/(1+d*z))-1.0,
        0.0, 1.0+R*k)
    low= -math.expm1(-Q)
    high= -math.expm1(-c*Q)
    risk_low=z/(1+z)
    risk_high=d*z/(1+d*z)
    return (Q,c*Q,(1-p)*low+p*high,z,d*z,
            (1-p)*risk_low+p*risk_high,low,high,risk_low,risk_high)


def run():
    p=Fraction(1,2)
    A=Fraction(4)
    R=Fraction(1)
    for c,z_expected,risk_expected in [(Fraction(1),Fraction(1,2),Fraction(1,2)),
                                       (Fraction(4),Fraction(3,2),Fraction(3,5))]:
        d=A/c
        check((1-p)/(1+z_expected)+p*A/(1+d*z_expected)==1/R,
              'exact branching scalar balance')
        precise=(1-p)*z_expected/(1+z_expected)+p*(d*z_expected)/(1+d*z_expected)
        check(precise==risk_expected,'exact survival probability')

    tested=0
    for p in [0.07,0.2,0.5,0.78,0.93]:
        for A in [1.15,1.75,4.0,11.0]:
            for factor in [1.005,1.08,1.5,3.0,11.0]:
                R=factor/((1-p)+p*A)
                prev=None
                for j in range(17):
                    c=1+(A-1)*j/16
                    q,h,T,z,dz,P,lo,hi,plo,phi=values(p,A,R,c)
                    check(abs(R*((1-p)*f(q)+p*A*f(h))-1)<2e-12,
                          'final-size identity')
                    check(abs(R*((1-p)/(1+z)+p*A/(1+dz))-1)<2e-12,
                          'branching identity')
                    check(abs(P-(1-1/(A*R)-(1-p)*(1-1/A)/(1+z)))<2e-12,
                          'outbreak probability identity')
                    check(abs(T-((1-p)*lo+p*hi))<1e-13,'size composition')
                    if prev:
                        q0,h0,T0,z0,dz0,P0,lo0,hi0,plo0,phi0=prev
                        check(q<q0 and h>h0 and T<T0 and z>z0 and dz<dz0 and P>P0,
                              'all simultaneous strict comparisons')
                        check(lo<lo0 and hi>=hi0 and plo>plo0 and phi<phi0,
                              'class-resolved strict comparisons '+str((p,A,R,c,lo,lo0,hi,hi0,plo,plo0,phi,phi0)))
                    prev=(q,h,T,z,dz,P,lo,hi,plo,phi)
                    tested+=1
    row=[]
    for c in (1.0,2.0,4.0):
        q,h,T,z,dz,P,lo,hi,plo,phi=values(0.5,4.0,1.0,c)
        row.append((c,T,P,lo,hi,q,z))
    print('parameter points:',tested,'; assertions:',CHECKS)
    for c,T,P,lo,hi,q,z in row:
        print('c=%.1f final=%.12f outbreak=%.12f low_final=%.12f high_final=%.12f pressure=%.12f survival_scale=%.12f' %
              (c,T,P,lo,hi,q,z))
    print('All diagnostics passed.')

if __name__ == '__main__':
    run()
