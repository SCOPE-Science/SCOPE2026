#!/usr/bin/env python3
"""Finite checks for radius-three Rips complexes of affine-plane nets.

Uses only the Python standard library; exact integer and binary arithmetic.
The theorem for all affine planes follows from the separate incidence proof.
"""
from collections import deque, defaultdict
from itertools import combinations, product
from math import comb


def affine_net(q):
    assert q in (2, 3, 5, 7), 'This coordinate construction uses prime orders.'
    pts = [('P', x, y) for x in range(q) for y in range(q)]
    lines = [('L', m, b) for m in range(q) for b in range(q)]
    v = pts + lines
    ix = {a: i for i, a in enumerate(v)}
    adj = [set() for _ in v]
    for x in range(q):
        for y in range(q):
            for m in range(q):
                p = ix[('P', x, y)]
                ell = ix[('L', m, (y - m * x) % q)]
                adj[p].add(ell)
                adj[ell].add(p)
    blocks = [[ix[('P', x, y)] for y in range(q)] for x in range(q)]
    blocks += [[ix[('L', m, b)] for b in range(q)] for m in range(q)]
    return v, adj, blocks


def graph_distances(adj):
    out = []
    for s in range(len(adj)):
        d = [-1] * len(adj)
        d[s] = 0
        queue = deque([s])
        while queue:
            a = queue.popleft()
            for b in adj[a]:
                if d[b] < 0:
                    d[b] = d[a] + 1
                    queue.append(b)
        assert all(z >= 0 for z in d)
        out.append(d)
    return out


def all_net_faces(blocks):
    faces = set()
    for z in product(*[(None, *block) for block in blocks]):
        face = tuple(sorted(a for a in z if a is not None))
        if face:
            assert face not in faces
            faces.add(face)
    return faces


def rank_mod2_boundaries(faces):
    by = defaultdict(list)
    for f in faces:
        by[len(f) - 1].append(f)
    for arr in by.values():
        arr.sort()
    ranks = {}
    for d in range(1, max(by) + 1):
        lower = {face: i for i, face in enumerate(by[d - 1])}
        pivot = {}
        for f in by[d]:
            word = 0
            for j in range(len(f)):
                word ^= 1 << lower[f[:j] + f[j + 1:]]
            while word:
                h = word.bit_length() - 1
                if h in pivot:
                    word ^= pivot[h]
                else:
                    pivot[h] = word
                    break
        ranks[d] = len(pivot)
    betti = {d: len(by[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d in by}
    return ranks, betti


def check(q):
    verts, adj, blocks = affine_net(q)
    d = graph_distances(adj)
    assert len(verts) == 2 * q * q
    assert sum(map(len, adj)) // 2 == q**3
    assert max(max(row) for row in d) == 4
    id_to_block = {a: i for i, block in enumerate(blocks) for a in block}
    assert len(id_to_block) == len(verts)
    for i in range(len(verts)):
        for j in range(i + 1, len(verts)):
            a, b = verts[i], verts[j]
            if a[0] == b[0]:
                expected = 4 if id_to_block[i] == id_to_block[j] else 2
            else:
                expected = 1 if j in adj[i] else 3
            assert d[i][j] == expected, (q, a, b, d[i][j], expected)
            assert (d[i][j] <= 3) == (id_to_block[i] != id_to_block[j])
    print('order', q, 'vertices', len(verts), 'edges', q**3,
          'blocks', len(blocks), 'predicted top betti', (q-1)**(2*q))
    if q <= 3:
        faces = all_net_faces(blocks)
        f_vector = tuple(sum(len(f) == k for f in faces)
                         for k in range(1, 2*q + 1))
        assert f_vector == tuple(comb(2*q,k)*q**k for k in range(1, 2*q+1))
        assert all(all(d[i][j] <= 3 for i, j in combinations(f, 2)) for f in faces)
        ranks, betti = rank_mod2_boundaries(faces)
        assert all((betti[k] == (q - 1)**(2*q) if k == 2*q-1
                    else betti[k] == (1 if k == 0 else 0)) for k in betti)
        print('order', q, 'face_vector', f_vector,
              'boundary_ranks', ranks, 'mod2_betti', betti)

if __name__ == '__main__':
    for order in (2,3,5,7):
        check(order)
    print('AFFINE_NET_SCALE3_CHECKS_OK')
