"""Standalone finite checks of the rank/nilpotency-index census for chain partial isometries.

Standard-library only. Run: python3 verify.py
"""
from collections import Counter
from math import comb


def all_partial_isometries(n):
    """Enumerate literal partial maps, independently of nilpotency formulas."""
    found = set()
    for d in range(1 - n, n):
        eligible = [x for x in range(1, n + 1) if 1 <= x + d <= n]
        for mask in range(1 << len(eligible)):
            found.add(tuple((x, x + d) for j, x in enumerate(eligible) if mask >> j & 1))
    for c in range(2, 2 * n + 1):
        eligible = [x for x in range(1, n + 1) if 1 <= c - x <= n]
        for mask in range(1 << len(eligible)):
            found.add(tuple((x, c - x) for j, x in enumerate(eligible) if mask >> j & 1))
    return found


def nil_index(f):
    """Find the least positive k with f^k empty, composing literal maps."""
    if not f:
        return 1
    base = dict(f)
    power = dict(f)
    for k in range(1, len(f) + 2):
        if not power:
            return k
        power = {x: base[y] for x, y in power.items() if y in base}
    return None


def poly_product(a, b):
    result = Counter()
    for i, u in a.items():
        for j, v in b.items():
            result[i + j] += u * v
    return result


def no_run_polynomial(length, k):
    """Brute-force binary strings avoiding k consecutive selected positions."""
    coeff = Counter()
    for mask in range(1 << length):
        current = maximum = 0
        for j in range(length):
            current = current + 1 if mask & (1 << j) else 0
            maximum = max(maximum, current)
        if maximum < k:
            coeff[mask.bit_count()] += 1
    return coeff


def cumulative_polynomial(n, k):
    result = Counter({0: 1})
    for d in range(1, n):
        a, b = divmod(n, d)
        term = Counter({0: 1})
        for _ in range(b):
            term = poly_product(term, no_run_polynomial(a, k))
        for _ in range(d - b):
            term = poly_product(term, no_run_polynomial(a - 1, k))
        term[0] -= 1
        for rank, count in term.items():
            result[rank] += 2 * count
    if k >= 2:
        for center in range(2, 2 * n + 1):
            m = sum(1 for x in range(1, n + 1) if 1 <= center - x <= n)
            for rank in range(2, m // 2 + 1):
                result[rank] += (2 ** rank) * comb(m // 2, rank)
    return +result


def closed_nilpotent_total(n):
    if n % 2 == 0:
        return 2 ** (n + 1) + 3 ** (n // 2 + 1) - n * n - 3 * n - 4
    return 2 ** (n + 1) + 5 * 3 ** (n // 2) - n * n - 3 * n - 4


def closed_rank_count(n, rank):
    if rank == 0:
        return 1
    if rank == 1:
        return n * (n - 1)
    h = n // 2
    eta = 1 if n % 2 == 0 else 3
    def choose(a, b):
        return comb(a, b) if 0 <= b <= a else 0
    return 2 * choose(n, rank + 1) + 2 ** rank * (4 * choose(h, rank + 1) + eta * choose(h, rank))


def verify():
    totals = []
    for n in range(1, 10):
        actual = Counter()
        maps = all_partial_isometries(n)
        for partial_map in maps:
            k = nil_index(partial_map)
            if k is not None:
                actual[(len(partial_map), k)] += 1
        total = sum(actual.values())
        assert total == closed_nilpotent_total(n), (n, 'total', total)
        for rank in range(n + 1):
            seen = sum(count for (r, _), count in actual.items() if r == rank)
            assert seen == closed_rank_count(n, rank), (n, 'rank', rank, seen)
        for k in range(1, n + 2):
            measured = Counter()
            for (rank, depth), count in actual.items():
                if depth <= k:
                    measured[rank] += count
            assert +measured == cumulative_polynomial(n, k), (n, k)
        assert len(maps) == 3 * 2 ** (n + 1) - (n + 2) ** 2 - 1
        totals.append(total)
        print('EXHAUSTIVE_OK n={} monoid={} nilpotents={}'.format(n, len(maps), total))
    assert totals == [1, 3, 9, 27, 65, 151, 317, 663, 1317], totals
    print('JOINT_RANK_INDEX_OK n=1..9')
    print('CLOSED_RANK_AND_TOTAL_OK n=1..9')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
