"""Exact integer certificates for cyclic binary de Bruijn order-five palindrome counts.

Two independent complete methods are implemented: directed Matrix--Tree cofactors
and DFS of every order-five Euler circuit with its unique zero-loop first.
All arithmetic is integer; no third-party dependencies are needed.
"""
from collections import Counter

N = 5
V = 1 << (N - 1)
ROOT = 0
BASE_EDGES = [(v, ((v << 1) | bit) & (V - 1)) for v in range(V) for bit in (0, 1)]


def smooth(edges, v):
    """Force transitions 0v->v0 and 1v->v1 and suppress the vertex v."""
    assert v not in (0, V - 1)
    first_in = v >> 1
    second_in = (1 << (N - 2)) | (v >> 1)
    first_out = (v << 1) & (V - 1)
    second_out = first_out | 1
    assert edges.count((first_in, v)) == 1
    assert edges.count((second_in, v)) == 1
    assert edges.count((v, first_out)) == 1
    assert edges.count((v, second_out)) == 1
    result = [(x, y) for x, y in edges if x != v and y != v]
    result += [(first_in, first_out), (second_in, second_out)]
    return result


def det_bareiss(matrix):
    """Fraction-free exact integer determinant with row pivots."""
    a = [list(r) for r in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            i = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if i is None:
                return 0
            a[k], a[i] = a[i], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[n - 1][n - 1]


def rooted_arborescences(edges):
    vertices = sorted({a for a, b in edges} | {b for a, b in edges})
    assert ROOT in vertices
    ix = {v: i for i, v in enumerate(vertices)}
    outdegree = Counter(a for a, b in edges)
    indegree = Counter(b for a, b in edges)
    assert all(outdegree[v] == indegree[v] == 2 for v in vertices)
    lap = [[0] * len(vertices) for _ in vertices]
    for a, b in edges:
        lap[ix[a]][ix[a]] += 1
        lap[ix[a]][ix[b]] -= 1
    r = ix[ROOT]
    reduced = [[lap[i][j] for j in range(len(vertices)) if j != r]
               for i in range(len(vertices)) if i != r]
    return det_bareiss(reduced)


cofactor = {}
for subset in ((), (6,), (9,), (6, 9)):
    graph = BASE_EDGES[:]
    for v in subset:
        graph = smooth(graph, v)
    cofactor[subset] = rooted_arborescences(graph)
assert cofactor == {(): 2048, (6,): 768, (9,): 768, (6, 9): 256}, cofactor

# Independently enumerate rooted Euler tours using the unique 00000 n-gram
# as a fixed initial edge, so each rotational class occurs exactly once.
hist = Counter()
joint = Counter()
visited_nodes = 0


def dfs(vertex, used, bits):
    global visited_nodes
    visited_nodes += 1
    if len(bits) == 1 << N:
        assert vertex == ROOT
        s = ''.join(map(str, bits))
        doubled = s + s
        fivegrams = {doubled[i:i + N] for i in range(1 << N)}
        assert len(fivegrams) == 1 << N
        sixgrams = {doubled[i:i + N + 1] for i in range(1 << N)}
        assert not ({'000000', '100001', '011110', '111111'} & sixgrams)
        aa = ('001100' in sixgrams)
        bb = ('010010' in sixgrams)
        assert aa == ('101101' in sixgrams)
        assert bb == ('110011' in sixgrams)
        joint[int(aa), int(bb)] += 1
        hist[2 * (int(aa) + int(bb))] += 1
        return
    for bit in (0, 1):
        edge = (vertex << 1) | bit
        if not (used & (1 << edge)):
            dfs(edge & (V - 1), used | (1 << edge), bits + [bit])


dfs(ROOT, 1, [0])
assert joint == Counter({(0, 0): 768, (1, 0): 512, (0, 1): 512, (1, 1): 256}), joint
assert hist == Counter({0: 768, 2: 1024, 4: 256}), hist
assert sum(hist.values()) == cofactor[()] == 2048
assert joint[(1, 0)] + joint[(1, 1)] == cofactor[(6,)]
assert joint[(0, 1)] + joint[(1, 1)] == cofactor[(9,)]
assert joint[(1, 1)] == cofactor[(6, 9)]
print('PASS: exact cofactors 2048/768/768/256 and independent Euler tour DFS 768/1024/256')
print('Directed DFS calls:', visited_nodes)
