#!/usr/bin/env python3
"""Standalone direct bracket-matrix checks for truncated Witt nilradicals.

Use: python check.py. No nonstandard Python packages are required.
"""
from itertools import product
from collections import Counter
from random import Random


class Field:
    def __init__(self, p, extension=False):
        self.p = p
        self.extension = extension
        if extension and p != 5:
            raise ValueError('The quadratic implementation uses alpha^2=2 over F_5')
        self.q = p*p if extension else p

    def add(self, a, b):
        p = self.p
        if not self.extension:
            return (a+b) % p
        return ((a%p+b%p)%p) + p*((a//p+b//p)%p)

    def neg(self, a):
        p = self.p
        if not self.extension:
            return -a % p
        return (-a % p) + p*((-(a//p)) % p)

    def mul(self, a, b):
        p = self.p
        if not self.extension:
            return a*b % p
        a0, a1 = a%p, a//p
        b0, b1 = b%p, b//p
        return ((a0*b0+2*a1*b1)%p) + p*((a0*b1+a1*b0)%p)

    def inv(self, a):
        assert a
        z = 1
        b = a
        e = self.q-2
        while e:
            if e & 1:
                z = self.mul(z,b)
            b = self.mul(b,b)
            e //= 2
        assert self.mul(z,a) == 1
        return z


def matmul(A,B,F):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for h in range(n):
            a=A[i][h]
            if a:
                for j in range(n):
                    if B[h][j]:
                        C[i][j]=F.add(C[i][j],F.mul(a,B[h][j]))
    return C


def rank(A,F):
    M=[r.copy() for r in A]
    rows=len(M)
    cols=len(M[0]) if rows else 0
    i=0
    for j in range(cols):
        piv=next((k for k in range(i,rows) if M[k][j]),None)
        if piv is None:continue
        M[i],M[piv]=M[piv],M[i]
        inv=F.inv(M[i][j])
        M[i]=[F.mul(v,inv) for v in M[i]]
        for k in range(i+1,rows):
            if M[k][j]:
                fac=M[k][j]
                M[k]=[F.add(u,F.neg(F.mul(fac,v))) for u,v in zip(M[k],M[i])]
        i+=1
        if i==rows:break
    return i


def bracket_matrix(f,F,full=False):
    p=F.p
    basis=list(range(p)) if full else list(range(2,p))
    ix={j:a for a,j in enumerate(basis)}
    A=[[0]*len(basis) for _ in basis]
    for column,j in enumerate(basis):
        for k in range(2,p):
            h=k+j-1
            if h>=p or h not in ix:continue
            coeff=F.mul((j-k)%p,f[k-2])
            A[ix[h]][column]=F.add(A[ix[h]][column],coeff)
    return A


def rank_powers(A,F):
    n=len(A)
    C=[row.copy() for row in A]
    v=[]
    for k in range(1,n+1):
        v.append(rank(C,F))
        C=matmul(C,A,F)
    return tuple(v)


def target(p,i):
    return tuple(max(0,p-2-k*(i-1)) - int(i+k*(i-1)<=p-1) for k in range(1,p-1))


def verify_exhaustive(p,extension=False):
    F=Field(p,extension)
    q=F.q
    n=p-2
    by_order=Counter()
    signatures=Counter()
    for f in product(range(q),repeat=n):
        i=next((j+2 for j,v in enumerate(f) if v),None)
        observed=rank_powers(bracket_matrix(f,F),F)
        predicted=(0,)*n if i is None else target(p,i)
        assert observed==predicted,(p,q,i,f,observed,predicted)
        by_order[i]+=1
        signatures[observed]+=1
    assert by_order[None] == 1
    for i in range(2,p):
        assert by_order[i] == (q-1)*q**(p-i-1)
    assert sum(by_order.values())==q**n
    print(f'EXHAUSTIVE p={p} q={q} elements={q**n} orders={sorted((str(i),n) for i,n in by_order.items())} jordan_signatures={len(signatures)} OK')


def verify_random(p,tests,seed):
    F=Field(p)
    rng=Random(seed)
    for t in range(tests):
        f=[rng.randrange(p) for _ in range(p-2)]
        i=next((j+2 for j,v in enumerate(f) if v),None)
        observed=rank_powers(bracket_matrix(f,F),F)
        predicted=(0,)*(p-2) if i is None else target(p,i)
        assert observed==predicted,(p,f,observed,predicted)
    print(f'RANDOM p={p} q={p} trials={tests} OK')


def verify_ambient_boundary(p):
    F=Field(p)
    f=[1]+[0]*(p-3)
    g=[1,1]+[0]*(p-4)
    Rf=rank_powers(bracket_matrix(f,F,full=True),F)
    Rg=rank_powers(bracket_matrix(g,F,full=True),F)
    assert Rf==tuple(max(0,p-3-k)+max(0,3-k) for k in range(1,p+1))
    assert Rg==tuple(max(0,p-1-k) for k in range(1,p+1))
    assert rank_powers(bracket_matrix(f,F),F)==rank_powers(bracket_matrix(g,F),F)
    print(f'AMBIENT p={p} monomial_partition={tuple(sorted((p-3,3),reverse=True))} perturbed_partition={(p-1,1)} OK')


if __name__=='__main__':
    verify_exhaustive(5)
    verify_exhaustive(7)
    verify_exhaustive(5,True)
    verify_random(11,500,1)
    verify_random(13,500,2)
    for p in (5,7,11,13):
        verify_ambient_boundary(p)
    print('WITT_NILRADICAL_JORDAN_DIRECT_BRACKET_OK')
