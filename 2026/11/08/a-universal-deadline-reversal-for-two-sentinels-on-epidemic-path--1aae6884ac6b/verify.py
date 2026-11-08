#!/usr/bin/env python3
"""Standalone checks for finite-horizon two-sentinel detection on paths.

Requires Python 3, SymPy, NumPy, SciPy. All scientific claims are proved
in RESULT.md; sampled matrix exponentials only check implementation.
"""
from __future__ import annotations
import itertools
import math
import numpy as np
from scipy.linalg import expm
import sympy as sp


def tail(distance: int, x: float) -> float:
    if distance == 0:
        return 0.0
    return math.exp(-x) * sum(x**j / math.factorial(j) for j in range(distance))


def analytic_failure(n: int, sensors: tuple[int, int], x: float) -> float:
    a, b = sensors
    total = 0.0
    for seed in range(n):
        if seed == a or seed == b:
            continue
        if seed < a:
            total += tail(a - seed, x)
        elif seed > b:
            total += tail(seed - b, x)
        else:
            total += tail(seed - a, x) * tail(b - seed, x)
    return total / n


def exact_ctmc_generator(n: int) -> np.ndarray:
    # Column convention: Q[new_state, old_state] is rate of old -> new.
    m = 1 << n
    Q = np.zeros((m, m), dtype=float)
    for s in range(1, m):
        for v in range(n):
            if (s >> v) & 1:
                continue
            nbr_infected = (int(v > 0 and ((s >> (v-1)) & 1))
                            + int(v + 1 < n and ((s >> (v+1)) & 1)))
            if nbr_infected:
                Q[s | (1 << v), s] += nbr_infected
                Q[s, s] -= nbr_infected
    assert np.allclose(Q.sum(axis=0), 0)
    return Q


def ctmc_failure(expQ: np.ndarray, n: int,
                 sensors: tuple[int, int]) -> float:
    mask = (1 << sensors[0]) | (1 << sensors[1])
    avoiding = [state for state in range(1 << n) if state & mask == 0]
    return sum(expQ[np.ix_(avoiding, [1 << seed])].sum()
               for seed in range(n)) / n


def main() -> None:
    x = sp.symbols('x', positive=True)
    f01 = sp.exp(-x) * (x + 2) / 4
    f02 = (sp.exp(-x) + sp.exp(-2*x)) / 4
    f03 = sp.exp(-2*x) * (1+x) / 2
    f12 = sp.exp(-x) / 2
    # Exact P4 probability identities and equal mean hitting times.
    assert sp.simplify((f02-f03)-sp.exp(-2*x)*(sp.exp(x)-1-2*x)/4) == 0
    assert sp.simplify(f01-f02 - sp.exp(-2*x)*((x+1)*sp.exp(x)-1)/4) == 0
    assert sp.simplify(f12-f02 - sp.exp(-2*x)*(sp.exp(x)-1)/4) == 0
    assert sp.integrate(f02, (x, 0, sp.oo)) == sp.Rational(3,8)
    assert sp.integrate(f03, (x, 0, sp.oo)) == sp.Rational(3,8)
    threshold = float(sp.nsolve(sp.exp(x)-1-2*x, 1.3))
    assert abs(threshold - 1.2564312086261697) < 1e-13
    assert np.isclose(analytic_failure(3, (0,2), 1), np.exp(-2)/3)
    analytical_vs_ctmc = 0
    for n in range(2, 9):
        Q = exact_ctmc_generator(n)
        for h in (0.07, 0.4, 1.25, 3.5):
            P = expm(Q*h)
            for pair in itertools.combinations(range(n), 2):
                result = ctmc_failure(P, n, pair)
                target = analytic_failure(n, pair, h)
                assert abs(result-target) < 4e-12, (n,h,pair,result,target)
                analytical_vs_ctmc += 1
    small_and_large = 0
    for n in range(4, 19):
        endpoint = (0, n-1)
        short_alternative = (0,2) if n==4 else (1,n-2)
        assert analytic_failure(n,short_alternative,1e-4) < analytic_failure(n,endpoint,1e-4)
        # A finite sample of the guaranteed eventual endpoint dominance.
        x_big = 2*n*n
        for pair in itertools.combinations(range(n),2):
            if pair != endpoint:
                # Use high-precision via mpmath to avoid underflow.
                import mpmath as mp
                mp.mp.dps = 110
                xm = mp.mpf(x_big)
                def st(k):
                    return mp.exp(-xm)*sum(xm**j/mp.factorial(j) for j in range(k)) if k else mp.mpf(0)
                def f(p):
                    a,b=p
                    result=mp.mpf(0)
                    for i in range(n):
                        if i in p:continue
                        if i<a:result += st(a-i)
                        elif i>b:result += st(i-b)
                        else:result += st(i-a)*st(b-i)
                    return result/n
                assert f(endpoint)<f(pair), (n,pair)
                small_and_large += 1
    print('P4 symbolic identities and mean-time tie: PASS')
    print('P4 unique positive threshold:', format(threshold,'.16f'))
    print('Independent full-SI-state CTMC comparisons:', analytical_vs_ctmc, 'PASS')
    print('Small/large-horizon sample comparisons:', small_and_large, 'PASS')
    print('All checks passed. Numerical checks do not replace general proof.')


if __name__ == '__main__':
    main()
