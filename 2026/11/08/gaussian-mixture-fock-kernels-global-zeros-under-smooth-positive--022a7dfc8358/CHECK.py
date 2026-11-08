"""Finite numerical checks for two-Gaussian weighted Fock kernels. Python >=3.9; stdlib only."""
import cmath
import math
from fractions import Fraction

checks = 0

def require(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)

def direct_series(t, eps, a, b, N=120):
    value = 0j
    term = 1+0j
    for n in range(N):
        if n:
            term *= t/n
        value += term/((1-eps)*a**(-n) + eps*b**(-n))
    return value

def exponential_series(t, eps, a, b, N=70):
    q = eps/(1-eps)
    r = a/b
    return sum((-q)**k*cmath.exp(a*r**k*t) for k in range(N))/(1-eps)

def normalized(z, q, r, N=90):
    return sum((-q)**k*cmath.exp((r**k-1)*z) for k in range(N))

# Exact moment identity for mixed normalized Gaussian measures.
for n in range(20):
    a,b,eps = Fraction(1), Fraction(2), Fraction(1,10)
    moment = math.factorial(n)*((1-eps)*a**(-n)+eps*b**(-n))
    reciprocal_coeff = 1/((1-eps)*a**(-n)+eps*b**(-n))
    require(moment * reciprocal_coeff == math.factorial(n), 'rational moment')

for eps in (0.0001,0.001,0.01,0.1):
    for t in (-1.3, -0.5+0.7j, 0, 1.2+0.3j, 2.0):
        a, b = 1, 2
        u = direct_series(t,eps,a,b)
        v = exponential_series(t,eps,a,b)
        require(abs(u-v) < 1e-10 * (1+abs(u)), 'exponential versus moment kernel')

# Root of H_q on the negative axis; scaled h avoids destructive underflow.
r=0.5
for eps in (1e-3,1e-4,1e-5,1e-6,1e-7):
    q=eps/(1-eps)
    z0=math.log(q)/(1-r)
    left=z0-1.5
    right=z0+1.5
    fl=normalized(left,q,r).real
    fr=normalized(right,q,r).real
    require(fl<0<fr, 'real root bracketing')
    for it in range(90):
        mid=(left+right)/2
        if normalized(mid,q,r).real >0:
            right=mid
        else:
            left=mid
    z=(left+right)/2
    require(abs(normalized(z,q,r)) < 5e-10, 'root residual')
    require(abs(z-z0) <= 10*q**(1-r), 'logarithmic zero onset')
    approx=z0 - q**(1-r)/(1-r)
    require(abs(z-approx) < 10*q**(2*(1-r)), 'first zero correction')

# Uniform positive curvature lower bound, sample dimensions and parameters.
for d in (1,2,5):
    a,b = 1.0,2.0
    for eps in (0.0001,0.001,0.01):
        eta=(eps/(1-eps))*(b/a)**d
        if eta >= a*math.e/(2*(b-a)):
            continue
        for n in range(40):
            s=n/4
            p=eta*math.exp(-(b-a)*s)/(1+eta*math.exp(-(b-a)*s))
            tangent=a+(b-a)*p
            radial=tangent-(b-a)**2*s*p*(1-p)
            require(tangent>=a/2 and radial>=a/2, 'curvature lower bound')

print('PASS',checks,'finite checks')
