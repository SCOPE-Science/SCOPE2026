"""Standalone supplementary checks for parity-staggered k-mer adsorption.

Run with Python 3: python verify.py
This finite Monte Carlo check is not an infinite-volume proof.
"""
import math
import random


def occupancy(k, size, rng, slow_time=None):
    occupied = [False] * size
    starts = list(range(0, size, 2))
    rng.shuffle(starts)
    for start in starts:
        sites = [(start + j) % size for j in range(k)]
        if all(not occupied[u] for u in sites):
            for u in sites:
                occupied[u] = True
    fast = [sum(occupied[0::2]) / (size // 2),
            sum(occupied[1::2]) / (size // 2)]
    eligible = []
    for start in range(1, size, 2):
        sites = [(start + j) % size for j in range(k)]
        if all(not occupied[u] for u in sites):
            eligible.append(start)
    if k % 2 == 0:
        assert not eligible
    else:
        assert len(eligible) * k <= size - sum(occupied)
        # Distinct eligible slow rods cannot intersect after the fast stage.
        seen = set()
        for start in eligible:
            sites = [(start + j) % size for j in range(k)]
            assert all(u not in seen for u in sites)
            seen.update(sites)
    for start in eligible:
        if slow_time is not None and rng.expovariate(1.0) > slow_time:
            continue
        sites = [(start + j) % size for j in range(k)]
        assert all(not occupied[u] for u in sites)
        for u in sites:
            occupied[u] = True
    final = [sum(occupied[0::2]) / (size // 2),
             sum(occupied[1::2]) / (size // 2)]
    return fast, final, len(eligible)


def theta(r):
    # Composite Simpson quadrature of the exact uniform r-mer deposition law.
    n = 24000
    xmax = 35.0
    h = xmax / n
    s = 0.0
    for j in range(n + 1):
        t = h * j
        e = math.exp(-t - 2.0 * sum((1.0 - math.exp(-a * t)) / a
                                    for a in range(1, r)))
        s += (1.0 if j == 0 or j == n else 4.0 if j & 1 else 2.0) * e
    return r * s * h / 3.0


def check():
    assert abs(theta(2) - (1.0 - math.exp(-2.0))) < 3e-9
    assert abs(theta(3) - 0.8236529631773384) < 3e-9
    checks = 2
    rng = random.Random(104729)
    size = 3200
    reps = 85
    for k in range(4, 12):
        r = (k + 1) // 2
        hval = sum(1.0 / j for j in range(1, r))
        emax = math.exp(-2.0 * hval)
        th = theta(r)
        expected_fast = (th, th) if k % 2 == 0 else (th, (r - 1) * th / r)
        for stage in (0.4, 1.5, 8.0):
            ave = [0.0, 0.0]
            avefast = [0.0, 0.0]
            aveeligible = 0.0
            for _ in range(reps):
                f, g, eligible = occupancy(k, size, rng, stage)
                ave[0] += g[0] / reps
                ave[1] += g[1] / reps
                avefast[0] += f[0] / reps
                avefast[1] += f[1] / reps
                aveeligible += eligible / (size * reps)
                checks += 1
            if k % 2:
                p = 1.0 - math.exp(-stage)
                expected = (th + (r - 1) * emax * p,
                            (r - 1) * th / r + r * emax * p)
                assert abs(aveeligible - emax / 2.0) < 0.007, (k, stage, aveeligible, emax)
            else:
                expected = expected_fast
                assert aveeligible == 0.0
            for j in (0, 1):
                assert abs(avefast[j] - expected_fast[j]) < 0.011, (k, stage, j, avefast[j], expected_fast[j])
                assert abs(ave[j] - expected[j]) < 0.015, (k, stage, j, ave[j], expected[j])
                checks += 2
        print("k=%d, fast=(%.7f,%.7f), full=(%.7f,%.7f), jump=%.8f" %
              (k, expected_fast[0], expected_fast[1],
               th + ((r-1)*emax if k%2 else 0),
               ((r-1)*th/r + r*emax if k%2 else th),
               (k*emax/2 if k%2 else 0)))
    print("PARITY_STAGGERED_ADSORPTION_CHECKS_PASSED", checks)


if __name__ == "__main__":
    check()
