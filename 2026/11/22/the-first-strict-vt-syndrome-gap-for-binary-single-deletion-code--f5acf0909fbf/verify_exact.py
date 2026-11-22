"""Exact finite verification of maximum-run-two single-deletion codes.

Runs with Python 3 (standard library only). The branching algorithm searches
cliques in the compatibility graph, using greedy proper colorings for sound
upper bounds. No numerical solver or precomputed graph is needed.
"""
from itertools import product


def permitted(n):
    return [''.join(bits) for bits in product('01', repeat=n)
            if all(bits[i] != bits[i+1] or bits[i+1] != bits[i+2]
                   for i in range(n-2))]


def deletions(word):
    return frozenset(word[:i] + word[i+1:] for i in range(len(word)))


def maximum_clique(adj):
    """An exact branch-and-bound maximum clique on bitset adjacency masks."""
    best = []
    nodes = 0

    def color_order(mask):
        # Proper greedy colors of the induced *compatibility* graph.
        # Each color is an independent set, so a clique has <= colors.
        order, colors, c = [], [], 0
        while mask:
            c += 1
            available = mask
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                colors.append(c)
                mask ^= bit
                available ^= bit
                available &= ~adj[v]
        return order, colors

    def recurse(mask, chosen):
        nonlocal nodes, best
        nodes += 1
        if not mask:
            if len(chosen) > len(best):
                best = chosen[:]
            return
        if len(chosen) + mask.bit_count() <= len(best):
            return
        order, colors = color_order(mask)
        for j in range(len(order)-1, -1, -1):
            if len(chosen) + colors[j] <= len(best):
                break
            v = order[j]
            recurse(mask & adj[v], chosen + [v])
            mask &= ~(1 << v)

    recurse((1 << len(adj)) - 1, [])
    return best, nodes


def verify():
    predicted = [1, 2, 2, 3, 3, 6, 6, 10, 13]
    for n, expected in enumerate(predicted, 1):
        words = permitted(n)
        balls = [deletions(word) for word in words]
        adj = [sum(1 << j for j in range(len(words))
                   if i != j and balls[i].isdisjoint(balls[j]))
               for i in range(len(words))]
        selected, branches = maximum_clique(adj)
        answer = len(selected)
        assert answer == expected, (n, answer, expected)
        chosen = [words[i] for i in selected]
        for a in range(len(chosen)):
            for b in range(a+1, len(chosen)):
                assert deletions(chosen[a]).isdisjoint(deletions(chosen[b]))
        hist = [sum(1 for word in words if sum((i+1) * int(c)
                    for i, c in enumerate(word)) % (n+1) == r)
                for r in range(n+1)]
        assert max(hist) == expected if n < 9 else max(hist) == 12
        print('n={} source={} optimum={} largest_VT_intersection={} nodes={}'.format(
              n, len(words), answer, max(hist), branches))
        if n == 9:
            print('length_nine_witness=' + ','.join(sorted(chosen)))
    print('PASS: optimum 13 at length nine; first strict gap from VT intersections')


if __name__ == '__main__':
    verify()
