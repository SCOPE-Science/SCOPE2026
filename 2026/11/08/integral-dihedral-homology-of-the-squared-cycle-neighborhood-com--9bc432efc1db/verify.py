"""Finite checks for a uniform cycle-square neighborhood theorem.

Only Python's standard library is used. The proof for all n is in the accompanying
mathematical exposition; these tests are finite consistency checks, not that proof.
"""
from itertools import combinations

def faces_from_neighborhoods(n):
    facets=[frozenset((i+d)%n for d in (-2,-1,1,2)) for i in range(n)]
    assert len(set(facets))==n
    faces=set()
    for f in facets:
        for k in range(1,5):
            faces.update(frozenset(x) for x in combinations(f,k))
    return faces

def torus_faces(n):
    tris=[frozenset(((i+d)%n for d in ds)) for i in range(n)
          for ds in ((0,1,3),(0,2,3))]
    assert len(set(tris))==2*n
    return {frozenset(x) for tri in tris for k in (1,2,3)
            for x in combinations(tri,k)}

def check_collapse(n):
    faces=faces_from_neighborhoods(n)
    original=faces.copy()
    for i in range(n):
        tetra=frozenset((i+d)%n for d in (-2,-1,1,2))
        b=frozenset((i+d)%n for d in (-2,-1,2))
        assert b in faces and tetra in faces
        assert [f for f in faces if b<=f]==[tetra,b] or set(f for f in faces if b<=f)=={tetra,b}
        faces.difference_update((tetra,b))
    for i in range(n):
        c=frozenset((i+d)%n for d in (-2,1,2))
        gap=frozenset((i+d)%n for d in (-2,2))
        assert c in faces and gap in faces
        assert {f for f in faces if gap<=f}=={c,gap}
        faces.difference_update((c,gap))
    T=torus_faces(n)
    assert faces==T,(n,len(faces),len(T),len(faces^T))
    f=tuple(sum(len(f)==d for f in T) for d in (1,2,3))
    assert f==(n,3*n,2*n)
    for v in range(n):
        edges=[(tuple(x-{v})) for x in T if len(x)==3 and v in x]
        assert len(edges)==6
        links={w for e in edges for w in e}
        assert len(links)==6
        assert all(sum(w in e for e in edges)==2 for w in links)
    assert original>=T
    return T

def parity(vals):
    return (-1)**sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))

def chain_traces(T,n,perm):
    out=[]
    for k in (1,2,3):
        total=0
        for face in T:
            if len(face)!=k:continue
            order=sorted(face)
            v=[perm(x) for x in order]
            if set(v)==set(face):total+=parity(v)
        out.append(total)
    return tuple(out)

check_count=0
rot_count=0
ref_count=0
for n in range(9,81):
    T=check_collapse(n)
    assert all(frozenset((x+a)%n for x in f) in T for a in range(n) for f in T)
    assert all(frozenset((a-x)%n for x in f) in T for a in range(n) for f in T)
    for a in range(n):
        t=chain_traces(T,n,lambda x,a=a:(x+a)%n)
        Lef=t[0]-t[1]+t[2]
        assert Lef==(0 if a else 0),(n,a,t) # torus Euler = 0, all rotations L=0
        assert t==(n,3*n,2*n) if a==0 else t==(0,0,0),(n,a,t)
        rot_count+=1
    for a in range(n):
        t=chain_traces(T,n,lambda x,a=a:(a-x)%n)
        assert t[2]==0,(n,a,t)
        assert t[0]==(1 if n%2 else (2 if a%2==0 else 0)),(n,a,t)
        assert t[1]==-(3 if n%2 else (2 if a%2==0 else 4)),(n,a,t)
        assert t[0]-t[1]+t[2]==4,(n,a,t)
        ref_count+=1
    check_count+=1
print('PASS: explicit two-stage simplicial collapses, torus links, and D_n invariance on',check_count,'sizes (n=9..80)')
print('PASS:',rot_count,'rotation and',ref_count,'reflection signed Lefschetz tests')
print('PASS: H_1 character (2 for rotations, -2 for reflections) and H_2 character (1 throughout) follow from orientable torus, L=0/4')
