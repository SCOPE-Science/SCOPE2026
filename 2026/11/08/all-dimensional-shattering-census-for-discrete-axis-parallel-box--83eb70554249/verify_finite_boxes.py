"""Standalone exact checks for shattering by nonempty discrete axis-parallel boxes.

No third-party packages required. Run: python3 verify_finite_boxes.py
This tests finite instances; the all-grid formulas require the accompanying proof.
"""
from itertools import product, combinations
from math import comb, factorial, prod
from random import Random


def capacities(shape):
    return sum(0 if n == 1 else 1 if n == 2 else 2 for n in shape)


def local_counts(n, k):
    unique_min = sum(t ** (k - 1) for t in range(n))
    opposite_extrema = sum((n - h - 1) * h ** (k - 2)
                            for h in range(n - 1))
    return unique_min, opposite_extrema


def predicted_profile(shape):
    count = prod(shape)
    bound = capacities(shape)
    out = [1]
    if bound >= 1:
        out.append(count)
    if bound >= 2:
        out.append(comb(count, 2))
    for k in range(3, bound + 1):
        terms = 0
        for j in range(k + 1):
            coordinate_factor = 1
            for n in shape:
                low, two = local_counts(n, k)
                coordinate_factor *= n ** k - 2 * j * low + j * (j - 1) * two
            terms += (-1) ** j * comb(k, j) * coordinate_factor
        assert terms % factorial(k) == 0
        out.append(terms // factorial(k))
    if bound >= 3:
        lead = 2 ** sum(n == 2 for n in shape)
        for n in shape:
            if n >= 3:
                lead *= local_counts(n, bound)[1]
        assert out[-1] == lead, (shape, out[-1], lead)
    return out


def box_masks(shape):
    grid = list(product(*(range(n) for n in shape)))
    intervals = [list(combinations_with_replacement(range(n), 2)) for n in shape]
    masks = set()
    for choices in product(*intervals):
        bitmask = 0
        for index, point in enumerate(grid):
            if all(a <= value <= b for value, (a, b) in zip(point, choices)):
                bitmask |= 1 << index
        assert bitmask != 0
        masks.add(bitmask)
    return grid, list(masks)


def combinations_with_replacement(iterable, size):
    data = list(iterable)
    for idx in combinations(range(len(data) + size - 1), size):
        yield tuple(data[i - j] for j, i in enumerate(idx))


def shattered(support, masks):
    traces = set()
    target = 1 << len(support)
    for box in masks:
        trace = sum((1 << i) for i, pos in enumerate(support) if (box >> pos) & 1)
        traces.add(trace)
        if len(traces) == target:
            return True
    return False


def test_full(shape):
    grid, boxes = box_masks(shape)
    expected = predicted_profile(shape)
    observed = [1]
    checked = 0
    for k in range(1, len(expected) + 1):
        total = 0
        for positions in combinations(range(len(grid)), k):
            checked += 1
            total += shattered(positions, boxes)
        observed.append(total)
    assert observed[:len(expected)] == expected, (shape, expected, observed)
    # The first coefficient outside the predicted range must vanish.
    if len(expected) < len(observed):
        assert observed[len(expected)] == 0, (shape, observed)
    return checked


def test_sampled(shape, trials=1500):
    grid, boxes = box_masks(shape)
    expected = predicted_profile(shape)
    rng = Random(7122020 + sum(shape))
    checked = 0
    for k in range(3, min(len(grid), len(expected) + 2) + 1):
        for _ in range(trials):
            support = tuple(sorted(rng.sample(range(len(grid)), k)))
            good = all(any((point[i] < min(grid[other][i] for other in support if other != ix))
                           or (point[i] > max(grid[other][i] for other in support if other != ix))
                           for i in range(len(shape)))
                       for ix in support for point in [grid[ix]])
            assert shattered(support, boxes) == good, (shape, support)
            checked += 1
    return checked


def main():
    shapes = [(1,), (2,), (3,), (4,), (2, 2), (2, 3), (2, 4),
              (3, 3), (3, 4), (4, 4), (2, 2, 2), (2, 2, 3),
              (2, 2, 2, 2), (2, 3, 3)]
    checked_full = 0
    for shape in shapes:
        checked_full += test_full(shape)
    checked_sampled = 0
    for shape in [(3, 3, 3), (2, 2, 2, 3), (3, 4, 2)]:
        checked_sampled += test_sampled(shape)
    assert predicted_profile((3, 3)) == [1, 9, 36, 16, 1]
    assert predicted_profile((2, 2, 2, 2)) == [1, 16, 120, 160, 16]
    assert predicted_profile((3, 3, 3)) == [1, 27, 351, 1184, 821, 90, 1]
    assert predicted_profile((2, 3, 3)) == [1, 18, 153, 264, 72, 2]
    print('ALL_FINITE_BOX_SHATTERING_CHECKS_PASS')
    print('full_grids', len(shapes), 'support_tests', checked_full)
    print('sampled_grids', 3, 'support_tests', checked_sampled)
    print('profiles', {str(s): predicted_profile(s) for s in
           [(2, 3), (3, 3), (2, 2, 2, 2), (3, 3, 3), (2, 3, 3)]})


if __name__ == '__main__':
    main()
