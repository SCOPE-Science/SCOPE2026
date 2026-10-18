"""Finite checks for the sharp coherence level of disjoined constancy atoms.

Run with Python >=3.9: python verify.py
The unrestricted result is proved symbolically in RESULT.md; finite tests are ancillary.
"""
from fractions import Fraction
from itertools import product
from random import Random


def hyperplane_masks(r, alphabet):
    pts = list(product(range(alphabet), repeat=r))
    masks = []
    for selector in pts:
        mask = 0
        for pos, pt in enumerate(pts):
            if any(pt[j] == selector[j] for j in range(r)):
                mask |= 1 << pos
        masks.append(mask)
    return pts, masks


def is_coverable(team_mask, covers):
    return any((team_mask & ~cover) == 0 for cover in covers)


def rank_rational(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    nr, nc = len(a), len(a[0])
    lead = 0
    rank = 0
    for col in range(nc):
        pivot = next((i for i in range(lead, nr) if a[i][col]), None)
        if pivot is None:
            continue
        a[lead], a[pivot] = a[pivot], a[lead]
        d = a[lead][col]
        a[lead] = [v / d for v in a[lead]]
        for i in range(nr):
            if i != lead and a[i][col]:
                d = a[i][col]
                a[i] = [v - d * w for v, w in zip(a[i], a[lead])]
        rank += 1
        lead += 1
        if lead == nr:
            break
    return rank


def polynomial_coefficients(pt):
    r = len(pt)
    out = []
    for monomial in range(1 << r):
        coeff = 1
        for i in range(r):
            if not (monomial & (1 << i)):
                coeff *= -pt[i]
        out.append(coeff)
    return out


def check_exhaustive(r, alphabet):
    pts, covers = hyperplane_masks(r, alphabet)
    full = (1 << len(pts)) - 1
    failures = 0
    max_minimal_failure = 0
    checked = 0
    for team in range(full + 1):
        checked += 1
        if is_coverable(team, covers):
            continue
        failures += 1
        minimal = all(is_coverable(team ^ (1 << bit), covers)
                      for bit in range(len(pts)) if team & (1 << bit))
        if minimal:
            size = team.bit_count()
            max_minimal_failure = max(max_minimal_failure, size)
            assert size <= 2 ** r, (r, alphabet, size)
    return checked, failures, max_minimal_failure


def check_cube(r):
    pts, covers = hyperplane_masks(r, 2)
    full = (1 << len(pts)) - 1
    assert not is_coverable(full, covers)
    assert all(is_coverable(full ^ (1 << bit), covers)
               for bit in range(len(pts)))
    assert rank_rational([polynomial_coefficients(pt) for pt in pts]) == 2 ** r


def random_ternary_triplets(trials=12000):
    r = 3
    pts, covers = hyperplane_masks(r, 3)
    rng = Random(31173)
    bad = 0
    for _ in range(trials):
        mask = 0
        for i in range(len(pts)):
            if rng.randrange(4) != 0:
                mask |= 1 << i
        if is_coverable(mask, covers):
            continue
        bad += 1
        for i in range(len(pts)):
            if (mask & (1 << i)) and not is_coverable(mask ^ (1 << i), covers):
                mask ^= 1 << i
        assert mask.bit_count() <= 2 ** r
        assert not is_coverable(mask, covers)
        assert all(is_coverable(mask ^ (1 << i), covers)
                   for i in range(len(pts)) if mask & (1 << i))
    return bad


def main():
    for r in range(1, 5):
        check_cube(r)
        print('CUBE_OK', r, 'size', 2 ** r, 'polynomial_rank', 2 ** r)
    configs = [(1, 2), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3)]
    total = 0
    for r, alphabet in configs:
        checked, bad, largest = check_exhaustive(r, alphabet)
        total += checked
        print('CENSUS_OK', r, alphabet, 'teams', checked,
              'noncoverable', bad, 'largest_minimal', largest)
    bad_random = random_ternary_triplets()
    print('RANDOM_OK', 'ternary_r3', 'bad_samples', bad_random)
    print('VERIFY_OK', 'exhaustive_team_masks', total)


if __name__ == '__main__':
    main()
