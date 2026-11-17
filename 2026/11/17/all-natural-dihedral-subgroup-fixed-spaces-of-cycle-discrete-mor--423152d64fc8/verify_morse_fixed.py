#!/usr/bin/env python3
"""Finite independent checks of geometric fixed-orbit models for cycle Morse complexes.
This program needs only the Python standard library.
"""
from itertools import combinations
from math import gcd
from collections import defaultdict, Counter


def inc_arcs(n):
    # Incidence vertex w_{2i} matches vertex i to edge i and points i -> i+1;
    # w_{2i+1} matches vertex i+1 to edge i and points i+1 -> i.
    return [((j//2)%n, (j//2+1)%n) if j%2==0 else ((j//2+1)%n, (j//2)%n) for j in range(2*n)]


def rooted_forest(n, mask):
    arcs = inc_arcs(n)
    out = {}
    for j, (u,v) in enumerate(arcs):
        if mask & (1<<j):
            if u in out or out.get(v,None)==u: return False
            out[u] = v
    for x in out:
        seen = set()
        cur=x
        while cur in out:
            if cur in seen:return False
            seen.add(cur)
            cur=out[cur]
    return True


def group_orbits(n,t,reflect=False,b=0):
    m=2*n
    generators=[lambda j:(j+2*t)%m] if t<n else []
    if reflect:
        generators.append(lambda j:(-1-j-2*b)%m)
    unseen=set(range(m)); orbits=[]
    while unseen:
        seed=min(unseen); cur={seed};queue=[seed]
        for x in queue:
            for f in generators:
                y=f(x)
                if y not in cur:cur.add(y);queue.append(y)
        unseen-=cur
        orbits.append(frozenset(cur))
    return orbits


def actual_fixed_faces(n,t,reflect=False,b=0):
    orbits=group_orbits(n,t,reflect,b)
    masks=[sum(1<<x for x in orbit) for orbit in orbits]
    faces=[]
    for sub in range(1<<len(orbits)):
        chosen=0
        for i,mask in enumerate(masks):
            if sub&(1<<i):chosen|=mask
        if rooted_forest(n,chosen):faces.append(sub)
    return orbits,faces


def predicted_exact_faces(t, reflect, b, orbits):
    # Explicit orbit-label bijection, independently checked against full rooted-forest enumeration.
    if reflect:
        label=[]
        for orbit in orbits:
            qs={min((j+b)%(2*t), 2*t-1-((j+b)%(2*t))) for j in orbit}
            assert len(qs)==1,(t,b,orbit,qs)
            label.append(next(iter(qs)))
        assert sorted(label)==list(range(t))
    else:
        label=[]
        for orbit in orbits:
            residues={j%(2*t) for j in orbit}
            assert len(residues)==1,(t,orbit,residues)
            label.append(next(iter(residues)))
        assert sorted(label)==list(range(2*t))
    out=[]
    for face in range(1<<len(orbits)):
        chosen={label[i] for i in range(len(orbits)) if face>>i&1}
        if reflect:
            valid=0 not in chosen and (t-1) not in chosen and all(i+1 not in chosen for i in chosen)
        else:
            valid=not (set(range(0,2*t,2)).issubset(chosen) or set(range(1,2*t,2)).issubset(chosen))
            valid=valid and all((i+1)%(2*t) not in chosen for i in chosen)
        if valid:out.append(face)
    return out


def predicted_face_counts(t,reflect=False):
    # Graph model of geometric fixed complex, including the augmented empty face.
    if reflect:
        if t<=2:return {0:1}
        v=t-2; graph_edges={(i,i+1) for i in range(v-1)}
        forbidden=[]
    else:
        if t==1:return {0:1}
        v=2*t; graph_edges={(i,(i+1)%v) for i in range(v)}
        forbidden=[sum(1<<i for i in range(0,v,2)),sum(1<<i for i in range(1,v,2))]
    out=Counter()
    for mask in range(1<<v):
        if mask in forbidden:continue
        if any((mask>>a)&1 and (mask>>b)&1 for a,b in graph_edges):continue
        out[mask.bit_count()]+=1
    return dict(out)


def fvec(faces):
    return dict(Counter(x.bit_count() for x in faces))


def betti_f2(faces):
    dd=defaultdict(list)
    for face in faces:
        if face: dd[face.bit_count()-1].append(face)
    ranks={}
    for dim in sorted(dd,reverse=True):
        if dim<1:continue
        idx={m:i for i,m in enumerate(dd[dim-1])};pivots={}; rank=0
        for face in dd[dim]:
            v=0;rem=face
            while rem:
                bit=rem&-rem;rem-=bit
                v ^= 1<<idx[face^bit]
            while v:
                p=v.bit_length()-1
                if p in pivots:v ^= pivots[p]
                else:pivots[p]=v;rank+=1;break
        ranks[dim]=rank
    out={dim:len(fs)-ranks.get(dim,0)-ranks.get(dim+1,0)-(1 if dim==0 else 0) for dim,fs in dd.items()}
    return {k:v for k,v in out.items() if v}


def expected_betti(t,reflect=False):
    if reflect:
        if t<=2:return {}
        m=t-2
        if m%3==1:return {}
        return {(m//3-1 if m%3==0 else m//3):1}
    if t==1:return {}
    if t==2:return {0:3}
    d=(2*t-2)//3
    return dict(Counter({d:2 if t%3==0 else 1})+Counter({t-2:2}))

checks=0; total_subsets=0;mods=0
for n in range(3,13):
    for t in range(1,n+1):
        if n%t: continue
        for reflect,b in ([(False,0)] if n<=8 or t<n else []) + [(True,b) for b in range(t)]:
            orbits,faces=actual_fixed_faces(n,t,reflect,b)
            assert faces==predicted_exact_faces(t,reflect,b,orbits),(n,t,reflect,b)
            got=fvec(faces)
            want=predicted_face_counts(t,reflect)
            assert got==want,(n,t,reflect,b,got,want)
            checks+=1;total_subsets+=1<<len(orbits)
            if n<=8 and len(orbits)<=14:
                got_betti=betti_f2(faces)
                want_betti=expected_betti(t,reflect)
                assert got_betti==want_betti,(n,t,reflect,b,got_betti,want_betti)
                mods+=1
print('parameters_checked',checks)
print('orbit_subsets_examined',total_subsets)
print('independent_mod2_homology_checks',mods)
print('FULL_CYCLE_MORSE_DIHEDRAL_FIXED_MODELS_PASS')
