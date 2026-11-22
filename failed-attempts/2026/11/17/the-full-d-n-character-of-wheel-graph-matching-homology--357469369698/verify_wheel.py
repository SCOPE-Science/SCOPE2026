#!/usr/bin/env python3
"""Finite exact checks of wheel-matching dihedral character formulas.
No external libraries or data are needed. The all-n proof is in RESULT.md.
"""
from itertools import combinations
from math import gcd


def path_eval(m):
    assert m >= 0
    if m == 0:
        return 1
    if m == 1:
        return 0
    a, b = 1, 0
    for _ in range(2, m + 1):
        a, b = b, b - a
    return b


def cycle_eval(m):
    # Independent-set polynomial of the simple m-cycle at -1,
    # extended for m=1,2 by their orbit-quotient conventions.
    assert m >= 1
    return (2, 1, -1, -2, -1, 1)[m % 6]


def degree(n):
    assert n >= 3
    return (n - 1) // 3


def rank(n):
    return 2 if n % 3 == 0 else n - 1 if n % 3 == 1 else n + 1


def formula(n, a, reflect):
    sign = (-1) ** (degree(n) + 1)
    if reflect:
        signed_sum = 0 if n % 2 else path_eval(n // 2 + 1)
    elif a % n == 0:
        signed_sum = cycle_eval(n) - n * path_eval(n - 2)
    else:
        signed_sum = cycle_eval(gcd(n, a))
    return sign * signed_sum


def enumerate_matchings(n):
    # Rim edges are numbered 0..n-1; spokes are numbered n..2n-1.
    edges = [(i, (i + 1) % n) for i in range(n)] + [(n, i) for i in range(n)]
    out = [()]
    def recurse(next_edge, used_vertices, selected):
        for j in range(next_edge, 2 * n):
            u, v = edges[j]
            if u not in used_vertices and v not in used_vertices:
                child = selected + (j,)
                out.append(child)
                recurse(j + 1, used_vertices | {u, v}, child)
    recurse(0, set(), ())
    return out


def signed_face_sum(faces, edge_permutation):
    result = 0
    for face in faces:
        image = [edge_permutation[i] for i in face]
        if set(image) != set(face):
            continue
        inversion_parity = 0
        for i, j in combinations(image, 2):
            if i > j:
                inversion_parity ^= 1
        result += (-1) ** (len(face) + inversion_parity)
    return result


def dihedral_permutation(n, a, reflect):
    if reflect:
        rim = [(a - i - 1) % n for i in range(n)]
        spokes = [n + (a - i) % n for i in range(n)]
    else:
        rim = [(a + i) % n for i in range(n)]
        spokes = [n + (a + i) % n for i in range(n)]
    return rim + spokes


def direct_independence_eval(m, path):
    result = 0
    for mask in range(1 << m):
        if path:
            ok = all(not ((mask >> i) & 3 == 3) for i in range(m - 1))
        else:
            ok = all(not ((mask >> i) & 1 and (mask >> ((i + 1) % m)) & 1) for i in range(m))
        if ok:
            result += (-1) ** mask.bit_count()
    return result


def direct_path_reversal_eval(m):
    value = 0
    for mask in range(1 << m):
        if any((mask >> i) & 1 and (mask >> (i + 1)) & 1 for i in range(m - 1)):
            continue
        indices = [i for i in range(m) if (mask >> i) & 1]
        image = [m - 1 - i for i in indices]
        if set(indices) != set(image):
            continue
        inv = sum(i > j for i, j in combinations(image, 2))
        value += (-1) ** (len(indices) + inv)
    return value


def verify_independence():
    for m in range(1, 19):
        assert direct_independence_eval(m, True) == path_eval(m)
        assert direct_independence_eval(m, False) == cycle_eval(m) or m == 1
        reverse_value = direct_path_reversal_eval(m)
        expected = path_eval((m - 2) // 2) if m % 2 == 0 else path_eval((m + 1) // 2)
        assert reverse_value == expected, ('path-reversal', m, reverse_value, expected)
    print('INDEPENDENCE_EXACT m=1..18 OK')


def verify_wheel():
    checked = 0
    faces_total = 0
    for n in range(3, 17):
        faces = enumerate_matchings(n)
        faces_total += len(faces)
        for a in range(n):
            for ref in (False, True):
                perm = dihedral_permutation(n, a, ref)
                direct = (-1) ** (degree(n) + 1) * signed_face_sum(faces, perm)
                expected = formula(n, a, ref)
                assert direct == expected, (n, a, ref, direct, expected)
                checked += 1
        assert formula(n, 0, False) == rank(n)
    print('WHEEL_EXACT n=3..16 faces=%d dihedral_elements=%d OK' % (faces_total, checked))


def verify_invariants():
    for n in range(3, 301):
        rot = sum(formula(n, a, False) for a in range(n))
        allsum = rot + sum(formula(n, a, True) for a in range(n))
        assert rot % n == 0 and allsum % (2 * n) == 0
        cyclic_expected = (0, 0, 1, 0, 1, 2)[n % 6]
        dihedral_expected = int(n % 12 in (2, 5, 10, 11))
        assert rot // n == cyclic_expected
        assert allsum // (2 * n) == dihedral_expected
    print('INVARIANTS_ALL n=3..300 OK')




def verify_homology_mod2():
    # Independent finite chain calculation: columns of oriented boundaries modulo 2.
    from collections import defaultdict
    def rank_mod2(columns):
        pivots = {}
        for x in columns:
            while x:
                leading = x.bit_length() - 1
                if leading in pivots:
                    x ^= pivots[leading]
                else:
                    pivots[leading] = x
                    break
        return len(pivots)
    for n in range(3, 12):
        faces = enumerate_matchings(n)
        levels = defaultdict(list)
        for face in faces:
            if face:
                levels[len(face) - 1].append(face)
        ranks = {}
        for dim in range(1, max(levels) + 1):
            lower_index = {face: j for j, face in enumerate(levels[dim - 1])}
            columns = []
            for face in levels[dim]:
                boundary = 0
                for j in range(len(face)):
                    boundary ^= 1 << lower_index[face[:j] + face[j+1:]]
                columns.append(boundary)
            ranks[dim] = rank_mod2(columns)
        betti = []
        for dim in range(max(levels) + 1):
            value = len(levels[dim]) - ranks.get(dim, 0) - ranks.get(dim + 1, 0)
            if dim == 0:
                value -= 1  # reduced degree-zero correction
            if value:
                betti.append((dim, value))
        assert betti == [(degree(n), rank(n))], (n, betti)
    print('HOMOLOGY_MOD2 n=3..11 exact boundary ranks OK')

if __name__ == '__main__':
    verify_independence()
    verify_wheel()
    verify_homology_mod2()
    verify_invariants()
    print('VERIFY_OK')
