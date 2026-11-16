"""Numerical spot check of the polar Jacobian and sharp half-order scaling.

The theoretical proof is independent of these quadrature checks.  The test
function is radial about the north pole and vanishes to all orders outside an
annular band in geodesic distance.
"""
import math


def bump(t):
    if not 1 < t < 2:
        return 0.0
    q = (t-1)*(2-t)
    return math.exp(-1/q)


def bump_prime(t):
    if not 1 < t < 2:
        return 0.0
    q = (t-1)*(2-t)
    return math.exp(-1/q) * (3-2*t)/(q*q)


def simpson(fn, a=1.0, b=2.0, n=4096):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3*(fn(a)+fn(b)+4*sum(fn(a+h*i) for i in range(1,n,2))
                +2*sum(fn(a+h*i) for i in range(2,n,2)))


I0 = simpson(lambda x: bump(x)**2)
I1 = simpson(lambda x: bump_prime(x)**2)
J0 = simpson(lambda x: x*bump(x)**2)
J1 = simpson(lambda x: x*bump_prime(x)**2)
assert I0 > 0 and I1 > 0 and J0 > 0 and J1 > 0

# Exact formulas (with the Euclidean torus measure d(lambda)d(theta),
# and spherical measure sin(theta)d(theta)d(lambda)):
# sphere L2 squared = 2*pi*eps*integral h(u)^2 sin(eps*u) du
# torus L2 squared  = 4*pi*eps*integral h(u)^2 du
# sphere H1 seminorm squared = (2*pi/eps)* integral h'(u)^2 sin(eps*u) du
# torus H1 seminorm squared  = (4*pi/eps)*integral h'(u)^2 du

header = 'epsilon sqrt(epsilon)*L2_ratio sqrt(epsilon)*H1_seminorm_ratio'
print(header)
for eps in [0.2,0.1,0.05,0.025,0.0125]:
    j0_eps = simpson(lambda u: bump(u)**2*math.sin(eps*u))
    j1_eps = simpson(lambda u: bump_prime(u)**2*math.sin(eps*u))
    norm_ratio0 = math.sqrt(2*I0/j0_eps)
    norm_ratio1 = math.sqrt(2*I1/j1_eps)
    scaled0,scaled1=math.sqrt(eps)*norm_ratio0,math.sqrt(eps)*norm_ratio1
    print(f'{eps:.7f} {scaled0:.9f} {scaled1:.9f}')
    assert abs(scaled0-math.sqrt(2*I0/J0)) < .08
    assert abs(scaled1-math.sqrt(2*I1/J1)) < .08

# Exact asymptotic limits from sin(eps*u)/eps -> u.
print(f'limits: {math.sqrt(2*I0/J0):.9f} {math.sqrt(2*I1/J1):.9f}')
print('PASS: exact Jacobian formulas and five near-pole scaling tests')
