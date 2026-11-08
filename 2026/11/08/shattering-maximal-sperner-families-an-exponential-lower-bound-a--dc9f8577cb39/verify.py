#!/usr/bin/env python3
"""Complete finite checks for maximal antichain membership classes of Boolean lattices."""
from itertools import permutations
from collections import Counter
import json
from pathlib import Path


def maximal_antichains(n):
    nsets = 1 << n
    incomparables = [0] * nsets
    for x in range(nsets):
        for y in range(nsets):
            if x != y and (x & y) != x and (x & y) != y:
                incomparables[x] |= 1 << y
    # Maximal cliques of the incomparability graph, without external libraries.
    found = []
    def visit(r, p, x):
        if not p and not x:
            found.append(r)
            return
        united = p | x
        pivot = None
        best = -1
        while united:
            vbit = united & -united
            v = vbit.bit_length() - 1
            united ^= vbit
            score = (p & incomparables[v]).bit_count()
            if score > best:
                best, pivot = score, v
        choices = p & ~incomparables[pivot] if pivot is not None else p
        while choices:
            vb = choices & -choices
            v = vb.bit_length() - 1
            choices ^= vb
            visit(r | vb, p & incomparables[v], x & incomparables[v])
            p ^= vb
            x |= vb
    visit(0, (1 << nsets) - 1, 0)
    assert len(found) == len(set(found))
    for c in found:
        members = [x for x in range(nsets) if (c >> x) & 1]
        for x in members:
            assert c & ~((1 << x) | incomparables[x]) == 0
        for y in range(nsets):
            if not (c >> y & 1):
                assert any((x & y) == x or (x & y) == y for x in members)
    return found, incomparables


def shattering_levels(n, concepts, incomparables):
    nsets = 1 << n
    active = (1 << len(concepts)) - 1
    member = [sum(1 << i for i, c in enumerate(concepts) if c >> x & 1)
              for x in range(nsets)]
    next_larger_incomparable = [sum(1 << y for y in range(x + 1, nsets)
                                     if (incomparables[x] >> y) & 1)
                                for x in range(nsets)]
    levels = []
    candidates = [((), (active,), (1 << nsets) - 1)]
    for k in range(nsets + 1):
        levels.append([t[0] for t in candidates])
        grown = []
        for support, trace_classes, available in candidates:
            remaining = available
            while remaining:
                vb = remaining & -remaining
                x = vb.bit_length() - 1
                remaining ^= vb
                positive_mask = member[x]
                new_traces = []
                for group in trace_classes:
                    yes = group & positive_mask
                    no = group ^ yes
                    if not yes or not no:
                        break
                    new_traces.extend((no, yes))
                else:
                    grown.append((support + (x,), tuple(new_traces),
                                  available & next_larger_incomparable[x]))
        candidates = grown
        if not candidates:
            levels.append([])
            break
    return levels


def orbits(n, supports):
    transforms = []
    for permutation in permutations(range(n)):
        transforms.append([sum((1 << permutation[i]) for i in range(n) if x & (1 << i))
                           for x in range(1 << n)])
    hist = Counter()
    for s in supports:
        canonical = min(tuple(sorted(t[x] for x in s)) for t in transforms)
        hist[canonical] += 1
    return hist


def main():
    expected_concepts = {1: 2, 2: 3, 3: 7, 4: 29, 5: 376}
    expected_levels = {
        1: [1, 2, 0],
        2: [1, 4, 0],
        3: [1, 8, 9, 0],
        4: [1, 16, 55, 52, 0],
        5: [1, 32, 285, 1090, 1780, 1224, 310, 0]
    }
    for n in range(1, 6):
        concepts, inc = maximal_antichains(n)
        levels = shattering_levels(n, concepts, inc)
        counts = [len(level) for level in levels]
        assert len(concepts) == expected_concepts[n], (n, len(concepts))
        assert counts == expected_levels[n], (n, counts)
        print('n=%d concepts=%d shattered_by_size=%s' % (n, len(concepts), counts))
        if n == 5:
            orb = orbits(n, levels[6])
            assert len(orb) == 11 and sum(orb.values()) == 310
            assert sorted(orb.values()) == [5, 5, 10, 15, 15, 20, 30, 30, 60, 60, 60]
            orbit_file = Path(__file__).with_name('ORBIT_CLASSES.json')
            archived = json.loads(orbit_file.read_text(encoding='utf-8'))
            actual_rows = [{'support_bitmasks': list(rep), 'orbit_size': count}
                           for rep, count in sorted(orb.items())]
            assert archived['n'] == 5 and archived['support_size'] == 6
            assert archived['total_shattered_supports'] == 310
            assert archived['orbit_count'] == 11
            assert archived['orbits'] == actual_rows
            print('n=5 six-support orbits=%d orbit_sizes=%s' %
                  (len(orb), sorted(orb.values())))
            print('star_support=', [7,11,13,19,21,25],
                  'shattered=', (7,11,13,19,21,25) in levels[6])
    print('BOOLEAN_MAXIMAL_ANTICHAIN_SHATTERING_PASS')


if __name__ == '__main__':
    main()
