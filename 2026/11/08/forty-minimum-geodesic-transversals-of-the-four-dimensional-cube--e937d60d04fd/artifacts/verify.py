#!/usr/bin/env python3
"""Exact finite certificate for six-vertex geodesic transversals of Q4.

Run: python3 artifacts/verify.py
Only Python 3 standard library is required.
"""
from itertools import combinations, permutations
from pathlib import Path

D = 4
V = range(1 << D)
ALL = (1 << (1 << D)) - 1


def mask(vertices):
    return sum(1 << x for x in vertices)


def paths():
    found = set()
    for a in V:
        for ordering in permutations(range(D)):
            x = a
            nodes = [x]
            for i in ordering:
                x ^= 1 << i
                nodes.append(x)
            assert len(set(nodes)) == D + 1 and x == (a ^ 15)
            found.add(mask(nodes))
    assert len(found) == 192
    return sorted(found)


def maps():
    result = []
    for p in permutations(range(D)):
        for shift in V:
            result.append(tuple(sum(((v >> i) & 1) << p[i] for i in range(D)) ^ shift for v in V))
    assert len(set(result)) == 384
    return result


def move(S, permutation):
    return mask(permutation[v] for v in V if S & (1 << v))


def orbit(S, automorphisms):
    return {move(S, P) for P in automorphisms}


def family_A():
    # Hamming spheres of radius exactly two in Q4.
    return {mask(v for v in V if (v ^ center).bit_count() == 2) for center in V}


def family_B():
    # For one free axis, the three neighbours of an arbitrary centre
    # in the remaining Q3, lifted across the free coordinate.
    family = set()
    for free in range(D):
        fixed_axes = [i for i in range(D) if i != free]
        for center in V:
            if (center >> free) & 1:
                continue
            base = [center ^ (1 << i) for i in fixed_axes]
            family.add(mask([v ^ flip for v in base for flip in (0, 1 << free)]))
    return family


def certificate_records():
    result = []
    for line in Path(__file__).with_name('orbit_certificate.tsv').read_text('utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        fields = line.split('\t')
        assert len(fields) == 3
        result.append(tuple(int(f) for f in fields))
    return result


def main():
    P = paths()
    perms = maps()
    A, B = family_A(), family_B()
    assert len(A) == 8 and len(B) == 32 and not A.intersection(B)
    for S in A:
        assert S.bit_count() == 6
        assert all((S & p) != 0 for p in P)
        assert all(((u ^ v).bit_count() != 1) for u in V for v in V if u < v and S >> u & 1 and S >> v & 1)
    for S in B:
        assert S.bit_count() == 6
        assert all((S & p) != 0 for p in P)
        assert sum(((u ^ v).bit_count() == 1) for u in V for v in V if u < v and S >> u & 1 and S >> v & 1) == 3
    print('TWO_CONSTRUCTIVE_FAMILIES_OK sphere8=8 prism32=32')

    # Exhaustive direct hitting check, including all 5-sets for minimality.
    s5 = 0
    for C in combinations(V, 5):
        S = mask(C)
        if all(S & p for p in P):
            s5 += 1
    assert s5 == 0
    print('NO_FIVE_VERTEX_TRANSVERSALS_OK tested=4368')
    hits = []
    for C in combinations(V, 6):
        S = mask(C)
        if all(S & p for p in P):
            hits.append(S)
    assert len(hits) == 40 and set(hits) == A | B
    print('ALL_SIX_VERTEX_SETS_EXHAUSTED_OK tested=8008 hits=40')

    # Independently replay orbit certificate, not relying on the direct count.
    cert = certificate_records()
    assert len(cert) == 50
    all_six = {mask(C) for C in combinations(V, 6)}
    unseen = all_six.copy()
    good = []
    total = 0
    for rep, expected_size, forbidden_geodesic in cert:
        assert rep == min(unseen)
        cls = orbit(rep, perms)
        assert cls.issubset(unseen), 'orbit overlaps a preceding row'
        assert len(cls) == expected_size
        if forbidden_geodesic:
            assert forbidden_geodesic in P
            assert rep & forbidden_geodesic == 0
        else:
            assert all(rep & p for p in P)
            good.append((rep, expected_size))
        unseen.difference_update(cls)
        total += len(cls)
    assert not unseen and total == 8008
    assert sorted(size for _, size in good) == [8, 32]
    assert {rep for rep, size in good if size == 8}.issubset(A)
    assert {rep for rep, size in good if size == 32}.issubset(B)
    print('FIFTY_AUTOMORPHISM_ORBIT_CERTIFICATE_OK all=8008 accepted_orbits=8,32 rejected=48')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
