"""Exact-rational checks for the sharp node-averaged friendship-gap envelope.

Run using Python 3.9 or newer: python3 verify.py
No third-party packages are needed.
"""
from fractions import Fraction as F
from itertools import combinations, product


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def center(a):
    m = sum(a, F(0))/len(a)
    return [x-m for x in a]


def connected(n, edges):
    seen = {0}
    while True:
        nxt = seen | {b for a,b in edges if a in seen} | {a for a,b in edges if b in seen}
        if nxt == seen:
            return len(seen) == n
        seen = nxt


def invariants(n, edges):
    neighbors = [set() for _ in range(n)]
    for a,b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    deg = [F(len(x)) for x in neighbors]
    delta = [sum((F(1, len(neighbors[j])) for j in neighbors[i]), F(0)) for i in range(n)]
    u, w = center(deg), [x-F(1) for x in delta]
    return neighbors, deg, delta, u, w


def test_graph(n, edges):
    N, deg, delta, u, w = invariants(n, edges)
    if all(x == deg[0] for x in deg):
        return 0
    assert sum(delta) == n
    U, W, D = dot(u,u), dot(w,w), dot(u,w)
    assert U > 0 and W > 0 and D > 0
    assert D*D <= U*W
    count = 4
    samples = [deg, delta, [F(j*j - 2*j + 3) for j in range(n)],
               [x+3*y for x,y in zip(u,w)],
               [x-2*y for x,y in zip(u,w)],
               [x-(D/W)*y for x,y in zip(u,w)]]
    for a in samples:
        ac = center(a)
        A = dot(ac,ac)
        direct = sum((sum((a[j] for j in N[i]),F(0))/len(N[i]) - a[i]
                      for i in range(n)), F(0))/n
        gap = dot(w,a)/n
        assert direct == gap
        count += 1
        if A:
            Du, Wv = dot(u,ac), dot(w,ac)
            left = (U*Wv-D*Du)**2
            right = (U*W-D**2)*(U*A-Du**2)
            assert left <= right
            count += 1
    # On the span of the degree and reciprocal-degree vectors, the envelope is exact.
    for k in [-3,-1,0,1,3]:
        ac = [x+F(k)*y for x,y in zip(u,w)]
        A = dot(ac,ac)
        if not A:
            continue
        assert (U*dot(w,ac)-D*dot(u,ac))**2 == (U*W-D*D)*(U*A-dot(u,ac)**2)
        count += 1
    # The positive-correlation extremizer of the zero-gap hyperplane.
    a0 = [x-(D/W)*y for x,y in zip(u,w)]
    assert dot(w,a0) == 0
    if D*D < U*W:
        assert dot(u,a0)>0
        a0norm = dot(a0,a0)
        # Its squared Pearson correlation equals the sharp threshold rho^2.
        assert dot(u,a0)**2/(U*a0norm) == (U*W-D*D)/(U*W)
        count += 2
        for denominator in [100,1000,10000]:
            eps = F(1, denominator)
            a = [x-eps*y for x,y in zip(a0,w)]
            if dot(u,a)>0:
                assert dot(w,a)<0
                assert dot(u,a)**2/(U*dot(a,a)) < (U*W-D*D)/(U*W)
                count += 2
    else:
        assert a0 == [F(0)]*n
        count += 1
    return count


def run():
    total = 0
    graphs = 0
    pro = 0
    for n in range(3, 6):
        edges_all = list(combinations(range(n),2))
        for mask in range(1,1<<len(edges_all)):
            edges = [e for j,e in enumerate(edges_all) if (mask>>j)&1]
            if not connected(n, edges):
                continue
            cnt=test_graph(n, edges)
            if cnt:
                graphs+=1
                total+=cnt
                N,d,delta,u,w=invariants(n,edges)
                pro+=(dot(u,w)**2 == dot(u,u)*dot(w,w))
    n=4
    paw=[(0,1),(0,2),(1,2),(0,3)]
    _,d,delta,u,w=invariants(n,paw)
    assert d == [F(3), F(2), F(2), F(1)]
    assert delta == [F(2), F(5,6), F(5,6), F(1,3)]
    assert dot(u,u) == 2 and dot(w,w) == F(3,2) and dot(u,w)==F(5,3)
    assert 1-dot(u,w)**2/(dot(u,u)*dot(w,w))==F(2,27)
    total+=5
    print(f"PASS: {graphs} connected nonregular labeled graphs (n=3..5); {pro} pro-SGFP; {total} exact-rational check units")
    print("Paw graph sharp squared threshold = 2/27; all endpoints and strictness checked.")


if __name__ == '__main__':
    run()
