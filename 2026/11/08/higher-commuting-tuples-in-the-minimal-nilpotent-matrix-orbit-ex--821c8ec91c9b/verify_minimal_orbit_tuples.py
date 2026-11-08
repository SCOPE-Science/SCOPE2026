#!/usr/bin/env python3
"""Independent finite-field checks for commuting tuples of rank-one nilpotents.
Run: python3 verify_minimal_orbit_tuples.py
No external Python packages are required.
"""
from itertools import product
from functools import lru_cache
from math import comb, prod

class Field:
    def __init__(self, order):
        self.q = order
        assert order in (2, 3, 4, 5)
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q
    def mul(self, a, b):
        if self.q != 4: return (a * b) % self.q
        x = 0
        for i in range(2):
            if (b >> i) & 1: x ^= a << i
        if x & 8: x ^= 0b1100
        if x & 4: x ^= 0b111
        return x
    def dot(self, u, v):
        a=0
        for x,y in zip(u,v): a=self.add(a,self.mul(x,y))
        return a


def gaussian(n,d,q):
    return prod(q**(n-i)-1 for i in range(d)) // prod(q**(d-i)-1 for i in range(d))

def surjective_nonzero_columns(r,d,q):
    def surj(c):
        if c<d: return 0
        return prod(q**c-q**i for i in range(d))
    return sum((-1)**j*comb(r,j)*surj(r-j) for j in range(r+1))

def formula_by_d(n,r,q):
    return {d:gaussian(n,d,q)*surjective_nonzero_columns(r,d,q)*((q**(n-d)-1)//(q-1))**r
            for d in range(1,min(n-1,r)+1)}

def minimal_orbit(n, field):
    q=field.q
    out=set()
    for u in product(range(q),repeat=n):
        if not any(u): continue
        for f in product(range(q),repeat=n):
            if not any(f) or field.dot(u,f):continue
            out.add(tuple(field.mul(x,y) for x in u for y in f))
    return sorted(out)

def matmul(A,B,n,F):
    return tuple(F.dot(A[n*i:n*(i+1)], tuple(B[n*k+j] for k in range(n))) for i in range(n) for j in range(n))

def rank_rows(rows,F):
    if not rows:return 0
    m=[list(row) for row in rows]
    h=len(m); w=len(m[0]); rank=0
    for c in range(w):
        piv=next((i for i in range(rank,h) if m[i][c]),None)
        if piv is None: continue
        m[rank],m[piv]=m[piv],m[rank]
        inv=next(x for x in range(1,F.q) if F.mul(x,m[rank][c])==1)
        m[rank]=[F.mul(inv,x) for x in m[rank]]
        for i in range(h):
            if i!=rank and m[i][c]:
                t=m[i][c]
                m[i]=[F.add(m[i][j],F.mul(t,m[rank][j]) if F.q==4 or F.q==2 else (-F.mul(t,m[rank][j]))%F.q) for j in range(w)]
        rank+=1
        if rank==h:break
    return rank

def image_span(A_tuple,n,F):
    # Columns of the stacked matrix of images.
    cols=[tuple(A[n*i+j] for i in range(n)) for A in A_tuple for j in range(n)]
    return rank_rows(cols,F)

def check(n,r,q):
    F=Field(q); orbit=minimal_orbit(n,F)
    zero=(0,)*(n*n)
    assert len(orbit)==((q**n-1)*(q**(n-1)-1))//(q-1)
    near=[0]*len(orbit)
    for i,A in enumerate(orbit):
        for j,B in enumerate(orbit):
            AB=matmul(A,B,n,F);BA=matmul(B,A,n,F)
            commute=(AB==BA)
            annihilate=(AB==zero and BA==zero)
            assert commute==annihilate,(n,q,A,B)
            if commute: near[i] |= 1<<j
    predicted=formula_by_d(n,r,q)
    measured={d:0 for d in predicted}
    # For r>3 only small cases; bitset clique tests plus genuine rank-of-span.
    vectors=[]; types={}; indices=[]
    for A in orbit:
        v=next(tuple(A[n*i+j] for i in range(n)) for j in range(n)
               if any(A[n*i+j] for i in range(n)))
        if v not in types:
            types[v]=len(vectors);vectors.append(v)
        indices.append(types[v])
    @lru_cache(None)
    def span_rank(keys):
        return rank_rows([vectors[j] for j in keys],F)
    def dfs(seq,mask):
        if len(seq)==r:
            d=span_rank(tuple(sorted(indices[i] for i in seq)))
            measured[d]+=1
            return
        x=mask
        while x:
            bit=x&-x; i=bit.bit_length()-1; x-=bit
            dfs(seq+[i],mask & near[i])
    dfs([], (1<<len(orbit))-1)
    assert measured==predicted,(n,r,q,predicted,measured)
    print('PASS n=%d r=%d q=%d orbit=%d distribution=%s total=%d' % (
        n,r,q,len(orbit),measured,sum(measured.values())))

if __name__ == '__main__':
    for n,r,q in [(2,3,2),(2,4,3),(3,3,2),(3,3,3),(3,2,4),
                  (4,3,2)]:check(n,r,q)
    print('ALL_MINIMAL_ORBIT_TUPLE_CHECKS_PASS')
