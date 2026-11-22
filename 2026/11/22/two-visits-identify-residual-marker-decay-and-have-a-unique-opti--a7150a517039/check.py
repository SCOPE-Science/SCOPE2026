#!/usr/bin/env python3
"""Standalone arithmetic checks for two-visit residual-marker occupancy theorem.
All general claims are established by the written proof, not by these finite checks.
"""
from fractions import Fraction as F
from math import exp, log, isclose


def determinant_3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def probs(p, a, b, q):
    # Observations are independent conditional on the fixed site class.
    z = (1-p)
    return [z*(1-a)*(1-b)+p*(1-q)*(1-q),
            z*(1-a)*b+p*(1-q)*q,
            z*a*(1-b)+p*q*(1-q),
            z*a*b+p*q*q]


def fish_det_perfect(p, a, b):
    # Rows: P00, P01, P10, P11; cols: p, a, b.
    rows = [
        [-(1-a)*(1-b), -(1-p)*(1-b), -(1-p)*(1-a)],
        [-(1-a)*b, -(1-p)*b, (1-p)*(1-a)],
        [-a*(1-b), (1-p)*(1-b), -(1-p)*a],
        [1-a*b, (1-p)*b, (1-p)*a],
    ]
    ps = probs(p, a, b, F(1))
    I = [[sum(rows[k][i]*rows[k][j]/ps[k] for k in range(4))
          for j in range(3)] for i in range(3)]
    return determinant_3(I)


exact = 0
for pp in range(1, 10):
    p = F(pp, 11)
    for aa in range(1, 9):
        a = F(aa, 10)
        for bb in range(1, aa+1):
            b = F(bb, 12)
            # q known, all four binary probabilities identify 3 parameters.
            for q in [F(1), F(9, 10), F(19, 20)]:
                if a >= q:
                    continue
                Ps = probs(p, a, b, q)
                assert sum(Ps)==1 and all(v>0 for v in Ps)
                m0=Ps[2]+Ps[3]
                m1=Ps[1]+Ps[3]
                cov=Ps[3]-m0*m1
                ratio=cov/((q-m0)*(q-m1))
                recovered_p=ratio/(1+ratio)
                recovered_a=(m0-recovered_p*q)/(1-recovered_p)
                recovered_b=(m1-recovered_p*q)/(1-recovered_p)
                assert (recovered_p,recovered_a,recovered_b)==(p,a,b)
                exact += 1
            actual=fish_det_perfect(p,a,b)
            expected=(1-p)/(a*b*(p+(1-p)*a*b))
            assert actual==expected, (p,a,b,actual,expected)
            exact += 1


def zstar(p,alpha):
    C=(1-p)*alpha**2/p
    lo,hi=2.0,2.0+2*C
    for _ in range(95):
        mid=(lo+hi)/2
        if mid<2+2*C*exp(-mid): lo=mid
        else: hi=mid
    return (lo+hi)/2


def objective(p,alpha,delta,t):
    b=alpha*exp(-delta*t)
    return (1-p)*t*t*b/(alpha*(p+(1-p)*alpha*b))

numeric=0
for p in [.001,.005,.01,.03,.1,.2,.4,.6,.8,.99]:
    for alpha in [.1,.4,.7,.95]:
        for delta in [.03,.1,.4,3]:
            z=zstar(p,alpha)
            t=z/delta
            assert 2<z and abs(z-2-2*(1-p)*alpha**2/p*exp(-z)) < 1e-10
            optimum=objective(p,alpha,delta,t)
            for factor in [.001,.02,.1,.2,.5,.8,.95,1.05,1.2,2,4,10,50]:
                assert objective(p,alpha,delta,t*factor)<optimum*(1+2e-13)
                numeric+=1
            numeric+=2
    zs=[zstar(p,a) for a in [.1,.4,.7,.95]]
    assert all(zs[i]<zs[i+1] for i in range(3)); numeric+=1
for alpha in [.2,.7,.95]:
    zs=[zstar(p,alpha) for p in [.001,.01,.1,.4,.9,.99]]
    assert all(zs[i]>zs[i+1] for i in range(len(zs)-1)); numeric+=1

# Independent finite-difference log-slope check at a known parameter point.
p,a,d=0.2,0.6,0.1
z=zstar(p,a)
assert abs(z-2.291275616944311)<2e-13
h=1e-4
L=lambda t:log(objective(p,a,d,t))
assert abs((L((z/d)+h)-L((z/d)-h))/(2*h))<5e-11
numeric+=2
print(f'PASS exact_fraction_checks={exact} numeric_checks={numeric}')
print(f'example_p_0.2_alpha_0.6_delta_0.1: normalized_gap={z:.12f} gap={z/d:.12f}')
