"""Independent exhaustive fixed-sink sandpile enumeration.

Run: python check_exhaustive.py
Uses only Python's standard library. No files or network required.
"""
from collections import Counter
from itertools import product


def expected(k):
    # (total topplings, grains lost to sink) -> count
    c = Counter()
    def put(t, loss, mult): c[t, loss] += mult
    p = 3 ** (k - 1)
    put(0, 0, 2 * k * p)
    put(1, 1, p)
    put(2 * k - 1, 1, p)
    put(2 * k, 2, 2 * p)
    if k > 1:
        b = 2 * (k - 1) * 3 ** (k - 2)
        for t, loss in ((1,0), (2*k,1), (2*k+1,1),
                        (2*k+1,2), (2*k+2,2), (4*k+1,3)):
            put(t, loss, b)
    return +c


def graph(k):
    N = 2 * k + 1
    adj = [set() for _ in range(N)]
    for i in range(k):
        a, b = 2*i + 1, 2*i + 2
        for u,v in ((0,a),(0,b),(a,b)):
            adj[u].add(v); adj[v].add(u)
    sink = 1
    vertices = tuple(v for v in range(N) if v != sink)
    return adj, sink, vertices


def burning(h, adj, sink, vertices):
    # Direct Dhar burning, using residual internal degree.
    unburnt = set(vertices)
    while unburnt:
        ready = [v for v in unburnt if h[v] >= len(adj[v] & unburnt)]
        if not ready: return False
        unburnt.difference_update(ready)
    return True


def stabilize(h, adj, sink, vertices):
    h = list(h)
    fired = [0] * len(adj)
    lost = 0
    steps = 0
    while True:
        v = next((v for v in vertices if h[v] >= len(adj[v])), None)
        if v is None:
            return sum(fired), lost
        steps += 1
        assert steps < 100000
        h[v] -= len(adj[v])
        fired[v] += 1
        for w in adj[v]:
            if w == sink: lost += 1
            else: h[w] += 1


def run():
    for k in range(1, 8):
        adj, sink, vertices = graph(k)
        deg = [len(adj[v]) for v in vertices]
        histogram = Counter()
        recurrent = 0
        for values in product(*(range(d) for d in deg)):
            h = [0] * len(adj)
            for v, height in zip(vertices, values): h[v] = height
            if not burning(h, adj, sink, vertices):
                continue
            recurrent += 1
            for vertex in vertices:
                x = h.copy()
                x[vertex] += 1
                histogram[stabilize(x, adj, sink, vertices)] += 1
        assert recurrent == 3**k, (k, recurrent)
        assert histogram == expected(k), (k,histogram-expected(k),expected(k)-histogram)
        assert sum(histogram.values()) == 2*k*3**k
        print(f"k={k}: {recurrent} recurrent states, "
              f"{sum(histogram.values())} additions, all joint counts PASS")


if __name__ == '__main__':
    run()
