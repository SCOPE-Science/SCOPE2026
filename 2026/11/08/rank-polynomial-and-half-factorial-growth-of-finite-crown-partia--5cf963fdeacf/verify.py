#!/usr/bin/env python3
"""Exact checks of crown partial-automorphism rank counts (Python standard library)."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def signature(n, mask):
    if mask == 0:
        return ()
    if mask == (1 << n) - 1:
        return ('FULL',)
    types = []
    for a in range(n):
        if (mask >> a) & 1 and not ((mask >> ((a - 1) % n)) & 1):
            length = 0
            while (mask >> ((a + length) % n)) & 1:
                length += 1
            if length == 1:
                typ = ('s',)
            elif length % 2 == 0:
                typ = ('e', length)
            else:
                typ = ('o', length, a % 2)
            types.append(typ)
    return tuple(sorted(types))


def type_profiles_from_subsets(n):
    profiles = defaultdict(int)
    for mask in range(1, (1 << n) - 1):
        profiles[signature(n, mask)] += 1
    return dict(profiles)


def type_profiles_from_cyclic_runs(n):
    """Independent exact run/gap computation of [z^n] tr(T^r)."""
    profiles = defaultdict(Fraction)
    for r in range(1, n // 2 + 1):
        for cuts in combinations(range(1, n), 2 * r - 1):
            edges = (0,) + cuts + (n,)
            parts = [edges[i + 1] - edges[i] for i in range(2 * r)]
            for initial_parity in (0, 1):
                parity = initial_parity
                types = []
                for i in range(r):
                    length, gap = parts[2 * i], parts[2 * i + 1]
                    if length == 1:
                        typ = ('s',)
                    elif length % 2 == 0:
                        typ = ('e', length)
                    else:
                        typ = ('o', length, parity)
                    types.append(typ)
                    parity = (parity + length + gap) % 2
                assert parity == initial_parity
                profiles[tuple(sorted(types))] += Fraction(n, 2 * r)
    assert all(count.denominator == 1 for count in profiles.values())
    return {signature: int(count) for signature, count in profiles.items()}


def automorphisms_of_type(signature):
    multiplicities = Counter(signature)
    answer = 1
    for typ, count in multiplicities.items():
        answer *= factorial(count)
        if typ[0] == 'o':
            answer *= 2 ** count
    return answer


def rank_polynomial(n, profiles):
    ranks = [0] * (n + 1)
    ranks[0] = 1
    ranks[n] = n
    for signature, count in profiles.items():
        k = sum(1 if typ == ('s',) else typ[1] for typ in signature)
        ranks[k] += count * count * automorphisms_of_type(signature)
    return ranks


def crown_comparable(n, a, b):
    return a % 2 == 0 and (a - b) % n in (1, n - 1)


def rank_polynomial_direct(n):
    """Enumerate actual partial injections, with no component-type assumptions."""
    nodes = range(n)
    result = [0] * (n + 1)
    for k in range(n + 1):
        for source in combinations(nodes, k):
            relations = tuple(tuple(crown_comparable(n, source[i], source[j])
                                    for j in range(k)) for i in range(k))
            for target in combinations(nodes, k):
                for outputs in permutations(target):
                    if all(relations[i][j] == crown_comparable(n, outputs[i], outputs[j])
                           for i in range(k) for j in range(k)):
                        result[k] += 1
    return result


def main():
    known = {
        4:  [1, 16, 24, 16, 4],
        6:  [1, 36, 198, 204, 90, 36, 6],
        8:  [1, 64, 864, 2624, 2176, 832, 256, 64, 8],
        10: [1, 100, 2550, 18700, 38850, 27780, 9900, 2500, 550, 100, 10],
        12: [1, 144, 5976, 84624, 402336, 641232, 410496, 139536,
             32112, 6000, 1008, 144, 12],
        14: [1, 196, 12054, 284396, 2606506, 8937796, 11693164,
             6859972, 2247630, 494116, 83888, 12348, 1666, 196, 14],
        16: [1, 256, 21888, 780544, 12049920, 78433536, 208186368,
             233447680, 127500544, 40521472, 8682240, 1403136, 188800,
             22784, 2560, 256, 16]
    }
    for n in (4, 6, 8, 10, 12, 14):
        profiles = type_profiles_from_subsets(n)
        assert profiles == type_profiles_from_cyclic_runs(n)
        ranks = rank_polynomial(n, profiles)
        assert ranks == known[n]
        print('RUN_TRANSFER_OK', n, 'types', len(profiles), 'total', sum(ranks))
    n = 16
    ranks = rank_polynomial(n, type_profiles_from_subsets(n))
    assert ranks == known[n]
    print('RANKS_OK', n, 'total', sum(ranks))
    for n, ranks in known.items():
        assert ranks[0] == 1 and ranks[1] == n*n and ranks[n-1] == n*n and ranks[n] == n
        assert ranks[2] == n*n + (n*n*(n-3)*(n-3))//2
        if n >= 6:
            assert ranks[n-2] == n*n*(3*n-8)//4
    print('BOUNDARY_FORMULAS_OK')
    for n in (4, 6, 8):
        direct = rank_polynomial_direct(n)
        assert direct == known[n]
        print('DIRECT_MAPS_OK', n, 'total', sum(direct))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
