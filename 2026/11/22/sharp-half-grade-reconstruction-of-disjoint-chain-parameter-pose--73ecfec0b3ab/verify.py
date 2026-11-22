#!/usr/bin/env python3
"""Reproducible finite tests for a graded one-point extension theorem."""
from itertools import product
from collections import defaultdict


def partitions(n, lower=1):
    if n == 0:
        yield ()
        return
    for i in range(lower, n + 1):
        for rest in partitions(n - i, i):
            yield (i,) + rest


def closed_spectrum(lengths):
    polynomial = [1]
    for length in lengths:
        next_poly = [0] * (len(polynomial) + length)
        for degree, value in enumerate(polynomial):
            for extension in range(length + 1):
                next_poly[degree + extension] += value
        polynomial = next_poly
    polynomial = [2 * value for value in polynomial]
    polynomial[0] -= 1
    for length in lengths:
        for degree in range(2, length + 1):
            polynomial[degree] += degree - 1
    return polynomial


def direct_spectrum(lengths):
    """Enumerate ternary adjacency diagrams; directly test transitivity."""
    points = []
    for chain, length in enumerate(lengths):
        for j in range(length):
            points.append((chain, j))
    n = len(points)
    old_lt = [[a[0] == b[0] and a[1] < b[1]
               for b in points] for a in points]
    result = [0] * (n + 1)
    for word in product((-1, 0, 1), repeat=n):
        # -1 means old vertex < new; +1 means new < old.
        edges = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                edges[i][j] = old_lt[i][j]
            edges[i][n] = word[i] == -1
            edges[n][i] = word[i] == 1
        # Independently check irreflexivity and all ordered triple implications.
        if any(edges[i][i] for i in range(n + 1)):
            continue
        valid = True
        for i in range(n + 1):
            if not valid:
                break
            for j in range(n + 1):
                if edges[i][j]:
                    for k in range(n + 1):
                        if edges[j][k] and not edges[i][k]:
                            valid = False
                            break
                    if not valid:
                        break
        if valid:
            result[sum(v != 0 for v in word)] += 1
    return result


def truncated_reconstruction(n, coefficients):
    if n == 1:
        return (1,)
    r = n // 2
    k = coefficients[1] // 2
    assert coefficients[1] == 2 * k
    if r == 1:
        profiles = [p for p in partitions(n) if len(p) == k]
        assert len(profiles) == 1
        return profiles[0]
    # q_j = number of chain components of length at least j.
    q = {1: k}
    multiplicities = {}
    for j in range(2, r + 1):
        base = [1]
        for s in range(1, j - 1):
            for _ in range(multiplicities.get(s, 0)):
                extended = [0] * (len(base) + s)
                for degree, value in enumerate(base):
                    for h in range(s + 1):
                        extended[degree + h] += value
                base = extended
        unresolved = k - sum(multiplicities.values())
        for _ in range(unresolved):
            extended = [0] * (len(base) + j - 1)
            for degree, value in enumerate(base):
                for h in range(j):
                    extended[degree + h] += value
            base = extended
        base_coefficient = base[j] if j < len(base) else 0
        difference = coefficients[j] - 2 * base_coefficient
        assert difference >= 0 and difference % (j + 1) == 0
        q[j] = difference // (j + 1)
        multiplicities[j - 1] = q[j - 1] - q[j]
        assert multiplicities[j - 1] >= 0
    result = [s for s, multiplicity in multiplicities.items() for _ in range(multiplicity)]
    t = q[r]
    total_remaining = n - sum(result)
    assert 0 <= t <= 2
    if t == 1:
        assert total_remaining >= r
        result.append(total_remaining)
    elif t == 2:
        assert total_remaining in (2 * r, 2 * r + 1)
        result.extend((r, total_remaining - r))
    else:
        assert total_remaining == 0
    assert len(result) == k
    return tuple(sorted(result))


def main():
    direct_cases = 0
    for n in range(1, 9):
        for partition in partitions(n):
            closed = closed_spectrum(partition)
            independent = direct_spectrum(partition)
            assert closed == independent, (partition, closed, independent)
            direct_cases += 1
    print(f'DIRECT_TRANSITIVITY_AGREEMENT {direct_cases} disjoint-chain profiles through 8 named parameters')

    partitions_tested = 0
    for n in range(1, 31):
        r = n // 2
        seen = set()
        for partition in partitions(n):
            coefficients = closed_spectrum(partition)
            key = tuple(coefficients[:r + 1])
            assert key not in seen, (n, partition, key)
            seen.add(key)
            assert truncated_reconstruction(n, coefficients[:r + 1]) == partition
            partitions_tested += 1
        if n >= 2:
            if n <= 3:
                examples = ((n,), tuple([1] * n))
            elif n % 2 == 0:
                examples = ((r - 1, r + 1), (r, r))
            else:
                examples = ((1, r - 1, r + 1), (1, r, r))
            first, second = examples
            f, g = closed_spectrum(first), closed_spectrum(second)
            assert f[:r] == g[:r]
            assert f[:r + 1] != g[:r + 1]
            if n >= 4:
                assert f[r] - g[r] == -(r + 1)
    print(f'ALL_TRUNCATED_RECONSTRUCTIONS {partitions_tested} integer partitions through n=30')
    print('SHARP_LOWER_CUTOFF n=2..30 verified')
    assert closed_spectrum((1, 3)) == [1, 4, 5, 6, 2]
    assert closed_spectrum((2, 2)) == [1, 4, 8, 4, 2]
    assert sum(closed_spectrum((1, 4, 12))) == 331
    assert sum(closed_spectrum((2, 2, 13))) == 331
    assert closed_spectrum((1, 4, 12)) != closed_spectrum((2, 2, 13))
    print('SCALAR_COLLISION same n=17, same k=3, total=331 but graded profiles differ')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
