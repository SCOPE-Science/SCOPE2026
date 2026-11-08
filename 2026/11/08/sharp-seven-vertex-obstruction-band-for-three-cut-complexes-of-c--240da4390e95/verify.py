#!/usr/bin/env python3
"""Exact reproducibility checks for a seven-vertex simplicial-link obstruction."""
from itertools import combinations
from math import ceil


def adjacency(n, p, a, b):
    d = (a-b) % n
    return 0 < min(d, n-d) <= p


def triple_disconnected(n, p, tr):
    seen = {tr[0]}
    stack = [tr[0]]
    while stack:
        x = stack.pop()
        for y in tr:
            if y not in seen and adjacency(n, p, x, y):
                stack.append(y)
                seen.add(y)
    return len(seen) < 3


def cut_faces(n, p):
    vertices = set(range(n))
    facets = {frozenset(vertices.difference(tr))
              for tr in combinations(range(n), 3)
              if triple_disconnected(n, p, tr)}
    fs = {frozenset()}
    for facet in facets:
        for k in range(1, len(facet)+1):
            fs.update(frozenset(a) for a in combinations(sorted(facet), k))
    return fs, facets


def collapse_pairs(faces):
    S = set(faces)
    pairs = []
    while True:
        options = []
        for face in S:
            if not face:
                continue
            supersets = [s for s in S if face < s]
            if len(supersets) == 1:
                big = supersets[0]
                if len(big) == len(face)+1:
                    options.append((face, big))
        if not options:
            break
        face, big = min(options, key=lambda pair:
                        (-len(pair[0]), tuple(sorted(pair[0])), tuple(sorted(pair[1]))))
        assert face in S and big in S
        S.remove(face)
        S.remove(big)
        pairs.append((tuple(sorted(face)),tuple(sorted(big))))
    return S, pairs


def check_seed():
    faces, facets = cut_faces(7, 2)
    assert len(facets) == 7
    fvector = tuple(sum(len(f)==k for f in faces) for k in range(1, 5))
    assert fvector == (7, 21, 21, 7), fvector
    triples = {tuple(sorted(set(range(7)).difference(F))) for F in facets}
    assert triples == {tuple(sorted((i,(i+3)%7,(i+4)%7))) for i in range(7)}
    residual, pairs = collapse_pairs(faces)
    assert len(pairs) == 25, len(pairs)
    assert residual == {frozenset()} | {frozenset((i,)) for i in (4,5,6)} | {
        frozenset(e) for e in combinations((4,5,6), 2)}, residual
    print('SEED_OK', 'facets=7', 'fvector=7,21,21,7', 'collapse_pairs=25',
          'remaining_cycle=4-5-6-4')
    print('COLLAPSE_CERTIFICATE_BEGIN')
    for j, (a, b) in enumerate(pairs, 1):
        print(f'{j:02d} {",".join(map(str,a))} | {",".join(map(str,b))}')
    print('COLLAPSE_CERTIFICATE_END')


def check_embedding(p, n):
    W = [j*n//7 for j in range(7)]
    assert len(set(W)) == 7
    for i, j in combinations(range(7), 2):
        assert adjacency(n, p, W[i], W[j]) == adjacency(7, 2, i, j), (p,n,i,j,W)
    return W


def check_sharpness_small():
    tested = 0
    for p in range(2, 5):
        for n in range(2*p+1, 4*p+4):
            exists = False
            for W in combinations(range(n), 7):
                if all(adjacency(n,p,W[i],W[j]) == adjacency(7,2,i,j)
                       for i,j in combinations(range(7),2)):
                    exists = True
                    break
            expected = ceil(7*(p+1)/3) <= n <= (7*p//2)
            assert exists == expected, (p,n,exists,expected)
            tested += 1
    print('EXHAUSTIVE_SMALL_OK','p=2..4','cases='+str(tested))


def check_inclusions():
    cases = 0
    for p in range(2, 101):
        for n in range(ceil(7*(p+1)/3), 7*p//2 + 1):
            check_embedding(p, n)
            cases += 1
    assert cases > 1000
    print('EMBEDDING_OK', 'p=2..100', 'cases='+str(cases))
    # Verify the link formula explicitly for representative graph sizes.
    checked = 0
    for p in range(2, 7):
        for n in range(ceil(7*(p+1)/3), 7*p//2 + 1):
            W = set(check_embedding(p,n))
            comp = frozenset(set(range(n)) - W)
            seed_facets = {frozenset(i for i in range(7) if i not in tr)
                           for tr in combinations(range(7),3)
                           if triple_disconnected(7,2,tr)}
            by_embedding = {frozenset(sorted(W)[i] for i in F) for F in seed_facets}
            ambient_link_facets = set()
            for tr in combinations(range(n),3):
                if not triple_disconnected(n,p,tr):
                    continue
                F = frozenset(set(range(n))-set(tr))
                if comp.issubset(F):
                    ambient_link_facets.add(F-comp)
            assert ambient_link_facets == by_embedding, (p,n)
            checked += 1
    print('LINK_OK','p=2..6','cases='+str(checked))


if __name__ == '__main__':
    check_seed()
    check_sharpness_small()
    check_inclusions()
    print('ALL_VERIFY_OK')
