#!/usr/bin/env python3
"""Finite-state verification for all cycle orders >= 11, not a bounded-n guess.
Every eleven-bit window records whether its center is locally minimal-dominating
and whether an expansion/contraction centered there is possible. Frozen cyclic
words correspond exactly to closed walks of the ten-bit de Bruijn automaton.
Run: python verify_structure.py
"""

WINDOW = 11
MASK = (1 << 10) - 1


def local_good(w, center):
    def bit(i):
        return (w >> i) & 1
    if not (bit(center - 1) or bit(center) or bit(center + 1)):
        return False
    if bit(center) and not any(sum(bit(k) for k in (j - 1, j, j + 1)) == 1
                                for j in (center - 1, center, center + 1)):
        return False
    return True


def locally_movable(w):
    center = 5
    left, right = 4, 6
    if (w >> center) & 1:
        candidates = [i for i in (left, right) if not ((w >> i) & 1)]
        for t in range(1, 1 << len(candidates)):
            alt = w ^ (1 << center)
            for j, i in enumerate(candidates):
                if (t >> j) & 1:
                    alt |= 1 << i
            if all(local_good(alt, i) for i in range(2, 9)):
                return True
    else:
        candidates = [i for i in (left, right) if ((w >> i) & 1)]
        for t in range(1, 1 << len(candidates)):
            alt = w | (1 << center)
            for j, i in enumerate(candidates):
                if (t >> j) & 1:
                    alt ^= 1 << i
            if all(local_good(alt, i) for i in range(2, 9)):
                return True
    return False


def components(graph):
    # Tarjan SCC algorithm implemented independently, no external packages.
    index = 0
    indices, low, stack, active, result = {}, {}, [], set(), []
    def dfs(v):
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        active.add(v)
        for u in graph.get(v, ()):
            if u not in indices:
                dfs(u)
                low[v] = min(low[v], low[u])
            elif u in active:
                low[v] = min(low[v], indices[u])
        if low[v] == indices[v]:
            group = []
            while True:
                u = stack.pop()
                active.remove(u)
                group.append(u)
                if u == v:
                    break
            result.append(set(group))
    for v in sorted(graph):
        if v not in indices:
            dfs(v)
    return result


def main():
    # An edge represents an eleven-bit window with a valid center and no
    # possible move at that center. Adjacent windows overlap in ten bits.
    g = {}
    count = 0
    for w in range(1 << WINDOW):
        if local_good(w, 5) and not locally_movable(w):
            a, b = w & MASK, w >> 1
            g.setdefault(a, set()).add(b)
            g.setdefault(b, set())
            count += 1
    recurrent = [s for s in components(g)
                 if len(s) > 1 or any(v in g[v] for v in s)]
    expected = {204, 409, 614, 819}
    assert len(recurrent) == 1 and recurrent[0] == expected, recurrent
    internal_edges = {(v, u) for v in expected for u in g[v] if u in expected}
    assert len(internal_edges) == 4
    assert all(len([u for u in g[v] if u in expected]) == 1 for v in expected)
    print('admissible windows:', count)
    print('unique recurrent SCC:', sorted(expected))
    print('internal cycle edges:', sorted(internal_edges))
    print('PASS: every frozen cyclic word of length >= 11 repeats 1100')


if __name__ == '__main__':
    main()
