"""Independent finite checks for the stated cycle pair-coalition theorem.

Run: python3 verify_cycle_pairs.py
Requires only the Python standard library.
These are finite checks; the general result rests on the accompanying proof.
"""
from itertools import combinations
from math import comb


def all_pair_partitions(vertices):
    if not vertices:
        yield ()
        return
    head = vertices[0]
    for j in range(1, len(vertices)):
        tail = vertices[1:j] + vertices[j + 1:]
        for rest in all_pair_partitions(tail):
            yield ((head, vertices[j]),) + rest


def neighboring(a, b, n):
    return (a - b) % n in (1, n - 1)


def is_swap_stable(pairs, n):
    # Compare the two swapping agents' utilities, for all pair-to-pair swaps.
    for i, (a, b) in enumerate(pairs):
        for c, d in pairs[i + 1:]:
            for x, old_x, y, old_y in (
                (a, b, c, d), (a, b, d, c),
                (b, a, c, d), (b, a, d, c),
            ):
                initial_x = neighboring(x, old_x, n)
                initial_y = neighboring(y, old_y, n)
                final_x = neighboring(x, old_y, n)
                final_y = neighboring(y, old_x, n)
                if ((final_x > initial_x and final_y >= initial_y)
                    or (final_y > initial_y and final_x >= initial_x)):
                    return False
    return True


def local_criterion(pairs, n):
    paired = {frozenset(p) for p in pairs}
    unmatched = {x for a, b in pairs if not neighboring(a, b, n) for x in (a, b)}
    if any((x + 1) % n in unmatched for x in unmatched):
        return False
    for x, y in pairs:
        if x not in unmatched:
            continue
        for origin, dest in ((x, y), (y, x)):
            if (dest - origin) % n == 3:
                if frozenset(((origin + 1) % n, (origin + 2) % n)) in paired:
                    return False
    return True


def odd_double_factorial(m):
    # (m-1)!! for m nonnegative even, including (-1)!!=1.
    answer = 1
    for r in range(1, m, 2):
        answer *= r
    return answer


def matchings_of_cycle_edges(u, j):
    return u * comb(u - j, j) // (u - j)


def closed_formula(n):
    counts = {0: 2}
    for u in range(2, n // 3 + 1, 2):
        s = (n - 3 * u) // 2
        if u == 2:
            count = (n // 2) * max(0, s - 1)
        else:
            terms = [(-1) ** j * matchings_of_cycle_edges(u, j)
                     * odd_double_factorial(u - 2 * j)
                     * comb(s + u - j - 1, u - j - 1)
                     for j in range(0, u // 2 + 1)]
            numerator = n * sum(terms)
            assert numerator % u == 0
            count = numerator // u
        if count:
            counts[u] = count
    return counts


def finite_exhaustion():
    reviewed = 0
    stable = 0
    for n in (6, 8, 10, 12, 14):
        observed = {}
        for pairs in all_pair_partitions(tuple(range(n))):
            reviewed += 1
            direct = is_swap_stable(pairs, n)
            local = local_criterion(pairs, n)
            assert direct == local, ('criterion mismatch', n, pairs)
            if direct:
                stable += 1
                u = sum(2 for a, b in pairs if not neighboring(a, b, n))
                observed[u] = observed.get(u, 0) + 1
        assert observed == closed_formula(n), (n, observed, closed_formula(n))
        print(f'n={n}: stable by unmatched count {observed}; total {sum(observed.values())}')
    print(f'PASS: {reviewed} partitions checked with direct swaps; {stable} stable.')


def check_larger_counts():
    expected = {16: 82, 18: 185, 20: 437, 22: 1058, 24: 2595,
                26: 6528, 28: 16795, 30: 43846}
    for n, target in expected.items():
        counts = closed_formula(n)
        assert sum(counts.values()) == target, (n, counts, target)
        u_max = max(counts)
        assert u_max == 2 * (n // 6)
    print('PASS: exact integer formula and worst stable welfare checked through n=30.')


if __name__ == '__main__':
    finite_exhaustion()
    check_larger_counts()
