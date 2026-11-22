"""Independent small-group checks for projective three-cube avoidance.

Python 3, standard library only. A cube includes all seven nonempty
subset sums of three (not necessarily distinct) group elements.
"""
from itertools import combinations, product


def group(moduli):
    pts = list(product(*(range(m) for m in moduli)))
    idx = {x: i for i, x in enumerate(pts)}
    add = [[idx[tuple((x[k] + y[k]) % moduli[k]
                       for k in range(len(moduli)))] for y in pts] for x in pts]
    zero = idx[tuple(0 for _ in moduli)]
    return pts, add, zero


def cube_masks(add):
    n = len(add)
    cubes = set()
    for x in range(n):
        for y in range(n):
            xy = add[x][y]
            for z in range(n):
                bits = (1 << x) | (1 << y) | (1 << z)
                bits |= (1 << xy) | (1 << add[x][z])
                bits |= (1 << add[y][z]) | (1 << add[xy][z])
                cubes.add(bits)
    return tuple(cubes)


def is_free(bits, cubes):
    return all((bits & cube) != cube for cube in cubes)


def extremizers(moduli):
    points, add, zero = group(moduli)
    n = len(points)
    assert n % 3 == 0
    cubes = cube_masks(add)
    good = []
    for choice in combinations((i for i in range(n) if i != zero), 2*n//3):
        bits = sum(1 << i for i in choice)
        if is_free(bits, cubes):
            good.append(bits)
    return points, add, zero, good


def test_small():
    for moduli, expected in [((3,), 1), ((9,), 1), ((15,), 1), ((3, 3), 4)]:
        pts, add, zero, good = extremizers(moduli)
        assert len(good) == expected, (moduli, len(good))
        n = len(pts)
        allbits = (1 << n) - 1
        for A in good:
            B = allbits ^ A
            S = {i for i in range(n) if ((A >> i) & 1)
                 and ((A >> add[i][i]) & 1)}
            assert len(S) >= n//3 and zero not in S
            for x in S:
                three_x = add[x][add[x][x]]
                shift_B = sum(1 << add[b][three_x] for b in range(n)
                              if ((B >> b) & 1))
                assert shift_B == B
        print('EXHAUSTIVE_OPTIMA', moduli, 'N=', n, 'COUNT=', len(good))
    print('RANK_ONE_UNIQUENESS_AND_RANK_TWO_FOUR_CASES_PASS')


def test_lifting():
    pts, add, zero, good = extremizers((3, 3))
    L, op, iz = group((9, 3))
    cubes = cube_masks(op)
    projection = {i: pts.index((p[0] % 3, p[1])) for i, p in enumerate(L)}
    assert len(good) == 4
    for A in good:
        lift = sum(1 << i for i in range(len(L))
                   if ((A >> projection[i]) & 1))
        assert lift.bit_count() == 18
        assert is_free(lift, cubes)
    print('FULL_INVERSE_IMAGE_CUBE_FREENESS_PASS', len(good), 'rank-two patterns')


if __name__ == '__main__':
    test_small()
    test_lifting()
    print('VERIFY_OK')
