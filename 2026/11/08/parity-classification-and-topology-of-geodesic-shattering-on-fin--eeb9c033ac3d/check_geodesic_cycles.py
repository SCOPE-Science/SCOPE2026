"""Independent exhaustive checks of shortest-path traces on finite cycles.

Uses only the Python standard library.  The topology check computes the
simplicial homology boundary rank over the field with two elements; the
universal homotopy statement is proved separately.
"""
from itertools import combinations
from math import comb


def all_geodesic_vertex_sets(n):
    """Construct all shortest paths by comparing both cycle arcs for endpoints."""
    paths = set()
    for u in range(n):
        for v in range(u, n):
            forward = (v-u) % n
            backward = (u-v) % n
            shortest = min(forward, backward)
            if forward == shortest:
                paths.add(frozenset((u+t) % n for t in range(forward+1)))
            if backward == shortest:
                paths.add(frozenset((u-t) % n for t in range(backward+1)))
    return paths


def is_shattered(paths, vertices):
    vertices = tuple(vertices)
    patterns = {tuple(int(v in p) for v in vertices) for p in paths}
    return len(patterns) == (1 << len(vertices))


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            pivot = col.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = col
                break
            col ^= pivots[pivot]
    return len(pivots)


def homology_betti(n, triangles):
    """Reduced dimension-one and dimension-two Betti numbers over F_2."""
    edges = list(combinations(range(n), 2))
    loc = {edge: k for k, edge in enumerate(edges)}
    boundaries = [sum(1 << loc[edge] for edge in combinations(t,2))
                  for t in triangles]
    r2 = gf2_rank(boundaries)
    # The one-skeleton is the connected complete graph K_n.
    return (len(edges) - (n-1) - r2, len(triangles) - r2)


def main():
    for n in range(3, 19):
        paths = all_geodesic_vertex_sets(n)
        shattered = {}
        for k in range(1, 5):
            shattered[k] = [s for s in combinations(range(n), k)
                            if is_shattered(paths, s)]
        assert len(shattered[1]) == n
        assert len(shattered[2]) == comb(n,2)
        assert not shattered[4]
        expected_triples = [s for s in combinations(range(n),3)
                            if n % 2 == 0 and any((b-a) == n//2
                                                for a,b in combinations(s,2))]
        assert shattered[3] == expected_triples
        assert len(expected_triples) == (n*(n-2)//2 if n % 2 == 0 else 0)
        b1,b2 = homology_betti(n,shattered[3])
        if n % 2:
            want = (comb(n-1,2),0)
        else:
            m=n//2
            want = (comb(m-1,2), comb(m,2))
        assert (b1,b2) == want, (n,(b1,b2),want)
        print('n=%2d  paths=%3d  pairs=%3d  triples=%3d  betti_1=%2d  betti_2=%2d  OK'
              %(n,len(paths),len(shattered[2]),len(shattered[3]),b1,b2))
    print('ALL_CYCLE_GEODESIC_SHATTERING_CHECKS_PASS')


if __name__ == '__main__':
    main()
