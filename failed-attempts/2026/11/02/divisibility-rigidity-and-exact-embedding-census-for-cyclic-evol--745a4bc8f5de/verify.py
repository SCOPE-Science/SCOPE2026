"""Finite-field checks of cyclic evolution-algebra homomorphisms.

Run: python3 verify.py
Only finite computations are performed; the general classification has a separate proof.
"""
from itertools import product
from math import gcd


class Field:
    def __init__(self, q):
        self.q = q
        self.binary_mod = {4: 0b111, 8: 0b1011, 16: 0b10011}.get(q)
        if q not in (2, 3, 4, 5, 7, 8, 16):
            raise ValueError('unsupported test field')

    def add(self, a, b):
        return a ^ b if self.q in (2, 4, 8, 16) else (a+b) % self.q

    def mul(self, a, b):
        if self.q not in (2, 4, 8, 16):
            return a*b % self.q
        z = 0
        modulus = self.binary_mod or 0b11
        d = self.q.bit_length()-1
        while b:
            if b & 1:
                z ^= a
            b >>= 1
            a <<= 1
            if a & (1 << d):
                a ^= modulus
        return z

    def power(self, a, e):
        out = 1
        while e:
            if e & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            e >>= 1
        return out

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError
        return self.power(a, self.q-2)


def product_evolution(a,b,F):
    m=len(a)
    v=[0]*m
    for j in range(m):
        v[(j+1)%m]=F.mul(a[j],b[j])
    return tuple(v)


def valid_hom(cols,F):
    n=len(cols); m=len(cols[0]); zero=(0,)*m
    for i in range(n):
        if product_evolution(cols[i],cols[i],F)!=cols[(i+1)%n]:
            return False
        for j in range(i+1,n):
            if product_evolution(cols[i],cols[j],F)!=zero:
                return False
    return True


def canonical(n,m,r,c,F):
    assert m % n == 0 and 0<=r<n and c!=0
    assert F.power(c,2**m-1)==1
    first=[0]*m
    for t in range(m//n):
        first[r+n*t]=F.power(c,2**(n*t))
    cols=[tuple(first)]
    for _ in range(n-1):
        cols.append(product_evolution(cols[-1],cols[-1],F))
    return tuple(cols)


def predicted(n,m,F):
    return 1 if m%n else 1+n*gcd(F.q-1,2**m-1)


def check_all_linear(n,m,q):
    F=Field(q)
    found=set()
    for flat in product(range(q),repeat=n*m):
        cols=tuple(tuple(flat[i*m:(i+1)*m]) for i in range(n))
        if valid_hom(cols,F):
            found.add(cols)
    expected={tuple([(0,)*m]*n)}
    if m%n==0:
        roots=[c for c in range(1,q) if F.power(c,2**m-1)==1]
        for r in range(n):
            for c in roots:
                expected.add(canonical(n,m,r,c,F))
    assert found==expected,(n,m,q,len(found),len(expected))
    assert len(found)==predicted(n,m,F)
    print('FULL',n,m,q,len(found),'PASS')


def subspace_signature(cols,F):
    # Disjoint nonzero column supports imply that normalized, pivot-sorted columns
    # are the unique row-reduced echelon basis of the image subspace.
    normalized=[]
    for col in cols:
        ix=next(i for i,a in enumerate(col) if a)
        s=F.inv(col[ix])
        normalized.append((ix,tuple(F.mul(s,a) for a in col)))
    return tuple(v for _,v in sorted(normalized))


def check_subalgebras(n,m,q):
    F=Field(q)
    roots=[c for c in range(1,q) if F.power(c,2**m-1)==1]
    maps=[canonical(n,m,r,c,F) for r in range(n) for c in roots]
    signatures={subspace_signature(cols,F) for cols in maps}
    want=gcd(q-1,2**m-1)//gcd(q-1,2**n-1)
    assert len(signatures)==want
    assert len(maps)==n*gcd(q-1,2**m-1)
    print('SUBALGEBRAS',n,m,q,len(signatures),'PASS')


def main():
    exhaustive=[(1,1,2),(1,2,2),(1,3,3),(1,3,8),
                (2,2,2),(2,2,3),(2,2,4),(2,3,2),
                (2,4,2),(2,4,3),(2,4,4),
                (3,2,3),(3,3,2),(3,3,3),(3,4,2),
                (4,2,2),(1,4,16)]
    for n,m,q in exhaustive:
        check_all_linear(n,m,q)
    for n,m,q in [(1,3,8),(2,4,16),(1,4,16),(2,6,4),(3,6,8)]:
        check_subalgebras(n,m,q)
    print('CYCLIC_EVOLUTION_EMBEDDINGS_OK',len(exhaustive),'complete linear-map enumerations, 5 subalgebra censuses')

if __name__=='__main__':
    main()
