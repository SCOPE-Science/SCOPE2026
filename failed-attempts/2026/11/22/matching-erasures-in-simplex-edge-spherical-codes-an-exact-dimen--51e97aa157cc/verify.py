#!/usr/bin/env python3
"""Finite regression for the matching-erased simplex-edge spherical covering theorem.
The universal proof is geometric; random testing is not an exhaustive proof.
"""
import itertools
import math
import random


def run():
    rng = random.Random(20261116)
    checked = 0
    samples = 0
    for n in range(5, 12):
        R = math.sqrt(2 * (n - 2) / n)
        alpha = math.sqrt(2 / ((n - 1) * (n - 2)))
        gamma = (n - 4) / (2 * (n - 2))
        rho = min(alpha, gamma)
        for t in range(1, n // 2 + 1):
            missing = {tuple(sorted((2 * k, 2 * k + 1))) for k in range(t)}
            surviving = [p for p in itertools.combinations(range(n), 2) if p not in missing]

            def support(v):
                return max((v[i] + v[j]) / R for i, j in surviving)

            erased_dirs = []
            for a, b in sorted(missing):
                v = [float(k in (a, b)) - 2 / n for k in range(n)]
                norm = math.sqrt(sum(x * x for x in v))
                erased_dirs.append([x / norm for x in v])
            low_dirs = []
            for i in range(n):
                v = [1 / n - float(k == i) for k in range(n)]
                norm = math.sqrt(sum(x * x for x in v))
                low_dirs.append([x / norm for x in v])

            for k, v in enumerate(erased_dirs + low_dirs):
                val = support(v)
                is_deep = (n < 7 and k < t) or (n >= 7 and k >= t)
                if is_deep:
                    assert math.isclose(val, rho, rel_tol=0, abs_tol=2e-12), (n, t, k, val, rho)
                else:
                    assert val > rho + 1e-8, (n, t, k, val, rho)
                checked += 1
            for _ in range(200):
                v = [rng.gauss(0.0, 1.0) for _ in range(n)]
                mean = sum(v) / n
                v = [x - mean for x in v]
                norm = math.sqrt(sum(x * x for x in v))
                v = [x / norm for x in v]
                assert support(v) >= rho - 1e-10, (n, t)
                samples += 1
    print(f"PASS: {checked} facet-normal tests, {samples} randomized supporting directions")


if __name__ == '__main__':
    run()
