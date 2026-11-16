#!/usr/bin/env python3
"""Exact Walsh/orbit computation for labelled forests of complete graphs."""
from collections import Counter
from itertools import combinations, permutations
from math import gcd
from functools import reduce


def forest(mask, edges, n):
    parent = list(range(n))
    def root(i):
        while i != parent[i]:
            i = parent[i]
        return i
    for k, (u, v) in enumerate(edges):
        if mask & (1 << k):
            a, b = root(u), root(v)
            if a == b:
                return False
            parent[a] = b
    return True


def hadamard(a):
    a = a[:]
    step = 1
    while step < len(a):
        for base in range(0, len(a), 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j+step]
                a[j], a[j+step] = u + v, u - v
        step *= 2
    return a


def check():
    for n in range(3, 7):
        edges = list(combinations(range(n), 2))
        E = len(edges)
        F = [int(forest(mask, edges, n)) for mask in range(1 << E)]
        W = hadamard(F)
        assert sum(v*v for v in W) == (1 << E)*sum(F)
        if n < 6:
            assert 0 not in W
        if n == 3:
            assert sum(F) == 7
        elif n == 4:
            assert sum(F) == 38
        elif n == 5:
            assert sum(F) == 291
        else:
            assert sum(F) == 2932
            assert len(W) == 32768
            zeros = {i for i, x in enumerate(W) if x == 0}
            assert len(zeros) == 3105
            assert Counter(i.bit_count() for i in zeros) == {5:180,7:1080,9:1800,11:45}
            assert min(abs(x) for x in W if x) == 4
            assert reduce(gcd, W) == 4
            assert len(set(W)) == 49
            assert W[0] == 2932
            signed = Counter(W)
            assert sum(signed.values()) == 32768
            print('SIGNED_LEVELS=' + ';'.join('%s:%s'%(v,signed[v]) for v in sorted(signed)))
            edgeid = {e:j for j,e in enumerate(edges)}
            rem = zeros.copy()
            reps = []
            perm_maps = []
            for p in permutations(range(n)):
                perm_maps.append([edgeid[tuple(sorted((p[u],p[v])))] for u,v in edges])
            while rem:
                rep = min(rem)
                orbit = set()
                for pm in perm_maps:
                    img = 0
                    for e in range(E):
                        if rep >> e & 1:
                            img |= 1 << pm[e]
                    orbit.add(img)
                assert orbit.issubset(zeros)
                assert orbit.issubset(rem)
                rem.difference_update(orbit)
                reps.append((rep,len(orbit),rep.bit_count()))
            assert len(reps) == 10
            assert Counter(m for _,m,_ in reps) == {45:1,90:2,180:2,360:3,720:2}
            print('ORBIT_REPS=' + ';'.join('%s:%s:%s'%r for r in reps))
            P = [int(w != 0) for w in W]
            numerator = sum(abs(x) for x in hadamard(P))
            d = gcd(numerator, 1 << E)
            assert numerator == 1210058
            assert (numerator // d, (1 << E)//d) == (605029,16384)
            print('K6 forests=2932 rank=29663 nullity=3105 gap=4 orbits=10 projection_L1=605029/16384')
    print('VERIFY_WALSH_OK')
if __name__ == '__main__':
    check()
