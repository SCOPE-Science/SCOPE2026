#!/usr/bin/env python3
"""Deterministic finite diagnostics for sector-constrained nearest-neighbor cycles."""
import math
import random


def configuration(k, alpha):
    assert k >= 3 and math.pi < alpha < 2 * math.pi
    delta = (alpha - math.pi) / 2.0
    step_span = min(1.0, math.tan(delta)) / 8.0
    return [(i * step_span / (k - 2), 0.0) for i in range(k - 1)] + [(-step_span, 1.0)]


def neighbors(points, alpha):
    answer = []
    for i, (xi, yi) in enumerate(points):
        admissible = []
        for j, (xj, yj) in enumerate(points):
            if i == j:
                continue
            dx, dy = xj - xi, yj - yi
            if alpha >= 2 * math.pi or abs(math.atan2(dy, dx)) <= alpha / 2:
                admissible.append((dx * dx + dy * dy, j))
        answer.append(min(admissible)[1] if admissible else None)
    return answer


def cycle_lengths(mapping):
    cycles = []
    for source in range(len(mapping)):
        seen = {}
        node = source
        while node is not None and node not in seen:
            seen[node] = len(seen)
            node = mapping[node]
        if node is not None and node == source:
            cycles.append(len(seen))
    return cycles


def main():
    checks = 0
    apertures = [math.pi + v for v in (1e-5, 1e-4, 0.01, 0.05, 0.5, 1.0, 2.0, 3.0, math.pi - 1e-5)]
    rng = random.Random(20261102)
    for alpha in apertures:
        for k in (3, 4, 5, 6, 8, 10, 20, 50):
            points = configuration(k, alpha)
            assert neighbors(points, alpha) == list(range(1, k)) + [0]
            checks += 1
            span = points[k - 2][0]
            perturb_scale = min(1e-7, span / (100000 * k),
                                (2 * math.pi - alpha) * span / (1000 * k),
                                (alpha - math.pi) * span / (1000 * k))
            for rep in range(10):
                perturbed = [(x + rng.uniform(-perturb_scale, perturb_scale),
                              y + rng.uniform(-perturb_scale, perturb_scale)) for x, y in points]
                assert neighbors(perturbed, alpha) == list(range(1, k)) + [0]
                checks += 1
    for trial in range(100):
        points = [(rng.random(), rng.random()) for _ in range(20)]
        nng = neighbors(points, 2 * math.pi)
        assert all(l == 2 for l in cycle_lengths(nng))
        checks += 1
        half = neighbors(points, math.pi)
        assert not cycle_lengths(half)
        checks += 1
    print(f"PASS: {checks} deterministic finite checks")


if __name__ == "__main__":
    main()
