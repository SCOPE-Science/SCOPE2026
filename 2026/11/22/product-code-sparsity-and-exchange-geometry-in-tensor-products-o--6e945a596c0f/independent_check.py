"""Independent finite checks using graph neighborhoods and explicit tensor vertices.
Run: python independent_check.py
Requires only Python 3 standard library.
"""
from itertools import combinations, product
from collections import Counter
from math import prod


def graph(bicliques):
    shores = [tuple((i, side, vertex)
                    for side, size in enumerate(pair)
                    for vertex in range(size))
              for i, pair in enumerate(bicliques)]
    vertices = list(product(*shores))
    neighbours = []
    for v in vertices:
        neighbours.append({j for j,w in enumerate(vertices)
                           if all(x[1] != y[1] for x,y in zip(v,w))})
    return vertices, neighbours


def is_code(subset, neighbours):
    chosen = set(subset)
    return all(len(chosen & nbh) == 1 for nbh in neighbours)


def product_codes(bicliques, vertices):
    choices = [list(product(range(p),range(q))) for p,q in bicliques]
    for factors in product(*choices):
        choice = [{(i,0):pair[0], (i,1):pair[1]} for i,pair in enumerate(factors)]
        yield frozenset(j for j,v in enumerate(vertices)
                        if all(x[2] == choice[i][i,x[1]] for i,x in enumerate(v)))


def enumerate_case(bicliques):
    vertices, neighbours = graph(bicliques)
    n = len(vertices)
    r=len(bicliques)
    assert r == 2
    success = {frozenset(c) for c in combinations(range(n),4)
               if is_code(c, neighbours)}
    B=prod(p*q for p,q in bicliques)
    assert len(success)==B*B
    generated=set(product_codes(bicliques,vertices))
    assert len(generated)==B and generated <= success
    chosen=next(iter(generated))
    dist=Counter(4-len(chosen & other) for other in generated)
    s=[p+q-2 for p,q in bicliques]
    expected={0:1,2:sum(s),3:prod(s),4:B-prod(p+q-1 for p,q in bicliques)}
    assert dist==expected,(dist,expected)
    print('independent r=2',bicliques, 'codes',len(success),'products',B,'dist',dict(dist),'PASS')


def sharp_cover_radius_example():
    # For each of the three dimensions, give each side-pattern its own
    # coordinate label. Any two non-complementary positions then conflict.
    from itertools import product
    r=3
    patterns=list(product((0,1),repeat=r))
    ambient={}
    for e in patterns:
        labels=[]
        for i in range(r):
            rest=tuple(e[j] for j in range(r) if j!=i)
            labels.append(rest[0]*2+rest[1])
        ambient[e]=tuple(labels)
    best=0
    for chosen in product(range(4),repeat=2*r):
        common=sum(all(chosen[2*i+e[i]]==ambient[e][i] for i in range(r))
                   for e in patterns)
        best=max(best,common)
    assert best==2,best
    print('r=3 4x4 biclique factors: sharp covering radius',8-best,'PASS')

def sample_arity_three():
    pair=[(2,2)]*3
    vertices,ng=graph(pair)
    generated=list(product_codes(pair,vertices))
    assert len(generated)==64 and len(set(generated))==64
    assert all(is_code(c,ng) for c in generated)
    chosen=generated[0]
    dist=Counter(8-len(chosen&other) for other in generated)
    assert dist=={0:1,4:6,6:12,7:8,8:37},dist
    # 1000 deterministic componentwise random points, sampled from larger family.
    import random
    rng=random.Random(126734)
    choices={}
    for j,v in enumerate(vertices):
        e=tuple(x[1] for x in v)
        choices.setdefault(e,[]).append(j)
    for _ in range(1000):
        code=frozenset(rng.choice(options) for options in choices.values())
        assert len(code)==8 and is_code(code,ng)
    print('independent r=3',pair,'products',len(generated),
          'predicted_all',64**4,'distance',dict(dist),'1000 valid samples PASS')

if __name__ == '__main__':
    enumerate_case([(2,2),(2,2)])
    enumerate_case([(2,3),(2,2)])
    sample_arity_three()
    sharp_cover_radius_example()
