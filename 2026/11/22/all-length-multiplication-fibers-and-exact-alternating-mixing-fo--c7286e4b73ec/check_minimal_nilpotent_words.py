#!/usr/bin/env python3
"""Direct finite-field matrix multiplication versus exact nilpotent word fibers.

The script enumerates rank-one square-zero matrices from their normalized outer
products and performs ordinary matrix multiplication. No external packages.
"""
from itertools import product
from collections import defaultdict

class Field:
    def __init__(self, q):
        self.q = q
        if q not in (2,3,4,5):
            raise ValueError('supported verification fields: 2,3,4,5')
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q
    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.q
        t = 0
        for i in range(2):
            for j in range(2):
                if (a >> i) & 1 and (b >> j) & 1:
                    t ^= 1 << (i+j)
        if t & 8:  # reduction by z^2+z+1, harmless for degree<4
            t ^= 0b1100
        if t & 4:
            t ^= 0b111
        return t
    def dot(self, a, b):
        s = 0
        for x,y in zip(a,b): s = self.add(s, self.mul(x,y))
        return s
    def inv(self, a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b) == 1)

def matrices(n, F):
    vecs = [v for v in product(range(F.q), repeat=n) if any(v)]
    out = set()
    for u in vecs:
        first = next(x for x in u if x)
        if first != 1: continue
        for v in vecs:
            if F.dot(u,v) == 0:
                out.add(tuple(F.mul(a,b) for a in u for b in v))
    return sorted(out)

def multiply(A,B,n,F):
    return tuple(
        fold(F, (F.mul(A[i*n+t],B[t*n+j]) for t in range(n)))
        for i in range(n) for j in range(n)
    )

def fold(F, terms):
    a=0
    for b in terms: a=F.add(a,b)
    return a

def rank1_targets(n,F):
    vecs = [v for v in product(range(F.q),repeat=n) if any(v)]
    out=set()
    for u in vecs:
        if next(x for x in u if x) != 1: continue
        for v in vecs:
            out.add(tuple(F.mul(a,b) for a in u for b in v))
    return out

def predicted(M,n,q,k,F):
    if not any(M):
        N = (q**n-1)*(q**(n-1)-1)//(q-1)
        return N**k - N*(q**(n-1)*(q**(n-1)-1))**(k-1)
    P = (q**n-1)//(q-1)
    H = (q**(n-1)-1)//(q-1)
    r=k-1
    trace=fold(F,(M[i*n+i] for i in range(n)))
    sign=(-1)**r
    projective = H * ((P-1)**r-sign)//P + (sign if trace==0 else 0)
    return (q**(n-2)*(q-1))**r * projective

def check(n,q,top):
    F=Field(q)
    nil=matrices(n,F)
    zero=(0,)*(n*n)
    N=(q**n-1)*(q**(n-1)-1)//(q-1)
    assert len(nil)==N,(n,q,len(nil),N)
    targets=rank1_targets(n,F)
    expected_targets=(q**n-1)**2//(q-1)
    assert len(targets)==expected_targets
    dist={m:1 for m in nil}
    for k in range(2,top+1):
        nxt=defaultdict(int)
        for a,ways in dist.items():
            if a==zero:
                nxt[zero]+=ways*N
                continue
            for b in nil:
                nxt[multiply(a,b,n,F)]+=ways
        dist=dict(nxt)
        assert sum(dist.values())==N**k
        assert not (set(dist)-targets-{zero})
        for c in targets:
            assert dist.get(c,0)==predicted(c,n,q,k,F),(n,q,k,c,dist.get(c,0),predicted(c,n,q,k,F))
        assert dist.get(zero,0)==predicted(zero,n,q,k,F)
        r=k-1
        P=(q**n-1)//(q-1)
        H=(q**(n-1)-1)//(q-1)
        f_nil=(q**(n-2)*(q-1))**r * (H*((P-1)**r-(-1)**r)//P+(-1)**r)
        f_non=(q**(n-2)*(q-1))**r * (H*((P-1)**r-(-1)**r)//P)
        assert f_nil - f_non == (-q**(n-2)*(q-1))**r
        print(f'PASS n={n} q={q} k={k} factors={N} nonzero_targets={len(targets)} zero_fiber={dist.get(zero,0)} nil_fiber={f_nil} nonnil_fiber={f_non}')

if __name__ == '__main__':
    for n,q,top in [(2,2,6),(2,3,6),(2,4,5),(2,5,5),(3,2,5),(3,3,4),(3,4,3),(4,2,3)]:
        check(n,q,top)
    print('VERIFY_OK')
