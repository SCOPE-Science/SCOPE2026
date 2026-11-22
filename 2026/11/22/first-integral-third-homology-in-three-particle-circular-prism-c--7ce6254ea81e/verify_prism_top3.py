#!/usr/bin/env python3
"""Exact finite proof certificate for the first nonzero top H3 of three-particle cyclic prisms.

Requires only Python 3.10+. All edge/vertex cells are enumerated, with exact F2
boundary column elimination. The two torus generators are checked integrally.
"""
from itertools import combinations, product
from collections import defaultdict


def subdivided_prism(n):
    assert n >= 3
    original = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    original |= {tuple(sorted((n+i, n+(i + 1) % n))) for i in range(n)}
    original |= {(i, n+i) for i in range(n)}
    original = tuple(sorted(original))
    midpoint = {e: 2*n+j for j,e in enumerate(original)}
    edges = tuple(sorted(tuple(sorted((v, midpoint[(a,b)])))
                         for a,b in original for v in (a,b)))
    indices = {e: i for i,e in enumerate(edges)}
    return 2*n+len(original), edges, indices, midpoint


def cells(k, num_verts, edges):
    for es in combinations(range(len(edges)), k):
        support = 0
        for e in es:
            u,v = edges[e]
            support |= (1<<u) | (1<<v)
        if support.bit_count() != 2*k:
            continue
        remaining = (v for v in range(num_verts) if not (support>>v)&1)
        for vs in combinations(remaining, 3-k):
            yield vs, es


def rank_mod2_d3(n):
    nv,edges,_,_ = subdivided_prism(n)
    two = list(cells(2, nv, edges))
    threes = list(cells(3, nv, edges))
    indices = {c:i for i,c in enumerate(two)}
    pivots = {}
    for vertices, es in threes:
        column = 0
        for k,e in enumerate(es):
            others = es[:k] + es[k+1:]
            for v in edges[e]:
                idx = indices[(tuple(sorted(vertices+(v,))),others)]
                column ^= 1 << idx
        while column:
            p = column.bit_length()-1
            if p not in pivots:
                pivots[p] = column
                break
            column ^= pivots[p]
    return (len(two), len(threes), len(pivots), len(threes)-len(pivots))


def oriented_face_edges(n, face, indices, midpoint):
    top_a = face
    top_b = (face+1) % n
    bottom_a = top_a + n
    bottom_b = top_b + n
    face_path = (top_a, top_b, bottom_b, bottom_a, top_a)
    result = []
    for a,b in zip(face_path[:-1], face_path[1:]):
        m = midpoint[tuple(sorted((a,b)))]
        for x,y in ((a,m),(m,b)):
            eid = indices[tuple(sorted((x,y)))]
            sign = 1 if x < y else -1
            result.append((eid, sign))
    assert len(result) == 8
    return result


def triple_face_torus(n, starts, indices, midpoint):
    sums = defaultdict(int)
    cycles = [oriented_face_edges(n, i, indices, midpoint) for i in starts]
    for factors in product(*cycles):
        edge_ids = [e for e,_ in factors]
        assert len(set(edge_ids)) == 3
        inversion_count = sum(edge_ids[i] > edge_ids[j]
                              for i in range(3) for j in range(i+1,3))
        sign = (-1 if inversion_count & 1 else 1)
        for _, coeff in factors: sign *= coeff
        sums[tuple(sorted(edge_ids))] += sign
    return {k:v for k,v in sums.items() if v}


def check_cycle(torus, edges):
    boundary = defaultdict(int)
    for es, coeff in torus.items():
        support = [v for e in es for v in edges[e]]
        assert len(set(support)) == 6, (es, support)
        for j,e in enumerate(es):
            other = es[:j] + es[j+1:]
            u,v = edges[e]
            boundary[((v,),other)] += coeff * (-1)**j
            boundary[((u,),other)] -= coeff * (-1)**j
    return {k:v for k,v in boundary.items() if v}


def main():
    for n,expected in ((3,(1386,432,432,0)),
                       (4,(3840,1296,1296,0)),
                       (5,(8190,2880,2880,0)),
                       (6,(14976,5400,5398,2))):
        actual = rank_mod2_d3(n)
        assert actual == expected, (n,actual,expected)
        print('N',n,'C2,C3,RANK_F2_D3,KERNEL_F2',actual)
    n=6
    _, edges, indices, midpoint = subdivided_prism(n)
    even = triple_face_torus(n,(0,2,4),indices,midpoint)
    odd  = triple_face_torus(n,(1,3,5),indices,midpoint)
    assert not check_cycle(even,edges)
    assert not check_cycle(odd,edges)
    def witness(indices_of_faces):
        out=[]
        for f in indices_of_faces:
            a,b=f,(f+1)%n
            m=midpoint[tuple(sorted((a,b)))]
            out.append(indices[tuple(sorted((a,m)))])
        return tuple(sorted(out))
    w0=witness((0,2,4))
    w1=witness((1,3,5))
    evaluation=((even.get(w0,0),odd.get(w0,0)),
                (even.get(w1,0),odd.get(w1,0)))
    det=evaluation[0][0]*evaluation[1][1]-evaluation[0][1]*evaluation[1][0]
    assert abs(det)==1, (evaluation,det)
    print('TORI',len(even),len(odd),'WITNESSES',w0,w1,'EVAL',evaluation,'DET',det)
    print('PRISM_THREE_POINT_TOP_HOMOLOGY_OK')

if __name__ == '__main__': main()
