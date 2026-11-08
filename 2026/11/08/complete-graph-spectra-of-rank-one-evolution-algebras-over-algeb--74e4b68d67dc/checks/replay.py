"""Exact finite-family checks for graph spectra of rank-one evolution algebras.
Requires sympy 1.14.0.  These checks are illustrations, not an exhaustive proof.
"""
from itertools import combinations
from math import comb
import sympy as s
I=s.I

def support(v):
    return {i for i,x in enumerate(v) if s.simplify(x)!=0}

def refl(a,b):
    u=a-b
    sq=s.simplify((u.T*u)[0])
    if all(s.simplify(x)==0 for x in u):return s.eye(len(a))
    if sq==0:return None
    return s.eye(len(a))-2*u*u.T/sq

def orth_map(a,b):
    assert s.simplify((a.T*a)[0]-(b.T*b)[0])==0
    h=refl(a,b)
    if h is not None:return h
    n=len(a)
    trials=[s.eye(n)[:,i] for i in range(n)]
    trials += [s.eye(n)[:,i]+s.eye(n)[:,j] for i in range(n) for j in range(i+1,n)]
    for t in trials:
        if s.simplify((t.T*t)[0])==0:continue
        ht=s.eye(n)-2*t*t.T/(t.T*t)[0]
        c=ht*a
        h2=refl(c,b)
        if h2 is not None:return h2*ht
    raise AssertionError('reflection search failed')

def build(d,r,flavor,sa,sr):
    n=d+r
    if flavor=='radical':
        assert r and not sa and sr
        z=s.Matrix([int(j in sr) for j in range(r)])
        pivot=min(sr)
        q=s.Matrix.hstack(z,*[s.eye(r)[:,j] for j in range(r) if j!=pivot]) if r>1 else s.Matrix([[1]])
        assert q.det()!=0
        pr=q.inv()
        P=s.diag(*([1]*d+[1]*r))
        P[d:,d:]=pr
        v=s.Matrix([0]*d+[1]+[0]*(r-1))
    else:
        assert sa and (flavor=='anisotropic' or len(sa)>=2)
        w=s.Matrix(([1]+[0]*(d-1)) if flavor=='anisotropic' else [1,I]+[0]*(d-2))
        ordered=sorted(sa); k=len(ordered)
        z=s.zeros(d,1)
        for j in ordered[:-1]:z[j]=2 if flavor=='anisotropic' else 1
        if flavor=='anisotropic': z[ordered[-1]]=s.sqrt(1-4*(k-1))
        else: z[ordered[-1]]=s.sqrt(-(k-1))
        assert support(z)==set(sa)
        H=orth_map(z,w)
        assert all(s.simplify(x)==0 for x in H.T*H-s.eye(d))
        P=s.eye(n);P[:d,:d]=H
        if r:
            j=ordered[0]
            for idx in sr:
                P[d+idx,j]=-1/z[j]
        v=s.Matrix(list(w)+[0]*r)
    gram=s.diag(*([1]*d+[0]*r))
    assert P.det()!=0
    assert all(s.simplify(x)==0 for x in P.T*gram*P-gram)
    coords=P.inv()*v
    assert support(coords)==set(sa)|{d+j for j in sr}
    assert all(s.simplify(x)==0 for x in P*coords-v)
    return P,coords

def subsets(u):
    return [set(c) for k in range(len(u)+1) for c in combinations(u,k)]

count=0
for d in range(1,4):
    for r in range(0,3):
        for flavor in ('radical','anisotropic','isotropic'):
            if flavor=='radical' and r==0:continue
            if flavor=='isotropic' and d<2:continue
            got=0
            for a in subsets(range(d)):
                for b in subsets(range(r)):
                    valid=(not a and bool(b)) if flavor=='radical' else (len(a)>= (2 if flavor=='isotropic' else 1))
                    if not valid:continue
                    P,z=build(d,r,flavor,a,b)
                    got+=1;count+=1
            exp={'radical':2**r-1,'anisotropic':2**r*(2**d-1),
                 'isotropic':2**r*(2**d-d-1)}[flavor]
            assert got==exp,(d,r,flavor,got,exp)
            print('OK d=%s r=%s %s patterns=%s'%(d,r,flavor,got))
print('VERIFY_OK constructed_patterns=%d'%count)
