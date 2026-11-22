"""Finite reproducibility checks for exponential-mixture posted-price revenue.

The global zero-count theorem and the all-integer construction are proved in
RESULT.md. Numerical tests do not establish either infinite statement.
"""
from __future__ import annotations
import math
import random

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def derivative(price, rates):
    return sum(rate * (1.0 - rate * price) * math.exp(-rate * price)
               for rate in rates)

def revenue(price, rates):
    return price * sum(rate * math.exp(-rate * price) for rate in rates)

def max_root(left, right, rates):
    check(derivative(left, rates) > 0.0, 'positive left sign')
    check(derivative(right, rates) < 0.0, 'negative right sign')
    for _ in range(110):
        mid = (left + right) / 2.0
        if derivative(mid, rates) > 0.0:
            left = mid
        else:
            right = mid
    return (left + right) / 2.0

def run():
    L = 400
    # Proved universal bound for the relative peak-height spread.
    bound = math.e * (1.5/(L-1) + 0.5*math.exp(-L/4)/(1-math.exp(-L/4)))
    check(bound < 0.011, 'analytic relative height bound')
    for n in range(1, 9):
        rates = [float(L ** j) for j in range(n)]
        roots = []
        heights = []
        for j in range(n):
            rate = rates[j]
            left = 0.5 / rate
            right = 1.5 / rate
            root = max_root(left, right, rates)
            roots.append(root)
            height = revenue(root, rates)
            heights.append(height)
            check(left < root < right, 'maximizer lies in announced interval')
            check(height >= 1 / math.e - 1e-13, 'local peak lower bound')
            check(height <= 1 / math.e + bound / math.e + 1e-12,
                  'local peak upper bound')
            for frac in [0.51, 0.6, 0.75, 0.9, 1.1, 1.25, 1.4, 1.49]:
                d = derivative(frac / rate, rates)
                check((d > 0) if frac < 1 else (d < 0),
                      'sample derivative sign around isolated mode')
        check(all(roots[i] > roots[i+1] for i in range(n-1)),
              'distinct ordered modes')
        check(max(heights) / min(heights) < 1.011,
              'uniform near-equal local peak heights')
        # Relative peak heights are unchanged by probability normalization.
        total = sum(rates)
        check(abs((max(heights)/total)/(min(heights)/total)
                  - max(heights)/min(heights)) < 1e-12,
              'normalization invariance')
    # Illustrative stress tests on ordinary heterogeneous mixtures.
    rng = random.Random(920241)
    for n in range(1, 7):
        for _ in range(200):
            rates = sorted(math.exp(rng.uniform(-3, 3)) for j in range(n))
            weights = [math.exp(rng.uniform(-3, 3)) for j in range(n)]
            grid = [math.exp(-8 + k*16/2400) for k in range(2401)]
            signs = []
            for p in grid:
                d = sum(w * (1-r*p) * math.exp(-r*p)
                        for r,w in zip(rates,weights))
                signs.append(d)
            observed_maxima = sum(signs[k-1] > 0 > signs[k]
                                  for k in range(1,len(signs)))
            check(observed_maxima <= n, 'sampled peak bound')
    print(f'PASS {CHECKS} finite numerical assertions')
    print('The all-n proof and analytic height bound are in RESULT.md.')

if __name__ == '__main__':
    run()
