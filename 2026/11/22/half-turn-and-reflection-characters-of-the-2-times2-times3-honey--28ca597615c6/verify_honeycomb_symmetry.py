"""Exact rational symmetry trace verifier for the 2x2x3 honeycomb perfect-matching complex.

No nonstandard dependencies. A tiling is encoded as a monotone 2x2 plane partition.
Lozenge locations are projected to the plane along the (1,1,1) diagonal.
"""
from collections import Counter

A, B, C = 2, 2, 3


def partitions():
    out = []
    def extend(vals):
        if len(vals) == A * B:
            out.append(tuple(vals))
            return
        x, y = divmod(len(vals), B)
        up = vals[(x-1)*B+y] if x else C
        left = vals[-1] if y else C
        for z in range(min(up, left), -1, -1):
            extend(vals + [z])
    extend([])
    return out


def lozenges(h):
    result = []
    for x in range(A):
        for y in range(B):
            z = h[x*B+y]
            result.append(('z', x-z, y-z))
    for x in range(A):
        for z in range(1, C+1):
            y = sum(h[x*B+j] >= z for j in range(B))
            result.append(('y', x-y, z-y))
    for y in range(B):
        for z in range(1, C+1):
            x = sum(h[i*B+y] >= z for i in range(A))
            result.append(('x', y-x, z-x))
    return frozenset(result)


def swap(e):
    typ, u, v = e
    return {'x': ('y',u,v), 'y': ('x',u,v), 'z': ('z',v,u)}[typ]


def halfturn(e):
    typ, u, v = e
    return {'x': ('x',B-A-1-u,C+1-A-v),
            'y': ('y',A-B-1-u,C+1-B-v),
            'z': ('z',A-C-1-u,B-C-1-v)}[typ]


def transformed(mask, perm):
    out = 0
    while mask:
        bit = mask & -mask
        mask -= bit
        out |= 1 << perm[bit.bit_length()-1]
    return out


def build():
    heights = partitions()
    facets = [lozenges(h) for h in heights]
    labels = sorted(set().union(*facets))
    ind = {e:i for i,e in enumerate(labels)}
    masks = [sum(1 << ind[e] for e in F) for F in facets]
    permutations = {
        'swap': [ind[swap(e)] for e in labels],
        'halfturn': [ind[halfturn(e)] for e in labels],
    }
    permutations['other_reflection'] = [permutations['swap'][i] for i in permutations['halfturn']]
    assert len(heights)==50 and len(labels)==41 and len(set(masks))==50
    assert all(x.bit_count()==16 for x in masks)
    for p in permutations.values():
        assert len(set(p))==41
        assert all(p[p[i]]==i for i in range(41))
        assert {transformed(f,p) for f in masks}==set(masks)
    assert all(permutations['swap'][permutations['halfturn'][i]] ==
               permutations['halfturn'][permutations['swap'][i]] for i in range(41))
    return masks, labels, permutations


def all_subfaces(facets):
    faces = {0}
    for facet in facets:
        subs = [0]
        while facet:
            bit = facet & -facet
            facet -= bit
            subs += [s|bit for s in subs]
        faces.update(subs)
    return faces


def orbit_complex(facets, p):
    seen=set()
    orbits=[]
    for i in range(len(p)):
        if i in seen:continue
        group=[]
        j=i
        while j not in seen:
            seen.add(j);group.append(j);j=p[j]
        assert j==i
        orbits.append(sum(1<<j for j in group))
    orbit_facets=[]
    for F in facets:
        orbit_facets.append(sum(1<<j for j,orbit in enumerate(orbits)
                                if (F & orbit)==orbit))
    orbit_faces = all_subfaces(orbit_facets)
    reduced_euler=sum((-1)**(F.bit_count()-1) for F in orbit_faces if F)-1
    return len(orbits),len(orbit_faces)-1,reduced_euler


def direct_signed_trace(faces,p):
    """Independent check via all invariant original simplices, not orbit facets."""
    paired=[]
    for i,j in enumerate(p):
        if i<j:
            paired.append(((1<<i),(1<<j)))
    fixed_faces=0;trace=0
    for face in faces:
        if not face:continue
        selected_pairs=0
        for x,y in paired:
            a=bool(face&x)
            b=bool(face&y)
            if a != b:
                break
            if a:selected_pairs+=1
        else:
            fixed_faces+=1
            orientation = -1 if selected_pairs%2 else 1
            trace += (-1 if face.bit_count()%2==0 else 1)*orientation
    return fixed_faces,trace-1


def morse_check(faces):
    """Independent ordered-pivot acyclic matching, including every nonempty face."""
    unmatched = set(faces)
    unmatched.remove(0)
    total_pairs=0
    stages=[]
    for j in range(41):
        bit=1<<j
        lower=[f for f in unmatched if not (f&bit) and (f|bit) in unmatched]
        for f in lower:
            unmatched.remove(f)
            unmatched.remove(f|bit)
        total_pairs+=len(lower)
        stages.append(len(lower))
    dimensions=Counter(f.bit_count()-1 for f in unmatched)
    assert total_pairs==1258892
    assert dimensions == {0:1,4:2}, dimensions
    assert 2*total_pairs+len(unmatched)==len(faces)-1
    return stages,dimensions


def main():
    facets,labels,p = build()
    faces=all_subfaces(facets)
    fvec=Counter(f.bit_count()-1 for f in faces if f)
    assert len(faces)-1==2517787
    assert [fvec[d] for d in range(16)] == [41,706,6186,31566,104477,241386,
                        407750,517618,501141,371866,210600,89700,27900,6000,800,50]
    print('perfect matchings:',len(facets))
    print('rhombus edges:',len(labels))
    print('nonempty simplices:',len(faces)-1)
    print('reduced Euler characteristic:',sum((-1)**(f.bit_count()-1) for f in faces if f)-1)
    assert sum((-1)**(f.bit_count()-1) for f in faces if f)-1==2
    stages, critical=morse_check(faces)
    print('ordered-pivot discrete-Morse pairs:',sum(stages))
    print('critical cells:',dict(sorted(critical.items())))
    for name, expected in [('swap',(23,7175,-2)),('halfturn',(21,1369,0)),
                           ('other_reflection',(21,85,0))]:
        orb=orbit_complex(facets,p[name]); assert orb==expected,(name,orb)
        directly=direct_signed_trace(faces,p[name]);assert directly[1]==expected[-1],(name,directly)
        print(f'{name}: vertex-orbits={orb[0]}, orbit-faces={orb[1]}, reduced Lefschetz={orb[2]}, direct-fixed-faces={directly[0]}')
    print('homology character [identity, swap, halfturn, other_reflection]: [2,-2,0,0]')
    print('rational quotient beta4 [swap, halfturn, other_reflection, full]: [0,1,1,0]')
    print('all assertions passed')

if __name__=='__main__':
    main()
