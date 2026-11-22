#!/usr/bin/env python3
"""Independent permutation-orbit and set-based observation verification."""
from itertools import combinations, permutations
from collections import Counter, deque
import csv

VERTICES = tuple(frozenset(x) for x in combinations(range(7), 3))
INDEX = {x: i for i, x in enumerate(VERTICES)}
ADJ = tuple(frozenset(j for j, y in enumerate(VERTICES) if x.isdisjoint(y)) for x in VERTICES)
GROUP = tuple(tuple(INDEX[frozenset(p[t] for t in x)] for x in VERTICES)
              for p in permutations(range(7)))

def closure(indices):
    active = set(indices)
    for x in tuple(active): active.update(ADJ[x])
    initial = len(active)
    rounds = 0
    while True:
        forced = set()
        for x in active:
            remaining = ADJ[x] - active
            if len(remaining) == 1: forced.update(remaining)
        if not forced - active:
            return len(active), initial, rounds
        active.update(forced)
        rounds += 1

def classify_orbits(k):
    remainder = set(combinations(range(35), k))
    result = []
    while remainder:
        rep = min(remainder)
        orbit = {tuple(sorted(g[i] for i in rep)) for g in GROUP}
        assert orbit <= remainder
        remainder.difference_update(orbit)
        observed, initial, rounds = closure(rep)
        result.append((rep, len(orbit), observed, initial, rounds))
    return result

def canonical_fans():
    found = set()
    for center in range(7):
        rest = [x for x in range(7) if x != center]
        for p1 in combinations(rest, 2):
            rem1 = [x for x in rest if x not in p1]
            for p2 in combinations(rem1, 2):
                p3 = tuple(x for x in rem1 if x not in p2)
                groups = tuple(sorted((tuple(sorted(p1)), tuple(sorted(p2)), tuple(sorted(p3)))))
                if groups[0] != tuple(sorted(p1)): continue
                for x in groups[0]:
                    for y in groups[1]:
                        for z in groups[2]:
                            terms = [frozenset((center,) + pair) for pair in groups]
                            terms.append(frozenset((x, y, z)))
                            found.add(tuple(sorted(INDEX[t] for t in terms)))
    return found

def main():
    small = classify_orbits(3)
    large = classify_orbits(4)
    assert len(small) == 10 and len(large) == 38
    assert sum(o[1] for o in small) == 6545
    assert sum(o[1] for o in large) == 52360
    assert not any(o[2] == 35 for o in small)
    accepted = [o for o in large if o[2] == 35]
    assert len(accepted) == 1 and accepted[0][1] == 840
    assert accepted[0][3:] == (20, 2)
    target = canonical_fans()
    assert len(target) == 840
    orbit = {tuple(sorted(g[i] for i in accepted[0][0])) for g in GROUP}
    assert target == orbit
    # Every possible neighbor of the representative is checked using set propagation;
    # the permutation action then transports this verified degree profile to all states.
    rep = accepted[0][0]
    nbrs = set()
    slides = set()
    for old in rep:
        for new in range(35):
            if new in rep: continue
            alternate = tuple(sorted((set(rep) - {old}) | {new}))
            if alternate in target:
                nbrs.add(alternate)
                if new in ADJ[old]: slides.add(alternate)
    assert len(nbrs) == 13 and len(slides) == 1
    # Independent shortest-path computation using orbit-defined vertices and set adjacency.
    all_configs = sorted(target)
    pos = {c: i for i, c in enumerate(all_configs)}
    graph = [[] for _ in all_configs]
    for i, s in enumerate(all_configs):
        sset = set(s)
        for old in s:
            for new in range(35):
                if new in sset: continue
                other = tuple(sorted((sset - {old}) | {new}))
                if other in pos: graph[i].append(pos[other])
        assert len(graph[i]) == 13
    start = pos[rep]
    levels = {start: 0}; queue = deque([start])
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if y not in levels:
                levels[y] = levels[x] + 1
                queue.append(y)
    hist = Counter(levels.values())
    assert hist == {0: 1, 1: 13, 2: 39, 3: 87, 4: 204, 5: 320, 6: 176}
    assert len(levels) == 840
    with open('orbit_census.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['k','representative_3_subsets','orbit_size','closure_size','initial_observed','propagation_rounds'])
        for k,group in ((3,small),(4,large)):
            for rep,size,observed,initial,rounds in group:
                writer.writerow([k, ' '.join(''.join(map(str,sorted(VERTICES[i]))) for i in rep), size,observed,initial,rounds])
    print('PASS: 10 triple orbits, none successful; 38 quadruple orbits, exactly one successful')
    print('PASS: 840 distinct central-fan configurations and single symmetry orbit')
    print('PASS: root has 13 jump neighbors and one slide neighbor; symmetry makes degrees global')
    print('PASS: jump distance counts from root', sorted(hist.items()))
    print('PASS: full orbit census written to orbit_census.csv')

if __name__ == '__main__': main()
