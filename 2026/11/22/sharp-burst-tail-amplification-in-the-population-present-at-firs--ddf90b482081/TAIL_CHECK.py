#!/usr/bin/env python3
"""Finite-sum numerical tests of power-tail first-binding amplification.
Standard Python 3 only. The analytic infinite-tail statements are proved separately.
The integral tails below are approximations to positive monotone series, not
certificates of an infinite limit.
"""
import math

def sums(alpha, F, N=700000):
    # Unnormalised mass weights p_j=j^(-1-alpha), so the zeta normalizer cancels.
    q=1-F
    logq=math.log1p(-F)
    numer=0.0; denom=0.0; moment=0.0; second=0.0
    for j in range(1,N+1):
        numer+=j**(-alpha)*(-math.expm1((j-1)*logq))
        denom+=j**(-1-alpha)*(-math.expm1(j*logq))
        moment+=j**(-alpha)
        if alpha>2: second+=j**(1-alpha)
    # Because F*N >>1, tails in numerator and denominator have 1-q^j ~1.
    numer += (N+0.5)**(1-alpha)/(alpha-1)
    denom += (N+0.5)**(-alpha)/alpha
    moment += (N+0.5)**(1-alpha)/(alpha-1)
    if alpha>2: second += (N+0.5)**(2-alpha)/(alpha-2)
    measured=1+numer/denom
    if alpha<2: predicted=math.gamma(2-alpha)/((alpha-1)*moment)*F**(alpha-2)
    elif alpha==2: predicted=math.log(1/F)/moment
    else: predicted=second/moment
    return measured,predicted

count=0
for alpha, fvals, tolerance in ((1.5,(.001,.0001),.035),(2.0,(.001,.0001),.16),(3.0,(.001,.0001),.01)):
    for F in fvals:
        observed,predicted=sums(alpha,F)
        print(f'alpha={alpha}, F={F:.4g}, exact-series approximation={observed:.8f}, leading asymptotic={predicted:.8f}, ratio={observed/predicted:.6f}')
        assert abs(observed/predicted-1)<tolerance
        count+=1
print('PASS',count,'finite power-tail comparisons; the proof does not rely on these sums')
