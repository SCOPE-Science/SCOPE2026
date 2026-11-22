"""Independent exact enumeration of Euclidean vertex-chord shells.

The polytope is the type-C Gale interval [emptyset, {2,4,...,2r}]
in unscaled 0/1 coordinates. No external packages are required.
"""
from collections import Counter
from math import comb


def vertices(r):
    n = 2*r
    top = set(range(2, n+1, 2))
    result = []
    for mask in range(1 << n):
        if all(sum((mask >> (j-1)) & 1 for j in range(i, n+1))
               <= sum(j >= i for j in top) for i in range(1, n+1)):
            result.append(mask)
    return result


def pair_walk_shell_counts(r):
    """Independent dynamic enumeration of pairs of suffix-barrier walks."""
    n = 2*r
    # (height_x, height_y, Hamming distance) -> number of ordered pairs
    states = {(0, 0, 0): 1}
    for t in range(n):
        new = {}
        for (h, k, dist), ways in states.items():
            for step_x in (-1, 1):
                for step_y in (-1, 1):
                    nh, nk = h + step_x, k + step_y
                    if nh < -1 or nk < -1:
                        continue
                    nd = dist + (step_x != step_y)
                    if nd < n - 1 - (n - t - 1):
                        continue  # cannot reach either of the two top shells
                    key = (nh, nk, nd)
                    new[key] = new.get(key, 0) + ways
        states = new
    full = sum(v for (h, k, d), v in states.items() if d == n)
    near = sum(v for (h, k, d), v in states.items() if d == n - 1)
    return full // 2, near // 2


def verify():
    pairs = 0
    for r in range(1, 7):
        n = 2*r
        vs = vertices(r)
        assert len(vs) == comb(2*r+1,r), (r, len(vs))
        shell = Counter()
        incidence = Counter()
        for i, x in enumerate(vs):
            for y in vs[i+1:]:
                distance_squared = (x ^ y).bit_count()
                shell[distance_squared] += 1
                if distance_squared == n:
                    incidence[x] += 1
                    incidence[y] += 1
                pairs += 1
        assert max(shell) == n
        assert shell[n] == 2**(r-1), (r, 'diametral', shell[n])
        assert shell[n-1] == 2*(3**r-2**r), (r, 'penultimate', shell[n-1])
        assert len(incidence) == 2**r
        assert set(incidence.values()) == {1}
        print('r=%d vertices=%d diameter_pairs=%d near_pairs=%d' %
              (r,len(vs),shell[n],shell[n-1]))
    for r in range(1, 16):
        full, near = pair_walk_shell_counts(r)
        assert full == 2**(r-1), (r, full)
        assert near == 2*(3**r-2**r), (r, near)
    print('ALTERNATING_GALE_TOP_SHELL_PASS brute_r=1..6 walk_dp_r=1..15 unordered_pairs=%d' % pairs)


if __name__ == '__main__':
    verify()
