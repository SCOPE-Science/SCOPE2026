"""Exhaustive closed-translate coverage over F_27; Python 3 standard library."""
from itertools import combinations
from math import comb

q = 27
v = [tuple((a // (3**i)) % 3 for i in range(3)) for a in range(q)]


def encode(coeffs):
    return sum((c % 3) * 3**i for i, c in enumerate(coeffs))


def negative_square(a):
    coeffs = [0] * 5
    for i, x in enumerate(v[a]):
        for j, y in enumerate(v[a]):
            coeffs[i + j] -= x * y
    for deg in (4, 3):
        # Use X^3=X-1 in F_3[X]/(X^3-X+1).
        coeffs[deg - 2] += coeffs[deg]
        coeffs[deg - 3] -= coeffs[deg]
    return encode(coeffs[:3])


def main():
    assert all((a**3 - a + 1) % 3 != 0 for a in range(3))
    add = [[encode(c + d for c, d in zip(a, b)) for b in v] for a in v]
    left = sorted({negative_square(a) for a in range(q)})
    assert len(left) == 14 and 0 in left
    covered = {}
    for d in (3, 4):
        covered[d] = {
            tuple(sorted(row[a] for a in subset))
            for subset in combinations(left, d)
            for row in add
        }
    assert len(covered[3]) == comb(q, 3) == 2925
    assert len(covered[4]) == 16146
    missing = [s for s in combinations(range(q), 4) if s not in covered[4]]
    normalized = [s for s in missing if add[add[s[0]][s[1]]][add[s[2]][s[3]]] == 0]
    assert len(missing) == 1404 and len(normalized) == 52
    assert q * len(normalized) == len(missing)
    deficit = 24 * len(normalized)
    assert (deficit, q**3 - deficit) == (1248, 18435)
    print('covered triples=2925; covered quartets=16146')
    print('uncovered quartets=1404; normalized quartets=52')
    print('missing ordered targets=1248; square-image size=18435')


if __name__ == '__main__':
    main()
