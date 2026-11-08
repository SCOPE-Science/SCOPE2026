"""Standalone finite checks of identities used by the analytic Sibuya mesh-risk argument.
Run: python verify.py. These finite computations do not replace the infinite-series proof.
"""
from fractions import Fraction
import math
import mpmath as mp

mp.mp.dps = 55
count = 0

def check(flag, description):
    global count
    assert flag, description
    count += 1

# Sibuya probabilities, computed without gamma-function cancellation.
a = Fraction(3, 4)
p = a
s = Fraction(0)
for k in range(1, 1001):
    check(p > 0, 'positive Sibuya mass')
    s += p
    check(s < 1, 'partial probability sum')
    # P(K>k)=prod_{j=1}^{k}(1-alpha/j), proved by telescoping.
    tail = Fraction(1)
    for j in range(1, k+1) if k <= 35 else []:
        tail *= 1 - a/Fraction(j, 1)
    if k <= 35:
        check(s + tail == 1, 'exact Sibuya survival identity')
    p *= (Fraction(k, 1) - a) / Fraction(k+1, 1)

# The Gamma ratio first-order asymptotic coefficient d=alpha(alpha+1)/2.
for a_str in ['0.25', '0.5', '0.75']:
    alpha = mp.mpf(a_str)
    c = alpha/mp.gamma(1-alpha)
    d = alpha*(alpha+1)/2
    for k in [3000, 12000, 48000]:
        pk = alpha*mp.gamma(k-alpha)/(mp.gamma(1-alpha)*mp.gamma(k+1))
        scaled = mp.mpf(k)*(pk/(c*mp.power(k, -alpha-1))-1)
        check(abs(scaled-d) < mp.mpf('0.0015'), 'gamma ratio asymptotic')

for alpha,beta in [(mp.mpf(3)/4,mp.mpf(1)/4),
                   (mp.mpf(1)/2,mp.mpf(1)/8),
                   (mp.mpf(3)/4,mp.mpf(1)/2)]:
    c=alpha/mp.gamma(1-alpha)
    I=c*mp.beta(beta+1,alpha-beta)
    d=alpha*(alpha+1)/2
    J=mp.beta(beta+1,alpha+1-beta)
    check(abs(c*d*J/I-alpha*(alpha-beta)/2) < mp.mpf('1e-48'),
          'sharp first-order bias coefficient')
    integral=mp.quad(lambda r: (r-1)**beta/r**(1+alpha), [1,2,10,mp.inf])
    check(abs(integral-mp.beta(beta+1,alpha-beta)) < mp.mpf('1e-12'),
          'continuum Marchaud beta integral')
    if 2*beta < alpha:
        C=c*mp.beta(2*beta+1,alpha-2*beta)
        second=mp.quad(lambda r: (r-1)**(2*beta)/r**(1+alpha), [1,2,10,mp.inf])
        check(abs(c*second-C)<mp.mpf('1e-12'), 'variance beta integral')
        B=I*alpha*(alpha-beta)/2
        N=mp.mpf(100000)
        h=(alpha*C/(2*B**2*N))**(1/(alpha+2))
        # Exact derivative of the leading MSE at its unique minimizer.
        check(abs(2*B**2*h-alpha*C/(N*h**(alpha+1)))<mp.mpf('1e-45'),
              'mesh-budget stationary balance')
        check(h>0, 'optimal mesh positive')

# Divergence and convergence illustrated without calling finite sums proofs.
alpha=0.75
p=alpha
S_high=0.0
S_low=0.0
prev_high=0.0
prev_low=0.0
for k in range(1, 200001):
    S_high+=p*k**(1.0)   # beta=1/2 gives 2beta=1 > alpha
    S_low+=p*k**(0.5)    # beta=1/4 gives 2beta=1/2 < alpha
    if k in [2000,20000,200000]:
        check(S_high>prev_high, 'divergent partial second moment grows')
        check(S_low>prev_low, 'convergent partial second moment increases to limit')
        prev_high, prev_low=S_high,S_low
    p *= (k-alpha)/(k+1)

print(f'PASS {count} checks; analytic tails and first-order limits require the proof in RESULT.md')
