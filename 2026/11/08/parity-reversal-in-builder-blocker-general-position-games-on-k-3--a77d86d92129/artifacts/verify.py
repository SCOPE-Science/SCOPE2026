"""Exact finite checks for Builder–Blocker general-position games on 3-by-n rook graphs.

Pure standard Python; legality comes from shortest-path distances, not a star-forest formula.
"""
from functools import lru_cache


def verify(n):
    m = 3
    v = m * n
    def d(x, y):
        if x == y:
            return 0
        return 1 if x // n == y // n or x % n == y % n else 2

    blockers = [[] for _ in range(v)]
    bad_triples = 0
    for a in range(v):
        for b in range(a + 1, v):
            for c in range(b + 1, v):
                if d(a, b) + d(b, c) == d(a, c) or d(a, c) + d(c, b) == d(a, b) or d(b, a) + d(a, c) == d(b, c):
                    bad_triples += 1
                    blockers[a].append((1 << b) | (1 << c))
                    blockers[b].append((1 << a) | (1 << c))
                    blockers[c].append((1 << a) | (1 << b))

    @lru_cache(None)
    def legal_additions(mask):
        out = []
        for x in range(v):
            if mask >> x & 1:
                continue
            if not any(mask & q == q for q in blockers[x]):
                out.append(x)
        return tuple(out)

    @lru_cache(None)
    def solve(mask, builder):
        options = legal_additions(mask)
        if not options:
            return mask.bit_count()
        outcomes = [solve(mask | (1 << x), not builder) for x in options]
        return max(outcomes) if builder else min(outcomes)

    builder_first = solve(0, True)
    blocker_first = solve(0, False)
    assert builder_first == n + (n % 2), (n, builder_first)
    assert blocker_first == n + (1 - n % 2), (n, blocker_first)
    # Verify directly that two cells in one row are a strategically optimal reply,
    # for either player, against every first cell.
    for first in range(v):
        same_row = [x for x in range(v) if x != first and x // n == first // n]
        for wants_builder in (False, True):
            outcomes = [solve((1 << first) | (1 << x), not wants_builder) for x in same_row]
            first_turn = wants_builder
            required = solve(1 << first, first_turn)
            assert all(q == required for q in outcomes), (n, first, wants_builder, outcomes, required)
    return n, bad_triples, builder_first, blocker_first, solve.cache_info().currsize, legal_additions.cache_info().currsize


if __name__ == '__main__':
    total = 0
    for n in range(3, 9):
        out = verify(n)
        total += out[4]
        print('GRAPH_OK n=%d forbidden_triples=%d B=%d Bprime=%d solved_states=%d legality_states=%d' % out)
    print('VERIFY_OK graph_orders=3..8 independent_distance_triples=PASS adversarial_minimax=PASS same_row_best_reply=PASS solved_states=%d' % total)
