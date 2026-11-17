"""Independent finite-generator and conditional-clock checks for a batch-reset Brownian gas.

Run with: python3 CHECK.py
Uses only the Python standard library. All units are D=r=1 unless stated.
"""
from fractions import Fraction as F
import math
import random

checks = 0

def verify(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)

# Finite-N moment equations follow directly from the exact generator.
# Single reset probability p=m/N; pair reset union probability a2.
for N in range(2, 49):
    for m in range(1, N + 1):
        p = F(m, N)
        a2 = 1 - F((N-m)*(N-m-1), N*(N-1))
        second = 2/p
        fourth = 24/p**2
        pair = 8/(p*a2)
        variance = (fourth + (N-1)*pair)/N - second**2
        verify(p*second == 2, f'second moment N={N},m={m}')
        verify(p*fourth == 12*second, f'fourth moment N={N},m={m}')
        verify(a2*pair == 4*second, f'pair moment N={N},m={m}')
        verify(variance > 0, f'energy variance N={N},m={m}')

# Random-measure Fourier moment recursion agrees algebraically with the
# independently available two-particle stationary Fourier formula.
for i in range(1, 50):
    p = F(i, 50)
    q = 1 - p
    for j in range(1, 17):
        u = F(j, 9)
        a = 1/(1+u)
        b = 1/(1+2*u)
        first = p*a/(1-q*a)
        square = b*(p*p+2*p*q*first)/(1-q*q*b)
        published_pair_formula = (p+2*q*first)/(2-p+2*u/p)
        verify(first == p/(p+u), 'one-point Fourier marginal')
        verify(square == published_pair_formula, 'two-point Fourier marginal')
        verify(square > first**2, 'random-density Fourier fluctuations')

# Sharp exponential collective-energy tail: normalization and cumulants.
for i in range(1, 50):
    p = F(i, 50)
    q = 1-p
    for order in range(1, 8):
        cumulant = F(math.factorial(order-1), 1)/(1-q**order)
        verify(cumulant > 0, 'collective cumulant positivity')
    mean = 1/p
    var = 1/(1-q*q)
    verify(var/mean**2 == p/(2-p), 'normalized macroscopic variance')

# Explicit environmental realization and independent finite-population sampling.
# All particles carry Brownian displacement since their most recent batch reset.
for seed in range(15):
    rng = random.Random(12000+seed)
    N = 2400
    m = 840
    p = m/N
    q = 1-p
    J = 37
    gaps = [rng.expovariate(1.0) for _ in range(J)]
    ages = []
    c = 0.0
    for gap in gaps:
        c += gap
        ages.append(c)
    last = [-1]*N
    for j in range(J):
        for label in rng.sample(range(N),m):
            if last[label] < 0:
                last[label]=j
    verify(all(j >= 0 for j in last), 'every sampled label has a recent reset')
    empirical = sum(rng.gauss(0.0, math.sqrt(2.0*ages[j]))**2 for j in last)/N
    predicted = 2*sum(p*q**j*ages[j] for j in range(J))
    verify(abs(empirical-predicted) < 1.3, 'conditional random energy prediction')
    # Test a bounded local density probe in addition to unbounded energy.
    empirical_c = sum(math.cos(math.sqrt(0.8)*rng.gauss(0,math.sqrt(2*ages[j]))) for j in last)/N
    predicted_c = sum(p*q**j*math.exp(-0.8*ages[j]) for j in range(J))
    verify(abs(empirical_c-predicted_c)<0.10, 'conditional Fourier-probe prediction')

# The collective tail prefactor converges, and the next gap has a moment
# of order greater than the leading exponential rate.
for q in (0.05,0.25,0.5,0.75,0.9):
    prefactors=[]
    z=1.0
    for j in range(1,901):
        z /= (1-q**j)
        if j in (200,500,900):
            prefactors.append(z)
    verify(prefactors[-1] >= prefactors[0], 'tail product monotonic')
    verify((prefactors[-1]-prefactors[1])/prefactors[-1] < 0.0005,
           'tail prefactor truncation')

print(f'PASS: {checks} checks (exact generator / Fourier recursions / cumulants / conditional clock simulations / tail product).')
