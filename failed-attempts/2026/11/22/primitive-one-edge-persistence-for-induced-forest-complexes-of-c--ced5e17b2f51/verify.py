#!/usr/bin/env python3
"""Independent finite enumeration of vertex-induced forest complexes for matching-complement graphs before/after one cross edge deletion."""
import itertools
from collections import defaultdict

def enumerate_faces(m, delete_extra=False):
    n=2*m
    edges={(u,v) for u in range(n) for v in range(u+1,n) if u//2!=v//2}
    if delete_extra:edges.remove((0,2))
    faces=defaultdict(list)
    for r in range(n+1):
        for t in itertools.combinations(range(n),r):
            # union-find cycle detector
            parent={v:v for v in t}
            def root(x):
                while parent[x]!=x:x=parent[x]
                return x
            ok=True
            for u,v in itertools.combinations(t,2):
                if (u,v) not in edges:continue
                a,b=root(u),root(v)
                if a==b:ok=False;break
                parent[a]=b
            if ok and r:faces[r-1].append(t)
    return faces

def rank_gf(faces,p):
    rs=[]
    for d in sorted(faces):
        if d==0:continue
        idx={c:i for i,c in enumerate(faces[d-1])}
        piv={}
        for t in faces[d]:
            vec={idx[t[:j]+t[j+1:]]: (-1)**j%p for j in range(d+1)}
            while vec:
                k=min(vec)
                if k not in piv:
                    inv=pow(vec[k],-1,p)
                    piv[k]={a:b*inv%p for a,b in vec.items() if b%p}
                    break
                c=vec[k]
                for a,b in piv[k].items():
                    vec[a]=(vec.get(a,0)-c*b)%p
                    if not vec[a]:vec.pop(a,None)
        rs.append((d,len(piv)))
    return dict(rs)

def reduced_bettis(faces, p):
    ranks=rank_gf(faces,p);ans={}
    for d in sorted(faces):
        betti=len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:betti-=1
        if betti:ans[d]=betti
    return ans

def main():
    for m in range(2,7):
        for p in (2,3,5):
            base=enumerate_faces(m)
            faulty=enumerate_faces(m,True)
            b=reduced_bettis(base,p)
            c=reduced_bettis(faulty,p)
            expected={1:(m-1)*(m-2)//2,2:m*(m-1)//2}
            expected={k:v for k,v in expected.items() if v}
            exp2={1:(m-2)*(m-3)//2,2:m*(m-1)//2+m-3}
            exp2={k:v for k,v in exp2.items() if v}
            assert b==expected,(m,p,b,expected)
            assert c==exp2,(m,p,c,exp2)
            added={d:len(faulty[d])-len(base.get(d,[])) for d in faulty}
            assert added.get(2,0)==2*m-4 and added.get(3,0)==1,(m,added)
            print(f'm={m} p={p} baseline={b} fault={c} added_faces={added}')
if __name__=='__main__':main()

# Additional exact face and integral chain assertions, independent of field ranks.
def boundary(cell):
    out={}
    for i in range(len(cell)):
        face=cell[:i]+cell[i+1:]
        out[face]=out.get(face,0)+(-1)**i
    return out

def addchains(*weighted):
    result={}
    for mul,chain in weighted:
        for c,v in chain.items():result[c]=result.get(c,0)+mul*v
    return {k:v for k,v in result.items() if v}

def bdchain(chain):
    out={}
    for c,a in chain.items():
        for f,v in boundary(c).items():out[f]=out.get(f,0)+a*v
    return {k:v for k,v in out.items() if v}

def exact_checks():
    for m in range(2,7):
        old=enumerate_faces(m); new=enumerate_faces(m,True)
        n=2*m
        allowed_old=set(itertools.combinations(range(n),1)) | set(itertools.combinations(range(n),2))
        allowed_old|={t for t in itertools.combinations(range(n),3) if any(a//2==b//2 for a,b in itertools.combinations(t,2))}
        assert set().union(*map(set,old.values()))==allowed_old
        expected_new=allowed_old | {(0,2,x) for x in range(4,n)} | {(0,1,2,3)}
        assert set().union(*map(set,new.values()))==expected_new
        sphere12=boundary((0,1,2,3))
        assert all(f in old[2] for f in sphere12)
        assert not bdchain(sphere12)
        for k in range(2,m):
            # The tetrahedral boundary uses two new triangles and two old triangles;
            # it is a geometrically embedded two-sphere, not a filled tetrahedron.
            verts=(0,2,2*k,2*k+1)
            z=boundary(verts)
            assert all(c in new[2] for c in z)
            assert (verts not in new.get(3,[]))
            assert not bdchain(z)
            diff=addchains((1,boundary((0,2,2*k))),(-1,boundary((0,2,2*k+1))))
            assert diff == addchains((-1,boundary((0,2*k,2*k+1))),(1,boundary((2,2*k,2*k+1))))
        print(f'EXACT m={m} face-prediction=PASS old-sphere-boundary=PASS new-sphere-cycles=PASS')
if __name__=='__main__':exact_checks()
