"""Independent bitset checks for apex coalition bounds and explicit witnesses.

Pure standard-library Python; run: python3 verify.py
"""
from itertools import combinations


def is_ld(neigh, mask):
    seen = set()
    for u in range(len(neigh)):
        if not (mask >> u) & 1:
            trace = neigh[u] & mask
            if trace == 0 or trace in seen:
                return False
            seen.add(trace)
    return True


def apex_neighborhoods(base):
    n = len(base)
    return [(1 << n) | base[i] for i in range(n)] + [(1 << n) - 1]


def maxima_all_small_bases():
    instances = valid_nonld = 0
    for n in range(1, 6):
        edges = list(combinations(range(n), 2))
        for encoded in range(1 << len(edges)):
            base = [0] * n
            for k, (u, v) in enumerate(edges):
                if encoded >> k & 1:
                    base[u] |= 1 << v
                    base[v] |= 1 << u
            deg = max((row.bit_count() for row in base), default=0)
            neigh = apex_neighborhoods(base)
            hub = 1 << n
            for part in range(1 << n):
                a = part | hub
                instances += 1
                if is_ld(neigh, a):
                    continue
                valid_nonld += 1
                partners = sum(is_ld(neigh, a | (1 << v)) for v in range(n) if not (part >> v) & 1)
                assert partners <= 2 * deg + 2, (n, encoded, a, deg, partners)
    print('UNIVERSAL_SMALL_BASE_CERTIFICATE_OK', instances, 'sets', valid_nonld, 'nonLD')


def subdivided_stars(d):
    # two independent once-subdivided d-stars; center_i, intermediate_i,j, leaf_i,j
    n = 4 * d + 2
    base = [0] * n
    leaves = []
    for i in range(2):
        c = i * (2 * d + 1)
        for j in range(d):
            m = c + 1 + j
            t = c + 1 + d + j
            base[c] |= 1 << m
            base[m] |= (1 << c) | (1 << t)
            base[t] |= 1 << m
            leaves.append(t)
    return base, leaves


def sharp_constructions():
    for d in range(2, 21):
        base, leaves = subdivided_stars(d)
        neigh = apex_neighborhoods(base)
        n = len(base)
        a = (1 << n) | sum(1 << v for v in leaves)
        assert not is_ld(neigh, a)
        outsiders = [v for v in range(n) if not a >> v & 1]
        assert len(outsiders) == 2 * d + 2
        assert all(is_ld(neigh, a | (1 << w)) for w in outsiders)
        assert all(not is_ld(neigh, 1 << w) for w in outsiders)
        assert max(row.bit_count() for row in base) == d
    print('SHARP_INFINITE_FAMILY_REPLAY_OK', 19, 'values')


def wheel_checks():
    for m in range(10, 121):
        base = [((1 << ((i - 1) % m)) | (1 << ((i + 1) % m))) for i in range(m)]
        neigh = apex_neighborhoods(base)
        outside = [1, 2, 3, 6, 7, 8]
        a = (1 << (m + 1)) - 1
        for i in outside:
            a ^= 1 << i
        assert not is_ld(neigh, a)
        assert all(is_ld(neigh, a | (1 << w)) for w in outside)
        assert all(not is_ld(neigh, 1 << w) for w in outside)
    print('SEVEN_CLASS_WHEELS_OK', 111, 'orders')


def exact_wheel_partner_maxima():
    maxima = {}
    for m in range(3, 14):
        base = [((1 << ((i - 1) % m)) | (1 << ((i + 1) % m))) for i in range(m)]
        neigh = apex_neighborhoods(base)
        big = 0
        for rim_a in range(1 << m):
            a = rim_a | (1 << m)
            if is_ld(neigh, a):
                continue
            partners = sum(is_ld(neigh, a | (1 << w)) for w in range(m) if not rim_a >> w & 1)
            big = max(big, partners)
        assert big <= 6
        maxima[m] = big
    assert all(maxima[m] == 6 for m in range(10, 14))
    print('EXHAUSTIVE_WHEEL_HUB_PARTNERS_OK', maxima)


if __name__ == '__main__':
    maxima_all_small_bases()
    sharp_constructions()
    wheel_checks()
    exact_wheel_partner_maxima()
    print('VERIFY_OK')
