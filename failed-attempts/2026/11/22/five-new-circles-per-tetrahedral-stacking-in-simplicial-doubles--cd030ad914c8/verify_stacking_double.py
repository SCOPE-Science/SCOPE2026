"""Independent combinatorial checks for the simplicial double under 1-to-4 moves.
Run with Python 3.9 or later; uses only the standard library.
"""
from itertools import combinations
from collections import deque


def edges_from_tetrahedra(facets):
    return {tuple(sorted(e)) for f in facets for e in combinations(f, 2)}


def double_graph(facets):
    vertices = edges_from_tetrahedra(facets)
    adj = {e: set() for e in vertices}
    for f in facets:
        for e in combinations(f, 2):
            e = tuple(sorted(e))
            opposite = tuple(sorted(set(f).difference(e)))
            adj[e].add(opposite)
            adj[opposite].add(e)
    return adj


def components(adj):
    unseen = set(adj)
    out = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        todo = [seed]
        piece = {seed}
        while todo:
            for other in adj[todo.pop()]:
                if other in unseen:
                    unseen.remove(other)
                    piece.add(other)
                    todo.append(other)
        out.append(piece)
    return out


def graph_betti(adj):
    nverts = len(adj)
    nedges = sum(map(len, adj.values())) // 2
    ncomp = len(components(adj))
    return nverts, nedges, ncomp, nedges - nverts + ncomp


def stack(facets, face, new_vertex):
    target = tuple(sorted(face))
    assert target in facets
    result = set(facets)
    result.remove(target)
    result.update(tuple(sorted((new_vertex,) + t)) for t in combinations(face, 3))
    return frozenset(result)


def check_move(facets, face, new_vertex):
    old = double_graph(facets)
    new = double_graph(stack(facets, face, new_vertex))
    assert new_vertex not in {x for f in facets for x in f}
    old_comps = components(old)
    six = set(combinations(face, 2))
    six = {tuple(sorted(p)) for p in six}
    k = sum(bool(c & six) for c in old_comps)
    assert 1 <= k <= 3
    v, e, c, b = graph_betti(old)
    v1, e1, c1, b1 = graph_betti(new)
    assert (v1 - v, e1 - e, c1 - c, b1 - b) == (4, 9, 1-k, 6-k)
    # Exactly 3 old double-edges disappear. They pair the six old
    # edge-vertices of the selected tetrahedron in opposite pairs.
    old_edge_set = {frozenset((a, b)) for a in old for b in old[a]}
    new_edge_set = {frozenset((a, b)) for a in new for b in new[a]}
    removed = old_edge_set-new_edge_set
    added = new_edge_set-old_edge_set
    assert len(removed) == 3 and len(added) == 12
    assert all(a in six and b in six for a,b in (tuple(pair) for pair in removed))
    assert all(sum(new_vertex in part for part in pair) == 1 for pair in (tuple(ed) for ed in added))
    assert old_edge_set - removed == new_edge_set - added
    return k


def main():
    seed = frozenset(tuple(sorted(f)) for f in combinations(range(5), 4))
    assert graph_betti(double_graph(seed)) == (10, 15, 1, 6)
    stack_histories = {seed}
    counts = []
    for n in range(5, 10):
        expected = 5*n - 19
        for facets in stack_histories:
            graph = double_graph(facets)
            v,e,c,b = graph_betti(graph)
            assert (v,e,c,b) == (4*n-10, 9*n-30, 1, expected), (n,v,e,c,b)
        counts.append((n,len(stack_histories),expected))
        if n == 9:
            break
        new_histories = set()
        for facets in stack_histories:
            for tet in facets:
                assert check_move(facets,tet,n) == 1
                new_histories.add(stack(facets,tet,n))
        stack_histories = new_histories
    # Additional local checks for complexes not restricted to manifold spheres.
    base = frozenset({(0,1,2,3)})
    assert check_move(base,(0,1,2,3),4) == 3
    base_two = frozenset({(0,1,2,3),(4,5,6,7)})
    assert check_move(base_two,(0,1,2,3),8) == 3
    from random import Random
    rng=Random(42791)
    all_tets=list(combinations(range(7),4))
    sampled=0
    observed=set()
    for _ in range(1000):
        fs=frozenset(f for f in all_tets if rng.getrandbits(1))
        if not fs:continue
        face=rng.choice(tuple(fs))
        observed.add(check_move(fs,face,7))
        sampled+=1
    print('stacked boundary cases (vertex-count, labeled facet sets, circle-rank):')
    for n,number,beta in counts: print(n,number,beta)
    print('additional arbitrary complexes:', sampled+2)
    print('local component counts observed:',sorted(observed|{3}))
    print('all checks passed')

if __name__ == '__main__':main()
