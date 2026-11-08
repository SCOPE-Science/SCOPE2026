"""Exact verification of the perfect-edge-domination census for open ladders.

Requires Python 3 standard library only.  The 81-state graph and independent
edge-subset enumerator are constructed directly from the definitions.
"""
from itertools import product

WHITE, YELLOW, BLACK = range(3)
COLS = tuple(product(range(3), repeat=2))
NODES = tuple(product(COLS, repeat=2))


def condition(color, neighbor_colors):
    if color == WHITE:
        return all(c == YELLOW for c in neighbor_colors)
    if color == YELLOW:
        return sum(c != WHITE for c in neighbor_colors) == 1
    return all(c != WHITE for c in neighbor_colors)


def left_endpoint(a, b):
    return all(condition(a[r], (a[1-r], b[r])) for r in range(2))


def right_endpoint(a, b):
    return all(condition(b[r], (a[r], b[1-r])) for r in range(2))


def middle(a, b, c):
    return all(condition(b[r], (a[r], b[1-r], c[r])) for r in range(2))


def reach(seeds, neighbors):
    visited = set(seeds)
    todo = list(seeds)
    while todo:
        for p in neighbors[todo.pop()]:
            if p not in visited:
                visited.add(p)
                todo.append(p)
    return visited


def edges(n):
    return ([(2*i, 2*i+1) for i in range(n)] +
            [(2*i+r, 2*(i+1)+r) for i in range(n-1) for r in (0, 1)])


def edge_set_from_colors(colors):
    # Every selected edge has both endpoints nonwhite; all others are omitted.
    n = len(colors)
    return frozenset(e for e in edges(n)
                     if all(colors[v//2][v%2] != WHITE for v in e))


def check_ped(n, chosen):
    all_edges = edges(n)
    chosen = set(chosen)
    return all(e in chosen or sum(len(set(e) & set(f)) > 0 for f in chosen) == 1
               for e in all_edges)


def brute_polynomial(n):
    es = edges(n)
    adj = [sum(1 << j for j, f in enumerate(es)
               if j != i and (e[0] in f or e[1] in f))
           for i, e in enumerate(es)]
    d = {}
    for s in range(1 << len(es)):
        if all((s & (1 << i)) or (s & adj[i]).bit_count() == 1
               for i in range(len(es))):
            k = s.bit_count()
            d[k] = d.get(k, 0) + 1
    return d


def edge_weight(colors):
    return len(edge_set_from_colors(colors))


def main():
    forward = {p: [(p[1], c) for c in COLS if middle(p[0], p[1], c)]
               for p in NODES}
    reverse = {p: [] for p in NODES}
    for p in NODES:
        for q in forward[p]:
            reverse[q].append(p)
    initials = {p for p in NODES if left_endpoint(*p)}
    finals = {p for p in NODES if right_endpoint(*p)}
    accessible = reach(initials, forward)
    coaccessible = reach(finals, reverse)
    live = accessible & coaccessible
    assert len(NODES) == 81
    assert (len(initials), len(finals), len(accessible), len(coaccessible), len(live)) == (13, 13, 15, 15, 7)

    W, Y, B = WHITE, YELLOW, BLACK
    cycle = [((W,Y),(Y,B)), ((Y,B),(W,Y)), ((W,Y),(Y,W)),
             ((Y,W),(B,Y)), ((B,Y),(Y,W)), ((Y,W),(W,Y))]
    bb = ((B,B),(B,B))
    assert live == set(cycle) | {bb}
    for i, p in enumerate(cycle):
        assert [q for q in forward[p] if q in live] == [cycle[(i+1)%6]]
    assert [q for q in forward[bb] if q in live] == [bb]
    assert {i for i, p in enumerate(cycle) if p in initials} == {0,1,3,4}
    assert {i for i, p in enumerate(cycle) if p in finals} == {0,1,3,4}
    assert bb in initials and bb in finals
    print('EXACT_81_STATE_TRIM_CERTIFICATE_OK active=7 six_cycle=6 trivial_loop=1')

    # A complete nontrivial trajectory of n columns is uniquely determined
    # by a permitted starting pair on the six-cycle and n-2 transitions.
    for n in range(2, 130):
        candidates = []
        for i in (0,1,3,4):
            if cycle[(i+n-2)%6] not in finals:
                continue
            colors = (cycle[i][0], cycle[i][1])
            for j in range(n-2):
                colors += (cycle[(i+j+1)%6][1],)
            assert len(colors) == n
            chosen = edge_set_from_colors(colors)
            assert len(chosen) == n
            assert check_ped(n, chosen)
            candidates.append(chosen)
        assert len(set(candidates)) == len(candidates)
        assert len(candidates) == (4 if n%3 == 2 else 2)
        # Full set is the seventh recurrent state and its weight is 3n-2.
        assert len(edges(n)) == 3*n-2
    print('PERIOD_SIX_ALL_PARAMETERS_REDUCED_TO_SIX_STATE_CYCLE_OK n=2..129')

    # The six-step weight shift is an exact identity for each cyclic phase:
    # all edges added by a six-column extension are counted locally.
    for i in (0,1,3,4):
        for n in range(2,8):
            old = (cycle[i][0],cycle[i][1])
            for j in range(n-2): old += (cycle[(i+j+1)%6][1],)
            new = (cycle[i][0],cycle[i][1])
            for j in range(n+4): new += (cycle[(i+j+1)%6][1],)
            assert edge_weight(new)-edge_weight(old) == 6
    print('SIX_COLUMN_WEIGHT_INCREMENT_IDENTITY_OK')

    for n in range(2,8):
        expected = {n: (4 if n%3 == 2 else 2),3*n-2:1}
        assert brute_polynomial(n) == expected, (n,brute_polynomial(n),expected)
    print('INDEPENDENT_EXHAUSTIVE_EDGE_SUBSETS_OK n=2..7')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
