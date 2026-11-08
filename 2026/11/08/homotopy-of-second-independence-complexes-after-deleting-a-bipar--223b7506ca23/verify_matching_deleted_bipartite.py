"""Independent finite checks of the P3-free complex for partial matching deletions."""
from itertools import combinations
from math import comb


def subsets_of(vertices):
    vertices = tuple(vertices)
    for k in range(len(vertices)+1):
        yield from combinations(vertices, k)


def all_subsets(facet):
    result = set()
    for subset in subsets_of(facet):
        result.add(tuple(sorted(subset)))
    return result


def by_induced_degree(a,b,t):
    # A uses labels 0,...,a-1 and B uses a,...,a+b-1.
    result=set()
    for face in subsets_of(range(a+b)):
        aa=[x for x in face if x<a]
        bb=[x-a for x in face if x>=a]
        good=all(sum(j!=i or i>=t for j in bb)<=1 for i in aa)
        good=good and all(sum(j!=i or i>=t for j in aa)<=1 for i in bb)
        if good:
            result.add(face)
    return result


def by_facets(a,b,t):
    result=all_subsets(range(a)) | all_subsets(range(a,a+b))
    for i in range(a):
        for j in range(b):
            result.add(tuple(sorted((i,a+j))))
    for i in range(t):
        for j in range(t):
            if i<j:
                result |= all_subsets((i,j,a+i,a+j))
        for j in range(t,a):
            result |= all_subsets((i,j,a+i))
        for j in range(t,b):
            result |= all_subsets((i,a+i,a+j))
    return result



def check_reduction(a,b,t,faces):
    if t==0:
        return
    rest=set(faces)
    # Every mixed face involving exactly one unmatched index is deleted
    # by a free-edge/triangle elementary collapse.
    free_pairs=[]
    for i in range(t):
        for j in range(t,a):
            free_pairs.append(((j,a+i),(i,j,a+i)))
        for j in range(t,b):
            free_pairs.append(((i,a+j),(i,a+i,a+j)))
    for edge,triangle in free_pairs:
        edge=tuple(sorted(edge))
        triangle=tuple(sorted(triangle))
        assert triangle in rest and edge in rest
        cofaces=[face for face in rest if set(edge).issubset(face)]
        assert cofaces==[edge,triangle] or set(cofaces)=={edge,triangle}, (a,b,t,edge,cofaces)
        rest.remove(edge)
        rest.remove(triangle)
    # The remaining isolated cross edges have two unmatched endpoints.
    mixed_core=all_subsets(range(a)) | all_subsets(range(a,a+b))
    for i in range(t):
        mixed_core.add((i,a+i))
        for j in range(i+1,t):
            mixed_core |= all_subsets((i,j,a+i,a+j))
    for i in range(t,a):
        for j in range(t,b):
            mixed_core.add((i,a+j))
    assert rest==mixed_core, (a,b,t,'collapse-remainder')
    # After omitting the maximal unmatched-unmatched edges, the
    # remaining complex retracts simplicially to the matched core.
    y=rest-{(i,a+j) for i in range(t,a) for j in range(t,b)}
    for f in y:
        mapped=tuple(sorted(set((v if v<t else 0) if v<a
                            else (v if v<a+t else a) for v in f)))
        # A-side unmatched vertices go to A_0; B-side unmatched to B_0.
        assert tuple(sorted(set(f)|set(mapped))) in y, (a,b,t,f,mapped)
    if t>=2:
        tt=set()
        for i in range(t):
            for j in range(i+1,t):
                tt |= all_subsets((i,j,a+i,a+j))
        for f in tt:
            mapped=tuple(sorted(set(v if v<a else v-a for v in f)))
            assert tuple(sorted(set(f)|set(mapped))) in tt, (a,b,t,'tetra-retraction',f)

def gf2_rank(columns):
    pivots={}
    for col in columns:
        while col:
            b=col.bit_length()-1
            if b in pivots:
                col ^= pivots[b]
            else:
                pivots[b]=col
                break
    return len(pivots)


def mod2_betti(faces):
    layers={}
    for face in faces:
        if face:
            layers.setdefault(len(face)-1, []).append(face)
    for layer in layers.values():
        layer.sort()
    maxdim=max(layers)
    ranks={}
    for k in range(1,maxdim+1):
        rows={f:i for i,f in enumerate(layers[k-1])}
        cols=[]
        for f in layers.get(k, []):
            mask=0
            for j in range(len(f)):
                mask ^= 1 << rows[f[:j]+f[j+1:]]
            cols.append(mask)
        ranks[k]=gf2_rank(cols)
    return tuple(len(layers.get(k,[]))-ranks.get(k,0)-ranks.get(k+1,0) for k in range(maxdim+1))


def predicted(a,b,t):
    if not t:
        return (1, a*b-1)
    b1=(a-t)*(b-t)
    b2=comb(t-1,2) if t>=2 else 0
    return (1,b1,b2)


def run():
    checks=0
    for a in range(1,7):
        for b in range(1,7):
            for t in range(min(a,b)+1):
                direct=by_induced_degree(a,b,t)
                facets=by_facets(a,b,t)
                assert direct == facets, (a,b,t,'face-decomposition',direct ^ facets)
                check_reduction(a,b,t,direct)
                betti=mod2_betti(direct)
                target=predicted(a,b,t)
                assert tuple(betti[k] if k<len(betti) else 0 for k in range(max(len(betti),len(target)))) == tuple(target[k] if k<len(target) else 0 for k in range(max(len(betti),len(target)))), (a,b,t,betti,target)
                checks+=1
    print(f'FACE_COLLAPSE_RETRACTION_AND_MOD2_CHECKS_PASS cases={checks} a,b=1..6 t=0..min(a,b)')
    for a,b,t in [(3,3,3),(4,4,4),(5,5,5),(5,5,3),(6,5,2),(6,6,0)]:
        f=by_induced_degree(a,b,t)
        print(f'a={a} b={b} t={t} faces={len(f)} betti={mod2_betti(f)}')


if __name__ == '__main__':
    run()
