#!/usr/bin/env python3
"""Independent finite exact checks for face-flip sectors of truncated prisms.
Public reproducibility script; only Python standard library is needed.
"""
from collections import Counter
from itertools import product


def configurations(n):
    return [(a, d) for a in range(1 << n) for d in (0, 1)]


def bits(a, n):
    return [(a >> i) & 1 for i in range(n)]


def transitions(n, a, d):
    x = bits(a, n)
    out = set()
    if d == 0:
        for i in range(n):
            if x[(i - 1) % n] == 1 and x[(i + 1) % n] == 1:
                out.add((a ^ (1 << i), d))
    if a in (0, (1 << n) - 1):
        # Upper rim: toggle all a bits and d; lower rim: only toggle d.
        out.add((a ^ ((1 << n) - 1), d ^ 1))
        out.add((a, d ^ 1))
    return out


def zero_core(n, a):
    x = bits(a, n)
    return frozenset(i for i in range(n) if not x[i] and
                     (not x[(i - 1) % n] or not x[(i + 1) % n]))


def components(n):
    universe = set(configurations(n))
    adj = {s: transitions(n, *s) for s in universe}
    assert all(s in adj[t] for s in universe for t in adj[s])
    groups = []
    while universe:
        seed = universe.pop()
        todo = [seed]
        comp = {seed}
        while todo:
            for t in adj[todo.pop()]:
                if t in universe:
                    universe.remove(t)
                    comp.add(t)
                    todo.append(t)
        groups.append(comp)
    return adj, groups


def predicted_parts(n):
    universe = set(range(n))
    core_sets = []
    for bmask in range(1 << n):
        B = frozenset(i for i in range(n) if bmask >> i & 1)
        if all(((i - 1) % n in B or (i + 1) % n in B) for i in B):
            core_sets.append(B)
    expected = []
    full = (1 << n) - 1
    giant = {(a, 0) for a in range(1 << n) if not zero_core(n, a)}
    giant |= {(0, 0), (0, 1), (full, 1)}
    expected.append(giant)
    for B in core_sets:
        if not B or len(B) == n:
            continue
        comp = {(a, 0) for a in range(1 << n) if zero_core(n, a) == B}
        assert comp
        # Every mobile zero is outside B and its external neighbor set.
        F = universe - B - {i % n for b in B for i in (b - 1, b + 1)}
        independent = 0
        for subset in range(1 << len(F)):
            S = {i for j, i in enumerate(sorted(F)) if subset >> j & 1}
            if all((i + 1) % n not in S for i in S):
                independent += 1
        assert len(comp) == independent
        expected.append(comp)
    expected.extend([{(a, 1)} for a in range(1 << n) if a not in (0, full)])
    assert sum(map(len, expected)) == 2 ** (n + 1)
    return expected, len(core_sets)


def lucas(n):
    return sum(all(not (a >> i & 1 and a >> ((i + 1) % n) & 1)
                   for i in range(n)) for a in range(1 << n))


def main():
    previous_B = {}
    for n in range(3, 12):
        adj, groups = components(n)
        predicted, B = predicted_parts(n)
        sig = {frozenset(C) for C in groups}
        assert sig == {frozenset(C) for C in predicted}, n
        assert len(groups) == 2 ** n + B - 3
        assert max(map(len, groups)) == lucas(n) + 3
        frozen = sum(len(adj[s]) == 0 for s in adj)
        prediction = 2 ** n - 3 + (lucas(n) if n & 1 else lucas(n // 2)**2)
        assert frozen == prediction
        previous_B[n] = B
        if n >= 6:
            assert B == 2*previous_B[n-1] - previous_B[n-2] + previous_B[n-3]
        print(f'n={n:2d} coverings={2**(n+1):5d} cores={B:4d} '
              f'components={len(groups):5d} largest={max(map(len, groups)):4d} '
              f'frozen={frozen:5d} '
              f'flip_edges={sum(map(len, adj.values()))//2:5d}')
    print('PASS: complete component identities and recurrence values')


if __name__ == '__main__':
    main()
