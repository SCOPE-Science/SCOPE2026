#!/usr/bin/env python3
"""Exact exhaustive verifier of a binary restricted-overlap code bound.

Python 3 standard library only. All branches are finite; no MILP solver,
randomness, network or external certificates.
"""

def overlap(prefix, suffix, k):
    """Whether some t in {1,...,k} has matching prefix/suffix."""
    for t in range(1, k + 1):
        if (prefix >> (k - t)) == (suffix & ((1 << t) - 1)):
            return True
    return False


def bipartite_masks(k):
    """Normalize first prefix bit 0 and last suffix bit 1."""
    h = 1 << (k - 1)
    prefixes = list(range(h))
    suffixes = list(range(1, 2 * h, 2))
    forward = []
    for p in prefixes:
        forward.append(sum((not overlap(p, s, k)) << j
                           for j, s in enumerate(suffixes)))
    backward = []
    for j, s in enumerate(suffixes):
        backward.append(sum(((forward[i] >> j) & 1) << i
                            for i in range(h)))
    return prefixes, suffixes, forward, backward


def exact_max_product(masks):
    """Complete include/exclude search with proved upper bounds and dominance.

    At recursion state (i,c,B), c chosen vertices from the first i,
    and B contains exactly the compatible opposite vertices. All unchosen
    vertices may be excluded. Every completion has product <=
    (c + M-i)*popcount(B). At the same (i,B), a state with smaller c
    is dominated by a previously explored state with larger c.
    """
    M = len(masks)
    order = sorted(range(M), key=lambda j: (masks[j].bit_count(), j))
    arranged = [masks[j] for j in order]
    seen = {}
    visited = 0
    best = 0
    witness = ()

    def recurse(i, c, possible, chosen):
        nonlocal best, visited, witness
        visited += 1
        count = possible.bit_count()
        if c * count > best:
            best, witness = c * count, chosen
        if i == M or (c + M - i) * count <= best:
            return
        key = i, possible
        if seen.get(key, -1) >= c:
            return
        seen[key] = c
        added = possible & arranged[i]
        if added:
            recurse(i + 1, c + 1, added, chosen + (order[i],))
        recurse(i + 1, c, possible, chosen)

    recurse(0, 0, (1 << M) - 1, ())
    return best, visited, len(seen), witness


def direct_small(k, masks):
    M = len(masks)
    result = 0
    for bits in range(1 << M):
        allowed = (1 << M) - 1
        for i in range(M):
            if (bits >> i) & 1:
                allowed &= masks[i]
        result = max(result, bits.bit_count() * allowed.bit_count())
    return result


def main():
    expected = [1, 2, 6, 20, 64, 216, 744]
    for k in range(1, 8):
        p, s, forward, backward = bipartite_masks(k)
        r1, n1, d1, w1 = exact_max_product(forward)
        r2, n2, d2, w2 = exact_max_product(backward)
        assert r1 == r2 == expected[k-1], (k, r1, r2)
        if k <= 4:
            assert direct_small(k, forward) == r1
        print('k=%d, optimum=%d, forward_nodes=%d, reverse_nodes=%d,'
              ' forward_memo=%d, reverse_memo=%d'
              % (k, r1, n1, n2, d1, d2))

    k = 7
    p, s, forward, backward = bipartite_masks(k)
    P = list(range(24))
    allowed = (1 << 64) - 1
    for pi in P:
        allowed &= forward[pi]
    S = [s[j] for j in range(64) if (allowed >> j) & 1]
    assert len(P) == 24 and len(S) == 31 and len(P)*len(S) == 744
    assert all(not overlap(pi, sj, k) for pi in P for sj in S)
    # Independently verify against the explicit string overlap definition.
    assert all(not any(format(pi, '07b')[:t] == format(sj, '07b')[-t:]
                       for t in range(1, 8)) for pi in P for sj in S)
    print('explicit_lower_witness_P=', ','.join(format(x, '07b') for x in P))
    print('explicit_lower_witness_S=', ','.join(format(x, '07b') for x in S))
    print('PASS: exact maximum 744 for (1,7)-overlap-free binary codes'
          ' of every blocklength n >= 14, with factor 2^(n-14).')

if __name__ == '__main__':
    main()
