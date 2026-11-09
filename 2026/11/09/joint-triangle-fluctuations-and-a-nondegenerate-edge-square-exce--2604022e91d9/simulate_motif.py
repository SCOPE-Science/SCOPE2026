"""Seeded finite-size diagnostic for the triangle--edge-square fluctuation law.

This is an illustration of finite-size behavior, not a proof of convergence.
"""
import math
import random
import statistics


def run(n=2500, replicates=2300, M=3, rho=0.4, delta=0.7, seed=20261101):
    rng = random.Random(seed)
    values = []
    for _ in range(replicates):
        past = []
        ones = 0
        edges = 0
        triangles = 0
        for j in range(1, n + 1):
            old_count = min(M, j - 1)
            probability = (rho + delta * ones) / (1 + delta * old_count)
            x = rng.random() < probability
            if x:
                triangles += edges
                edges += j - 1
            past.append(x)
            ones += x
            if len(past) > M:
                ones -= past.pop(0)
        e = edges / (n * (n - 1) / 2)
        t = triangles / (n * (n - 1) * (n - 2) / 6)
        values.append(math.sqrt(n) * (t - e**2))
    D = 1 + 2 * M * delta + M * (M - 1) * delta**2 / (1 + delta)
    predicted = 2 / 15 * rho**3 * (1 - rho) * D
    print('sample_mean', statistics.mean(values))
    print('sample_variance', statistics.variance(values))
    print('asymptotic_variance', predicted)
    print('ratio', statistics.variance(values) / predicted)


if __name__ == '__main__':
    run()
