#!/usr/bin/env python3
"""Exact finite certificate for a period-gap theorem in three-colour threshold CA.

Uses the Python standard library only. No random sampling, numerical tolerance,
network access, or auxiliary data. The proof in RESULT.md explains why the
finite signature compatibility graphs are exhaustive for periods <= 8.
"""
from itertools import combinations, product


def c_event(a, ua, b, ub, p):
    """Total oriented successor exposures at advances along one edge."""
    x, y, out = a, b, 0
    for t in range(p):
        dx, dy = (ua >> t) & 1, (ub >> t) & 1
        out += dx * (y == (x + 1) % 3) + dy * (x == (y + 1) % 3)
        x = (x + dx) % 3
        y = (y + dy) % 3
    return out


def local_edge_inequality():
    total, strict = 0, 0
    for a, b, du, dv in product(range(3), range(3), (0, 1), (0, 1)):
        a1, b1 = (a + du) % 3, (b + dv) % 3
        c = du * (b == (a + 1) % 3) + dv * (a == (b + 1) % 3)
        slack = du + dv + (a != b) - (a1 != b1) - 2 * c
        assert slack >= 0, (a, b, du, dv)
        strict += slack > 0
        total += 1
    assert total == 36 and strict == 9
    return total, strict


def first_four_clique(adj):
    """Detect a 4-clique exactly, with a bitset adjacency matrix."""
    for a, bits in enumerate(adj):
        b_candidates = bits & ~((1 << (a + 1)) - 1)
        while b_candidates:
            lb = b_candidates & -b_candidates
            b = lb.bit_length() - 1
            b_candidates ^= lb
            common = (adj[a] & adj[b]) & ~((1 << (b + 1)) - 1)
            c_candidates = common
            while c_candidates:
                lc = c_candidates & -c_candidates
                c = lc.bit_length() - 1
                c_candidates ^= lc
                d_candidates = common & adj[c] & ~((1 << (c + 1)) - 1)
                if d_candidates:
                    d = (d_candidates & -d_candidates).bit_length() - 1
                    return (a, b, c, d)
    return None


def check(p, changes):
    times = range(p)
    sig = [(color, sum(1 << i for i in subset))
           for color in range(3) for subset in combinations(times, changes)]
    n = len(sig)
    adj = [0] * n
    count = 0
    for i in range(n):
        a, ua = sig[i]
        assert c_event(a, ua, a, ua, p) == 0
        for j in range(i):
            b, ub = sig[j]
            if c_event(a, ua, b, ub, p) == changes:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
                count += 1
    witness = first_four_clique(adj)
    return n, count, witness


def main():
    total, strict = local_edge_inequality()
    expected = {
        (3, 3): (3, 3),
        (4, 3): (12, 24),
        (5, 3): (30, 120),
        (6, 3): (60, 444),
        (6, 6): (3, 3),
        (7, 3): (105, 1323),
        (7, 6): (21, 42),
        (8, 3): (168, 3360),
        (8, 6): (84, 372),
    }
    cases = 0
    for p in range(3, 9):
        for s in range(3, p + 1, 3):
            n, edges, witness = check(p, s)
            assert (n, edges) == expected[p, s], (p, s, n, edges)
            assert witness is None, (p, s, witness)
            print('p=%d changes=%d signatures=%d compatible_pairs=%d K4=absent'
                  % (p, s, n, edges))
            cases += 1
    assert cases == 9
    n, edges, witness = check(9, 3)
    assert (n, edges) == (252, 7560) and witness is not None
    print('p=9 changes=3 signatures=%d compatible_pairs=%d K4=present' % (n, edges))
    print('VERIFY_OK local_cases=%d strict_cases=%d ruled_out_signature_graphs=%d'
          % (total, strict, cases))


if __name__ == '__main__':
    main()
