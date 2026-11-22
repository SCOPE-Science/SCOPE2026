#!/usr/bin/env python3
"""Standalone finite checks for intrinsic Čech nerves of crown graphs.

No external packages. Integer-scale generators are derived from graph distances.
The general homotopy and equivariant assertions require the written proof.
"""
from itertools import permutations


def graph(n):
    V = tuple(range(2*n))
    E = {(i, n+j) for i in range(n) for j in range(n) if i != j}
    adj = {i: set() for i in V}
    for a,b in E:
        adj[a].add(b); adj[b].add(a)
    return V, E, adj


def neighborhoods(n, radius):
    V,E,adj = graph(n)
    dist = {}
    for v in V:
        d = {v: 0}
        todo = [v]
        for x in todo:
            for y in adj[x]:
                if y not in d:
                    d[y] = d[x]+1
                    todo.append(y)
        assert len(d) == len(V)
        dist[v] = d
    return {v: sum(1 << w for w in V if dist[v][w] <= radius) for v in V}


def facets(n, scale):
    V,E,adj = graph(n)
    q = scale // 2
    ball = neighborhoods(n,q)
    if scale % 2:
        return {ball[a] | ball[b] for a,b in E}
    return set(ball.values())


def downclosure(F):
    found = {0}
    for f in F:
        s = f
        while True:
            found.add(s)
            if s == 0: break
            s = (s-1) & f
    return found


def popcount(x):
    return x.bit_count()


def mod2_rank(vecs):
    piv = {}
    for x in vecs:
        while x:
            p = x.bit_length()-1
            if p not in piv:
                piv[p] = x; break
            x ^= piv[p]
    return len(piv)


def homology_mod2(faces, n):
    by_size = {}
    for f in faces:
        by_size.setdefault(popcount(f), []).append(f)
    max_size = max(by_size)
    rank = {1: 1}  # augmented boundary to the empty face
    for k in range(2, max_size+1):
        index = {f:i for i,f in enumerate(by_size.get(k-1, []))}
        cols = []
        for f in by_size.get(k, []):
            x = 0; bits = f
            while bits:
                low = bits & -bits
                x |= 1 << index[f ^ low]
                bits -= low
            cols.append(x)
        rank[k] = mod2_rank(cols)
    return {k-1: len(by_size[k]) - rank.get(k,0) - rank.get(k+1,0)
            for k in range(1,max_size+1)
            if len(by_size[k]) - rank.get(k,0) - rank.get(k+1,0) != 0}


def signature(values):
    inversions = sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))
    return -1 if inversions%2 else 1


def lefschetz_reduced(faces, perm):
    total = -1  # subtract the H_0 trace from ordinary Lefschetz
    for s in faces:
        if not s: continue
        verts = [i for i in range(len(perm)) if s >> i & 1]
        moved = [perm[i] for i in verts]
        if sorted(moved) != verts: continue
        ordered = [verts.index(j) for j in moved]
        total += (-1)**(len(verts)-1) * signature(ordered)
    return total


def check(n):
    V,E,adj=graph(n)
    full=(1 << (2*n))-1
    fs3 = facets(n,3)
    expected = {full ^ (1<<i) ^ (1<<(n+j)) for i in range(n) for j in range(n) if i != j}
    assert fs3 == expected, (n, 'scale-three maximal support mismatch')
    fs4 = facets(n,4)
    assert fs4 == {full ^ (1<<i) for i in V}
    fs5 = facets(n,5)
    assert fs5 == {full}
    k3 = downclosure(fs3)
    # Join of two simplex boundaries: proper subsets of both sides.
    a_mask = (1<<n)-1
    b_mask = full ^ a_mask
    join = {s for s in range(full+1) if s & a_mask != a_mask and s & b_mask != b_mask}
    deleted = {full ^ (1<<i) ^ (1<<(n+i)) for i in range(n)}
    assert k3 == join - deleted
    betti = homology_mod2(k3,n)
    assert betti == {2*n-4: n-1}, (n,betti)
    # Equivariant trace on the only reduced homology group.
    sampled = list(permutations(range(n))) if n <= 4 else [tuple(range(n)),tuple(reversed(range(n))),tuple((i+1)%n for i in range(n))]
    for pi in sampled:
        f = sum(pi[i]==i for i in range(n))
        for swap in (False,True):
            perm = [n+pi[i] if swap else pi[i] for i in range(n)] + [pi[i] if swap else n+pi[i] for i in range(n)]
            actual=lefschetz_reduced(k3,perm)
            predicted=(f-1)*((-1)**(n-1) if swap else 1)
            assert actual==predicted, (n,pi,swap,actual,predicted)
    print('n=%d; vertices=%d; scale3_facets=%d; faces=%d; reduced_F2=%s; symmetry_traces=PASS' % (n,2*n,len(fs3),len(k3),betti))


def main():
    for n in (3,4,5,6):
        check(n)
    print('ALL_FINITE_CHECKS_PASS')

if __name__ == '__main__':
    main()
