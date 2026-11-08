#!/usr/bin/env python3
"""Independent exact-state verification of a directed-star SI sentinel theorem.

All Laplace-transform calculations use fractions. The exhaustive finite grid is
not a substitute for the all-parameter proof given in the accompanying text.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import exp, isclose

checks = 0

def assert_equal(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def assert_close(x, y):
    global checks
    assert isclose(x, y, rel_tol=1e-12, abs_tol=1e-12), (x, y)
    checks += 1

def process_laplace(m, k, alpha, beta, s, center_monitored):
    """Exact epidemic CTMC transform; hub index 0, leaves 1..m."""
    monitored = ({0} | set(range(1, k))) if center_monitored else set(range(1, k+1))
    monitored_mask = sum(1 << j for j in monitored)
    @lru_cache(None)
    def value(mask):
        if mask & monitored_mask:
            return Q(1)
        transitions = []
        if mask & 1:
            transitions = [(Q(beta), mask | (1 << j))
                           for j in range(1, m + 1) if not (mask & (1 << j))]
        else:
            leaf_count = (mask >> 1).bit_count()
            if leaf_count:
                transitions = [(alpha * leaf_count, mask | 1)]
        total = sum((r for r, _ in transitions), Q(0))
        if not total:
            raise RuntimeError('Unmonitored absorbing infection state')
        return sum((rate * value(next_mask) for rate, next_mask in transitions), Q(0)) / (s + total)
    return sum((value(1 << seed) for seed in range(m+1)), Q(0)) / (m+1)

def predicted_laplace(m, k, alpha, beta, s, center_monitored):
    r = k*beta
    if center_monitored:
        return (k + (m-k+1)*alpha/(s+alpha))/(m+1)
    return (k + r/(s+r) + (m-k)*alpha*r/((s+alpha)*(s+r)))/(m+1)

def survival_values(m, k, alpha, beta, t):
    a, r = float(alpha), float(k*beta)
    eh, er = exp(-a*t), exp(-r*t)
    if abs(a-r) < 1e-14:
        integral = t*eh
        sum_survival = eh*(1+a*t)
    else:
        integral = (eh-er)/(r-a)
        sum_survival = (r*eh-a*er)/(r-a)
    H = (m-k+1)*eh/(m+1)
    L = (er+(m-k)*sum_survival)/(m+1)
    difference = ((m-k+1)*a-r)*integral/(m+1)
    return H, L, difference

for m in range(1, 8):
    for k in range(1, m+1):
        for alpha in (Q(1,3), Q(1), Q(5,2)):
            for beta in (Q(1,5), Q(1), Q(3), alpha*Q(m-k+1,k)):
                for s in (Q(1,4), Q(1), Q(4)):
                    H = process_laplace(m,k,alpha,beta,s,True)
                    L = process_laplace(m,k,alpha,beta,s,False)
                    assert_equal(H, predicted_laplace(m,k,alpha,beta,s,True))
                    assert_equal(L, predicted_laplace(m,k,alpha,beta,s,False))
                    predicted_difference = s*(k*beta-(m-k+1)*alpha) / ((m+1)*(s+alpha)*(s+k*beta))
                    assert_equal(L-H,predicted_difference)
                    assert_equal((L > H), (k*beta > (m-k+1)*alpha))
                for t in (Q(1,10),Q(1),Q(3)):
                    Sh,Sl,diff=survival_values(m,k,alpha,beta,float(t))
                    assert_close(Sl-Sh,diff)
                    assert_equal((Sl<Sh) if abs(diff)>1e-10 else True,
                                 (k*beta>(m-k+1)*alpha) if abs(diff)>1e-10 else True)
print('PASS exact-state and survival checks:',checks)
print('Example (m=5, alpha=beta=1):')
for k in (2,3,4):
    a=b=Q(1)
    H=Q(m-k+1,m+1) if False else Q(5-k+1,6)
    L=(Q(5-k,1)+Q(5-k+1,k))/6
    print(' k=',k,' center-monitor mean=',H,' leaf-only mean=',L)
