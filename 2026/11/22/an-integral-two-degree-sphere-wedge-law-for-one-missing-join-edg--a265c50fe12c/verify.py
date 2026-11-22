"""Independent exhaustive GF(2) checks of induced-forest edge-fault homotopy ranks.
The all-parameter and integral assertions follow from the separate proof, not this finite test.
Usage: python3 verify.py
"""
from itertools import combinations


def graph_edges(m, b, deleted):
    a = 2 * m
    edges = [(2 * i, 2 * i + 1) for i in range(m)]
    edges += [(x, a + j) for x in range(a) for j in range(b)
              if not deleted or (x, j) != (0, 0)]
    return edges


def is_forest(mask, edges, n):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        if mask >> u & 1 and mask >> v & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True


def faces(m, b, deleted):
    n = 2 * m + b
    edges = graph_edges(m, b, deleted)
    return {mask for mask in range(1 << n) if is_forest(mask, edges, n)}


def gf2_rank(columns):
    pivots = {}
    for vec in columns:
        while vec:
            t = vec.bit_length() - 1
            if t in pivots:
                vec ^= pivots[t]
            else:
                pivots[t] = vec
                break
    return len(pivots)


def reduced_betti(face_set, n):
    by_card = [[] for _ in range(n + 1)]
    for mask in face_set:
        by_card[mask.bit_count()].append(mask)
    boundary_rank = [0] * (n + 2)
    for card in range(1, n + 1):
        rows = {mask: k for k, mask in enumerate(by_card[card - 1])}
        columns = []
        for mask in by_card[card]:
            col = 0
            for bit in range(n):
                if mask >> bit & 1:
                    col ^= 1 << rows[mask ^ (1 << bit)]
            columns.append(col)
        boundary_rank[card] = gf2_rank(columns)
    result = {}
    for card in range(1, n + 1):
        d = len(by_card[card]) - boundary_rank[card] - boundary_rank[card + 1]
        if d:
            result[card - 1] = d
    # The boundary from vertices to the empty face already gives reduced H_0.
    return result


def expected(m, b, deleted):
    d = {}
    def add(deg, value):
        d[deg] = d.get(deg, 0) + value
    if deleted:
        add(2, b - 1)
        add(m, b - 1)
    else:
        add(2, (2 * m - 1) * (b - 1))
        add(m, b)
    return d


def main():
    cases = [(m, b) for m in range(2, 5) for b in range(2, 5)] + [(5, 2), (5, 3)]
    for m, b in cases:
        n = 2*m+b
        f = faces(m, b, True)
        f0 = faces(m, b, False)
        # Every old allowed set remains allowed after deleting an edge.
        assert f0 <= f
        full = reduced_betti(f, n)
        intact = reduced_betti(f0, n)
        assert full == expected(m, b, True), (m, b, 'fault', full)
        assert intact == expected(m, b, False), (m, b, 'intact', intact)
        # Exact simplicial vertex link of b_0 in the damaged graph.
        vertex = 2*m
        link = {mask & ~(1 << vertex) for mask in f if mask >> vertex & 1}
        expected_link = {1: 1}
        if b > 2:
            expected_link[2] = (2*m-2)*(b-2)
        assert reduced_betti(link, n) == expected_link, (m, b, 'link')
        print('PASS', 'm=', m, 'b=', b, 'faces=', len(f),
              'fault=', full, 'intact=', intact,
              'link=', expected_link)
    print('PASS: all 11 graph-fault, intact, link and monotonicity checks')

if __name__ == '__main__':
    main()
