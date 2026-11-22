#!/usr/bin/env python3
"""Exact finite-state verification for central quadrinomial residues modulo three."""
from collections import deque
from math import comb

RANGE = tuple(range(-2, 3))
INDEX = {r: i for i, r in enumerate(RANGE)}
P = []
for digit in range(3):
    c = [1]
    for _ in range(digit):
        q = [0] * (len(c) + 3)
        for j, coefficient in enumerate(c):
            for t in range(4):
                q[j + t] += coefficient
        c = q
    P.append(c)


def transition(vector, digit):
    out = [0] * 5
    for r in RANGE:
        for j, coefficient in enumerate(P[digit]):
            q = r + 2 * j - 3 * digit
            if q % 3 == 0 and q // 3 in INDEX:
                out[INDEX[q // 3]] += vector[INDEX[r]] * coefficient
    return tuple(t % 3 for t in out)


def graph(epsilon):
    v = [0] * 5
    v[INDEX[epsilon]] = 1
    first = (tuple(v), 0)
    ids = {first: 0}
    order = [first]
    edges = []
    q = deque([first])
    while q:
        vector, parity = q.popleft()
        targets = []
        for digit in range(3):
            node = (transition(vector, digit), (parity + digit) % 2)
            if node not in ids:
                ids[node] = len(order)
                order.append(node)
                q.append(node)
            targets.append(ids[node])
        edges.append(tuple(targets))
    return order, edges


def census(max_level):
    graphs = [graph(eps) for eps in (0, 1)]
    assert [len(g[0]) for g in graphs] == [8, 10]
    vector_counts = [[1] + [0] * (len(g[0]) - 1) for g in graphs]
    out = []
    for level in range(max_level + 1):
        distribution = [0, 0, 0]
        for eps, (states, _) in enumerate(graphs):
            for idx, (v, parity) in enumerate(states):
                if parity == eps:
                    distribution[v[INDEX[0]]] += vector_counts[eps][idx]
        assert sum(distribution) == 3**level
        out.append(tuple(distribution))
        new_counts = []
        for (states, edges), cnt in zip(graphs, vector_counts):
            next_counts = [0] * len(states)
            for idx, amount in enumerate(cnt):
                for target in edges[idx]:
                    next_counts[target] += amount
            new_counts.append(next_counts)
        vector_counts = new_counts
    return out


def polynomial_coefficients(max_n):
    poly = [1]
    for n in range(max_n + 1):
        yield n, poly[(3 * n) // 2] % 3
        next_poly = [0] * (len(poly) + 3)
        for i, value in enumerate(poly):
            for t in range(4):
                next_poly[i + t] = (next_poly[i + t] + value) % 3
        poly = next_poly


def verify():
    assert P == [[1], [1, 1, 1, 1], [1, 2, 3, 4, 3, 2, 1]]
    # The following is a full finite certificate of the transition table in
    # RESULT.md, independently regenerated from the polynomial coefficients.
    expected = [
        [
          ((0,0,1,0,0),0,(0,1,2)),
          ((0,1,0,1,0),1,(3,4,5)),
          ((1,0,1,0,1),0,(0,5,0)),
          ((0,0,0,0,0),1,(3,6,3)),
          ((0,0,2,0,0),0,(4,5,7)),
          ((0,2,0,2,0),1,(3,0,1)),
          ((0,0,0,0,0),0,(6,3,6)),
          ((2,0,2,0,2),0,(4,1,4)),
        ],
        [
          ((0,0,0,1,0),0,(1,2,3)),
          ((0,0,0,0,0),0,(1,4,1)),
          ((0,0,1,0,0),1,(2,5,6)),
          ((0,2,0,0,0),0,(1,7,0)),
          ((0,0,0,0,0),1,(4,1,4)),
          ((0,1,0,1,0),0,(1,7,8)),
          ((1,0,1,0,1),1,(2,8,2)),
          ((0,0,2,0,0),1,(7,8,9)),
          ((0,2,0,2,0),0,(1,2,5)),
          ((2,0,2,0,2),1,(7,5,7)),
        ],
    ]
    for eps in (0, 1):
        states, edges = graph(eps)
        assert [(v,p,edges[i]) for i,(v,p) in enumerate(states)] == expected[eps]
    data = census(25)
    for level, (n0, n1, n2) in enumerate(data):
        support, bias = n1 + n2, n1 - n2
        if level == 0:
            assert (support, bias) == (1, 1)
        if level == 1:
            assert (support, bias) == (3, 3)
        if level == 2:
            assert (support, bias) == (8, 4)
        if level >= 2:
            prev = [x[1] + x[2] for x in data]
            assert support == 3 * prev[level - 1] - prev[level - 2]
        if level >= 3:
            diff = [x[1] - x[2] for x in data]
            assert bias == 2 * diff[level - 2] + 3 * diff[level - 3]
        assert n0 == 3**level - support
        assert (support + bias) % 2 == 0
    # Finite certification for all levels: the 18-state combined graph has
    # a characteristic polynomial of degree 18. The discrepancy from an
    # order-2 (respectively order-3) candidate obeys a recurrence of order
    # at most 20 (respectively 21). Its first 20/21 terms vanish here.
    cumulative = [0, 0, 0]
    observed = [None] * 729
    for n, residue in polynomial_coefficients(728):
        observed[n] = residue
        cumulative[residue] += 1
        if n + 1 in [1, 3, 9, 27, 81, 243, 729]:
            L = {1:0, 3:1, 9:2, 27:3, 81:4, 243:5, 729:6}[n+1]
            assert tuple(cumulative) == data[L]
    for eps in (0, 1):
        states, edges = graph(eps)
        for node, row in zip(states, edges):
            for digit in range(3):
                target = (transition(node[0], digit), (node[1]+digit)%2)
                assert states[row[digit]] == target
    print('PASS: 18-state transition closure, 26 complete-level counts,')
    print('      729 independently expanded central coefficients,')
    print('      20/21 base terms certify both infinite recurrence laws.')
    for level in range(8):
        print('L=%d N0,N1,N2=%r' % (level, data[level]))

if __name__ == '__main__':
    verify()
