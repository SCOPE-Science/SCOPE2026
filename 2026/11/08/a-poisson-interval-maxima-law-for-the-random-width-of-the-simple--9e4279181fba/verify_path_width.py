"""Independent finite checks for the interval-simplex associahedron width law.

Python 3 standard library only. The analytic proof is in RESULT.md.
This program checks exact finite identities, the Poisson truncation integral,
and the direction normalization. It does not prove an asymptotic theorem.
"""
import math
import random
from statistics import NormalDist


def subarray_max_sum(a):
    n = len(a)
    left, right = [0] * n, [0] * n
    stack = []
    for i, value in enumerate(a):
        while stack and a[stack[-1]] < value:
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)
    return sum(a[i] * left[i] * right[i] for i in range(n))


def gaussian_width(a):
    center = sum(a) / len(a)
    norm = math.sqrt(sum((x - center) ** 2 for x in a))
    return (subarray_max_sum(a) + subarray_max_sum([-x for x in a])) / norm


def poisson_truncated(points, cutoff):
    """Exact integral over 0<s<t<1 of max(-cutoff, PPP marks)."""
    points = sorted(points)
    n = len(points)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    left, right = [0.0] * n, [1.0] * n
    stack = []
    for i, value in enumerate(ys):
        while stack and ys[stack[-1]] < value:
            stack.pop()
        left[i] = xs[stack[-1]] if stack else 0.0
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and ys[stack[-1]] <= ys[i]:
            stack.pop()
        right[i] = xs[stack[-1]] if stack else 1.0
        stack.append(i)
    return -cutoff / 2.0 + sum((ys[i] + cutoff) * (xs[i] - left[i])
                                    * (right[i] - xs[i]) for i in range(n))


def sample_poisson(rng, cutoff):
    """Finite PPP restricted to marks y > -cutoff."""
    mean = math.exp(cutoff)
    # Knuth's exact Poisson sampler; cutoff=5 makes the mean manageable.
    # Draw Poisson via counts in independent unit-rate blocks, avoiding underflow.
    remaining = mean
    count = 0
    while remaining > 0:
        block = min(remaining, 20.0)
        prod = 1.0
        threshold = math.exp(-block)
        k = 0
        while True:
            prod *= rng.random()
            if prod <= threshold:
                break
            k += 1
        count += k
        remaining -= block
    return poisson_truncated([(rng.random(), -cutoff + rng.expovariate(1))
                              for _ in range(count)], cutoff)


def check():
    rng = random.Random(731903)
    for n in range(2, 13):
        for _ in range(12):
            a = [rng.gauss(0, 1) for _ in range(n)]
            direct = sum(max(a[i:j + 1]) - min(a[i:j + 1])
                         for i in range(n) for j in range(i, n))
            via_stack = subarray_max_sum(a) + subarray_max_sum([-v for v in a])
            assert abs(direct - via_stack) < 1.e-9 * max(1., abs(direct))
    # For n=2, the only nontrivial summand is conv(e1,e2): fixed width sqrt(2).
    for _ in range(100):
        a = [rng.gauss(0, 1), rng.gauss(0, 1)]
        assert abs(gaussian_width(a) - math.sqrt(2)) < 1.e-9
    # Cartesian-tree domain areas partition interval pairs by their highest mark.
    points = [(0.11, 0.4), (0.29, 1.3), (0.43, -0.5), (0.66, 2.2), (0.83, 0.9)]
    cutoff = 2.0
    exact = poisson_truncated(points, cutoff)
    ngrid = 900
    numerical = 0.0
    # Midpoint quadrature on the triangle; equal-index diagonal cells are omitted.
    for i in range(ngrid):
        s = (i + 0.5) / ngrid
        for j in range(i + 1, ngrid):
            t = (j + 0.5) / ngrid
            numerical += max([-cutoff] + [v for x, v in points if s < x < t])
    numerical /= ngrid ** 2
    assert abs(exact - numerical) < 0.008, (exact, numerical)
    # Extreme-value centering: samples at large n should have a finite, negative
    # corrected location. This is a coarse diagnostic, not an asymptotic proof.
    n, runs = 4500, 200
    a_n = NormalDist().inv_cdf(1 - 1 / n)
    transformed = []
    for _ in range(runs):
        a = [rng.gauss(0, 1) for _ in range(n)]
        transformed.append(a_n * (math.sqrt(n) / n ** 2 * gaussian_width(a)
                                  - a_n * (1 + 1 / n)))
    assert -1.35 < sum(transformed) / len(transformed) < -0.68
    # PPP limit has known mean 2*(gamma/2-3/4)=gamma-3/2.
    # Finite cutoff raises that mean, so a broad empirical interval is used.
    draws = 550
    poisson_data = [sample_poisson(rng, 5) + sample_poisson(rng, 5)
                    for _ in range(draws)]
    poisson_mean = sum(poisson_data) / draws
    assert -1.12 < poisson_mean < -0.70, poisson_mean
    print('INTERVAL_ASSOCIAHEDRON_WIDTH_AND_POISSON_CHECKS_PASSED')
    print('finite_n=', n, 'scaled_mean=', round(sum(transformed)/runs, 6))
    print('poisson_cutoff_5_mean=', round(poisson_mean, 6))
    print('limiting_mean= gamma-3/2 = -0.922784335098467')


if __name__ == '__main__':
    check()
