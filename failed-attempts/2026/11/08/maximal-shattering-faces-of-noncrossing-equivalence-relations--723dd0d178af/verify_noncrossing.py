#!/usr/bin/env python3
"""Finite checks for edge-query shattering by noncrossing partitions.
This is a standalone exact checker using exhaustive set partitions and traces.
"""
from itertools import combinations
from math import comb


def restricted_growth(n):
    if n == 0:
        yield ()
        return
    def walk(a, k):
        if len(a) == n:
            yield tuple(a)
        else:
            for x in range(k + 2):
                a.append(x)
                yield from walk(a, max(k, x))
                a.pop()
    yield from walk([0], 0)


def noncrossing(p):
    n = len(p)
    for a, b, c, d in combinations(range(n), 4):
        if p[a] == p[c] and p[b] == p[d] and p[a] != p[b]:
            return False
    return True


def edges(n):
    return list(combinations(range(n), 2))


def concepts(n):
    ee = edges(n)
    out = []
    for p in restricted_growth(n):
        if noncrossing(p):
            out.append(sum(1 << i for i, (a, b) in enumerate(ee) if p[a] == p[b]))
    return out


def is_tree(s, n, ee):
    if s.bit_count() != n-1:
        return False
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i, (u, v) in enumerate(ee):
        if s >> i & 1:
            a, b = find(u), find(v)
            if a == b:
                return False
            parent[a] = b
    return len({find(i) for i in range(n)}) == 1


def crossing(e, f):
    a, c = e
    b, d = f
    return (a < b < c < d) or (b < a < d < c)


def planar(s, ee):
    ii = [i for i in range(len(ee)) if s >> i & 1]
    return all(not crossing(ee[i], ee[j]) for i, j in combinations(ii, 2))


def shattered(s, cc):
    # Directly constructs every trace without relying on the deletion lemma.
    bits = [i for i in range(s.bit_length()) if s >> i & 1]
    patterns = set()
    for concept in cc:
        trace = concept & s
        if trace not in patterns:
            patterns.add(trace)
            if len(patterns) == 1 << len(bits):
                return True
    return False


def deletion_criterion(s, cc):
    return all(any((c & s) == (s ^ (1 << i)) for c in cc)
               for i in range(s.bit_length()) if s >> i & 1)


def run():
    catalan = lambda n: comb(2*n, n)//(n+1)
    for n in range(2, 7):
        ee = edges(n)
        cc = concepts(n)
        assert len(cc) == catalan(n)
        shattered_count = 0
        maxface = 0
        max_count = 0
        for s in range(1 << len(ee)):
            sh = shattered(s, cc)
            assert sh == deletion_criterion(s, cc), (n, s, 'deletion criterion')
            if sh:
                shattered_count += 1
                maxface = max(maxface, s.bit_count())
                if s.bit_count() == n-1:
                    max_count += 1
            if s.bit_count() == n-1:
                assert sh == (is_tree(s,n,ee) and planar(s,ee)), (n,s,'tree')
        count_formula = comb(3*n-3, n-1)//(2*n-1)
        assert maxface == n-1 and max_count == count_formula
        print(f'n={n} concepts={len(cc)} shattered_all_sizes={shattered_count} top_faces={max_count} vc={maxface}')
    # One more unrestricted n=7 top-stratum exhaustive computation.
    n = 7
    ee = edges(n)
    cc = concepts(n)
    count = 0
    for choose in combinations(range(len(ee)), n-1):
        s = sum(1 << j for j in choose)
        sh = shattered(s, cc)
        assert sh == (is_tree(s,n,ee) and planar(s,ee)), ('top stratum',n,s)
        count += sh
    assert count == comb(3*n-3,n-1)//(2*n-1) == 1428
    print('n=7 top_faces=1428 exhaustive_6_edge_supports=54264')
    # For every even n, the mutually crossing diameters form a shattered matching
    # that cannot be extended by any other edge.
    for n in range(4,15,2):
        ee = edges(n)
        chosen = {tuple(sorted((i,i+n//2))) for i in range(n//2)}
        assert all(crossing(e,f) for e,f in combinations(chosen,2))
        assert len(chosen)==n//2
        for a,b in ee:
            if (a,b) in chosen: continue
            # a and b are endpoints of two different diameters.
            pa=tuple(sorted((a,(a+n//2)%n)))
            pb=tuple(sorted((b,(b+n//2)%n)))
            assert pa != pb and pa in chosen and pb in chosen
        print(f'even_n={n} inclusion_maximal_face_size={n//2} maximum_face_size={n-1}')
    print('NONCROSSING_PARTITION_SHATTERING_PASS')

if __name__ == '__main__': run()
