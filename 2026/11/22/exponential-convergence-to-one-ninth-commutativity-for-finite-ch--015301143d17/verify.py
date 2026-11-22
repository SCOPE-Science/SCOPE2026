"""Direct finite checks for commuting pairs of finite-chain partial translations.
Only standard Python is needed; exhaustive tests are finite corroboration.
"""
from collections import Counter
from math import comb


def partial_translations(n):
    # A map is a tuple of n outputs, with -1 meaning undefined.
    yield (-1,) * n, 0, 0
    for delta in range(1 - n, n):
        eligible = [i for i in range(n) if 0 <= i + delta < n]
        for bits in range(1, 1 << len(eligible)):
            tab = [-1] * n
            rank = 0
            for j, i in enumerate(eligible):
                if (bits >> j) & 1:
                    tab[i] = i + delta
                    rank += 1
            yield tuple(tab), delta, rank


def compose(f, g):
    # Conventional f after g, so composition is f(g(x)).
    return tuple(-1 if y < 0 else f[y] for y in g)


def check(n):
    maps = list(partial_translations(n))
    actual = len(maps)
    assert actual == 3 * (2 ** n) - 2 * (n + 1)
    is_id = [all(y < 0 or y == i for i, y in enumerate(tab)) for tab, _, _ in maps]
    assert sum(is_id) == 2 ** n
    rank_counts = Counter()
    nonidem_pairs = 0
    all_commuting = 0
    for i, (f, _, rf) in enumerate(maps):
        for j, (g, _, rg) in enumerate(maps):
            if compose(f, g) != compose(g, f):
                continue
            all_commuting += 1
            if is_id[i] and not is_id[j]:
                rank_counts[rg] += 1
            if not is_id[i] and not is_id[j]:
                nonidem_pairs += 1
    for r in range(1, n):
        predicted = 2 * comb(n, r + 1) * 2 ** (n - r)
        assert rank_counts[r] == predicted, (n, r, rank_counts[r], predicted)
    mixed_one_direction = sum(rank_counts.values())
    predicted_mixed = 4 * 3 ** n - (n + 2) * 2 ** (n + 1)
    assert mixed_one_direction == predicted_mixed
    assert all_commuting == 4 ** n + 2 * predicted_mixed + nonidem_pairs
    return actual, all_commuting, nonidem_pairs, mixed_one_direction


if __name__ == '__main__':
    for n in range(1, 10):
        size, commuting, nonid_nonid, one_way = check(n)
        print(f'n={n} size={size} commuting={commuting} nonid_nonid={nonid_nonid} id_nonid_one_direction={one_way}')
    print('VERIFY_OK_ODP_COMMUTING')
