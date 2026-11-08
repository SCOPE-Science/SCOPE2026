"""Independent finite diagnostics for the compact bilateral Aluthge model.

No external dependencies. Diagnostics are finite and are not an infinite proof.
"""
from fractions import Fraction
from math import comb, exp, sqrt, pi, lgamma, log, log1p

ASSERTIONS = 0

def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)

def rational_moment(n, t, k, alpha):
    return sum(Fraction(comb(n, j))*t**j*(1-t)**(n-j)*abs(k+j)**alpha
               for j in range(n+1))

# Exact binomial formula versus repeated nearest-neighbor log averaging.
for t in [Fraction(1, 2), Fraction(2, 5), Fraction(1, 3)]:
    for alpha in [1, 2, 3]:
        initial = {k: abs(k)**alpha for k in range(-25, 26)}
        values = initial
        for n in range(9):
            for k in range(-14, 15):
                check(values[k] == rational_moment(n, t, k, alpha),
                      'binomial iteration at n=%d k=%d' % (n, k))
            values = {k: (1-t)*values[k] + t*values[k+1]
                      for k in range(-25, 25-n)}

# Quadratic case: exact expression, not asymptotics.
for t in [Fraction(1, 2), Fraction(2, 5), Fraction(1, 3)]:
    for n in range(1, 24):
        mu = n*t
        sigma2 = n*t*(1-t)
        for k in range(-6, 7):
            check(rational_moment(n, t, k, 2) == sigma2 + (k+mu)**2,
                  'quadratic identity at n=%d k=%d' % (n, k))

# Laplace absolute deviation: exact telescoping formula for every n/t.
def pmf(n,t):
    return [exp(lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)
                + j*log(t)+(n-j)*log1p(-t)) for j in range(n+1)]

for t in [.23, .37, .5, .71]:
    for n in [10, 32, 72, 128, 256, 512]:
        weights = pmf(n,t)
        mu=n*t
        f_mu = sum(weights[j]*abs(j-mu) for j in range(n+1))
        exact = 2*n*t*(1-t)*pmf(n-1,t)[int(mu)]
        check(abs(f_mu-exact) < 3e-9, 'absolute-deviation identity')

# Numerical asymptotic checks of the two-scale norm/Schatten profile.
t=.37
a=.8
p=2.0
c=sqrt(2/pi)
for n in [512, 1024, 2048]:
    weights=pmf(n,t)
    mu=n*t
    sigma=sqrt(n*t*(1-t))
    m0=int(mu)
    f0=sum(prob*abs(j-m0) for j,prob in enumerate(weights))
    f1=sum(prob*abs(j-(m0+1)) for j,prob in enumerate(weights))
    fmin=min(f0,f1)
    check(abs(fmin/sigma-c) < .03, 'leading operator-norm exponent')
    radius=int(8*sigma)+1
    truncated_sum=0.0
    for m in range(max(0,int(mu)-radius),min(n,int(mu)+radius)+1):
        fm=sum(prob*abs(j-m) for j,prob in enumerate(weights))
        truncated_sum+=exp(-a*p*(fm-fmin))
    predicted=sqrt(sigma)*sqrt(2*pi/(a*p*c))
    check(abs(truncated_sum/predicted-1) < .13,
          'Gaussian Schatten asymptotic n=%d' % n)

print('PASS:', ASSERTIONS, 'finite diagnostics')
