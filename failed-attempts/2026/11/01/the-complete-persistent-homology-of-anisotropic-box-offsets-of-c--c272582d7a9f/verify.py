"""Finite rational/cubical checks for an anisotropic skeleton-offset theorem.
Run: python verify.py. No third-party packages required.
These finite tests supplement, and do not replace, the geometric proof.
"""
from itertools import product, combinations
from fractions import Fraction as F
from math import comb

def beta(q,k):
    return sum((-1)**(j-k-1)*2**(q-j)*comb(q,j) for j in range(k+1,q+1)) if q>k else 0

def rank_F2(vectors):
    basis={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in basis: v^=basis[p]
            else:
                basis[p]=v
                break
    return len(basis)

def cubical_betti(q,k):
    cells = [c for c in product((-1,0,1), repeat=q) if c.count(0)<=k]
    bydeg={j:[c for c in cells if c.count(0)==j] for j in range(k+1)}
    brank={0:0}
    for j in range(1,k+1):
        ids={c:i for i,c in enumerate(bydeg[j-1])}
        cols=[]
        for cell in bydeg[j]:
            v=0
            for a in range(q):
                if cell[a]==0:
                    for s in (-1,1):
                        f=list(cell);f[a]=s
                        v^=1<<ids[tuple(f)]
            cols.append(v)
        brank[j]=rank_F2(cols)
    vals={}
    for j in range(k+1):
        b=len(bydeg[j])-brank.get(j,0)-brank.get(j+1,0)
        vals[j]=b - (1 if j==0 else 0)
    return vals

def face_union_member(x,a,b,lam,k):
    d=len(a)
    if any(abs(x[i])>a[i]+lam*b[i] for i in range(d)): return False
    for fixed in combinations(range(d),d-k):
        if all(abs(abs(x[i])-a[i])<=lam*b[i] for i in fixed):
            return True
    return False

def slab_count_member(x,a,b,lam,k):
    if any(abs(z)>aa+lam*bb for z,aa,bb in zip(x,a,b)): return False
    return sum(abs(abs(z)-aa)<=lam*bb for z,aa,bb in zip(x,a,b))>=len(a)-k

def active_member(x,a,b,lam,k):
    if any(abs(z)>aa+lam*bb for z,aa,bb in zip(x,a,b)):return False
    act=[i for i in range(len(a)) if lam*b[i]<a[i]]
    return sum(abs(x[i])>=a[i]-lam*b[i] for i in act)>=len(act)-k

def test():
    checks=0
    for q in range(1,7):
        for k in range(q):
            val=cubical_betti(q,k)
            assert val[k]==beta(q,k),(q,k,val)
            assert all(n==0 for j,n in val.items() if j!=k),(q,k,val)
            checks+=1
    for q in range(2,9):
        for k in range(q):
            assert beta(q,k)>=beta(q-1,k)
            checks+=1
    for d in (2,3,4):
        a=[F(i+1) for i in range(d)]
        b=[F(1) for i in range(d)]
        for k in range(d):
            for lam in (F(0),F(1,2),F(1),F(3,2),F(2),F(3),F(4)):
                grids=[]
                for aa,bb in zip(a,b):
                    grids.append(sorted(set([-aa-lam*bb,-aa,-aa+lam*bb,F(0),aa-lam*bb,aa,aa+lam*bb])))
                for x in product(*grids):
                    z=face_union_member(x,a,b,lam,k)
                    assert z==slab_count_member(x,a,b,lam,k)==active_member(x,a,b,lam,k),(d,k,lam,x)
                    checks+=1
    print('PASS:',checks,'checks; cubical Betti ranks through dimension 6; rational skeleton-offset membership grids through dimension 4')

if __name__=='__main__':test()
