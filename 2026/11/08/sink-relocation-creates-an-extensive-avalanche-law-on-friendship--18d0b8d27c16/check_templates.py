"""Independent product-state and parallel-wave verification of the proof table.

Run: python check_templates.py
Uses no dependencies beyond the Python standard library.
"""
from itertools import product


def graph(k):
    n = 2 * k + 1
    neighbors = [[j for j in range(n) if
        ((i == 0 and j != 0) or (j == 0 and i != 0) or
         (i >= 1 and j >= 1 and (i-1)//2 == (j-1)//2 and i != j))]
        for i in range(n)]
    return neighbors


def waves(heights, neighbors, source, sink=1):
    y = heights[:]
    y[source] += 1
    N = len(y)
    firing = [0] * N
    lost = 0
    for _ in range(10000):
        active = [v for v in range(N) if v != sink and y[v] >= len(neighbors[v])]
        if not active:
            assert all(0 <= y[v] < len(neighbors[v]) for v in range(N) if v != sink)
            return (sum(firing), lost)
        changes = [0]*N
        for v in active:
            firing[v] += 1
            changes[v] -= len(neighbors[v])
            for w in neighbors[v]:
                if w == sink:
                    lost += 1
                else:
                    changes[w] += 1
        for i in range(N):
            y[i] += changes[i]
    raise AssertionError("nonterminating toppling")


def analytic(k, gate, pair, source):
    if source == 0:
        return ((0,0), (2*k-1,1), (2*k,2))[gate]
    if source == 2:
        return ((1,1), (0,0), (2*k,2))[gate]
    h = pair[0 if source % 2 == 1 else 1]
    partner = pair[1 if source % 2 == 1 else 0]
    if h == 0:
        return (0,0)
    if partner == 0:
        return ((1,0), (2*k,1), (2*k+1,2))[gate]
    return ((2*k+2,2), (2*k+1,1), (4*k+1,3))[gate]


def run():
    gates = lambda k: [(2*k-2,1), (2*k-1,0), (2*k-1,1)]
    triangles = [(1,0), (0,1), (1,1)]
    for k in range(1, 9):
        adj = graph(k)
        cases = 0
        for gate, tail in product(range(3), product(triangles, repeat=k-1)):
            heights = [0]*(2*k+1)
            heights[0], heights[2] = gates(k)[gate]
            for i, pair in enumerate(tail, start=1):
                heights[2*i+1], heights[2*i+2] = pair
            for vertex in range(len(heights)):
                if vertex == 1:continue
                pair = None if vertex <= 2 else tail[(vertex-3)//2]
                actual = waves(heights, adj, vertex)
                predicted = analytic(k, gate, pair, vertex)
                assert actual == predicted, (k,gate,tail,vertex,actual,predicted)
                cases += 1
        assert cases == 2*k*3**k
        print(f"k={k}: {cases} product-state additions match all local templates")


if __name__ == '__main__':
    run()
