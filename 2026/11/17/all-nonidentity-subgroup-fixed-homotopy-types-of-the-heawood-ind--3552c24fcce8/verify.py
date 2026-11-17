#!/usr/bin/env python3
"""Exact finite verification for subgroup-fixed independence complexes of the Fano incidence graph.

Uses integer arithmetic, sets, and elementary simplicial collapses only.
Run: python3 verify.py; optionally python3 verify.py --write-census
"""
import collections
import itertools
import json
import sys

N = 14

def pairing(a, b):
    return (a & b).bit_count() % 2

def linear(a, b, c, x):
    return ((a if x & 1 else 0) ^ (b if x & 2 else 0) ^ (c if x & 4 else 0))

def compose(p, q):
    return tuple(p[q[i]] for i in range(N))

def build_group():
    matrices = []
    for a, b, c in itertools.product(range(1, 8), repeat=3):
        if len({linear(a,b,c,x) for x in range(1,8)}) == 7:
            matrices.append((a,b,c))
    assert len(matrices) == 168
    perms = []
    for a,b,c in matrices:
        p = [linear(a,b,c,x)-1 for x in range(1,8)]
        dual = []
        for cov in range(1,8):
            compatible = [y for y in range(1,8) if all(
                pairing(cov,x) == pairing(y,linear(a,b,c,x))
                for x in range(1,8))]
            assert len(compatible)==1
            dual.append(6+compatible[0])
        perms.append(tuple(p+dual))
    swap = tuple(range(7,14))+tuple(range(7))
    perms = sorted(set(perms + [compose(p,swap) for p in perms]))
    assert len(perms)==336 and all(set(p)==set(range(N)) for p in perms)
    for p in perms:
        for x in range(1,8):
            for a in range(1,8):
                assert pairing(x,a)==0 if (p[x-1]<7 and p[a+6]>=7 and pairing(p[x-1]+1,p[a+6]-6)==0) or (p[x-1]>=7 and p[a+6]<7 and pairing(p[x-1]-6,p[a+6]+1)==0) else pairing(x,a)!=0
    lookup = {p:i for i,p in enumerate(perms)}
    product = [[lookup[compose(p,q)] for q in perms] for p in perms]
    identity = lookup[tuple(range(N))]
    inverse = [next(j for j in range(336) if product[i][j]==identity) for i in range(336)]
    return perms, product, inverse, identity

def subgroups(product, identity):
    found = {frozenset((identity,)):()}
    stack = [frozenset((identity,))]
    while stack:
        H = stack.pop()
        old_generators = found[H]
        for g in range(336):
            if g in H: continue
            generators = old_generators+(g,)
            closed = {identity}
            agenda = [identity]
            while agenda:
                h = agenda.pop()
                for k in generators:
                    z = product[h][k]
                    if z not in closed:
                        closed.add(z)
                        agenda.append(z)
            new = frozenset(closed)
            if new not in found:
                found[new] = generators
                stack.append(new)
    assert len(found)==413
    for H in found:
        assert identity in H
        assert all(product[g][h] in H for g in H for h in H)
    return found

def conjugacy(subgroups, product, inverse):
    remaining = set(subgroups)
    classes = []
    while remaining:
        H = next(iter(remaining))
        conj = {frozenset(product[product[g][h]][inverse[g]] for h in H) for g in range(336)}
        assert conj <= set(subgroups)
        classes.append((H,len(conj)))
        remaining -= conj
    classes.sort(key=lambda z:(len(z[0]),z[1]))
    assert len(classes)==23 and sum(c for H,c in classes)==413
    for H,c in classes: assert (336//c)*c==336
    return classes

def independent_orbit_faces(H, perms):
    remaining = set(range(N))
    orbits = []
    while remaining:
        i = min(remaining)
        orb = frozenset(perms[g][i] for g in H)
        assert orb<=remaining
        remaining -= orb
        orbits.append(orb)
    def compatible(A,B):
        return all(not ((a<7 and b>=7 and pairing(a+1,b-6)==0)
                        or (a>=7 and b<7 and pairing(a-6,b+1)==0))
                   for a in A for b in B)
    good=[x for x in orbits if compatible(x,x)]
    pair_good = [[compatible(a,b) for b in good] for a in good]
    faces = set()
    for mask in range(1,1<<len(good)):
        inds=[i for i in range(len(good)) if mask>>i&1]
        if all(pair_good[i][j] for i in inds for j in inds): faces.add(mask)
    return orbits, good, faces

def collapse(faces):
    """Exact elementary collapses: a free ridge and its unique facet."""
    F=set(faces)
    pairs=[]
    while True:
        facets = [f for f in F if not any((not f>>i&1) and (f|1<<i) in F for i in range(N))]
        choices=[]
        for facet in facets:
            for i in range(N):
                if not facet>>i&1: continue
                ridge=facet^(1<<i)
                if ridge==0 or ridge not in F:continue
                if sum((r&ridge)==ridge for r in facets)==1:
                    choices.append((ridge,facet))
        if not choices:break
        ridge,facet=max(choices,key=lambda x:(x[1].bit_count(),x[1],x[0]))
        assert ridge in F and facet in F
        F.remove(ridge); F.remove(facet)
        pairs.append((ridge,facet))
    return F,pairs

def simplex_vertices(s):
    return [i for i in range(N) if s>>i&1]

def graph_components(vertices,edges):
    remaining=set(vertices)
    comps=[]
    while remaining:
        a=min(remaining);remaining.remove(a);found={a};agenda=[a]
        while agenda:
            u=agenda.pop()
            for e in edges:
                if e>>u&1:
                    for v in simplex_vertices(e):
                        if v in remaining:
                            remaining.remove(v);found.add(v);agenda.append(v)
        comps.append(found)
    return comps

def sphere_check(triangles):
    assert triangles and all(t.bit_count()==3 for t in triangles)
    edge_counts=collections.Counter(t^(1<<i) for t in triangles for i in simplex_vertices(t))
    assert all(v==2 for v in edge_counts.values())
    vertices=set(i for t in triangles for i in simplex_vertices(t))
    assert len(vertices)-len(edge_counts)+len(triangles)==2
    assert len(graph_components(vertices,set(edge_counts)))==1
    # A connected, closed triangulated surface, with sphere Euler characteristic.
    for v in vertices:
        lk_edges=[t^(1<<v) for t in triangles if t>>v&1]
        link_verts=set(i for e in lk_edges for i in simplex_vertices(e))
        degrees=collections.Counter(i for e in lk_edges for i in simplex_vertices(e))
        assert link_verts and set(degrees.values())=={2}
        assert len(graph_components(link_verts,set(lk_edges)))==1
    return {'triangles':len(triangles),'vertices':len(vertices),'edges':len(edge_counts)}

def classify(residual):
    if not residual:return 'empty',{}
    levels=collections.Counter(f.bit_count() for f in residual)
    vertices=[f.bit_length()-1 for f in residual if f.bit_count()==1]
    edges={f for f in residual if f.bit_count()==2}
    triangles={f for f in residual if f.bit_count()==3}
    assert max(levels)<=3
    if len(vertices)==1 and len(residual)==1:return 'point',{}
    if len(vertices)==2 and len(residual)==2:return 'two_points',{}
    if not triangles:
        comps=graph_components(vertices,edges)
        assert len(comps)==1
        rank=len(edges)-len(vertices)+1
        assert rank==2
        return 'two_circles',{'vertices':len(vertices),'edges':len(edges)}
    counts=collections.Counter(t^(1<<i) for t in triangles for i in simplex_vertices(t))
    if sorted(set(counts.values()))==[2]:
        sphere=sphere_check(triangles)
        spare=edges-set(counts)
        assert len(spare)==1
        assert set(simplex_vertices(next(iter(spare)))) <= set(i for t in triangles for i in simplex_vertices(t))
        return 'sphere_two_circle_one',{'sphere':sphere,'extra_edge':simplex_vertices(next(iter(spare)))}
    assert set(counts.values())=={2,3}
    triple_edges={e for e,n in counts.items() if n==3}
    assert len(triple_edges)==3
    common_tri=[t for t in triangles if all((e&t)==e for e in triple_edges)]
    assert len(common_tri)==1
    T=common_tri[0]
    assert set(T^(1<<i) for i in simplex_vertices(T))==triple_edges
    remaining=triangles-{T}
    components=[]
    while remaining:
        t=min(remaining);remaining.remove(t);comp={t};agenda=[t]
        while agenda:
            a=agenda.pop()
            for b in list(remaining):
                if (a&b).bit_count()==2 and (a&b) not in triple_edges:
                    comp.add(b);remaining.remove(b);agenda.append(b)
        components.append(comp)
    assert len(components)==2
    checks=[sphere_check(c|{T}) for c in components]
    sph_faces=[]
    for c in components:
        fs=set(c|{T})
        fs|={t^(1<<i) for t in c|{T} for i in simplex_vertices(t)}
        fs|={1<<i for t in c|{T} for i in simplex_vertices(t)}
        sph_faces.append(fs)
    shared={T}|{T^(1<<i) for i in simplex_vertices(T)}|{1<<i for i in simplex_vertices(T)}
    assert sph_faces[0]&sph_faces[1]==shared
    assert sph_faces[0]|sph_faces[1]==residual
    return 'two_spheres',{'spheres':sorted(checks,key=lambda z:z['triangles']),'shared_triangle':simplex_vertices(T)}

def main():
    perms,product,inverse,identity=build_group()
    allgroups=subgroups(product,identity)
    classes=conjugacy(allgroups,product,inverse)
    histogram=collections.Counter()
    records=[]
    assert all(len(independent_orbit_faces(H,perms)[2])>=0 for H in allgroups)
    for H,cls_size in classes:
        orbits,good,faces=independent_orbit_faces(H,perms)
        if len(H)==1:
            # The identity case is previously established, not part of the new classification.
            assert len(faces)==457
            continue
        reduced,pairs=collapse(faces)
        try:
            type_name,shape=classify(reduced)
        except Exception as exc:
            print('UNCLASSIFIED',len(H),cls_size,'faces',len(faces),'reduced',len(reduced),'face_counts',dict(collections.Counter(f.bit_count() for f in reduced)), 'triangles', [simplex_vertices(t) for t in reduced if t.bit_count()==3]);raise
        histogram[type_name]+=cls_size
        # Every elementary move and residual type is reconstructed and checked above.
        records.append({'subgroup_order':len(H),'conjugacy_class_size':cls_size,
             'vertex_orbits':len(orbits),'admissible_vertex_orbits':len(good),
             'faces_before_collapse':len(faces),'elementary_collapse_pairs':len(pairs),
             'remaining_faces':len(reduced),'homotopy_type':type_name,'shape':shape,
             'representative_group_element_indices':sorted(H),
             'collapse_pairs_bitmasks':[list(x) for x in pairs],
             'residual_face_bitmasks':sorted(reduced)})
    expected={'two_spheres':21,'sphere_two_circle_one':14,'two_circles':42,
              'two_points':17,'empty':17,'point':301}
    assert dict(histogram)==expected,(histogram,expected)
    assert len(records)==22 and sum(r['conjugacy_class_size'] for r in records)==412
    census={'group_order':336,'subgroups_total':413,'subgroup_conjugacy_classes':23,
            'nonidentity_subgroups':412,'nonidentity_conjugacy_classes':22,
            'homotopy_type_subgroup_counts':dict(sorted(histogram.items())),
            'class_records':records}
    encoded=json.dumps(census,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if len(sys.argv)>1 and sys.argv[1]=='--write-census':
        open('CENSUS.json','w',encoding='utf-8').write(encoded)
    else:
        with open('CENSUS.json',encoding='utf-8') as f:
            assert f.read()==encoded
    for type_name in sorted(histogram):print(type_name,histogram[type_name])
    print('FANO_INDEPENDENCE_NONIDENTITY_SUBGROUP_FIXED_SPACES_PASS')

if __name__=='__main__':main()
