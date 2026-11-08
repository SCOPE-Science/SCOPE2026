"""Exact finite checks of Peirce-spectrum trichotomy for finite abelian cores.
Requires sympy; checks selected explicit idempotents and eigenvectors, not all idempotents.
"""
from itertools import product
import sympy as s

Z=s.Integer(0); I=s.I

def group(moduli):
    return list(product(*(range(n) for n in moduli)))

def op(x,y,moduli):
    return tuple((2*b-a)%n for a,b,n in zip(x,y,moduli))

def R(u,elts,mods):
    inds={x:i for i,x in enumerate(elts)}
    N=len(elts); M=s.zeros(N,N)
    for a,x in enumerate(elts):
        for b,y in enumerate(elts):
            if u[b]: M[inds[op(x,y,mods)],a]+=u[b]
    return M

def mul(u,v,elts,mods):
    inds={x:i for i,x in enumerate(elts)}
    out=s.zeros(len(elts),1)
    for a,x in enumerate(elts):
        for b,y in enumerate(elts):
            if u[a] and v[b]: out[inds[op(x,y,mods)]]+=u[a]*v[b]
    return out

def has_odd_factor(mods):
    return any(n // (n & -n) > 1 for n in mods)

all_groups=[(1,),(2,),(2,2),(3,),(5,),(6,),(9,),
            (2,3),(2,2,3),(4,),(8,),(12,),(2,4),(4,3)]
checks=0
for mods in all_groups:
    elements=group(mods);N=len(elements)
    zero=tuple(0 for n in mods)
    ix={x:i for i,x in enumerate(elements)}
    e0=s.zeros(N,1);e0[ix[zero]]=1
    w=s.ones(N,1)/N
    for u,label in [(e0,'basis'),(w,'uniform')]:
        assert mul(u,u,elements,mods)==u,(mods,label,'idempotent')
        checks+=1
        mat=R(u,elements,mods)
        eig=set(mat.eigenvals())
        if any(n%4==0 for n in mods):
            assert eig<={-1,0,1},(mods,eig)
        elif has_odd_factor(mods):
            assert eig<={-1,0,1},(mods,eig)
        else:
            assert eig=={1},(mods,eig)
        checks+=1
    # Every characteristic-four factor admits explicit idempotents with arbitrary sampled eigenvalue z.
    four=[j for j,n in enumerate(mods) if n%4==0]
    if four:
        j=four[0]
        for z in (s.Integer(0),s.Integer(1),s.Integer(2),-s.Integer(3),s.Rational(3,7),s.Integer(2)+3*I):
            # Fourier support only at the trivial and one sign character of order two.
            u=s.Matrix([(1+z*(-1)**x[j])/N for x in elements])
            assert sum(u)==1,(mods,z,'augmentation')
            assert all(s.simplify(t)==0 for t in mul(u,u,elements,mods)-u),(mods,z,'idempotent')
            checks+=2
            mat=R(u,elements,mods)
            vplus=s.Matrix([I**x[j]+(-I)**x[j] for x in elements])
            vminus=s.Matrix([I**x[j]-(-I)**x[j] for x in elements])
            assert vplus!=s.zeros(N,1) and vminus!=s.zeros(N,1)
            assert all(s.simplify(t)==0 for t in mat*vplus-z*vplus),(mods,z,'plus')
            assert all(s.simplify(t)==0 for t in mat*vminus+z*vminus),(mods,z,'minus')
            checks+=2
    if not four and has_odd_factor(mods):
        # Nontrivial odd component produces a -1 eigenvector of R(e0)
        e=next(x for x in elements if tuple((-a)%n for a,n in zip(x,mods))!=x)
        ne=tuple((-a)%n for a,n in zip(e,mods))
        v=s.zeros(N,1);v[ix[e]]=1;v[ix[ne]]=-1
        assert R(e0,elements,mods)*v==-v
        checks+=1
        # Uniform idempotent has a nonzero kernel when doubling image has >1 element.
        two=next(tuple((2*a)%n for a,n in zip(x,mods)) for x in elements if any((2*a)%n for a,n in zip(x,mods)))
        v=s.zeros(N,1);v[ix[zero]]=1;v[ix[two]]=-1
        assert R(w,elements,mods)*v==s.zeros(N,1)
        checks+=1
    print('CASE',mods,'order',N,'OK')
print('VERIFY_OK configurations=%d exact_assertions=%d all_verified=yes'%(len(all_groups),checks))
