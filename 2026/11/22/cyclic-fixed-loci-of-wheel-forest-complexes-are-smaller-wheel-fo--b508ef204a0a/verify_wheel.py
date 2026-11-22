"""Finite cross-checks for the wheel-forest fixed-locus and dihedral character theorem.

This checker is supplementary: the all-order result uses the combinatorial proof.
"""
from itertools import chain
from math import gcd


def edges(n):
    # Rim edge r_i and spoke s_i, in that order.
    return [((i, (i + 1) % n)) for i in range(n)] + [(i, n) for i in range(n)]


def forest(n, e, mask):
    parent = list(range(n + 1))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i, (a, b) in enumerate(e):
        if mask >> i & 1:
            a, b = root(a), root(b)
            if a == b:
                return False
            parent[a] = b
    return True


def orbits(perm):
    seen = set()
    ans = []
    for i in range(len(perm)):
        if i in seen:
            continue
        o = 0
        j = i
        while j not in seen:
            seen.add(j)
            o |= 1 << j
            j = perm[j]
        ans.append(o)
    return ans


def union_orbits(orbit_masks, mask):
    result = 0
    for j, o in enumerate(orbit_masks):
        if mask >> j & 1:
            result |= o
    return result


def fixed_reduced_euler(n, e, orbit_masks):
    s = -1  # Empty face
    for subset in range(1, 1 << len(orbit_masks)):
        if forest(n, e, union_orbits(orbit_masks, subset)):
            s += (-1) ** (subset.bit_count() - 1)
    return s


def run():
    # Check the graph-quotient correspondence for all rotational cycle types.
    checked_rotation_patterns = 0
    for n in range(3, 10):
        e = edges(n)
        for k in range(n):
            d = gcd(n, k)
            # Each rim/spoke orbit is the family with fixed index modulo d.
            orbit_masks = [sum(1 << i for i in range(n) if i % d == j)
                           for j in range(d)] + [
                           sum(1 << (n + i) for i in range(n) if i % d == j)
                           for j in range(d)]
            ed = edges(d)  # d=1: a loop; d=2: two parallel rim edges.
            for subset in range(1 << (2 * d)):
                lift = union_orbits(orbit_masks, subset)
                assert forest(n, e, lift) == forest(d, ed, subset), (n, k, subset)
            checked_rotation_patterns += 1

    # All odd-rim reflections: adjoining the unique fixed spoke is a cone pairing.
    checked_reflection_patterns = 0
    for n in (3, 5, 7, 9, 11):
        e = edges(n)
        reflection = [(-i - 1) % n for i in range(n)] + [
                      n + (-i) % n for i in range(n)]
        orb = orbits(reflection)
        apex = 1 << n  # spoke s_0, fixed by reflection
        assert apex in orb
        for subset in range(1 << len(orb)):
            m = union_orbits(orb, subset)
            if forest(n, e, m):
                assert forest(n, e, m | apex), (n, subset)
        checked_reflection_patterns += 1

    # Independently verify Lefschetz fixed Euler sums and twisted binary character.
    for n in (3, 5, 7, 9):
        e = edges(n)
        for k in range(n):
            d = gcd(n, k)
            perm = [((i + k) % n) for i in range(n)] + [
                    n + ((i + k) % n) for i in range(n)]
            chi = fixed_reduced_euler(n, e, orbits(perm))
            expected = (-1) ** (d - 1) * (2 ** d - 2)
            assert chi == expected, (n, k, chi, expected)
            binary_fixed = sum(all(((word >> i) & 1) ==
                          ((word >> ((i + k) % n)) & 1) for i in range(n))
                          for word in range(1, (1 << n) - 1))
            assert binary_fixed == 2 ** d - 2
        perm = [(-i - 1) % n for i in range(n)] + [n + (-i) % n for i in range(n)]
        assert fixed_reduced_euler(n, e, orbits(perm)) == 0
        # The reflection-complement operation has no fixed binary word.
        assert not any(all(((word >> i) & 1) != ((word >> (-i % n)) & 1)
                         for i in range(n)) for word in range(1 << n))
    print('WHEEL_FOREST_ROTATION_FIXED_LOCI_AND_ODD_DIHEDRAL_CHARACTER_OK',
          checked_rotation_patterns, checked_reflection_patterns)


if __name__ == '__main__':
    run()
