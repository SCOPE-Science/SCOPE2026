"""Exact integer-series and direct finite transformation checks.

Run with: python checker.py
Only the Python standard library is used.
"""
from collections import Counter
from itertools import permutations, product


def convolution(f, g, limit):
    return [sum(f[j] * g[n - j] for j in range(n + 1)) for n in range(limit + 1)]


def multiset_transform(species, limit):
    """OGF for multisets of unlabelled connected types with given size counts."""
    weighted_divisors = [0] * (limit + 1)
    for size in range(1, limit + 1):
        for k in range(size, limit + 1, size):
            weighted_divisors[k] += size * species[size]
    result = [1] + [0] * limit
    for n in range(1, limit + 1):
        numerator = sum(weighted_divisors[k] * result[n - k] for k in range(1, n + 1))
        assert numerator % n == 0
        result[n] = numerator // n
    return result


def predictions(limit=18):
    root_star = [0] + [1] * limit
    ordinary_star_multiset = multiset_transform(root_star, limit)
    two_cycle_types = [0] + [k // 2 for k in range(1, limit + 1)]
    two_cycle_multiset = multiset_transform(two_cycle_types, limit)
    unrestricted_fiber = convolution(
        convolution(root_star, ordinary_star_multiset, limit),
        two_cycle_multiset, limit,
    )
    no_cycle_fiber = convolution(root_star, ordinary_star_multiset, limit)
    essential_fiber = convolution(root_star, [1] + [1] * limit, limit)
    all_pairs = multiset_transform(unrestricted_fiber, limit)
    no_cycle_pairs = multiset_transform(no_cycle_fiber, limit)
    admissible_rank_two = multiset_transform(essential_fiber, limit)
    idempotent_orbits = ordinary_star_multiset
    return {
        'all_pairs': all_pairs,
        'no_cycle_pairs': no_cycle_pairs,
        'rank_one': idempotent_orbits,
        'rank_three': [all_pairs[k] - no_cycle_pairs[k] for k in range(limit + 1)],
        'essential_rank_two': [
            admissible_rank_two[k] - idempotent_orbits[k]
            for k in range(limit + 1)
        ],
    }


def direct_orbits(n):
    maps = tuple(product(range(n), repeat=n))
    idempotents = [e for e in maps if all(e[e[x]] == e[x] for x in range(n))]
    cubic = [t for t in maps if all(t[t[t[x]]] == t[x] for x in range(n))]
    admissible = {
        (t, e) for t in cubic for e in idempotents
        if all(e[t[x]] == e[x] == t[e[x]] for x in range(n))
    }
    rank_three = {
        (t, e) for t, e in admissible
        if any(t[t[x]] != t[x] for x in range(n))
    }
    rank_two_lifts = {
        (tuple(t[t[x]] for x in range(n)), e) for t, e in rank_three
    }
    orbits = Counter()
    while admissible:
        t, e = next(iter(admissible))
        orbit = set()
        for p in permutations(range(n)):
            inverse = [0] * n
            for i, j in enumerate(p):
                inverse[j] = i
            orbit.add((
                tuple(p[t[inverse[j]]] for j in range(n)),
                tuple(p[e[inverse[j]]] for j in range(n)),
            ))
        assert orbit <= admissible
        admissible -= orbit
        if t == e:
            tag = 'rank_one'
        elif (t, e) in rank_three:
            tag = 'rank_three'
        elif (t, e) in rank_two_lifts:
            tag = 'rank_two_from_rank_three'
        else:
            tag = 'essential_rank_two_candidate'
        orbits[tag] += 1
    return orbits


def main():
    data = predictions()
    for n in range(2, 6):
        observed = direct_orbits(n)
        assert observed['rank_one'] == data['rank_one'][n]
        assert observed['rank_three'] == data['rank_three'][n]
        assert sum(observed.values()) == data['all_pairs'][n]
        if n == 5:
            # Here an even-type rank-three element exists, so a rank-two
            # element is nonessential exactly when it has a rank-three lift.
            assert observed['essential_rank_two_candidate'] == data['essential_rank_two'][n]
            assert observed['rank_two_from_rank_three'] == 13
        print('n=%d orbit_counts=%s' % (n, dict(sorted(observed.items()))))
    for n in range(5, 13):
        rank_three = data['rank_three'][n]
        rank_two = data['essential_rank_two'][n]
        rank_end = 3 + rank_three + rank_two
        print('n=%d rank3_orbits=%d essential_rank2_orbits=%d monoid_rank=%d'
              % (n, rank_three, rank_two, rank_end))
    print('ALL_ENDOMORPHISM_MONOID_ORBIT_AND_RANK_CHECKS_PASSED')


if __name__ == '__main__':
    main()
