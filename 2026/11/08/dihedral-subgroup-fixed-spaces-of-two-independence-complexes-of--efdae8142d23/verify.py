#!/usr/bin/env python3
"""Finite independent checks for dihedral fixed spaces of two-independence complexes of cycles."""
from collections import deque, defaultdict
from math import gcd


def allowed_cycle(n, vertex_mask):
    return all(not all((vertex_mask >> ((i+j) % n)) & 1 for j in range(3)) for i in range(n))


def subgroup_orbits(n, step, axis=None):
    assert n % step == 0
    unseen = set(range(n))
    orbits = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {seed}
        stack = [seed]
        while stack:
            v = stack.pop()
            destinations = [(v + step) % n, (v - step) % n]
            if axis is not None:
                destinations.append((axis-v) % n)
            for u in destinations:
                if u not in orbit:
                    orbit.add(u)
                    stack.append(u)
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    return sorted(orbits)


def orbit_face_masks(n, orbits):
    masks = [sum(1 << x for x in orbit) for orbit in orbits]
    out = set()
    for t in range(1 << len(masks)):
        support=0
        for j,orbmask in enumerate(masks):
            if (t>>j)&1:
                support|=orbmask
        if allowed_cycle(n,support):
            out.add(t)
    return out


def folded_faces(length):
    out = set()
    for m in range(1<<length):
        if length>=2 and ((m&3)==3 or ((m>>(length-2))&3)==3):
            continue
        if any((m>>i)&7==7 for i in range(length-2)):
            continue
        out.add(m)
    return out


def canonical_axes(d, a):
    if d & 1:
        b = (a * pow(2,-1,d))%d
        m = d//2
        canonical=[frozenset([0])] + [frozenset([j,d-j]) for j in range(1,m+1)]
    elif a%2==0:
        b=(a//2)%d
        m=d//2
        canonical=[frozenset([0])] + [frozenset([j,d-j]) for j in range(1,m)] + [frozenset([m])]
    else:
        b=((a-1)//2)%d
        m=d//2
        canonical=[frozenset([(1-j)%d,j%d]) for j in range(1,m+1)]
    return b,canonical


def translated_faces(n, d, a, orbits, faces):
    b,canon=canonical_axes(d,a)
    lookup={orb:j for j,orb in enumerate(canon)}
    assert len(lookup)==len(canon)
    renaming=[]
    for orb in orbits:
        rest=frozenset(((v%d)-b)%d for v in orb)
        renaming.append(lookup[rest])
    assert len(set(renaming)) == len(renaming)
    out=set()
    for face in faces:
        m=0
        for i,j in enumerate(renaming):
            if face>>i & 1:m|=1<<j
        out.add(m)
    return out


def crosspoly_faces(l):
    k=l//2
    return {m for m in range(1<<(2*k)) if all(((m>>(2*j))&3)!=3 for j in range(k))}


def face_pivot(l,face):
    k=l//2
    for j in range(2,k+1):
        pair=(3<<(2*j-2))
        if face&pair == pair:
            return 2*j-4  # zero-based first vertex of preceding pair
    if l%2 and face>>(l-1)&1:
        return l-3
    return None


def check_relative_morse(l, do_dag=True):
    faces=folded_faces(l)
    K=crosspoly_faces(l)
    assert K <= faces
    matched=set()
    pairs=set()
    for f in faces-K:
        p=face_pivot(l,f)
        assert p is not None
        mate=f^(1<<p)
        assert mate in faces-K
        assert face_pivot(l,mate)==p
        pair=(min(f,mate),max(f,mate))
        pairs.add(pair)
        matched.add(f)
    assert matched==faces-K
    assert len(pairs)*2==len(faces-K)
    if do_dag:
        adj=defaultdict(list)
        deg={f:0 for f in faces}
        for hi in faces:
            for j in range(l):
                if hi>>j & 1:
                    low=hi^(1<<j)
                    if (low,hi) in pairs:
                        src,dst=low,hi
                    else:
                        src,dst=hi,low
                    adj[src].append(dst)
                    deg[dst]+=1
        q=deque(f for f,x in deg.items() if x==0)
        count=0
        while q:
            f=q.popleft();count+=1
            for g in adj[f]:
                deg[g]-=1
                if deg[g]==0:q.append(g)
        assert count==len(faces),('acyclic matching failed',l,count,len(faces))
    return len(faces),len(K),len(pairs)


def reduced_betti_mod2(faces):
    fs=defaultdict(list)
    for m in faces:
        fs[m.bit_count()-1].append(m)
    maxdim=max(fs)
    ranks={}
    for degree in range(1,maxdim+1):
        codomain={m:i for i,m in enumerate(fs[degree-1])}
        pivots={}
        for f in fs[degree]:
            col=0
            for j in range(f.bit_length()):
                if f>>j&1: col ^= 1<<codomain[f^(1<<j)]
            while col:
                top=col.bit_length()-1
                if top in pivots:
                    col^=pivots[top]
                else:
                    pivots[top]=col;break
        ranks[degree]=len(pivots)
    out={}
    for degree in range(maxdim+1):
        b=len(fs[degree])-ranks.get(degree,0)-ranks.get(degree+1,0)
        if degree==0:b-=1
        if b:out[degree]=b
    return out


def main():
    examples=0
    reflections=0
    cyclics=0
    empty=0
    for n in range(3,29):
        for d in (x for x in range(1,n+1) if n%x==0):
            if d<n:
                orbits=subgroup_orbits(n,d)
                f=orbit_face_masks(n,orbits)
                if d==1:
                    assert f=={0};empty+=1
                elif d==2:
                    assert f=={0,1,2};cyclics+=1
                else:
                    assert f=={mask for mask in range(1<<d) if allowed_cycle(d,mask)}
                    cyclics+=1
                examples+=1
            for a in range(d):
                orbits=subgroup_orbits(n,d,a)
                f=orbit_face_masks(n,orbits)
                if d==1:
                    assert f=={0};empty+=1
                elif d==2:
                    if a%2==0:
                        assert f=={0,1,2}
                    else:
                        assert f=={0};empty+=1
                else:
                    tf=translated_faces(n,d,a,orbits,f)
                    assert tf==folded_faces(len(orbits)),('orbit folding',n,d,a)
                reflections+=1;examples+=1
    morph_checks=[]
    for l in range(2,16):
        cnt=check_relative_morse(l,do_dag=l<=12)
        morph_checks.append((l,*cnt))
    homology_checks=[]
    for l in range(2,12):
        observed=reduced_betti_mod2(folded_faces(l))
        expected={l//2-1:1}
        assert observed==expected,('homology',l,observed,expected)
        homology_checks.append((l,observed))
    print('DIRECT_GROUP_ORBIT_COMPARISONS_OK',examples)
    print('REFLECTION_SUBGROUP_COMPARISONS_OK',reflections)
    print('NONTRIVIAL_CYCLIC_COMPARISONS_OK',cyclics)
    print('EMPTY_FIXED_MODELS_OK',empty)
    print('RELATIVE_ACYCLIC_MATCHING_OK',len(morph_checks),'sizes_2_through_15')
    print('INDEPENDENT_MOD2_HOMOLOGY_OK',len(homology_checks),'sizes_2_through_11')
    print('LARGEST_MATCHING_SAMPLE',morph_checks[-1])
    print('ALL_DIHEDRAL_SUBGROUP_TWO_INDEPENDENCE_FIXED_MODELS_OK')

if __name__=='__main__':main()
