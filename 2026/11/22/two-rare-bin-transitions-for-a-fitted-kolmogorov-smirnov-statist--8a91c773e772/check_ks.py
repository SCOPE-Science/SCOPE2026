"""Exact finite checks and seeded diagnostics for the fitted geometric KS regimes.
Usage: python3 check_ks.py . All dependencies are from the Python standard library.
"""
import itertools
import random
from fractions import Fraction
from statistics import mean


def statistic(ks):
    n = len(ks)
    total = sum(ks)
    q = Fraction(total, n + total)
    if max(ks) == 0:
        return Fraction(0)
    return max(abs(Fraction(sum(k >= j for k in ks), n) - q**j)
               for j in range(1, max(ks) + 2))


def direct_cdf(ks):
    n = len(ks)
    q = Fraction(sum(ks), n + sum(ks))
    return max(abs(Fraction(sum(k <= t for k in ks), n) - (1-q**(t+1)))
               for t in range(max(ks) + 2))


def special(a, n):
    return Fraction(a*a, n*(n+a))


count = 0
for n in range(1, 7):
    for ks in itertools.product(range(3), repeat=n):
        d = statistic(ks)
        assert Fraction(0) <= d <= Fraction(1)
        if max(ks) <= 1:
            assert d == special(sum(ks), n)
        count += 1
for n in range(1, 5):
    for ks in itertools.product(range(5), repeat=n):
        assert statistic(ks) == direct_cdf(ks)
        count += 1
for q in (Fraction(1, 3), Fraction(1, 5), Fraction(2, 5)):
    for j in range(1, 7):
        assert abs(float(sum((1-q)*q**k for k in range(j, j+300)) - q**j)) < 1e-90
        count += 1
print('Exact finite identities checked:', count)

rng = random.Random(32603791)
def geometric(q):
    k = 0
    while rng.random() < q:
        k += 1
    return k

def one_trial(n, q):
    ks = [geometric(q) for _ in range(n)]
    a = sum(x>=1 for x in ks)
    b = sum(x>=2 for x in ks)
    total=sum(ks)
    qhat=total/(n+total)
    d=max((abs(sum(x>=j for x in ks)/n - qhat**j)
           for j in range(1, max(ks)+2)),default=0.)
    return d, a, b

# Critical regime: n*q^2=1, so n*D has the |Poisson(1)-1| limit.
for n in (2000, 10000):
    q = n**(-0.5)
    pairs = [one_trial(n,q) for _ in range(200)]
    print('Critical n=',n,'mean(nD)=',round(mean(n*x[0] for x in pairs),4),
          'mean(|N2-1|)=',round(mean(abs(x[2]-1) for x in pairs),4))

# First-bin sparse regime: n*q=2. Rare higher-bin outliers can spoil moment
# convergence, so diagnose probability of a discrepancy, not its mean.
for n in (2000, 10000):
    pairs = [one_trial(n,2/n) for _ in range(200)]
    frac = mean(abs(n*n*x[0]-x[1]**2)>0.05 for x in pairs)
    print('Rare n=',n,'fraction |n^2 D-A^2|>0.05=',round(frac,4))
print('Checker PASS')
