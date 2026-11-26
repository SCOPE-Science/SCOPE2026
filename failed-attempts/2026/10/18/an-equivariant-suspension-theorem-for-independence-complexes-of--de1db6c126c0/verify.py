#!/usr/bin/env python3
"""Finite sanity checks for the equivariant Mycielski suspension theorem."""
from itertools import combinations, permutations


def graph(n, edges):
    adj = [0] * n
    for i, j in edges:
        assert 0 <= i < j < n
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    return adj


def mycielski(adj):
    n = len(adj)
    out = [0] * (2 * n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            if adj[i] >> j & 1:
                for a, b in ((i, j), (i, n + j), (j, n + i)):
                    out[a] |= 1 << b
                    out[b] |= 1 << a
        out[n + i] |= 1 << (2 * n)
        out[2 * n] |= 1 << (n + i)
    return out


def independent(mask, adj):
    for i in range(len(adj)):
        if mask >> i & 1 and adj[i] & mask:
            return False
    return True


def faces(adj):
    return [m for m in range(1 << len(adj)) if independent(m, adj)]


def permute_mask(mask, p):
    result = 0
    for i, j in enumerate(p):
        if mask >> i & 1:
            result |= 1 << j
    return result


def sign_restricted(mask, p):
    images = [p[i] for i in range(len(p)) if mask >> i & 1]
    inversions = sum(images[i] > images[j]
                     for i in range(len(images)) for j in range(i + 1, len(images)))
    return -1 if inversions % 2 else 1


def reduced_lefschetz(adj, p):
    s = 0
    for f in faces(adj):
        if permute_mask(f, p) == f:
            exponent = f.bit_count() - 1
            s += (-1 if exponent % 2 else 1) * sign_restricted(f, p)
    return s


def verify(adj, autos):
    n = len(adj)
    m = mycielski(adj)
    asub = m[:2 * n]
    asub = [row & ((1 << (2 * n)) - 1) for row in asub]
    all_a = faces(asub)
    all_g = faces(adj)
    all_k = faces(m)
    shadow = ((1 << n) - 1) << n
    for f in all_a:
        proj = (f & shadow) | ((f & ((1 << n) - 1)) << n)
        assert independent(proj, asub)
        assert independent(f | proj, asub), (n, f, proj)
    for f in all_k:
        if f >> (2 * n) & 1:
            assert f & shadow == 0
            assert (f & ((1 << n) - 1)) in all_g
    assert len(all_k) == len(all_a) + len(all_g)
    for p in autos:
        assert sorted(p) == list(range(n))
        for i in range(n):
            for j in range(n):
                assert bool(adj[i] >> j & 1) == bool(adj[p[i]] >> p[j] & 1)
        pm = p + [n + i for i in p] + [2 * n]
        for f in all_a:
            proj = (f & shadow) | ((f & ((1 << n) - 1)) << n)
            gp = permute_mask(f, pm)
            gproj = (gp & shadow) | ((gp & ((1 << n) - 1)) << n)
            assert permute_mask(proj, pm) == gproj
        assert reduced_lefschetz(m, pm) == -reduced_lefschetz(adj, p)
    return len(all_a), len(all_k)


def run():
    checked = 0
    for bits in range(1 << 6):
        es = list(combinations(range(4), 2))
        adj = graph(4, [edge for k, edge in enumerate(es) if bits >> k & 1])
        automorphisms = [list(p) for p in permutations(range(4))
                          if all((adj[i] >> j & 1) == (adj[p[i]] >> p[j] & 1)
                                 for i in range(4) for j in range(4))]
        verify(adj, automorphisms)
        checked += 1
    for n in (5, 7):
        adj = graph(n, [(i, (i + 1) % n) if i < (i + 1) % n
                        else ((i + 1) % n, i) for i in range(n)])
        autos = [[(sgn * i + shift) % n for i in range(n)]
                for sgn in (1, -1) for shift in range(n)]
        ac, kc = verify(adj, autos)
        print(f'C_{n}: A_faces={ac}, Mycielski_faces={kc}, symmetries={len(autos)}')
    print(f'VERIFY_OK four_vertex_graphs={checked} cycle_examples=2')


if __name__ == '__main__':
    run()
