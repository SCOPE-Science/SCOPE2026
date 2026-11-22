"""Independent configuration-space finite-time count-moment test (stdlib only).

Run: python3 verify_event_moments.py
The rate of each successful oriented nearest-neighbour hop is one.
"""
from itertools import combinations
from math import cos, exp, expm1, pi, sin, sqrt


def predicted(n, t):
    N = n - 1
    rate = 4 * (n - 2) / N
    variance = rate * t
    for ell in range(1, (n - 2) // 2 + 1):
        lam = 8 * sin(pi * ell / N) ** 2
        variance += 64 / N**2 * cos(pi * ell / N) ** 2 * (t / lam + expm1(-lam * t) / lam**2)
    return rate * t, variance


def independent_full_chain(n, t):
    # Full unordered configurations; no relative-distance or spectral reduction.
    configurations = list(combinations(range(n), 2))
    indexes = {s: i for i, s in enumerate(configurations)}
    size = len(configurations)
    transitions = []
    for occupied in configurations:
        edges = []
        for site in occupied:
            for target in ((site - 1) % n, (site + 1) % n):
                if target in occupied:
                    continue
                new = tuple(sorted((set(occupied) - {site}) | {target}))
                edges.append(indexes[new])
        transitions.append(edges)

    # Derivatives of E[exp(z C_t)] with respect to z, obtained directly
    # from the full tilted generator Q_z=e^z B - diag(q).
    # Repeated uniformization, with constant Lambda=4 (successful jump rates <=4).
    uniformization = 4.0
    v0 = [1.0] * size
    v1 = [0.0] * size
    v2 = [0.0] * size
    weight = exp(-uniformization * t)
    first = 0.0
    second = 0.0
    for k in range(0, max(110, int(uniformization * t + 35 * sqrt(uniformization * t + 1)))):
        first += weight * sum(v1) / size
        second += weight * sum(v2) / size
        if k > uniformization * t + 20 and weight < 1e-18:
            break
        next0, next1, next2 = [], [], []
        for i, destinations in enumerate(transitions):
            count = len(destinations)
            a0 = sum(v0[j] for j in destinations)
            a1 = sum(v1[j] for j in destinations)
            a2 = sum(v2[j] for j in destinations)
            next0.append(v0[i] + (a0 - count * v0[i]) / uniformization)
            next1.append(v1[i] + (a1 - count * v1[i] + a0) / uniformization)
            next2.append(v2[i] + (a2 - count * v2[i] + 2 * a1 + a0) / uniformization)
        v0, v1, v2 = next0, next1, next2
        weight *= uniformization * t / (k + 1)
    return first, second - first * first


def main():
    count = 0
    for n in range(3, 17):
        for t in (0.04, 0.25, 1.0, 3.0, 7.0):
            mean1, var1 = predicted(n, t)
            mean2, var2 = independent_full_chain(n, t)
            assert abs(mean1 - mean2) < 2e-9, (n, t, mean1, mean2)
            assert abs(var1 - var2) < 2e-8, (n, t, var1, var2)
            count += 1
    print(f"PASS: {count} full-state independent finite-time moment comparisons, n=3..16")


if __name__ == '__main__':
    main()
