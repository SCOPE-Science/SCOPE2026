"""Independent orbit and direct complement/frequency verification for 19 representatives."""
import json
from collections import Counter
from itertools import combinations, product
from pathlib import Path

q = 4
N = 16
xy = [(x % 4, x // 4) for x in range(N)]


def code(x, y):
    return (x % q) + q * (y % q)


def sumindex(i, j):
    return code(xy[i][0] + xy[j][0], xy[i][1] + xy[j][1])


def difference(i, j):
    return code(xy[i][0] - xy[j][0], xy[i][1] - xy[j][1])


def fourier_vanishes(T, frequency):
    real = imaginary = 0
    for t in T:
        exponent = (xy[t][0] * xy[frequency][0] + xy[t][1] * xy[frequency][1]) % q
        if exponent == 0:
            real += 1
        elif exponent == 1:
            imaginary += 1
        elif exponent == 2:
            real -= 1
        else:
            imaginary -= 1
    return real == imaginary == 0


def directly_tiles(A, T):
    return len({sumindex(a, t) for a in A for t in T}) == 16


def is_group(S):
    return all(sumindex(s, t) in S for s in S for t in S)


def anchor_normalizations(A):
    gl = []
    for a, b, c, d in product(range(4), repeat=4):
        if (a * d - b * c) % 2:
            gl.append((a, b, c, d))
    assert len(gl) == 96
    seen = set()
    for a, b, c, d in gl:
        image = {code(a * xy[x][0] + b * xy[x][1], c * xy[x][0] + d * xy[x][1]) for x in A}
        for anchor in image:
            seen.add(frozenset(difference(x, anchor) for x in image))
    return seen


def main():
    data = json.loads((Path(__file__).parent / 'orbit_witnesses.json').read_text(encoding='utf-8'))
    assert len(data) == 19
    unions = set()
    total_subgroup_bad = Counter()
    orbit_sizes = Counter()
    for row in data:
        A = set(row['tile'])
        S = set(row['universal_spectrum'])
        assert 0 in A and 0 in S and len(S) == 16 // len(A)
        orbit = anchor_normalizations(A)
        assert len(orbit) == row['orbit_size']
        assert not (unions & orbit), 'affine orbit overlap'
        unions |= orbit
        orbit_sizes[len(A)] += len(orbit)
        # Instead of recursive exact cover, directly test all possible complements
        # containing the identity, then perform Gaussian-integer character sums.
        complements = []
        for rest in combinations(range(1, 16), 16 // len(A) - 1):
            T = {0, *rest}
            if directly_tiles(A, T):
                complements.append(T)
        assert len(complements) == row['complements'], (row, len(complements))
        for T in complements:
            for x in S:
                for y in S:
                    if x != y:
                        assert fourier_vanishes(T, difference(x, y)), (row, T, x, y)
        subgroup_count = 0
        for rest in combinations(range(1, 16), len(S) - 1):
            H = {0, *rest}
            if is_group(H) and all(fourier_vanishes(T, difference(x, y))
                                   for T in complements for x in H for y in H if x != y):
                subgroup_count += 1
        assert subgroup_count == row['subgroup_spectra'], (row, subgroup_count)
        if subgroup_count == 0:
            total_subgroup_bad[len(A)] += len(orbit)
    assert (len(unions), sum(orbit_sizes.values())) == (715, 715)
    assert tuple(orbit_sizes[k] for k in (1, 2, 4, 8, 16)) == (1, 15, 311, 387, 1)
    assert tuple(total_subgroup_bad[k] for k in (1, 2, 4, 8, 16)) == (0, 12, 88, 360, 0)
    print('VERIFY_ORBITS_OK classes=19 affine_maps=1536 anchored_union=715 '
          'non_subgroup_anchored=460 all_witnesses_orthogonal=True')


if __name__ == '__main__':
    main()
