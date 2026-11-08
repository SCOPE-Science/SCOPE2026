"""Independent finite checks for normal two-agent S5 bundled knowledge."""
from itertools import combinations, permutations
from math import comb, factorial


def partitions(points):
    points = tuple(points)
    if not points:
        yield ()
        return
    head, rest = points[0], points[1:]
    for tail in partitions(rest):
        yield (frozenset((head,)),) + tail
        for i in range(len(tail)):
            t = list(tail)
            t[i] = t[i] | {head}
            yield tuple(t)


def laminar(pair):
    e, f = pair
    return all(not (a & b) or a <= b or b <= a for a in e for b in f)


def block_masks(partition, n):
    out = [0] * n
    for block in partition:
        mask = sum(1 << x for x in block)
        for x in block:
            out[x] = mask
    return out


def normality_from_valuations(pair, n):
    e, f = (block_masks(p, n) for p in pair)
    for w in range(n):
        def someone_knows(x):
            return (e[w] & x == e[w]) or (f[w] & x == f[w])
        for x in range(1 << n):
            if not someone_knows(x):
                continue
            for y in range(1 << n):
                if someone_knows(y) and not someone_knows(x & y):
                    return False
    return True


def bell_numbers(n):
    b = [1]
    for k in range(n):
        b.append(sum(comb(k, j) * b[j] for j in range(k + 1)))
    return b


def labelled_counts(n):
    bell = bell_numbers(n)
    c = [0] + [2 * bell[k] - 1 for k in range(1, n + 1)]
    counts = [1]
    for m in range(n):
        counts.append(sum(comb(m, j) * c[j + 1] * counts[m - j]
                          for j in range(m + 1)))
    return counts


def integer_partition_numbers(n):
    out = [1] + [0] * n
    for part in range(1, n + 1):
        for m in range(part, n + 1):
            out[m] += out[m - part]
    return out


def unlabelled_counts(n):
    p = integer_partition_numbers(n)
    out = [1] + [0] * n
    for k in range(1, n + 1):
        num_types = 2 * p[k] - 1
        for _ in range(num_types):
            for m in range(k, n + 1):
                out[m] += out[m - k]
    return out


def key_on_permutation(pair, perm):
    new_blocks = []
    for relation in pair:
        new_blocks.append(tuple(sorted(tuple(sorted(perm[x] for x in block))
                                       for block in relation)))
    return tuple(new_blocks)


def canonical(pair, n):
    return min(key_on_permutation(pair, perm) for perm in permutations(range(n)))


def main():
    expected_labelled = [1, 1, 4, 19, 111, 774, 6229]
    counts = labelled_counts(6)
    assert counts == expected_labelled, (counts, expected_labelled)
    expected_unlabelled = [1, 1, 4, 9, 24, 52]
    assert unlabelled_counts(5) == expected_unlabelled
    checked_pairs = 0
    checked_valuations = 0
    for n in range(1, 7):
        parts = list(partitions(range(n)))
        compatible = 0
        orbit_types = set()
        for e in parts:
            for f in parts:
                pair = (e, f)
                predicate = laminar(pair)
                compatible += predicate
                checked_pairs += 1
                if n <= 4:
                    normal = normality_from_valuations(pair, n)
                    checked_valuations += 1
                    assert normal == predicate, (n, pair)
                if n <= 4 and predicate:
                    orbit_types.add(canonical(pair, n))
        assert compatible == counts[n], (n, compatible, counts[n])
        if n <= 4:
            assert len(orbit_types) == expected_unlabelled[n], (n, len(orbit_types))
    print('NORMAL_BUNDLE_PARTITION_CENSUS_OK',
          'pair_tests=', checked_pairs,
          'valuation_pair_tests=', checked_valuations,
          'labelled=', counts,
          'unlabelled=', expected_unlabelled)


if __name__ == '__main__':
    main()
