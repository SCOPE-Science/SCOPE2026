#!/usr/bin/env python3
"""Exact stdlib verifier for the mod-2 homology of D_{6,3}."""
from itertools import combinations
from hashlib import sha256

N = 6
EDGES = list(combinations(range(N), 2))
M = len(EDGES)
EXPECTED_F = [15, 105, 455, 1185, 1647, 915, 180]
EXPECTED_RANKS = [14, 91, 364, 821, 711, 180]  # d_1,...,d_6
EXPECTED_BETTI = [1, 0, 0, 0, 115, 24, 0]
EXPECTED_EULER = 92
EXPECTED_FACE_DIGEST = "c69ad65ef152dfa4b2ec2a790d2d2bc7290d3aa0ac3a096dd2aac17e7c7f60d7"


def adjacency(mask):
    adj = [0] * N
    for i, (a, b) in enumerate(EDGES):
        if (mask >> i) & 1:
            adj[a] |= 1 << b
            adj[b] |= 1 << a
    return adj


def domination_number(mask):
    adj = adjacency(mask)
    ALL = (1 << N) - 1
    for k in range(1, N + 1):
        for C in combinations(range(N), k):
            covered = 0
            for v in C:
                covered |= (1 << v) | adj[v]
            if covered == ALL:
                return k
    raise AssertionError("domination number not found")


def gamma_at_least_three_direct(mask):
    """Independent implementation: rule out dominating sets of sizes 1 and 2."""
    adj = adjacency(mask)
    ALL = (1 << N) - 1
    closed = [(1 << v) | adj[v] for v in range(N)]
    if any(x == ALL for x in closed):
        return False
    for a, b in combinations(range(N), 2):
        if (closed[a] | closed[b]) == ALL:
            return False
    return True


def rank_mod2(columns):
    """Rank of a binary matrix whose columns are Python integers."""
    pivots = {}
    rank = 0
    for col in columns:
        x = col
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                rank += 1
                break
    return rank


def main():
    # Exhaust all 2^15 labeled graphs; compare two membership implementations.
    in_complex = []
    for mask in range(1 << M):
        by_definition = domination_number(mask) >= 3
        by_pair_test = gamma_at_least_three_direct(mask)
        assert by_definition == by_pair_test
        if mask and by_definition:
            in_complex.append(mask)

    faces = set(in_complex)
    by_dim = {}
    for mask in in_complex:
        d = mask.bit_count() - 1
        by_dim.setdefault(d, []).append(mask)
    f = [len(by_dim.get(d, [])) for d in range(7)]
    assert f == EXPECTED_F, (f, EXPECTED_F)
    assert len(in_complex) == sum(EXPECTED_F) == 4502

    # Downward closure check and canonical digest.
    for mask in in_complex:
        for i in range(M):
            if (mask >> i) & 1:
                sub = mask ^ (1 << i)
                if sub:
                    assert sub in faces
    payload = "\n".join(f"{x:04x}" for x in sorted(in_complex)).encode("ascii") + b"\n"
    assert sha256(payload).hexdigest() == EXPECTED_FACE_DIGEST

    # Boundary ranks over F_2. Each d-simplex has every (d-1)-face because
    # gamma >= 3 is monotone under deleting graph edges.
    indexes = {d: {x: i for i, x in enumerate(by_dim.get(d, []))}
               for d in range(7)}
    ranks = []
    for d in range(1, 7):
        cols = []
        for mask in by_dim[d]:
            col = 0
            for i in range(M):
                if (mask >> i) & 1:
                    sub = mask ^ (1 << i)
                    col ^= 1 << indexes[d - 1][sub]
            cols.append(col)
        ranks.append(rank_mod2(cols))
    assert ranks == EXPECTED_RANKS, (ranks, EXPECTED_RANKS)

    # Direct boundary-of-boundary check over F_2.
    for d in range(2, 7):
        for mask in by_dim[d]:
            second_boundary = set()
            for i in range(M):
                if (mask >> i) & 1:
                    facet = mask ^ (1 << i)
                    for j in range(M):
                        if (facet >> j) & 1:
                            ridge = facet ^ (1 << j)
                            if ridge in second_boundary:
                                second_boundary.remove(ridge)
                            else:
                                second_boundary.add(ridge)
            assert not second_boundary

    betti = []
    for d in range(7):
        rd = 0 if d == 0 else ranks[d - 1]
        rnext = 0 if d == 6 else ranks[d]
        betti.append(f[d] - rd - rnext)
    assert betti == EXPECTED_BETTI, (betti, EXPECTED_BETTI)

    euler = sum(((-1) ** d) * f[d] for d in range(7))
    assert euler == EXPECTED_EULER
    assert 1 + betti[4] - betti[5] == EXPECTED_EULER

    print("vertices_of_complex=15")
    print("nonempty_faces=4502")
    print("f_vector=" + repr(tuple(f)))
    print("boundary_ranks_F2=" + repr(tuple(ranks)))
    print("betti_F2=" + repr(tuple(betti)))
    print("euler_characteristic=92")
    print("face_digest_sha256=" + EXPECTED_FACE_DIGEST)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
