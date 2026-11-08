"""Independent finite checks for the shattering profile of anchored orthants.

Run: python verify.py
Only the Python standard library is used.
"""
from itertools import combinations, product
from math import comb, factorial, prod


def power_sum_unique(n, k):
    if k == 1:
        return n
    return sum((v - 1) ** (k - 1) for v in range(1, n + 1))


def coefficient(ns, k):
    if k == 0:
        return 1
    numerator = sum(
        (-1) ** j * comb(k, j)
        * prod(n ** k - j * power_sum_unique(n, k) for n in ns)
        for j in range(k + 1)
    )
    assert numerator % factorial(k) == 0
    return numerator // factorial(k)


def private_maximum(sample):
    if not sample:
        return True
    d = len(sample[0])
    return all(
        any(all(point[i] > other[i] for other in sample if other != point)
            for i in range(d))
        for point in sample
    )


def exhaustive_profile(ns):
    points = list(product(*(range(1, n + 1) for n in ns)))
    masks = []
    for t in product(*(range(n + 1) for n in ns)):
        mask = 0
        for i, p in enumerate(points):
            if all(a <= b for a, b in zip(p, t)):
                mask |= 1 << i
        masks.append(mask)
    counts = [1]
    for k in range(1, min(len(ns) + 2, len(points) + 1)):
        count = 0
        for idxs in combinations(range(len(points)), k):
            sample = [points[i] for i in idxs]
            traces = {
                sum((1 << j) for j, i in enumerate(idxs) if mask & (1 << i))
                for mask in masks
            }
            shattered = len(traces) == 1 << k
            assert shattered == private_maximum(sample), (ns, sample)
            count += shattered
        assert count == coefficient(ns, k), (ns, k, count, coefficient(ns, k))
        counts.append(count)
    return counts


def main():
    cases = [
        (1,), (2,), (3,), (1, 1), (2, 2), (3, 3),
        (1, 2, 3), (2, 2, 2), (2, 3, 3),
        (2, 3, 4), (3, 3, 3),
    ]
    expected = {
        (2, 2): [1, 4, 1, 0],
        (2, 2, 2): [1, 8, 9, 1, 0],
        (2, 3, 4): [1, 24, 120, 70, 0],
        (3, 3, 3): [1, 27, 162, 125, 0],
    }
    for ns in cases:
        result = exhaustive_profile(ns)
        if ns in expected:
            assert result == expected[ns], (ns, result)
        print("PASS", ns, result)
    print("ALL_ANCHORED_ORTHANT_PROFILE_CHECKS_PASS", len(cases))

if __name__ == "__main__":
    main()
