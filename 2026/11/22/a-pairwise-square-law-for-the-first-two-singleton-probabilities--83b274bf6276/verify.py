"""Exact finite diagnostics for the singleton gap at coupon completion.

Requires only Python 3 standard library. These finite tests do not prove
an assertion over all real probability vectors or all numbers of types.
"""
from fractions import Fraction
from functools import lru_cache
import itertools
import math
import random


def stopped_singleton_law(weights):
    """Independent finite Markov-state recursion, states are counts capped at 2."""
    den = sum(weights)
    p = tuple(Fraction(a, den) for a in weights)
    n = len(p)

    @lru_cache(maxsize=None)
    def recur(state):
        if all(v for v in state):
            res = [Fraction(0)] * (n + 1)
            res[state.count(1)] = Fraction(1)
            return tuple(res)
        wait_prob = sum(p[k] for k in range(n) if state[k] == 2)
        den0 = 1 - wait_prob
        ans = [Fraction(0)] * (n + 1)
        for k in range(n):
            if state[k] == 2:
                continue
            next_state = list(state)
            next_state[k] += 1
            next_law = recur(tuple(next_state))
            for j, v in enumerate(next_law):
                ans[j] += p[k] * v / den0
        return tuple(ans)

    return recur((0,) * n)


def pair_kernel(p, i, j):
    """Exact termwise expansion of positive convergent time integral."""
    remain = [k for k in range(len(p)) if k not in (i, j)]
    acc = Fraction(0)
    for options in itertools.product((0, 1, 2), repeat=len(remain)):
        coefficient = Fraction(1)
        exponent = 1
        rate = p[i] + p[j]
        for k, option in zip(remain, options):
            if option == 1:
                coefficient = -coefficient
                rate += p[k]
            elif option == 2:
                coefficient *= -p[k]
                exponent += 1
                rate += p[k]
        acc += coefficient * math.factorial(exponent) / rate ** (exponent + 1)
    return acc


def decomposed_gap(weights):
    den = sum(weights)
    p = tuple(Fraction(a, den) for a in weights)
    return sum(((p[i] - p[j]) ** 2 * pair_kernel(p, i, j)
                for i in range(len(p)) for j in range(i+1, len(p))),
               Fraction(0))


def main():
    rng = random.Random(310643)
    checks = 0
    for n in range(2, 7):
        count = 20 if n <= 5 else 10
        vectors = [[1] * n, list(range(1, n + 1))]
        vectors += [[rng.randint(1, 12) for k in range(n)]
                    for _ in range(count)]
        for weights in vectors:
            law = stopped_singleton_law(tuple(weights))
            gap = decomposed_gap(weights)
            assert sum(law) == 1
            checks += 1
            assert law[0] == 0
            checks += 1
            assert law[1] - law[2] == gap
            checks += 1
            assert (gap == 0) == (len(set(weights)) == 1)
            checks += 1
            assert law[1] >= law[2]
            checks += 1
            if len(weights) == 2:
                p = Fraction(weights[0], sum(weights))
                assert gap == (2*p - 1) ** 2
                checks += 1
    print(f"PASS; exact_rational_assertions={checks}; state_sizes=2..6")


if __name__ == '__main__':
    main()
