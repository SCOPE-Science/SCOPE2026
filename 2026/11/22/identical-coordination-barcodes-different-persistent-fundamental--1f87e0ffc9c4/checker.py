"""Exact finite checks for square-grid coordination filtrations.

Run: python checker.py
Uses only Python's standard library; symbolic all-size proof is in RESULT.md.
"""
from collections import defaultdict


def graph(L, twisted):
    v = [(x, y) for y in range(L) for x in range(L)]
    edges = set()
    def add(a, b):
        assert a != b
        edges.add(tuple(sorted((a, b))))
    for x, y in v:
        add((x, y), ((x+1) % L, y))
        if y < L-1:
            add((x, y), (x, y+1))
        else:
            add((x, y), ((-x) % L if twisted else x, 0))
    adj = {a: set() for a in v}
    for a,b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return v, sorted(edges), adj


def face_vertices(L, twisted):
    faces = []
    for y in range(L):
        for x in range(L):
            xx = (x+1) % L
            if y < L-1:
                v = ((x,y),(xx,y),(xx,y+1),(x,y+1))
            else:
                xx0 = (-xx)%L if twisted else xx
                x0 = (-x)%L if twisted else x
                v = ((x,y),(xx,y),(xx0,0),(x0,0))
            faces.append(v)
    return faces


def cycvec(c, index):
    out = 0
    for a,b in zip(c, c[1:]+c[:1]):
        out ^= 1 << index[tuple(sorted((a,b)))]
    return out


def rank_mod2(vecs):
    piv = {}
    for val in vecs:
        x = val
        while x:
            k = x.bit_length() - 1
            if k in piv:
                x ^= piv[k]
            else:
                piv[k] = x
                break
    return len(piv)


def all_3_4_cycles(vertices, adj):
    cycles3, cycles4 = set(), set()
    for a in vertices:
        for b in adj[a]:
            for c in adj[b] - {a}:
                if c in adj[a]:
                    cycles3.add(frozenset((a,b,c)))
                for d in adj[c] - {a,b}:
                    if d in adj[a] and len({a,b,c,d}) == 4:
                        cycles4.add(frozenset((a,b,c,d)))
    return cycles3, cycles4


def short_simple_cycles(vertices, adj, limit):
    # Vertices of cycle are restricted to have smallest start; normalized to
    # avoid repetitions in both directions.
    idx = {a: i for i, a in enumerate(vertices)}
    found = set()
    for a in vertices:
        for b in adj[a]:
            if idx[b] <= idx[a]:
                continue
            stack = [(b, [a,b], frozenset((a,b)))]
            while stack:
                z,path,used = stack.pop()
                for w in adj[z]:
                    if w == a:
                        if len(path)>=3:
                            body = path[1:]
                            if idx[body[0]] < idx[body[-1]]:
                                found.add(tuple(path))
                    elif len(path)<limit and w not in used and idx[w]>idx[a]:
                        stack.append((w,path+[w],used|{w}))
    return found


def check(L, twisted):
    vv,ee,adj=graph(L,twisted)
    assert len(vv)==L*L and len(ee)==2*L*L
    idx = {e:i for i,e in enumerate(ee)}
    faces = face_vertices(L,twisted)
    face_sets = {frozenset(f) for f in faces}
    assert len(face_sets)==L*L
    for f in faces:
        assert all(tuple(sorted((a,b))) in idx for a,b in zip(f,f[1:]+f[:1]))
    triangles, squares = all_3_4_cycles(vv,adj)
    assert not triangles
    assert squares==face_sets, (L,twisted,len(squares),len(face_sets))
    fv = [cycvec(list(f),idx) for f in faces]
    assert rank_mod2(fv)==L*L-1
    horiz = [(x,0) for x in range(L)]
    vert = [(0,y) for y in range(L)]
    assert rank_mod2(fv+[cycvec(horiz,idx),cycvec(vert,idx)]) == L*L+1
    checked_short = 0
    if L<=7:
        # Extra exact check: every simple cycle shorter than the systole is
        # an F2 combination of square faces.
        short=short_simple_cycles(vv,adj,L-1)
        checked_short = len(short)
        for c in short:
            assert rank_mod2(fv+[cycvec(list(c),idx)]) == L*L-1
    return {'side': L, 'twisted': twisted, 'vertices':len(vv),
        'edges':len(ee),'square_faces':len(face_sets),
        'square_boundary_rank':rank_mod2(fv),
        'cycle_space_rank':len(ee)-len(vv)+1,
        'independent_winding_classes':2,
        'short_simple_cycles_checked':checked_short}


if __name__=='__main__':
    for L in (5,6,7,8,9):
        for twist in (False,True):
            print(check(L,twist))
    print('ALL FINITE CHECKS PASS; all-L statement requires the supplied proof.')
