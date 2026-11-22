"""Finite checks of orbit stabilizers and integral boundary matrices for cycle independence complexes.

Run: python verify_cycle_new.py (requires SymPy). This is not a proof for arbitrary n.
"""
from itertools import combinations
from math import gcd
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def independent(s,n):
    t=set(s)
    return all((i+1)%n not in t for i in t)

def has_fixed_face(n,steps):
    unseen=set(range(n))
    orbits=[]
    while unseen:
        a=next(iter(unseen)); o={a}; q=[a]
        while q:
            b=q.pop()
            for f in steps:
                c=f(b)
                if c not in o:o.add(c);q.append(c)
        orbits.append(o);unseen-=o
    return any(independent(o,n) for o in orbits)

def check_stabilizers():
    for n in range(8,21):
        for a in range(1,n):
            got=has_fixed_face(n,[lambda v,a=a:(v+a)%n])
            assert got == (gcd(n,a)>1),(n,a,got)
        for k in range(n):
            assert has_fixed_face(n,[lambda v,k=k:(k-v)%n]),(n,k)

def orbit_chains(p):
    def rot(ss,j):return tuple(sorted((v+j)%p for v in ss))
    def rep(ss):return min(rot(ss,j) for j in range(p))
    faces={}
    for k in range(1,p//2+1):
        allf=[s for s in combinations(range(p),k) if independent(s,p)]
        faces[k]=sorted({rep(s) for s in allf})
        assert len(allf)==p*len(faces[k])
    mat={}
    for k in range(2,len(faces)+1):
        I={s:i for i,s in enumerate(faces[k-1])}
        B=sp.zeros(len(faces[k-1]),len(faces[k]))
        for j,s in enumerate(faces[k]):
            for h in range(k):
                sub=s[:h]+s[h+1:]
                target=rep(sub)
                shift=next(a for a in range(p) if rot(sub,a)==target)
                transformed=[(v+shift)%p for v in sub]
                inversions=sum(transformed[u]>transformed[v] for u in range(len(sub)) for v in range(u+1,len(sub)))
                B[I[target],j]+=(-1)**(h+inversions)
        mat[k]=B
    for k in range(3,len(faces)+1):
        assert mat[k-1]*mat[k]==sp.zeros(mat[k-1].rows,mat[k].cols)
    diag={}
    rank={}
    for k,B in mat.items():
        S=smith_normal_form(B,domain=ZZ)
        diag[k]=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
        rank[k]=B.rank()
    betti=[len(faces[k])-rank.get(k,0)-rank.get(k+1,0) for k in faces]
    d=(p-2)//3
    assert betti==[1]+[int(i==d) for i in range(1,len(faces))],(p,betti)
    assert [x for x in diag[3] if x!=1]==[p]
    assert sorted([x for D in diag.values() for x in D if x!=1])==[p]*((d-1)//2)
    print('p',p,'cells',list(map(len,faces.values())),'betti',betti,'nonunit invariants', [x for D in diag.values() for x in D if x!=1])

if __name__=='__main__':
    check_stabilizers()
    for p in [11,13,17]:orbit_chains(p)
    print('CYCLE_QUOTIENT_VERIFIED')
