#!/usr/bin/env python3
"""Exact integer and Fourier checks for the primitive nilpotent Cayley spectrum.

No dependencies beyond the Python standard library. Full frequency checks at
(3,2), (3,3), (5,2); direct character sums at (3,2) and selected higher levels.
"""
from collections import Counter
from itertools import product
from math import cos, sin, pi
from random import Random


def projective_representatives(p, k):
    n = p**k
    return [(1, x) for x in range(n)] + [(p*x, 1) for x in range(n//p)]


def primitive_nilpotents(p, k):
    n = p**k
    return [((-s*x*y)%n, (s*x*x)%n, (-s*y*y)%n, (s*x*y)%n)
            for x,y in projective_representatives(p,k)
            for s in range(n) if s%p]


def discriminant_data(A,p,k):
    # The quadratic form is (Ju)^T A u, for Ju=(-y,x).
    C=(A[2], A[3]-A[0], -A[1])
    t=0
    while t<k and all(c%(p**(t+1))==0 for c in C):
        t+=1
    if t==k:
        return t,k,0
    m=k-t; a,b,c=((v//(p**t))%(p**m) for v in C)
    return t,m,(b*b-4*a*c)%(p**m)


def valuation(d,p,m):
    for s in range(m):
        if d%(p**(s+1)):
            return s
    return m


def sign(d,p):
    x=d%p
    if x==0:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1


def eigenvalue(A,p,k):
    t,m,D=discriminant_data(A,p,k)
    if t==k:
        return (p*p-1)*p**(2*k-2)
    if m==1:
        s=sign(D,p)
        z=1+s  # 0,1,2 projective roots
        return p**(2*k-2)*(p*z-p-1)
    v=valuation(D,p,m)
    if m%2==0:
        h=m//2
        if v==m:return (p-1)*p**(k+t+h-1)
        if v==m-1:return -p**(k+t+h-1)
        return 0
    h=(m-1)//2
    if v==m-1:return sign(D//(p**(m-1)),p)*p**(k+t+h)
    return 0


def predicted_multiset(p,k):
    out=Counter()
    def add(lam,mul):out[lam]+=mul
    degree=(p*p-1)*p**(2*k-2)
    add(degree,p**k)
    base=p**(2*k-2)
    add(-(p+1)*base,p**k*p*(p-1)**2//2)
    add(-base,p**k*(p*p-1))
    add((p-1)*base,p**k*p*(p*p-1)//2)
    for m in range(2,k+1):
        t=k-m
        H=(p*p-1)*p**(2*m-2)
        if m%2==0:
            lam=p**(k+t+m//2-1)
            add((p-1)*lam,p**k*H)
            add(-lam,p**k*(p-1)*H)
        else:
            lam=p**(k+t+(m-1)//2)
            add(lam,p**k*(p-1)*H//2)
            add(-lam,p**k*(p-1)*H//2)
    nonzero=sum(v for lam,v in out.items() if lam)
    out[0]+=p**(4*k)-nonzero
    assert out[0]>=0
    return out


def direct_fourier(A,S,n):
    # Independent exponential computation, without Ramanujan or root formula.
    residues=Counter(sum(a*x for a,x in zip(A,N))%n for N in S)
    z=sum(v*complex(cos(2*pi*t/n),sin(2*pi*t/n)) for t,v in residues.items())
    return z


def verify():
    for p,k in ((3,2),(3,3),(5,2)):
        predicted=predicted_multiset(p,k)
        found=Counter(eigenvalue(A,p,k) for A in product(range(p**k),repeat=4))
        assert found==predicted,(p,k,found-predicted,predicted-found)
        assert sum(lam*cnt for lam,cnt in found.items())==0
        S_size=(p*p-1)*p**(2*k-2)
        assert sum(lam*lam*cnt for lam,cnt in found.items())==p**(4*k)*S_size
        assert found[0]==p**(4*k)-sum(cnt for lam,cnt in found.items() if lam)
        print(f'p={p}, k={k}: {p**(4*k)} eigenvalues, nonzero={p**(4*k)-found[0]}')
    for p,k in ((3,2),(5,2),(3,3),(3,4),(5,3)):
        n=p**k
        S=primitive_nilpotents(p,k)
        assert len(S)==(p*p-1)*p**(2*k-2)
        assert len(set(S))==len(S)
        rr=Random(301+p*100+k)
        if p==3 and k==2:
            inputs=product(range(n),repeat=4)
        else:
            inputs=[tuple(rr.randrange(n) for _ in range(4)) for _ in range(160)]
            inputs.extend([(0,0,0,0),(1,0,0,1),(0,0,0,1),(0,1,0,0)])
        for A in inputs:
            z=direct_fourier(A,S,n)
            target=eigenvalue(A,p,k)
            assert abs(z-target)<1e-6,(p,k,A,z,target)
        print(f'p={p}, k={k}: direct character-sum comparison PASS')
    print('PRIMITIVE_NILPOTENT_LOCAL_SPECTRUM_PASS')

if __name__=='__main__':
    verify()
