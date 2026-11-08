#!/usr/bin/env python3
"""Standalone finite-field checks of symmetric-matrix Fourier sampling.

No extra dependencies beyond Python's standard library and NumPy.
The symbolic proof for all odd prime powers is in RESULT.md;
these computations cover explicit finite fields only.
"""
import cmath
import itertools
import numpy as np


def field(p, degree):
    """For degree two use the irreducible X^2+1 over F_3."""
    if degree == 1:
        return list(range(p)), lambda a,b: (a+b)%p, lambda a,b:(a*b)%p, lambda a:a%p
    assert (p,degree)==(3,2)
    E=[(a,b) for a in range(p) for b in range(p)]
    add=lambda x,y:((x[0]+y[0])%p,(x[1]+y[1])%p)
    mul=lambda x,y:((x[0]*y[0]-x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    tr=lambda a:(2*a[0])%p
    return E,add,mul,tr


def analyze(p, degree, direct_S):
    E,add,mul,tr=field(p,degree)
    q=len(E);zero=E[0]
    sub=lambda a,b:add(a,neg(b))
    neg=lambda a:sub_int(a)
    def sub_int(a):
        if degree==1:return (-a)%p
        return ((-a[0])%p,(-a[1])%p)
    def dot(x,y):
        a,b,c=x;u,v,w=y
        return add(add(mul(a,u),add(mul(b,v),mul(b,v))),mul(c,w))
    def Q(x):
        a,b,c=x
        return sub(mul(a,c),mul(b,b))
    def character(z):return cmath.exp(2j*np.pi*tr(z)/p)
    V=list(itertools.product(E,repeat=3))
    C=[x for x in V if Q(x)==zero]
    S=[x for x in V if Q(x)!=zero]
    assert len(C)==q*q and len(S)==q*q*(q-1)
    if degree==1:
        leg=lambda z: 0 if z==0 else (1 if pow(z,(q-1)//2,q)==1 else -1)
    else:
        def leg(z):
            if z==zero:return 0
            z2=mul(z,z);z4=mul(z2,z2);return 1 if z4==(1,0) else -1
    # Exact integer combinatorics: the dual-conic Fourier formula.
    for u in V:
        if u== (zero,zero,zero):continue
        roots=sum(1 for v in C if dot(u,v)==zero)
        # Restriction of a linear functional to a union of conic lines:
        # q*k lines meet its kernel, where k = 1 + quadratic character.
        assert roots==1+(q-1)*(1+leg(neg(Q(u))))
    H=np.array([[character(dot(x,y)) for y in C] for x in C],dtype=complex)
    actual=np.linalg.eigvalsh(H.conj().T@H)
    target=sorted([q**3]+[q]*q+[q*q]*(q*q-q-1))
    assert np.max(np.abs(actual-target)) < 1e-6 * q**3
    if direct_S:
        F=np.array([[character(dot(x,y)) for y in S] for x in S],dtype=complex)
        spectrum=np.linalg.eigvalsh(F.conj().T@F)
        expected=sorted([q**3]*(q*q*(q-2)+1)+[q*q]*(q*q-q-1)+[q]*q)
        assert len(spectrum)==len(expected)
        assert np.max(np.abs(spectrum-expected))<1e-6*q**3
    print(f"PASS q={q}: |C|={len(C)}, |S|={len(S)}, expected levels q, q², q³; direct_S={direct_S}")


if __name__=='__main__':
    analyze(3,1,True)
    analyze(5,1,True)
    analyze(7,1,False)
    analyze(3,2,False)
    print('SYMMETRIC_NONDEGENERATE_FOURIER_PASS')
