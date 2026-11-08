"""Exact combinatorial topology certificate for the perfect-matching complex of Q4.

Usage: python3 verify.py
Pure Python standard library. Every face and every Hasse incidence is checked.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 16
EDGES = sorted((u, u ^ (1 << j)) for u in range(N) for j in range(4) if u < (u ^ (1 << j)))
assert len(EDGES) == 32
EDGE_ID = {edge:i for i, edge in enumerate(EDGES)}
ADJ = [[] for _ in range(N)]
for i, (u,v) in enumerate(EDGES):
    ADJ[u].append((v, i)); ADJ[v].append((u, i))
FULL = (1 << N) - 1


def perfect_matchings_by_vertices():
    result = []
    def recurse(free, edges_mask):
        if not free:
            result.append(edges_mask); return
        v = (free & -free).bit_length() - 1
        for w, i in ADJ[v]:
            if free & (1 << w):
                recurse(free ^ (1 << v) ^ (1 << w), edges_mask | (1 << i))
    recurse(FULL, 0)
    return set(result)


def perfect_matchings_by_bipartition():
    even = [u for u in range(N) if u.bit_count() % 2 == 0]
    result = set()
    def recurse(k, used_odd, selected):
        if k == len(even):
            result.add(selected); return
        for v,i in ADJ[even[k]]:
            if not (used_odd & (1 << v)):
                recurse(k+1, used_odd | (1 << v), selected | (1 << i))
    recurse(0, 0, 0)
    return result


def all_faces_from_facets(facets):
    all_faces = {0}
    for facet in facets:
        sub = facet
        while sub:
            all_faces.add(sub)
            sub = (sub-1) & facet
    return all_faces


def check_faces_by_extendability(faces):
    """Enumerate ALL matchings, then test an independent completion DP."""
    @lru_cache(None)
    def completable(free):
        if not free: return True
        u = (free & -free).bit_length() - 1
        return any((free & (1 << v)) and completable(free ^ (1 << u) ^ (1 << v))
                   for v, _ in ADJ[u])
    matching_count = 0
    extendable_count = 0
    def recurse(edge_index, occupied, selected):
        nonlocal matching_count, extendable_count
        if edge_index == len(EDGES):
            matching_count += 1
            ext = completable(FULL ^ occupied)
            if ext: extendable_count += 1
            assert ext == (selected in faces), (selected, ext)
            return
        recurse(edge_index+1, occupied, selected)
        u,v = EDGES[edge_index]
        bits = (1 << u) | (1 << v)
        if not occupied & bits:
            recurse(edge_index+1, occupied | bits, selected | (1 << edge_index))
    recurse(0, 0, 0)
    assert extendable_count == len(faces)
    return matching_count


def boundary(face):
    k=0
    while face:
        b = face & -face
        yield b, (1 if k%2==0 else -1)
        face ^= b
        k += 1


def toggle_matching(faces, backward=False):
    residual = set(faces)
    lower_upper = {}
    upper = set()
    for i in (range(31,-1,-1) if backward else range(32)):
        b=1 << i
        lows = [f for f in residual if not (f & b) and (f | b) in residual]
        for f in lows:
            g=f | b
            residual.remove(f);residual.remove(g)
            lower_upper[f]=g
            upper.add(g)
    assert 2*len(lower_upper)+len(residual)==len(faces)
    assert 0 not in residual  # the empty simplex is matched
    return lower_upper,upper,residual


def check_acyclicity(faces, lower_upper):
    """Orient unmatched covers downwards, matched covers upwards; Kahn test."""
    out = {f:[] for f in faces}
    indeg = {f:0 for f in faces}
    incidences = 0
    for f in faces:
        for b,_ in boundary(f):
            sub=f ^ b
            if lower_upper.get(sub)==f:
                src,dest=sub,f
            else:
                src,dest=f,sub
            out[src].append(dest);indeg[dest]+=1
            incidences+=1
    q=deque(f for f,d in indeg.items() if d==0)
    seen=0
    while q:
        x=q.popleft();seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert seen==len(faces), ('gradient cycle',seen,len(faces))
    return incidences


def morse_boundary(lower_upper,upper,critical,source_dim,target_dim):
    """Exact integer elementary elimination of matched face/coface pairs.

    For (L,U), the relation from d(U)=0 eliminates L. The recursive
    normal form is well-defined by the verified acyclic gradient graph.
    """
    @lru_cache(None)
    def project(f):
        if f in upper:return {}
        if f not in lower_upper:return {f:1}
        u=lower_upper[f]
        pivot_bit=u^f
        pivot_sign=-1 if (f&(pivot_bit-1)).bit_count()%2 else 1
        out={}
        for b,s in boundary(u):
            g=u^b
            if g==f:continue
            for h,c in project(g).items():
                out[h]=out.get(h,0)-pivot_sign*s*c
        return {h:c for h,c in out.items() if c}
    cols=sorted(f for f in critical if f.bit_count()-1==source_dim)
    rows=sorted(f for f in critical if f.bit_count()-1==target_dim)
    lookup={v:i for i,v in enumerate(rows)}
    matrix=[[0]*len(cols) for _ in rows]
    for j,c in enumerate(cols):
        accum={}
        for b,s in boundary(c):
            for h,v in project(c^b).items():accum[h]=accum.get(h,0)+s*v
        for h,v in accum.items():
            if v:
                assert h in lookup
                matrix[lookup[h]][j]=v
    return matrix, (len(rows),len(cols)),project.cache_info().currsize


def unit_reduction(matrix):
    """Exact integral elementary row/column operations, verifying every pivot is a unit."""
    a=[row[:] for row in matrix]
    n=len(a);m=len(a[0]) if n else 0
    k=0
    while k<min(n,m):
        loc=next(((r,c) for r in range(k,n) for c in range(k,m) if abs(a[r][c])==1),None)
        if loc is None:break
        r,c=loc
        a[r],a[k]=a[k],a[r]
        for row in a:row[c],row[k]=row[k],row[c]
        if a[k][k]==-1:a[k]=[-x for x in a[k]]
        for r in range(k+1,n):
            t=a[r][k]
            if t:
                for c in range(k,m):a[r][c]-=t*a[k][c]
        for c in range(k+1,m):
            t=a[k][c]
            if t:
                for r in range(k,n):a[r][c]-=t*a[r][k]
        k+=1
    remaining=[a[r][c] for r in range(k,n) for c in range(k,m)]
    assert all(x==0 for x in remaining), 'non-unit residual; no wedge conclusion'
    assert all(a[i][i]==1 for i in range(k))
    return k


def full_mod_two_boundary_ranks(faces):
    by_dim={d:sorted(f for f in faces if f.bit_count()-1==d) for d in range(-1,8)}
    out={}
    for d in range(8):
        targets={f:i for i,f in enumerate(by_dim[d-1])}
        basis={}
        for f in by_dim[d]:
            col=0
            for b,_ in boundary(f):col ^= 1 << targets[f^b]
            while col:
                k=col.bit_length()-1
                if k not in basis:
                    basis[k]=col;break
                col ^= basis[k]
        out[d]=len(basis)
    reduced_betti={d:len(by_dim[d])-out[d]-out.get(d+1,0) for d in range(8)}
    return out,reduced_betti


def run():
    f1=perfect_matchings_by_vertices()
    f2=perfect_matchings_by_bipartition()
    assert f1==f2 and len(f1)==272
    faces=all_faces_from_facets(f1)
    assert len(faces)==30561
    fv=Counter(f.bit_count()-1 for f in faces)
    assert [fv[k] for k in range(-1,8)]==[1,32,400,2496,7776,10560,6848,2176,272]
    matching_count=check_faces_by_extendability(faces)
    print('PERFECT_MATCHINGS',len(f1),'FACES',len(faces),'ALL_MATCHINGS',matching_count)
    print('FACE_VECTOR_MINUS1_TO7',[fv[k] for k in range(-1,8)])
    m1,u1,c1=toggle_matching(faces)
    m2,u2,c2=toggle_matching(faces,backward=True)
    h1=check_acyclicity(faces,m1)
    h2=check_acyclicity(faces,m2)
    assert h1==h2
    print('HASSE_INCIDENCES',h1)
    print('FORWARD_MATCHED_PAIRS',len(m1),'CRITICAL',sorted(Counter(f.bit_count()-1 for f in c1).items()))
    print('REVERSE_MATCHED_PAIRS',len(m2),'CRITICAL',sorted(Counter(f.bit_count()-1 for f in c2).items()))
    B1,shape1,cache1=morse_boundary(m1,u1,c1,4,3)
    r1=unit_reduction(B1)
    assert shape1==(124,91) and r1==70
    B2,shape2,cache2=morse_boundary(m2,u2,c2,4,3)
    B3,shape3,cache3=morse_boundary(m2,u2,c2,5,4)
    r2=unit_reduction(B2)
    r3=unit_reduction(B3)
    print('FORWARD_BOUNDARY_DIMENSIONS',shape1,'INTEGRAL_UNIT_RANK',r1,'MAX_ENTRY',max(abs(x) for row in B1 for x in row))
    print('REVERSE_BOUNDARIES',shape2,shape3,'INTEGRAL_UNIT_RANKS',r2,r3)
    assert r2+r3<=shape2[1]
    assert shape2[0]-r2==54 and shape2[1]-r2-r3==21 and shape3[1]-r3==0
    # Check chain relation of the reversed Morse model over the integers.
    assert all(sum(B2[i][j]*B3[j][k] for j in range(shape2[1]))==0
               for i in range(shape2[0]) for k in range(shape3[1]))
    ranks, betti=full_mod_two_boundary_ranks(faces)
    print('UNREDUCED_MOD2_BOUNDARY_RANKS',ranks)
    print('UNREDUCED_MOD2_REDUCED_BETTI',betti)
    assert betti=={0:0,1:0,2:0,3:54,4:21,5:0,6:0,7:0}
    print('HOMOTOPY_WEDGE_54_S3_AND_21_S4_VERIFIED')

if __name__=='__main__':run()
