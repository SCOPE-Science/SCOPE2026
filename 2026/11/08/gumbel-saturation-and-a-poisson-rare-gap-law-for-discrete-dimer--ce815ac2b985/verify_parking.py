#!/usr/bin/env python3
"""Exact independent finite-volume checks for Page dimer-parking saturation.
Science-only standalone script; uses Python standard library.
"""
from fractions import Fraction
from math import factorial, exp, log
from itertools import combinations, permutations

CHECKS = 0

def check(a, b, label):
    global CHECKS
    CHECKS += 1
    if a != b:
        raise AssertionError(f'{label}: {a} != {b}')

def endpoint_vacancy(n, v):
    return sum(((-v)**j / factorial(j) for j in range(n)), Fraction(0))

def count_available(n, attempted):
    """Applied first attempts in chronological order; returns vacant adjacent pairs."""
    occupied = [False] * n
    for edge in attempted:
        if not occupied[edge] and not occupied[edge + 1]:
            occupied[edge] = occupied[edge + 1] = True
    return [i for i in range(n - 1) if not occupied[i] and not occupied[i + 1]]

def exact_availability(n, v):
    """Independently enumerate the attempted subset and its uniform priority order."""
    probs = [Fraction(0) for _ in range(n - 1)]
    pzero = Fraction(0)
    falling = Fraction(0)
    for k in range(n):
        for comb in combinations(range(n - 1), k):
            weight = v**k * (1 - v)**(n - 1 - k) / factorial(k)
            for perm in permutations(comb):
                free_edges = count_available(n, perm)
                if not free_edges:
                    pzero += weight
                falling += len(free_edges) * weight
                for edge in free_edges:
                    probs[edge] += weight
    return probs, pzero, falling

def main():
    for n in range(2, 9):
        for v in [Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)]:
            probs, pzero, first_moment = exact_availability(n, v)
            expected = [
                (1-v)*endpoint_vacancy(i, v)*endpoint_vacancy(n-i, v)
                for i in range(1, n)
            ]
            for i in range(n-1):
                check(probs[i], expected[i], f'n={n},v={v},i={i}')
            check(first_moment, sum(expected, Fraction(0)), f'first moment n={n},v={v}')
            check(pzero >= 0 and pzero <= 1, True, f'pzero n={n},v={v}')
    # Pathwise jamming identity for all complete priority orders and every time cut.
    for n in range(2, 8):
        for perm in permutations(range(n-1)):
            for k in range(n):
                available = bool(count_available(n, perm[:k]))
                occ = [False]*n
                future_success = 0
                for edge in perm:
                    if not occ[edge] and not occ[edge+1]:
                        if perm.index(edge) >= k:
                            future_success += 1
                        occ[edge] = occ[edge+1] = True
                check(available, future_success > 0, f'jamming n={n},prefix={k}')
    # Exact boundary identity: endpoint vacancies satisfy a first-order Volterra recursion.
    for n in range(2, 30):
        for v in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1)]:
            check(endpoint_vacancy(n,v), endpoint_vacancy(n-1,v) + (-v)**(n-1)/factorial(n-1), f'telescoping n={n},v={v}')
    # Exact mean approaches e^(-2-x) at critical time log(n)+x, for x=0.
    for n in [200, 1000, 5000, 20000]:
        t=log(n)
        v=1-exp(-t)
        u=[sum((-v)**j/factorial(j) for j in range(min(k,170))) for k in range(1,n)]
        exact = exp(-t)*sum(u[i-1]*u[n-i-1] for i in range(1,n))
        limit=exp(-2)
        assert abs(exact-limit) < 1.2/n, (n, exact, limit)
        global CHECKS
        CHECKS += 1
    print('PASS:',CHECKS,'exact identities and controlled numerical mean checks')

if __name__ == '__main__':
    main()
