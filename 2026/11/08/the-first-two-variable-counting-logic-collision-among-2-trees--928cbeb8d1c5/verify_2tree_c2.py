#!/usr/bin/env python3
"""Exhaustive classification of C2 / color-refinement equivalence on 2-trees of order <=8.
Only Python standard library is used; assertions are exact, without graph hashes.
"""
from collections import Counter, defaultdict
from itertools import combinations


def edges(g):
    return [(i, j) for i in range(len(g)) for j in range(i+1, len(g)) if (g[i] >> j) & 1]


def add_ear(g, a, b):
    n = len(g)
    h = list(g)
    h[a] |= 1 << n
    h[b] |= 1 << n
    h.append((1 << a) | (1 << b))
    return tuple(h)


def make_graph(n, edgelist):
    g = [0] * n
    for u, v in edgelist:
        assert u != v and 0 <= u < n and 0 <= v < n
        assert not (g[u] >> v) & 1
        g[u] |= 1 << v
        g[v] |= 1 << u
    return tuple(g)


def degree(g):
    return tuple(int(x).bit_count() for x in g)


def invariant(g):
    d = degree(g)
    return (tuple(sorted(d)), tuple(sorted((d[i], tuple(sorted(d[j] for j in range(len(g)) if (g[i] >> j) & 1))) for i in range(len(g)))))


def isomorphic(g, h):
    n = len(g)
    if n != len(h) or invariant(g) != invariant(h):
        return False
    dg, dh = degree(g), degree(h)
    sigg = [(dg[i], tuple(sorted(dg[j] for j in range(n) if (g[i] >> j) & 1))) for i in range(n)]
    sigh = [(dh[i], tuple(sorted(dh[j] for j in range(n) if (h[i] >> j) & 1))) for i in range(n)]
    candidates = [[j for j in range(n) if sigh[j] == sigg[i]] for i in range(n)]
    order = sorted(range(n), key=lambda i: (len(candidates[i]), -dg[i]))
    f = [-1] * n
    used = [False] * n
    def dfs(t):
        if t == n:
            return True
        i = order[t]
        for j in candidates[i]:
            if not used[j] and all(((g[i] >> k) & 1) == ((h[j] >> f[k]) & 1) for k in order[:t]):
                f[i] = j
                used[j] = True
                if dfs(t+1):
                    return True
                used[j] = False
                f[i] = -1
        return False
    return dfs(0)


def joint_refinement_equal(g, h):
    n, m = len(g), len(h)
    c = [0] * (n+m)
    adj = [list(j for j in range(n) if (g[i]>>j)&1) for i in range(n)] + [list(n+j for j in range(m) if (h[i]>>j)&1) for i in range(m)]
    for _ in range(n+m+1):
        signatures = [(c[v], tuple(sorted(Counter(c[w] for w in adj[v]).items()))) for v in range(n+m)]
        palette = {signature:i for i,signature in enumerate(sorted(set(signatures)))}
        nxt = [palette[s] for s in signatures]
        if Counter(nxt[:n]) != Counter(nxt[n:]):
            return False
        if nxt == c:
            return True
        c = nxt
    raise AssertionError('Refinement should stabilize within |V|-1 proper steps')


def enumerate_2trees():
    B = {3: [make_graph(3, [(0,1),(0,2),(1,2)])]}
    for n in range(4, 9):
        classes = defaultdict(list)
        for old in B[n-1]:
            for u,v in edges(old):
                new = add_ear(old,u,v)
                key = invariant(new)
                if not any(isomorphic(new, prev) for prev in classes[key]):
                    classes[key].append(new)
        B[n] = [g for group in classes.values() for g in group]
    return B


def witnesses():
    # Core is K4 minus XY; each ear is attached to one existing core edge.
    A,B,X,Y,p,q,r,s = range(8)
    core = [(A,B),(A,X),(B,X),(A,Y),(B,Y)]
    grouped = [(A,p),(X,p),(A,q),(X,q),(B,r),(Y,r),(B,s),(Y,s)]
    spread = [(A,p),(X,p),(A,q),(Y,q),(B,r),(X,r),(B,s),(Y,s)]
    return make_graph(8, core+grouped), make_graph(8, core+spread)


def check_2tree(g):
    g = tuple(g)
    while len(g) > 3:
        n=len(g)
        ears = [v for v in range(n) if g[v].bit_count()==2]
        assert ears
        v=ears[0]
        u,w=[j for j in range(n) if (g[v]>>j)&1]
        assert (g[u]>>w)&1
        keep=[z for z in range(n) if z!=v]
        g=make_graph(n-1, [(i,j) for i in range(n-1) for j in range(i+1,n-1) if (g[keep[i]]>>keep[j])&1])
    assert len(edges(g))==3


def main():
    allgraphs = enumerate_2trees()
    expected = {3:1,4:1,5:2,6:5,7:12,8:39}
    assert {n:len(gs) for n,gs in allgraphs.items()} == expected
    collisions=[]
    for n,gs in allgraphs.items():
        for g in gs:
            assert len(edges(g))==2*n-3
            check_2tree(g)
        pairs=[(i,j) for i,j in combinations(range(len(gs)),2) if joint_refinement_equal(gs[i],gs[j])]
        assert len(pairs)==(1 if n==8 else 0), (n,pairs)
        print('ORDER',n,'ISOMORPHISM_TYPES',len(gs),'C2_CLASSES',len(gs)-len(pairs),'COLLISION_PAIRS',len(pairs))
        if n==8:collisions=[(gs[i],gs[j]) for i,j in pairs]
    g,h=witnesses()
    for z in (g,h):check_2tree(z)
    assert not isomorphic(g,h)
    assert joint_refinement_equal(g,h)
    assert any((isomorphic(g,a) and isomorphic(h,b)) or (isomorphic(g,b) and isomorphic(h,a)) for a,b in collisions)
    for z in (g,h):
        d = degree(z)
        assert Counter(d)==Counter({2:4,4:2,5:2})
        for v in range(8):
            count = Counter(d[w] for w in range(8) if (z[v]>>w)&1)
            expected = {2:{5:1,4:1},4:{5:2,2:2},5:{5:1,4:2,2:2}}[d[v]]
            assert count==expected,(v,count,expected)
    def ear_neighbor_sets(z):
        d=degree(z)
        return [frozenset(w for w in range(8) if (z[v]>>w)&1) for v in range(8) if d[v]==2]
    assert len(set(ear_neighbor_sets(g)))==2
    assert len(set(ear_neighbor_sets(h)))==4
    print('WITNESS_OK', 'degrees=',sorted(degree(g)), 'core=K4-minus-edge', 'one nontrivial C2 class')
    print('VERIFY_OK')

if __name__=='__main__':main()
