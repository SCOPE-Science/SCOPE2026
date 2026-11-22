"""Reproduce finite tests for the regular equivariant-map rank formula.

Python 3, standard library only.  Tests use complete transformation enumeration:
regularity is checked by existence of an actual equivariant inner inverse.
"""
from itertools import product
from collections import Counter
from math import comb


def generated_group(generators):
    n = len(generators[0])
    identity = tuple(range(n))
    seen = {identity}
    queue = [identity]
    while queue:
        a = queue.pop()
        for b in generators:
            c = tuple(a[b[i]] for i in range(n))
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return tuple(sorted(seen))


def orbits(group, n):
    unseen = set(range(n))
    result = []
    while unseen:
        x = min(unseen)
        orbit = tuple(sorted({g[x] for g in group}))
        assert set(orbit) <= unseen
        result.append(orbit)
        unseen.difference_update(orbit)
    return result


def maps(group, n):
    representative = [o[0] for o in orbits(group, n)]
    options = []
    for x in representative:
        stabilizer = [g for g in group if g[x] == x]
        options.append([y for y in range(n) if all(g[y] == y for g in stabilizer)])
    for chosen in product(*options):
        f = [None] * n
        for x, y in zip(representative, chosen):
            for g in group:
                source, target = g[x], g[y]
                assert f[source] in (None, target)
                f[source] = target
        assert all(z is not None for z in f)
        yield tuple(f)


def is_inner_inverse(f, h):
    return all(f[h[f[x]]] == f[x] for x in range(len(f)))


def table_data(group, n):
    orbit_list = orbits(group, n)
    stabilizers = [[g for g in group if g[o[0]] == o[0]] for o in orbit_list]
    # Number of G-maps from orbit a to orbit b.
    hom = [[sum(all(g[y] == y for g in stabilizers[a]) for y in orbit_list[b])
            for b in range(len(orbit_list))] for a in range(len(orbit_list))]
    types = []
    for a in range(len(orbit_list)):
        for t in types:
            b = t[0]
            if len(orbit_list[a]) == len(orbit_list[b]) and hom[a][b] > 0:
                assert hom[b][a] > 0
                t.append(a)
                break
        else:
            types.append([a])
    multiplicity = [len(t) for t in types]
    point_sizes = [len(orbit_list[t[0]]) for t in types]
    marks = [[hom[t[0]][u[0]] for u in types] for t in types]
    assert all(marks[i][i] > 0 for i in range(len(marks)))
    for t in types:
        for a in t:
            assert [hom[a][u[0]] for u in types] == marks[types.index(t)]
    return multiplicity, point_sizes, marks


def predicted_rank_profile(multiplicity, point_sizes, marks):
    k = len(multiplicity)
    result = Counter()
    for selected in product(*(range(m + 1) for m in multiplicity)):
        ways = 1
        for i, m in enumerate(multiplicity):
            allowed = sum(selected[j] * marks[i][j] for j in range(k))
            surj = sum((-1)**u * comb(selected[i], u) *
                       (allowed - u * marks[i][i])**m
                       for u in range(selected[i] + 1))
            ways *= comb(m, selected[i]) * surj
        result[sum(selected[i] * point_sizes[i] for i in range(k))] += ways
    return {degree: count for degree, count in sorted(result.items()) if count}


def predicted_total_regular(multiplicity, marks):
    return sum(predicted_rank_profile(multiplicity, [1]*len(multiplicity), marks).values())


def criterion_all_regular(multiplicity, marks):
    for j, m in enumerate(multiplicity):
        has_strict_lower = any(i != j and marks[i][j] for i in range(len(marks)))
        has_strict_higher = any(k != j and marks[j][k] for k in range(len(marks)))
        if has_strict_lower and (m >= 2 or has_strict_higher):
            return False
    return True


def test(name, generators):
    group = generated_group(generators)
    n = len(generators[0])
    all_maps = list(maps(group, n))
    brute_regular = [f for f in all_maps if any(is_inner_inverse(f, g) for g in all_maps)]
    brute_profile = Counter(len(set(f)) for f in brute_regular)
    multiplicity, point_sizes, marks = table_data(group, n)
    expected = predicted_rank_profile(multiplicity, point_sizes, marks)
    assert dict(sorted(brute_profile.items())) == expected, (name, brute_profile, expected)
    assert (len(brute_regular) == len(all_maps)) == criterion_all_regular(multiplicity, marks)
    total = 1
    for i, m in enumerate(multiplicity):
        total *= sum(multiplicity[j] * marks[i][j] for j in range(len(multiplicity)))**m
    assert total == len(all_maps)
    print(f"{name}: |G|={len(group)} all={len(all_maps)} regular={len(brute_regular)} "
          f"regular-ranks={expected}")


def main():
    test('trivial action on three points', [(0,1,2)])
    test('C2, one free orbit and two fixed points', [(1,0,2,3)])
    test('C2, two free orbits and two fixed points', [(1,0,3,2,4,5)])
    test('C2, three free orbits and one fixed point', [(1,0,3,2,5,4,6)])
    test('C4, a regular, an index-two, and a fixed orbit', [(1,2,3,0,5,4,6)])
    test('C3, a regular orbit and two fixed points', [(1,2,0,3,4)])
    test('S3, a natural orbit, a sign orbit, two fixed points',
         [(1,2,0,3,4,5,6), (1,0,2,4,3,5,6)])
    test('S3, two natural orbits and two fixed points',
         [(1,2,0,4,5,3,6,7), (1,0,2,4,3,5,6,7)])
    test('S3, two natural orbits, a sign orbit, two fixed points',
         [(1,2,0,4,5,3,6,7,8,9), (1,0,2,4,3,5,7,6,8,9)])
    test('S3, two conjugate but differently indexed natural orbits',
         [(1,2,0,4,5,3,6,7), (1,0,2,5,4,3,6,7)])
    print('REGULAR_EQUIVARIANT_RANK_TESTS_PASSED')


if __name__ == '__main__':
    main()
