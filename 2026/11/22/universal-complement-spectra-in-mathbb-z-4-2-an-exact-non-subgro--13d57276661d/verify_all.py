"""Exact exhaustive test of common Fourier spectra in (Z/4Z)^2.

Run with Python 3.10+; requires no third-party packages.
"""
from collections import Counter
from itertools import combinations

N = 16
FULL = (1 << N) - 1
xy = tuple((j % 4, j // 4) for j in range(N))
add = tuple(tuple((xy[x][0] + xy[y][0]) % 4 + 4 * ((xy[x][1] + xy[y][1]) % 4)
                  for y in range(N)) for x in range(N))
sub = tuple(tuple((xy[x][0] - xy[y][0]) % 4 + 4 * ((xy[x][1] - xy[y][1]) % 4)
                  for y in range(N)) for x in range(N))


def positions(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask -= b


def translate(mask, t):
    return sum(1 << add[t][x] for x in positions(mask))


def normalized_complements(A):
    """Every T with 0 in T and A+T uniquely equal to the full group."""
    translates = [translate(A, t) for t in range(N)]
    size = N // A.bit_count()

    def search(covered, T):
        if covered == FULL:
            assert T.bit_count() == size
            yield T
            return
        missing = (~covered) & FULL
        x = (missing & -missing).bit_length() - 1
        # x belongs to a+t for at least one a in A in any completion.
        for a in positions(A):
            t = sub[x][a]
            if not (covered & translates[t]):
                yield from search(covered | translates[t], T | (1 << t))

    return set(search(translates[0], 1))


def fourier_zero_mask(T):
    out = 0
    for f in range(1, N):
        real = imag = 0
        for t in positions(T):
            d = (xy[t][0] * xy[f][0] + xy[t][1] * xy[f][1]) % 4
            real += int(d == 0) - int(d == 2)
            imag += int(d == 1) - int(d == 3)
        if real == 0 and imag == 0:
            out |= 1 << f
    return out


def find_common_spectrum(zero, k):
    """Search for a k-clique containing frequency zero."""
    if k == 1:
        return 1
    allowed = [f for f in range(1, N) if zero & (1 << f)]

    def extend(prefix, remaining):
        if prefix.bit_count() == k:
            return prefix
        if prefix.bit_count() + len(remaining) < k:
            return 0
        for i, f in enumerate(remaining):
            eligible = [g for g in remaining[i + 1:] if zero & (1 << sub[f][g])]
            found = extend(prefix | (1 << f), eligible)
            if found:
                return found
        return 0

    return extend(1, allowed)


def is_subgroup(S):
    return all(S & (1 << add[x][y]) for x in positions(S) for y in positions(S))


def main():
    subgroup_candidates = {k: [S for S in range(1, 1 << N, 2)
                               if S.bit_count() == k and is_subgroup(S)]
                           for k in (1, 2, 4, 8, 16)}
    assert [len(subgroup_candidates[k]) for k in (1, 2, 4, 8, 16)] == [1, 3, 7, 3, 1]
    tiles = Counter()
    no_subgroup = Counter()
    comp_total = Counter()
    examined = 0
    for k in (1, 2, 4, 8, 16):
        for tail in combinations(range(1, N), k - 1):
            examined += 1
            A = 1 | sum(1 << x for x in tail)
            comps = normalized_complements(A)
            if not comps:
                continue
            assert all((T & 1) and T.bit_count() == N // k for T in comps)
            common_zero = FULL ^ 1
            for T in comps:
                common_zero &= fourier_zero_mask(T)
            spectrum = find_common_spectrum(common_zero, N // k)
            assert spectrum, ('no universal spectrum', A)
            # A fixed spectrum must be orthogonal on every tiling complement.
            assert all((common_zero >> sub[x][y]) & 1
                       for x in positions(spectrum) for y in positions(spectrum) if x != y)
            candidate_subgroups = [H for H in subgroup_candidates[N // k]
                                   if (H & ~1) & ~common_zero == 0]
            if not candidate_subgroups:
                no_subgroup[k] += 1
            tiles[k] += 1
            comp_total[k] += len(comps)
    assert examined == 6907, examined
    assert tuple(tiles[k] for k in (1, 2, 4, 8, 16)) == (1, 15, 311, 387, 1), tiles
    assert tuple(no_subgroup[k] for k in (1, 2, 4, 8, 16)) == (0, 12, 88, 360, 0), no_subgroup
    assert sum(tiles.values()) == 715
    assert sum(no_subgroup.values()) == 460
    # Each translation class has k choices of anchor; among 16 placements,
    # there are 16/k distinct sets containing no prescribed fixed point.
    all_tiles = sum(16 * tiles[k] // k for k in tiles)
    all_no_subgroup = sum(16 * no_subgroup[k] // k for k in no_subgroup)
    assert (all_tiles, all_no_subgroup) == (2155, 1168)
    print('VERIFY_ALL_OK candidates=6907 normalized_tiles=715 total_tiles=2155 '
          'non_subgroup_normalized=460 non_subgroup_total=1168 '
          'normalized_by_size=1,15,311,387,1 '
          'non_subgroup_by_size=0,12,88,360,0')
    print('complement_counts=' + ','.join(str(comp_total[k]) for k in (1, 2, 4, 8, 16)))


if __name__ == '__main__':
    main()
