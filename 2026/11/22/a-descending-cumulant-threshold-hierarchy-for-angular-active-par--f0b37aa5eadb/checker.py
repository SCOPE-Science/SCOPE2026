#!/usr/bin/env python3
"""Standalone finite numerical checks for the Brownian angular-exit cumulant hierarchy.
All infinite-order assertions are established analytically in RESULT.md, not here.
Run with python3 checker.py; Python standard library only.
"""
import math

P = math.pi
Q0 = 8 / P**2
V0 = 1 - Q0


def c_power(m, terms=3000):
    return sum((Q0 / (2*j + 1)**2)**m for j in range(terms))


def R(m, v):
    return c_power(m) * (1 - v**m) / (1-v)**m


def root_v(m):
    lo, hi = V0, 0.2
    for _ in range(78):
        mid = (lo + hi) / 2
        if R(m, mid) > 1:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def laplace_brownian(s, u=0.3, a=1., diffusivity=1.):
    h = a * math.sqrt(s / diffusivity)
    return math.cosh(u*h) / math.cosh(h)


def laplace_product(s, u=0.3, a=1., diffusivity=1., terms=10000):
    p = 1 - u*u
    value = 1.
    for j in range(terms):
        lam = diffusivity * P**2 * (2*j+1)**2 / (4*a*a)
        value *= (1-p) + p * lam/(lam+s)
    return value


def survival_spectral(t, u, terms=40):
    return sum(4/P*(-1)**j/(2*j+1) * math.cos((2*j+1)*P*u/2)
               *math.exp(-P**2*(2*j+1)**2*t/4) for j in range(terms))


checks = 0

def verify(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

# Explicit normalizations and inequalities used in the proof.
verify(1/9 < V0 < 1/5, 'location of spectral threshold')
verify(c_power(2) > 0 and abs(c_power(2)-2/3) < 1e-11, 'second spectral power')
verify(abs(c_power(3)-8/15) < 1e-12, 'third spectral power')
verify(math.pi**4/96-1 < (4/5)*V0**2, 'comparison bound for monotonicity')

# Nonzero-angle Euler-product factorization, not merely zero-angle sampling.
for u in [0.0,0.17,0.435,0.7,0.95]:
    for s in [0.1,0.5,1.,3.,8.]:
        exact = laplace_brownian(s,u)
        approximate = laplace_product(s,u)
        verify(abs(exact-approximate)< 3.0e-4, 'thinned exponential factorization')

# Strictly decreasing unique thresholds for m=2,...,13.
prev = 0.201
for m in range(2,14):
    v = root_v(m)
    verify(V0 < v <= 0.2000000000001, 'threshold bounds')
    verify(v < prev-1e-14, 'strict ordering of thresholds')
    verify(abs(R(m,v)-1)<2e-11, 'cumulant comparison equation')
    verify(R(m, V0)<1, 'spectral endpoint lower side')
    prev = v

for m, expected in [(2,.4472135954999579),(3,.4369501879659423),
                    (4,.4355013577510173),(5,.4352784783718598)]:
    verify(abs(math.sqrt(root_v(m))-expected)<1e-10,'root benchmark')

# Independent spectral survival and matched exponential: variance<exp,
# but ultimate survival larger in the narrow window (sqrt(V0),1/sqrt(5)).
for u in [0.438, 0.44, 0.445]:
    p = 1-u*u
    r = 2/p                 # dimensionless a=D=1
    lam0 = P**2/4
    verify(r > lam0, 'mean-matched exponential tail rate')
    verify((2/3)*(1+u*u)/(1-u*u) < 1, 'relative variance inequality')
    for t in [3.,4.,5.,10.]:
        verify(survival_spectral(t,u) > math.exp(-r*t), 'ultimate tail inequality')

print('PASS:',checks,'deterministic numerical assertions')
print('u_tail =',math.sqrt(V0))
for m in range(2,11):
    print('threshold',m, f'{math.sqrt(root_v(m)):.12f}')
