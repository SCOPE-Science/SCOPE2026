#!/usr/bin/env python3
"""Independent exhaustive geodesic and mod-two checks for a defective cocktail-party graph."""
from collections import deque
from itertools import combinations
from math import comb


def graph(n):
    """Vertices 2*i = p_i and 2*i+1 = q_i; 0-based indices."""
    size = 2*n
    adj = [set(range(size)) - {v, v^1} for v in range(size)]
    adj[0].remove(2)
    adj[2].remove(0)
    return adj


def all_distances(adj):
    result = []
    for source in range(len(adj)):
        d = [-1] * len(adj)
        d[source] = 0
        queue = deque([source])
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if d[y] < 0:
                    d[y] = d[x] + 1
                    queue.append(y)
        assert all(v >= 0 for v in d)
        result.append(d)
    return result


def faces_from_distances(n):
    dist = all_distances(graph(n))
    faces = []
    for mask in range(1 << (2*n)):
        vertices = [v for v in range(2*n) if (mask >> v) & 1]
        good = True
        for a,b,c in combinations(vertices,3):
            if (dist[a][c] == dist[a][b]+dist[b][c]
                or dist[a][b] == dist[a][c]+dist[c][b]
                or dist[b][c] == dist[b][a]+dist[a][c]):
                good = False
                break
        if good:
            faces.append(mask)
    return faces


def predicted_face(n,mask):
    # Base: crosspolytope boundary with the star of edge {p_0,p_1}
    # punctured above its edge; all matched-pair edges; two exceptional triangles.
    count=mask.bit_count()
    if count <= 2:
        return True
    if count == 3 and mask in ((1<<0)|(1<<1)|(1<<2),
                              (1<<0)|(1<<2)|(1<<3)):
        return True
    if mask & 5 == 5:
        return False
    return all(not ((mask>>(2*i))&1 and (mask>>(2*i+1))&1)
               for i in range(n))


def rank_gf2(columns):
    pivots={}
    for x in columns:
        while x:
            bit=x.bit_length()-1
            if bit in pivots:
                x ^= pivots[bit]
            else:
                pivots[bit]=x
                break
    return len(pivots)


def betti_numbers_mod_two(faces):
    by_dim={}
    for face in faces:
        if face:
            by_dim.setdefault(face.bit_count()-1,[]).append(face)
    boundary_rank={}
    for k in range(1,max(by_dim)+1):
        positions={face:i for i,face in enumerate(by_dim[k-1])}
        columns=[]
        for face in by_dim.get(k,[]):
            col=0
            tmp=face
            while tmp:
                bit=(tmp&-tmp).bit_length()-1
                col ^= 1<<positions[face^(1<<bit)]
                tmp &= tmp-1
            columns.append(col)
        boundary_rank[k]=rank_gf2(columns)
    return {k:len(v)-boundary_rank.get(k,0)-boundary_rank.get(k+1,0)
            for k,v in by_dim.items()}


def expected_f(n,k):
    # (1+2z)^n + n z^2 - z^2((1+2z)^(n-2)-1) + 2z^3
    return ((comb(n,k)*2**k if 0<=k<=n else 0)
        +(n+1 if k==2 else 0)
        + (2 if k==3 else 0)
        -(comb(n-2,k-2)*2**(k-2) if 2<=k<=n else 0))


def main():
    for n in range(3,9):
        faces=faces_from_distances(n)
        known=set(faces)
        assert all(((mask in known)==predicted_face(n,mask))
                   for mask in range(1<<(2*n)))
        f=[sum(m.bit_count()==k for m in faces) for k in range(n+1)]
        assert f == [expected_f(n,k) for k in range(n+1)]
        b=betti_numbers_mod_two(faces)
        assert b.get(0)==1 and b.get(1)==n-1
        assert all(v==0 for k,v in b.items() if k>=2)
        print(f'n={n}: faces(including empty)={len(faces)}, f_vector={f}, '
              f'H_1_mod2_rank={b[1]}, higher_mod2_ranks=0, exact_face_model=OK')
    print('PASS: independent BFS, full face enumeration, binomial f-vector, mod-two chains')

if __name__ == '__main__':
    main()
