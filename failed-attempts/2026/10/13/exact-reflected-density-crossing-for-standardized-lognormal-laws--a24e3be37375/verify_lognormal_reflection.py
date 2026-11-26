#!/usr/bin/env python3
import math

def g(sigma,z):
    # standardized lognormal density, with log-location 0
    s=sigma*sigma
    m=math.exp(s/2)
    c=math.sqrt(math.exp(s)-1.0)
    sd=m*c
    x=m+sd*z
    if x<=0:
        return 0.0
    return sd/(sigma*x*math.sqrt(2*math.pi))*math.exp(-(math.log(x))**2/(2*s))

def logratio_closed(sigma,z):
    s=sigma*sigma
    c=math.sqrt(math.exp(s)-1.0)
    u=c*z
    return math.atanh(u)*(-3.0-math.log1p(-u*u)/s)

def kappa(sigma):
    s=sigma*sigma
    return math.sqrt(math.exp(-s)+math.exp(-2*s)+math.exp(-3*s))

# Deterministic identity/sign checks at representative shape values.
for sigma in (0.1,0.3,0.7,1.0,1.7,2.5):
    s=sigma*sigma
    c=math.sqrt(math.exp(s)-1.0)
    k=kappa(sigma)
    assert 0.0 < k < 1.0/c
    for frac in (0.1,0.4,0.8,1.0,1.02):
        z=k*frac
        if z>=0.999999/c:
            continue
        lhs=math.log(g(sigma,z)/g(sigma,-z))
        rhs=logratio_closed(sigma,z)
        assert abs(lhs-rhs) < 2e-10*(1+abs(rhs))
        if frac < 1.0:
            assert lhs < 1e-10
        elif frac > 1.0:
            assert lhs > -1e-10
        else:
            assert abs(lhs) < 2e-10

# Unique one-standard-deviation crossing threshold q+q^2+q^3=1.
lo,hi=0.0,1.0
for _ in range(100):
    q=(lo+hi)/2
    if q+q*q+q*q*q < 1.0: lo=q
    else: hi=q
q=(lo+hi)/2
sigma_star=math.sqrt(-math.log(q))
assert abs(kappa(sigma_star)-1.0) < 2e-14
# Monotonicity on a deterministic mesh.
vals=[kappa(0.01+i*0.01) for i in range(1,500)]
assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))
print(f"VERIFY_OK sigma_star={sigma_star:.15f} q={q:.15f}")
