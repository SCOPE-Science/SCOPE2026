"""Independent finite checks for the two-subset Kneser independence complex.

Usage: python kneser_equivariant_check.py
Requires Python 3.9+, standard library only.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial


def partitions(n, mx=None):
    if n == 0:
        yield ()
        return
    mx = n if mx is None else min(mx, n)
    for j in range(mx, 0, -1):
        for rest in partitions(n-j, j):
            yield (j,) + rest


def representative(parts):
    out = []
    offset = 0
    for d in parts:
        out.extend(offset + (i+1) % d for i in range(d))
        offset += d
    return tuple(out)


def faces_and_vertices(n):
    vertices = list(combinations(range(n), 2))
    lookup = {e: i for i, e in enumerate(vertices)}
    faces = set()
    for i in range(n):
        star = [j for j, e in enumerate(vertices) if i in e]
        for k in range(1, len(star)+1):
            faces.update(combinations(star, k))
    for i, j, k in combinations(range(n), 3):
        faces.add(tuple(sorted([lookup[(i,j)], lookup[(i,k)], lookup[(j,k)]])))
    return vertices, faces


def face_image(face, vertices):
    if len(face) == 1:
        return frozenset(vertices[face[0]])
    common = set(vertices[face[0]])
    for j in face[1:]:
        common.intersection_update(vertices[j])
    if common:
        assert len(common) == 1
        return frozenset(common)
    assert len(face) == 3
    union = set()
    for j in face:
        union.update(vertices[j])
    assert len(union) == 3
    return frozenset(union)


def sign(perm):
    inv = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
    return -1 if inv % 2 else 1


def signed_l(F, vertices, perm):
    lookup = {e: i for i, e in enumerate(vertices)}
    vertex_action = [lookup[tuple(sorted(perm[v] for v in edge))] for edge in vertices]
    total = -1
    for f in F:
        moved = tuple(vertex_action[i] for i in f)
        if set(moved) != set(f):
            continue
        ranks = [f.index(i) for i in moved]
        total += ((-1) ** (len(f)-1)) * sign(ranks)
    return total


def expected_exterior_trace(parts):
    coeff = [1,0,0,0]
    for d in parts:
        if d > 3:
            continue
        # det(I+t P_d)=1 - (-t)^d
        nxt = list(coeff)
        for k in range(4-d):
            nxt[k+d] += -((-1)**d)*coeff[k]
        coeff = nxt
    # Divide by 1+t, because Q^n=W+triv.
    q = [0]*4
    q[0] = coeff[0]
    for j in range(1,4):
        q[j] = coeff[j]-q[j-1]
    return q[3]


def mod_rank(columns, rows_count, p):
    pivots = {}
    for col in columns:
        vec = {i: v%p for i,v in col.items() if v%p}
        while vec:
            i = min(vec)
            if i not in pivots:
                v = vec[i]
                iv = pow(v,-1,p)
                pivots[i] = {j: (w*iv)%p for j,w in vec.items()}
                break
            factor = vec[i]
            for j,w in pivots[i].items():
                x = (vec.get(j,0) - factor*w)%p
                if x:vec[j]=x
                else:vec.pop(j,None)
    return len(pivots)


def boundary_ranks(F,p):
    maxk = max(map(len,F))
    by_size={k:sorted(f for f in F if len(f)==k) for k in range(1,maxk+1)}
    ranks = {0:1}
    for k in range(2,maxk+1):
        below={f:i for i,f in enumerate(by_size[k-1])}
        columns=[]
        for f in by_size[k]:
            columns.append({below[f[:i]+f[i+1:]]:(-1)**i for i in range(k)})
        ranks[k-1] = mod_rank(columns,len(below),p)
    ranks[maxk]=0
    # Number of nonzero reduced homology classes by dimension.
    betti = {}
    for k in range(1,maxk+1):
        betti[k-1]=len(by_size[k])-ranks[k-1]-ranks[k]
    return betti


def cycle_type(perm):
    seen=set();out=[]
    for i in range(len(perm)):
        if i in seen:continue
        v=i;d=0
        while v not in seen:
            seen.add(v); d+=1;v=perm[v]
        out.append(d)
    return tuple(sorted(out,reverse=True))


def compositions(n):
    if n==0:
        yield ()
    else:
        for first in range(1,n+1):
            for rest in compositions(n-first):
                yield (first,) + rest


def check_young_invariants(n):
    checked=0
    for blocks in compositions(n):
        choices=[]
        base=0
        for d in blocks:
            choices.append([tuple(base+i for i in p) for p in permutations(range(d))])
            base+=d
        from itertools import product
        total=0;count=0
        for elems in product(*choices):
            perm=tuple(j for part in elems for j in part)
            total+=expected_exterior_trace(cycle_type(perm))
            count+=1
        expected=comb(len(blocks)-1,3) if len(blocks)>=4 else 0
        assert count == __import__('math').prod(factorial(d) for d in blocks)
        assert total == expected*count,(n,blocks,total,count,expected)
        checked+=1
    print(f'  young_subgroup_invariant_dimensions_checked={checked}')


def check(n):
    vertices, F = faces_and_vertices(n)
    imgs={f:face_image(f,vertices) for f in F}
    # Complete check that each comparable face chain maps to a target face chain.
    pairs=0
    for face in F:
        face_set=set(face)
        for sub in F:
            if len(sub)>=len(face) or not set(sub).issubset(face_set):
                continue
            a,b=imgs[sub],imgs[face]
            assert a.issubset(b) or b.issubset(a), (n,sub,face,a,b)
            pairs+=1
    triangle_cells=sum(1 for f in F if len(f)==3 and len(imgs[f])==3)
    assert triangle_cells == comb(n,3)
    # Each exceptional source triangle subdivides into six small triangles;
    # its images are exactly the six flags of the corresponding target triangle.
    for tri in (f for f in F if len(f)==3 and len(imgs[f])==3):
        flags=set()
        for singleton in combinations(tri,1):
            for pair in combinations(tri,2):
                if singleton[0] not in pair: continue
                flags.add((imgs[singleton],imgs[pair],imgs[tri]))
        assert len(flags)==6
        for a,b,c in flags:
            assert len(a)==2 and len(b)==1 and len(c)==3 and b<a<c
    perm_list = list(permutations(range(n))) if n <= 6 else [representative(p) for p in partitions(n)]
    Vindex={e:i for i,e in enumerate(vertices)}
    for perm in perm_list:
        va={i:Vindex[tuple(sorted(perm[v] for v in e))] for i,e in enumerate(vertices)}
        for f in F:
            moved=tuple(sorted(va[i] for i in f))
            assert imgs[moved]==frozenset(perm[i] for i in imgs[f])
    print(f'  face_map_equivariance_verified_for={len(perm_list)}_permutations')
    class_results=[]
    for parts in partitions(n):
        perm=representative(parts)
        observed=signed_l(F,vertices,perm)
        predicted=expected_exterior_trace(parts)
        assert observed==predicted, (n,parts,observed,predicted)
        class_results.append((parts,observed))
    print(f'n={n}: faces={len(F)}, f_vector={dict(sorted(Counter(len(f)-1 for f in F).items()))}, '
          f'comparable_pairs={pairs}, triangles={triangle_cells}, classes={len(class_results)}, '
          f'H2_rank={comb(n-1,3)}')
    print('  signed_Lefschetz_by_cycle_type=',class_results)
    if n<=6:
        check_young_invariants(n)
        for p in (2,3,101):
            b=boundary_ranks(F,p)
            assert b=={0:0,1:0,2:comb(n-1,3),**{k:0 for k in range(3,max(map(len,F)))}}
            print(f'  reduced_Betti_mod_{p}={b}')


if __name__=='__main__':
    for n in range(4,8):
        check(n)
    print('KNESER_TWO_SUBSET_EQUIVARIANT_CHECK_PASS')
