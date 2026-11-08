#!/usr/bin/env python3
"""Complete certificate checker for minimum closed-neighborhood identifying codes of the Fano incidence graph."""
from pathlib import Path
from itertools import combinations
from collections import Counter, deque

BASE = Path(__file__).resolve().parent
V = tuple(range(14))
point = range(7)
lines = range(7, 14)
edge_set = {frozenset((i, 7 + j)) for i in point for j in range(7)
            if (i - j) % 7 in (0, 1, 3)}
adj = {v: set() for v in V}
for pair in edge_set:
    a, b = tuple(pair)
    adj[a].add(b)
    adj[b].add(a)
closed = {v: adj[v] | {v} for v in V}


def identifies(s):
    signatures = [frozenset(closed[v].intersection(s)) for v in V]
    return all(signatures) and len(set(signatures)) == len(V)


def mask(s):
    return sum(1 << v for v in s)


def enumerate_codes():
    counts = {}
    codes = []
    for r in range(8):
        collection = [mask(s) for s in combinations(V, r) if identifies(set(s))]
        counts[r] = len(collection)
        if r == 7:
            codes = sorted(collection)
    return counts, codes


def graph_pairs(codes):
    jumps, slides = [], []
    for a, b in combinations(codes, 2):
        diff = a ^ b
        if diff.bit_count() != 2:
            continue
        jumps.append((a, b))
        changed = frozenset(i for i in V if (diff >> i) & 1)
        if changed in edge_set:
            slides.append((a, b))
    return jumps, slides


def graph_stats(codes, edges):
    neighbors = {a: set() for a in codes}
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    comps = []
    unseen = set(codes)
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        component = [start]
        for u in component:
            for v in sorted(neighbors[u]):
                if v in unseen:
                    unseen.remove(v)
                    component.append(v)
        comps.append(component)
    comps.sort(key=lambda c: (len(c), min(c)))
    result = []
    for comp in comps:
        ecc = Counter()
        dists = Counter()
        for source in comp:
            distance = {source: 0}
            queue = deque([source])
            while queue:
                u = queue.popleft()
                for v in neighbors[u]:
                    if v not in distance:
                        distance[v] = distance[u] + 1
                        queue.append(v)
            assert len(distance) == len(comp)
            ecc[max(distance.values())] += 1
            for target, d in distance.items():
                if source < target:
                    dists[d] += 1
        result.append((len(comp), sum(len(neighbors[u]) for u in comp)//2,
                       Counter(len(neighbors[u]) for u in comp), ecc, dists))
    return result


def certificate(name, values, pair=False):
    got = (BASE/name).read_text(encoding='utf-8').splitlines()
    want = [f'{a} {b}' for a, b in values] if pair else [str(a) for a in values]
    assert got == want, (name, len(got), len(want))


def main():
    counts, codes = enumerate_codes()
    assert counts == {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 268}
    jumps, slides = graph_pairs(codes)
    assert len(jumps) == 658 and len(slides) == 210
    certificate('states.txt', codes)
    certificate('jumps.txt', jumps, True)
    certificate('slides.txt', slides, True)
    tj = graph_stats(codes, jumps)
    ts = graph_stats(codes, slides)
    assert len(tj) == 3
    assert sorted((t[0], t[1]) for t in tj) == [(22, 63), (22, 63), (224, 532)]
    assert [t[2] for t in tj if t[0] == 22] == [Counter({5:21, 21:1})]*2
    assert [t[3] for t in tj if t[0] == 22] == [Counter({2:21, 1:1})]*2
    large = [t for t in tj if t[0] == 224][0]
    assert large[2] == Counter({5:168,4:56})
    assert large[3] == Counter({6:224})
    assert large[4] == Counter({1:532, 2:1848, 3:5376, 4:10332, 5:6216, 6:672})
    assert Counter((a, b) for a,b, *_ in ts) == Counter({(4,3):56, (22,21):2})
    assert all(t[2] == Counter({1:3, 3:1}) for t in ts if t[0] == 4)
    assert all(t[2] == Counter({1:21, 21:1}) for t in ts if t[0] == 22)
    assert all(t[3] == Counter({2:t[0]-1, 1:1}) for t in ts)
    # All seven points, all seven lines, and their incidence neighbors form the two small TJ components.
    for side in (range(7), range(7,14)):
        center = mask(side)
        expected = {center}
        for p in side:
            for q in V:
                if q not in side and frozenset((p,q)) in edge_set:
                    expected.add(center ^ (1<<p) ^ (1<<q))
        assert len(expected) == 22
        assert any(set(c) == expected for c in components_from(codes, jumps))
    print('PYTHON_VERIFY_OK codes=268 jump_edges=658 jump_components=22,22,224 main_eccentricity=6 slide_edges=210 slide_components=56*K1,3+2*K1,21')


def components_from(codes, edges):
    ad = {a:set() for a in codes}
    for a,b in edges:ad[a].add(b);ad[b].add(a)
    unseen=set(codes);out=[]
    while unseen:
        s=unseen.pop();q=[s]
        for u in q:
            for v in ad[u]&unseen:
                unseen.remove(v);q.append(v)
        out.append(q)
    return out


if __name__ == '__main__':
    main()
