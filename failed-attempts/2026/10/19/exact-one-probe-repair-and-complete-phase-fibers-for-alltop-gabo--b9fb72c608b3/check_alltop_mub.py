#!/usr/bin/env python3
"""Finite-field numerical checks for the Alltop MUB phase-fiber theorem.
Science only; uses no research service or external data.
"""
import cmath, math
import numpy as np


def base_prime(p):
    elems=list(range(p))
    add=lambda a,b:(a+b)%p
    neg=lambda a:(-a)%p
    mul=lambda a,b:(a*b)%p
    psi=lambda a:np.exp(2j*math.pi*(a%p)/p)
    return elems,add,neg,mul,psi


def base_25():
    # Elements a+bt, t^2=2 over F_5, trace(a+bt)=2a.
    elems=list(range(25))
    add=lambda x,y:((x%5+y%5)%5)+5*((x//5+y//5)%5)
    neg=lambda x:(-x%5)+5*((-(x//5))%5)
    mul=lambda x,y:((x%5*y%5+2*(x//5)*(y//5))%5)+5*(((x%5)*(y//5)+(x//5)*(y%5))%5)
    psi=lambda a:np.exp(2j*math.pi*((2*(a%5))%5)/5)
    return elems,add,neg,mul,psi


def check_field(name,data,rank=True):
    xs,add,neg,mul,psi=data
    q=len(xs)
    sub=lambda a,b:add(a,neg(b))
    cube=lambda a:mul(mul(a,a),a)
    V=np.empty((q*q,q),dtype=complex)
    for h in xs:
        for k in xs:
            for t in xs:
                z=add(cube(sub(t,h)),mul(k,t))
                V[h*q+k,t]=psi(z)/math.sqrt(q)
    # Each group of q rows is a mutually unbiased orthonormal basis.
    overlaps=V@V.conj().T
    for h in xs:
        D=overlaps[h*q:(h+1)*q,h*q:(h+1)*q]
        assert np.max(abs(D-np.eye(q)))<2e-12
        for j in range(h+1,q):
            C=overlaps[h*q:(h+1)*q,j*q:(j+1)*q]
            assert np.max(abs(abs(C)-1/math.sqrt(q)))<2e-12
    if rank:
        P=np.einsum('ni,nj->nij',V,V.conj()).reshape(q*q,q*q)
        d=int(np.linalg.matrix_rank(P,tol=1e-8))
        assert d==q*q-q+1,(q,d)
        # In particular all traceless diagonal observables vanish.
        for j in range(q-1):
            dtest=np.zeros((q,q),complex);dtest[j,j]=1;dtest[j+1,j+1]=-1
            assert np.max(np.abs(np.einsum('ni,ij,nj->n',V.conj(),dtest,V)))<1e-12
        print(f'q={q}: {q} mutually unbiased bases; operator rank {d} of {q*q}')
    else:
        print(f'q={q}: {q} mutually unbiased bases; exact rank predicted {q*q-q+1} (rank not computed)')
    x=np.zeros(q,complex); y=np.zeros(q,complex)
    x[0]=3/5;x[1]=4j/5
    y[0]=4/5;y[1]=3j/5
    m1=abs(V.conj()@x)**2
    m2=abs(V.conj()@y)**2
    assert np.max(abs(m1-m2))<1e-12
    bad=np.ones(q,complex)
    assert abs(abs(np.vdot(bad,x))**2-abs(np.vdot(bad,y))**2)<1e-12
    opt=np.sqrt(np.arange(q)*2/(q*(q-1)))
    assert abs(np.linalg.norm(opt)-1)<1e-12
    assert abs(abs(np.vdot(opt,x))**2-abs(np.vdot(opt,y))**2)>1e-9
    assert abs(np.min(np.diff(abs(opt)**2))-2/(q*(q-1)))<1e-13
    print(f'q={q}: exact 2-site ambiguity, equal-weight obstruction, separating probe and optimal gap verified')

for p in (5,7,11):
    check_field(str(p),base_prime(p))
check_field('25',base_25(),rank=False)
print('ALL CHECKS PASSED')
