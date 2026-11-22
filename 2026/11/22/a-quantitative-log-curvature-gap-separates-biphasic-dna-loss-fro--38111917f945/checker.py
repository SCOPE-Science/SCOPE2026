"""Supplementary finite-precision checks for a five-sample decay-model discriminator.

These tests are not a substitute for the analytic proof in RESULT.md.
Requires Python 3.11 or later; standard library only.
"""
from decimal import Decimal as D, getcontext
import math
import random

getcontext().prec = 75

def K(C):
    assert len(C) >= 5
    L = [x.ln() for x in C]
    return [L[j] - 2 * L[j+1] + L[j+2] for j in range(3)]

# Exact, simple rational concentration sample under the two-pool model.
C = [D(1), D(3)/8, D(5)/32, D(9)/128, D(17)/512]
k0,k1,k2=K(C)
assert abs(k0-(D(10)/9).ln()) < D('1e-65')
assert abs(k1-(D(27)/25).ln()) < D('1e-65')
assert abs(k2-(D(85)/81).ln()) < D('1e-65')
assert k1*k1 - k0*k2 > D('0.00084')
q=D('0.5')
s0=D(1)
s2=s0*q*q
def gap_bound(q,s0):
    s2=s0*q*q
    return (q.ln()**2)*min(2*q*s/((1+s)*(1+q*q*s)) for s in (s0,s2))
assert (k1*k1/(k0*k2)).ln() > gap_bound(q,s0)

# Explicit competing positive-hazard model exactly matches the first four
# concentrations; fifth is separated by strictly log-concave curvature.
r=k1/k0
beta=k0/(1-r)**2
alpha=(D(8)/3).ln()-k0/(1-r)
kappa=-r.ln()
assert D(0)<r<D(1) and beta>0 and alpha>0 and kappa>0
R = [(-alpha*D(j)-beta*(1-r**j)).exp() for j in range(5)]
for j in range(4):
    assert abs(R[j]-C[j]) < D('1e-64')
assert abs(R[4]-C[4]) > D('1e-5')
assert abs(K(R)[1]**2-K(R)[0]*K(R)[2]) < D('1e-60')

# Supplementary randomized checks. None replace the global analytic proof.
rng=random.Random(104729)
for _ in range(12000):
    w=rng.uniform(0.05,0.95)
    lam=rng.uniform(0.05,2)
    mu=lam+rng.uniform(0.08,3)
    h=rng.uniform(0.02,2)
    t0=rng.uniform(0,4)
    sample=[w*math.exp(-lam*(t0+j*h))+(1-w)*math.exp(-mu*(t0+j*h)) for j in range(5)]
    lc=[math.log(x) for x in sample]
    q=[lc[j]-2*lc[j+1]+lc[j+2] for j in range(3)]
    # Guard roundoff (strictness is independently established analytically).
    assert q[0]>0 and q[1]>0 and q[2]>0
    assert q[1]**2 >= q[0]*q[2] - 1e-12
    # Additional margin check away from severe roundoff; requires no solver.
    decay_ratio=math.exp(-(mu-lam)*h)
    pool_ratio=(1-w)/w*math.exp(-(mu-lam)*t0)
    end_ratio=pool_ratio*decay_ratio**2
    bound=math.log(decay_ratio)**2*min(2*decay_ratio*z/((1+z)*(1+decay_ratio**2*z)) for z in (pool_ratio,end_ratio))
    if min(q)>1e-7:
        actual=math.log(q[1]**2/(q[0]*q[2]))
        assert actual >= bound-2e-5

print('PASS: exact rational observations, positive four-point alias, fifth-point separation')
print('PASS: 12000 supplementary two-pool numerical comparisons')
print('witness r=',r)
print('witness alpha=',alpha)
print('witness beta=',beta)
print('witness kappa=',kappa)
print('witness curvature determinant=',k1*k1-k0*k2)
