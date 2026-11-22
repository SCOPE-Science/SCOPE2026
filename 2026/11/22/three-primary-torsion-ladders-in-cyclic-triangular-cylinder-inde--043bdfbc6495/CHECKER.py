#!/usr/bin/env python3
"""Direct exact finite simplicial-orbit and boundary-rank checks.

For m=4,...,9, build faces of Ind(P_m square C_3) and identify them
under simultaneous cyclic color shifts. All matrices use the integral
oriented simplicial quotient boundary, then are reduced modulo primes.
This finite checker corroborates, but does not prove, the infinite result.
"""
from collections import defaultdict
from hashlib import sha256


def orbit_rep(face):
    return min(tuple(3*(v // 3) + ((v % 3 + t) % 3) for v in face) for t in range(3))


def face_orbits(m):
    faces = [()]
    for row in range(m):
        nxt = faces[:]
        for f in faces:
            for color in range(3):
                if row == 0 or (3 * (row - 1) + color) not in f:
                    nxt.append(f + (3 * row + color,))
        faces = nxt
    orbs = [set() for _ in range(m)]
    for f in faces:
        if not f:
            continue
        assert len({orbit_rep(f), tuple(f)}) >= 1
        assert all(tuple(3 * (v // 3) + ((v % 3 + t) % 3) for v in f) != f
                   for t in (1, 2)), 'unexpected setwise fixed face'
        orbs[len(f) - 1].add(orbit_rep(f))
    assert sum(len(x) for x in orbs) * 3 == len(faces) - 1
    return [sorted(x) for x in orbs]


def boundaries(orbs):
    out = []
    for dim in range(1, len(orbs)):
        index = {f: j for j, f in enumerate(orbs[dim - 1])}
        cols = []
        for f in orbs[dim]:
            co = defaultdict(int)
            for j in range(dim + 1):
                co[index[orbit_rep(f[:j] + f[j+1:])]] += (-1)**j
            cols.append({k: v for k, v in co.items() if v})
        out.append(cols)
    return out


def rank_mod(columns, prime):
    pivots = {}
    for col in columns:
        x = {j: v % prime for j, v in col.items() if v % prime}
        while x:
            j = max(x)
            if j not in pivots:
                inv = pow(x[j], -1, prime)
                pivots[j] = {k: (v * inv) % prime for k, v in x.items()}
                break
            scalar = x[j]
            for k, v in pivots[j].items():
                x[k] = (x.get(k, 0) - scalar * v) % prime
                if not x[k]:
                    del x[k]
    return len(pivots)


def expected_betti(m, prime):
    if m % 3 == 0:
        d = 2 * (m // 3) - 1
    elif m % 3 == 1:
        d = 2 * (m // 3)
    else:
        d = 2 * (m // 3) + 1
    # All non-zero integral reduced H are 3-torsion in odd degrees < d
    # and an additional top Z at d when d is odd.
    ans = [0] * m
    if d & 1:
        ans[d] = 1
    if prime == 3:
        for j in range(1, d, 2):
            ans[j] += 1
            ans[j+1] += 1  # Tor from H_j into F_3-homology at j+1
    return ans


def square_zero(lower, upper):
    for col in upper:
        combined = defaultdict(int)
        for row, a in col.items():
            for j, b in lower[row].items():
                combined[j] += a * b
        assert all(v == 0 for v in combined.values()), 'd^2 != 0'


def main():
    print('Cyclic color orbit-chain exact checker; ordinary simplicial quotient')
    print('All arithmetic is integer or modulo a specified prime')
    for m in range(4, 10):
        orbs = face_orbits(m)
        mats = boundaries(orbs)
        for lower, upper in zip(mats, mats[1:]):
            square_zero(lower, upper)
        ranks = {p: [rank_mod(mat, p) for mat in mats] for p in (2, 3, 5)}
        observed = {p: [len(orbs[d]) - (ranks[p][d-1] if d else 1) -
                        (ranks[p][d] if d < len(mats) else 0)
                        for d in range(m)] for p in ranks}
        for p, b in observed.items():
            assert b == expected_betti(m, p), (m, p, b, expected_betti(m, p))
        print('m=%d orbits=%s mod3_betti=%s mod2+5=PASS d2=PASS' %
              (m, [len(x) for x in orbs], observed[3]), flush=True)
    print('ALL_CHECKS_PASS m=4..9: free simplex orbits, integer d^2=0, finite field ranks')


if __name__ == '__main__':
    main()
