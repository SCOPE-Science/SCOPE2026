"""Reproduce the homotopy-component census for Hom(C8, KG(5,2)).

Python 3.10+, standard library only. The external topological classification
used after this exact census is explicitly identified in RESULT.md.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations


def petersen():
    vertices = tuple(combinations(range(5), 2))
    adjacency = tuple(frozenset(j for j, w in enumerate(vertices)
                                if not set(v).intersection(w))
                      for v in vertices)
    assert len(vertices) == 10 and sum(map(len, adjacency)) == 30
    assert all(len(adjacency[i] & adjacency[j]) <= 1
               for i in range(10) for j in range(i + 1, 10))
    return adjacency


def homomorphisms(n, neighbors):
    out = []
    def visit(prefix):
        if len(prefix) == n:
            if prefix[0] in neighbors[prefix[-1]]:
                out.append(tuple(prefix))
            return
        for v in sorted(neighbors[prefix[-1]]):
            visit(prefix + [v])
    for start in range(len(neighbors)):
        visit([start])
    return tuple(out)


def components(maps, neighbors):
    unseen = set(maps)
    label = {}
    sizes = []
    while unseen:
        initial = min(unseen)
        unseen.remove(initial)
        queue = [initial]
        size = 0
        cid = len(sizes)
        while queue:
            f = queue.pop()
            label[f] = cid
            size += 1
            for i in range(len(f)):
                permitted = neighbors[f[(i - 1) % len(f)]] & neighbors[f[(i + 1) % len(f)]]
                for w in permitted:
                    if w == f[i]:
                        continue
                    g = f[:i] + (w,) + f[i + 1:]
                    if g in unseen:
                        unseen.remove(g)
                        queue.append(g)
        sizes.append(size)
    return label, sizes


def cells_by_component(maps, neighbors, labels):
    """Generate every polyhedral product face; test all adjacency constraints."""
    all_faces = set()
    n = len(maps[0])
    for f in maps:
        choices = []
        for i in range(n):
            common = neighbors[f[(i - 1) % n]] & neighbors[f[(i + 1) % n]]
            others = sorted(common - {f[i]})
            site = [(f[i],)]
            for k in range(1, len(others) + 1):
                for ext in combinations(others, k):
                    site.append(tuple(sorted((f[i],) + ext)))
            choices.append(site)

        def compatible(a, b):
            return all(y in neighbors[x] for x in a for y in b)

        def extend(i, current):
            if i == n:
                if compatible(current[-1], current[0]):
                    all_faces.add(tuple(current))
                return
            for s in choices[i]:
                if i and not compatible(current[-1], s):
                    continue
                if i == n - 1 and not compatible(s, current[0]):
                    continue
                extend(i + 1, current + [s])
        extend(0, [])

    counts = defaultdict(Counter)
    circle_triangles = defaultdict(list)
    for face in all_faces:
        vertex = tuple(s[0] for s in face)
        assert vertex in labels
        d = sum(len(s) - 1 for s in face)
        cid = labels[vertex]
        counts[cid][d] += 1
        if d == 2 and len(face) == 8 and sum(len(s) == 3 for s in face) == 1:
            circle_triangles[cid].append(face)
    return counts, circle_triangles


def simple_cycle_counts(neighbors, n):
    count = 0
    for w in homomorphisms(n, neighbors):
        if len(set(w)) == n:
            count += 1
    assert count % (2 * n) == 0
    return count // (2 * n)


def main():
    N = petersen()
    earlier = {}
    for n0 in (4, 6):
        m0 = homomorphisms(n0, N)
        _, sizes0 = components(m0, N)
        earlier[n0] = (len(m0), dict(Counter(sizes0)))
    assert earlier == {4: (150, {150:1}), 6: (990, {1:120, 870:1})}
    maps = homomorphisms(8, N)
    labels, component_sizes = components(maps, N)
    assert len(maps) == 7590
    assert Counter(component_sizes) == {1: 240, 48: 40, 5430: 1}
    assert all((component_sizes[labels[f]] == 1) == (len(set(f)) == 8) for f in maps)
    cells, triangles = cells_by_component(maps, N, labels)
    strata = defaultdict(Counter)
    for i, size in enumerate(component_sizes):
        strata[size][tuple(cells[i].get(d, 0) for d in range(9))] += 1
    assert strata[1] == Counter({(1, 0, 0, 0, 0, 0, 0, 0, 0): 240})
    assert strata[48] == Counter({(48, 72, 24, 0, 0, 0, 0, 0, 0): 40})
    assert strata[5430] == Counter({(5430, 20880, 33960, 30960, 17580,
                                      6480, 1560, 240, 20): 1})
    # Each 48-vertex component has pairwise edge-disjoint triangles; remove
    # one free edge and its triangle in each elementary collapse.  The
    # remaining connected graph has 48 vertices and 48 edges: a circle.
    for cid, size in enumerate(component_sizes):
        if size != 48:
            continue
        assert len(triangles[cid]) == 24
        used_edges = set()
        for face in triangles[cid]:
            i = next(j for j,s in enumerate(face) if len(s) == 3)
            for two in combinations(face[i], 2):
                edge = tuple(face[:i] + (two,) + face[i + 1:])
                assert edge not in used_edges
                used_edges.add(edge)
        assert len(used_edges) == 72
    assert (simple_cycle_counts(N, 6), simple_cycle_counts(N, 8)) == (10, 15)
    chis = Counter({size: sum((-1)**i*c for i,c in enumerate(next(iter(profiles))))
                    for size,profiles in strata.items()})
    assert chis == {1:1, 48:0, 5430:-10}
    print('Petersen vertices 10 edges 15; no quadrangles: PASS')
    print('Earlier even cycles C4 and C6 component profiles:', earlier)
    print('Hom(C8,P) vertices:', len(maps))
    print('Component sizes:', dict(sorted(Counter(component_sizes).items())))
    print('Polyhedral cell profiles by component size:')
    for size,profiles in sorted(strata.items()):
        print(' ', size, [(list(dims), count) for dims,count in profiles.items()])
    print('Component Euler characteristics:', dict(sorted(chis.items())))
    print('Every 48-map component has 24 triangles with disjoint edges: PASS')
    print('Isolated maps equal injective eight-cycle maps: PASS')
    print('Unoriented simple cycles (length 6, length 8):', (10, 15))
    print('Homotopy, using Fujii-Kimura-Nozaki Theorem 1.2:')
    print('  1 copy of connected bipartite double cover of P, 40 circles, 240 points')
    print('  H0=Z^281, H1=Z^51, all higher Hq=0')
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
