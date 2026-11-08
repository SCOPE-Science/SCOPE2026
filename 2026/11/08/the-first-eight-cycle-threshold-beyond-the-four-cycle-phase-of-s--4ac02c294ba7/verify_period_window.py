"""Exact checks for a negative-doubling survivor transition (standard library only).

All statements with unrestricted quantifiers are established by the accompanying proof;
finite tests here are independent cross-checks.
"""
from fractions import Fraction

A = Fraction(7, 17)
EDGES = [0, 3, 5, 6, 7, 10, 11, 12, 14, 17]
CELLS = [(EDGES[i], EDGES[i+1]) for i in range(len(EDGES)-1)
         if EDGES[i+1] <= 7 or EDGES[i] >= 10]
EXPECTED = [(5, 6, 7), (4,), (2, 3), (1,), (6,), (4, 5), (3,), (0, 1, 2)]


def T(x):
    assert x != Fraction(1, 2)
    return 1-2*x if x < Fraction(1, 2) else 2-2*x


def orbit(x):
    out = []
    while x not in out:
        out.append(x)
        x = T(x)
    assert x == out[0]
    return tuple(out)


def survives(x, a):
    visited = set()
    while x not in visited:
        if a < x < 1-a: return False
        visited.add(x)
        x = T(x)
    return True


def adjacency():
    graph = []
    for i, (l, r) in enumerate(CELLS):
        left, right = T(Fraction(l, 17)), T(Fraction(r, 17))
        assert right < left
        adj = tuple(j for j,(u,v) in enumerate(CELLS)
                    if Fraction(u,17)>=right and Fraction(v,17)<=left)
        assert adj == EXPECTED[i], (i, adj)
        graph.append(adj)
    return graph


def strongly_connected_components(graph):
    def reach(u):
        seen={u}; frontier=[u]
        while frontier:
            for v in graph[frontier.pop()]:
                if v not in seen:
                    seen.add(v); frontier.append(v)
        return seen
    sets = [reach(i) for i in range(len(graph))]
    return {frozenset(j for j in range(len(graph)) if i in sets[j] and j in sets[i])
            for i in range(len(graph))}


def periodic_points(n, a):
    denom=2**n-(-1)**n
    pts={Fraction(k, denom) for k in range(1, denom)}
    return {x for x in pts if survives(x, a)} | ({Fraction(0),Fraction(1)} if n%2==0 else set())


def main():
    checks=0
    graph=adjacency(); checks+=len(graph)
    scc=strongly_connected_components(graph)
    assert scc=={frozenset({0,7}), frozenset({1,3,4,6}), frozenset({2}),frozenset({5})}
    checks+=1
    periodic = [orbit(Fraction(0)),orbit(Fraction(1,3)),orbit(Fraction(2,3)),
                orbit(Fraction(1,5)), orbit(Fraction(7,17))]
    assert tuple(map(len,periodic))==(2,1,1,4,8)
    assert set(periodic[-1])=={Fraction(k,17) for k in (3,5,6,7,10,11,12,14)}
    for o in periodic:
        for x in o:
            assert T(x)==o[(o.index(x)+1)%len(o)]
            checks+=1
    # Contrasting periodic census at endpoint and between the two rational thresholds.
    for a in [Fraction(2,5),Fraction(81,200),Fraction(41,100),Fraction(7,17)]:
        for n in range(1,17):
            pts=periodic_points(n,a)
            predicted = (2 if n%2==0 else 0)+2+(4 if n%4==0 else 0)
            if a==A and n%8==0: predicted+=8
            assert len(pts)==predicted, (a,n,len(pts),predicted)
            checks+=1
    print(f'VERIFY_OK checks={checks}; endpoint_graph_edges={graph}; endpoint_periods=2,1,1,4,8')

if __name__=='__main__':main()
