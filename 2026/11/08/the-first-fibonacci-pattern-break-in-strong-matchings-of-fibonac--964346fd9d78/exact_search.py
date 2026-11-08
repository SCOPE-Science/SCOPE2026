"""Exact induced-matching census in Fibonacci cubes, using integer-bitset maximal-clique search.

Run: python exact_search.py
The algorithm visits all branches not eliminated by a certified greedy-color upper bound.
"""
from collections import Counter


def vertices_edges(n):
    vertices = [u for u in range(1 << n) if not (u & (u << 1))]
    vset = set(vertices)
    edges = sorted((u, u ^ (1 << i)) for u in vertices for i in range(n)
                   if u < (u ^ (1 << i)) and (u ^ (1 << i)) in vset)
    return vertices, edges


def compatible_edges(edges):
    n = len(edges)
    # The complement of the conflict graph: pairs can co-occur in an induced matching.
    compatible = []
    for i, (a, b) in enumerate(edges):
        mask = 0
        for j, (c, d) in enumerate(edges):
            if i != j and min((a ^ c).bit_count(), (a ^ d).bit_count(),
                              (b ^ c).bit_count(), (b ^ d).bit_count()) > 1:
                mask |= 1 << j
        compatible.append(mask)
    return compatible


def maximum_induced_matchings(n):
    vertices, edges = vertices_edges(n)
    compat = compatible_edges(edges)
    best = 0
    optima = []
    visited = 0

    def greedy_coloring(bits):
        """Properly color the compatibility graph restricted to bits.

        Each color class is pairwise nonadjacent in the compatibility graph.
        A clique uses at most one member per color, yielding a rigorous bound.
        """
        order, bound = [], []
        color = 0
        while bits:
            color += 1
            available = bits
            while available:
                bit = available & -available
                i = bit.bit_length() - 1
                order.append(i)
                bound.append(color)
                bits ^= bit
                available ^= bit
                available &= ~compat[i]
        return order, bound

    def recurse(candidates, chosen):
        nonlocal best, optima, visited
        visited += 1
        if candidates == 0:
            if len(chosen) > best:
                best = len(chosen)
                optima = []
            if len(chosen) == best:
                optima.append(tuple(sorted(chosen)))
            return
        order, bound = greedy_coloring(candidates)
        for pos in range(len(order)-1, -1, -1):
            # The suffix is exhausted. The remaining prefix has clique number
            # at most bound[pos]; strict inequality preserves tied optima.
            if len(chosen) + bound[pos] < best:
                return
            v = order[pos]
            recurse(candidates & compat[v], chosen + (v,))
            candidates &= ~(1 << v)

    recurse((1 << len(edges)) - 1, ())
    assert len(set(optima)) == len(optima)
    for solution in optima:
        assert len(solution) == best
        for i, a in enumerate(solution):
            for b in solution[i+1:]:
                assert (compat[a] >> b) & 1
    return vertices, edges, best, sorted(optima), visited


def reverse_bits(x, n):
    return int(f'{x:0{n}b}'[::-1], 2)


def reversal_orbits(n, edges, optima):
    lookup = {e: i for i, e in enumerate(edges)}
    def reverse_sol(solution):
        return tuple(sorted(lookup[tuple(sorted((reverse_bits(edges[i][0], n),
                                                  reverse_bits(edges[i][1], n))))]
                            for i in solution))
    seen = set()
    orbits = []
    for sol in optima:
        if sol in seen:
            continue
        orbit = tuple(sorted({sol, reverse_sol(sol)}))
        assert all(e in optima for e in orbit)
        seen.update(orbit)
        orbits.append(orbit)
    assert len(seen) == len(optima)
    return orbits


if __name__ == '__main__':
    for n in range(1, 9):
        V, E, maximum, solutions, nodes = maximum_induced_matchings(n)
        orbits = reversal_orbits(n, E, solutions)
        print(f'n={n} vertices={len(V)} edges={len(E)} maximum={maximum} '
              f'optimal={len(solutions)} reversal_orbits={len(orbits)} nodes={nodes}')
    assert maximum == 12 and len(solutions) == 12 and len(orbits) == 6
