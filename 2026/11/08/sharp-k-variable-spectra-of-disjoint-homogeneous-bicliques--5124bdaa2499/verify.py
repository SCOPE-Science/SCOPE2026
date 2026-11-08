#!/usr/bin/env python3
"""Finite corroboration of the width classification for homogeneous biclique unions.

Ordinary first-order k-variable equivalence is computed by non-counting
k-tuple refinement: the extension signature records SETS rather than
multisets of available one-coordinate replacement colours.
This executable checks only the explicitly enumerated finite graphs.
"""
from itertools import product


def biclique_union(n, r, s):
    size = n * (r+s)
    adjacency = [set() for _ in range(size)]
    for c in range(n):
        base = c * (r+s)
        for i in range(r):
            for j in range(s):
                x, y = base+i, base+r+j
                adjacency[x].add(y)
                adjacency[y].add(x)
    return adjacency


def refine(cases, k):
    models = []
    for parameters in cases:
        adj = biclique_union(*parameters)
        size = len(adj)
        states = list(product(range(size), repeat=k))
        lookup = {state: j for j, state in enumerate(states)}
        atomic = [tuple((t[i] == t[j], t[j] in adj[t[i]])
                        for i in range(k) for j in range(i)) for t in states]
        models.append((parameters, size, states, lookup, atomic))
    vocabulary = {a: j for j, a in enumerate(sorted({a for *_, atoms in models for a in atoms}))}
    colors = [[vocabulary[a] for a in atoms] for *_, atoms in models]
    for step in range(30):
        global_colors = {}
        next_colors = []
        for (params, size, states, lookup, atoms), old in zip(models, colors):
            painted = []
            for p, state in enumerate(states):
                profiles = []
                for index in range(k):
                    replacements = []
                    for vertex in range(size):
                        changed = list(state)
                        changed[index] = vertex
                        replacements.append(old[lookup[tuple(changed)]])
                    profiles.append(tuple(sorted(set(replacements))))
                signature = (old[p], tuple(profiles))
                if signature not in global_colors:
                    global_colors[signature] = len(global_colors)
                painted.append(global_colors[signature])
            next_colors.append(painted)
        if next_colors == colors:
            break
        colors = next_colors
    else:
        raise RuntimeError('refinement did not stabilize')
    return step, {m[0]: set(c) for m, c in zip(models, colors)}


def predicted(case, width):
    n, r, s = case
    if width <= 2:
        return ('all',)
    return (min(n,width), tuple(sorted((min(r,width), min(s,width)))))


def check(cases, width):
    steps, theories = refine(cases,width)
    pairs = 0
    for i, a in enumerate(cases):
        for b in cases[i:]:
            actual = bool(theories[a] & theories[b])
            expected = predicted(a,width) == predicted(b,width)
            assert actual == expected, (width,a,b,actual,expected)
            pairs += 1
    groups = {predicted(case,width) for case in cases}
    print(f'width={width} models={len(cases)} pairs={pairs} theories={len(groups)} refinement_rounds={steps} discrepancies=0')


def main():
    cases2 = [(n,r,s) for n in (1,2,3) for r,s in ((2,2),(2,3),(3,3))]
    check(cases2,2)
    cases3 = [(n,r,s) for n in range(1,4) for r in range(2,4) for s in range(r,4)]
    cases3 += [(4,2,2),(4,2,3),(1,2,4),(2,2,4),(3,2,4),(3,4,4),(4,4,4)]
    check(cases3,3)
    cases4 = [(1,2,2),(1,2,3),(1,3,3),(1,2,4),(1,3,4),
              (2,2,2),(2,2,3),(2,3,3),(3,2,2),(4,2,2)]
    check(cases4,4)
    print('FINITE_CORROBORATION_PASS')

if __name__ == '__main__':
    main()
