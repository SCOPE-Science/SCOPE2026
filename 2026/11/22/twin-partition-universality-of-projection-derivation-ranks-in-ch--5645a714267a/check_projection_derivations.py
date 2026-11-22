#!/usr/bin/env python3
"""Reproducible finite-field checks for composition-idempotent derivations of complete multipartite evolution algebras.

All graph algebras and fields here are mathematical inputs, not external data.
This code checks direct defining equations independently of the symplectic counting expression.
"""
from itertools import product
from collections import Counter
from math import prod

class GF2Power:
    def __init__(self, degree):
        self.degree = degree
        self.q = 1 << degree
        self.poly = {1: 0b11, 2: 0b111, 3: 0b1011}[degree]
    def add(self, a, b): return a ^ b
    def mul(self, a, b):
        v = 0
        for _ in range(self.degree):
            if b & 1: v ^= a
            b >>= 1
            a <<= 1
            if a & self.q: a ^= self.poly
        return v

def rank(a, F):
    a = [list(r) for r in a]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot = 0
    for j in range(cols):
        i = next((z for z in range(pivot, rows) if a[z][j]), None)
        if i is None: continue
        a[i], a[pivot] = a[pivot], a[i]
        for z in range(rows):
            if z != pivot and a[z][j]:
                ratio = a[z][j]
                if a[pivot][j] != 1:
                    # The possible fields here have small multiplicative groups.
                    inv = next(t for t in range(1, F.q) if F.mul(t, a[pivot][j]) == 1)
                    ratio = F.mul(ratio, inv)
                for c in range(j, cols): a[z][c] ^= F.mul(ratio, a[pivot][c])
        pivot += 1
        if pivot == rows: break
    return pivot

def matmul(a,b,F):
    n = len(a)
    return [[__import__('functools').reduce(lambda x, y: x ^ y, (F.mul(a[i][k], b[k][j]) for k in range(n)), 0) for j in range(n)] for i in range(n)]

def block_matrices(dim, F):
    # Unique symmetric zero-row-sum matrix for each freely chosen off-diagonal triangle.
    edges = [(i,j) for i in range(dim) for j in range(i+1,dim)]
    for vals in product(range(F.q),repeat=len(edges)):
        a = [[0]*dim for _ in range(dim)]
        for (i,j),v in zip(edges,vals): a[i][j] = a[j][i] = v
        for i in range(dim):
            x = 0
            for j in range(dim):
                if i!=j: x ^= a[i][j]
            a[i][i] = x
        yield a

def gf_gaussian(h,r,Q):
    n = 1
    for j in range(r):
        n *= (Q**(h-j)-1)
    for j in range(r):
        denom = Q**(r-j)-1
        assert n % denom == 0 if j==r-1 else True
    den = prod(Q**j-1 for j in range(1,r+1))
    return n//den

def formula(dim,q):
    h=(dim-1)//2
    even=int(dim%2==0)
    return {2*r:q**(2*r*(h-r)+2*r*even)*gf_gaussian(h,r,q*q) for r in range(h+1)}

def count_projections(dim,F,check_direct=True):
    ct=Counter()
    for a in block_matrices(dim,F):
        if check_direct:
            # derivation: for off-diagonal natural basis products, symmetry in each class,
            # and D of every squared element is zero (equivalent to zero row sums).
            assert all(a[i][j] == a[j][i] for i in range(dim) for j in range(dim))
            assert all(__import__('functools').reduce(lambda x,y:x^y,a[i],0)==0 for i in range(dim))
        if matmul(a,a,F)==a:
            ct[rank(a,F)] +=1
    return dict(sorted(ct.items()))

def multipartite_direct(parts, matrices, F):
    # Verify the exact original derivation equation on a natural basis, and D^2=D.
    n=sum(parts); mat=[[0]*n for _ in range(n)]
    index=[]; offset=0
    for j,(dim,a) in enumerate(zip(parts,matrices)):
        for i in range(dim):
            for t in range(dim): mat[offset+i][offset+t]=a[i][t]
            index.append(j)
        offset+=dim
    def mul(x,y):
        z=[0]*n
        for i in range(n):
            if x[i] and y[i]:
                for j in range(n):
                    if index[i]!=index[j]: z[j]^=F.mul(x[i],y[i])
        return z
    def apply(x):
        return [__import__('functools').reduce(lambda z,v:z^v,(F.mul(mat[i][j],x[j]) for j in range(n)),0) for i in range(n)]
    b=[[int(i==j) for i in range(n)] for j in range(n)]
    for x in b:
        for y in b:
            assert apply(mul(x,y))==[z^t for z,t in zip(mul(apply(x),y),mul(x,apply(y)))]
    assert all(apply(apply(x))==apply(x) for x in b)

if __name__=='__main__':
    for degree, sizes in [(1,[1,2,3,4,5,6]), (2,[2,3,4]),(3,[3,4])]:
        F=GF2Power(degree)
        for dim in sizes:
            got=count_projections(dim,F)
            expect=formula(dim,F.q)
            assert got == expect, (degree,dim,got,expect)
            print('BLOCK',F.q,dim,got)
    for parts in [(1,2,3),(2,3),(3,4),(3,3,4)]:
        F=GF2Power(1)
        mats=[next(a for a in block_matrices(d,F) if matmul(a,a,F)==a and (rank(a,F)>0 or d==1)) if d>2 else [[0]*d for _ in range(d)] for d in parts]
        multipartite_direct(parts,mats,F)
        print('MULTIPARTITE',parts,'rank',sum(rank(a,F) for a in mats),'verified')
    print('COMPLETE_MULTIPARTITE_PROJECTION_DERIVATIONS_VERIFIED')

def graph_derivation_basis(n, edges):
    # Independent linear-equation calculation over F_2, not using twin classes.
    nbr=[set() for _ in range(n)]
    for i,j in edges:
        assert 0<=i<j<n
        nbr[i].add(j); nbr[j].add(i)
    eq=[]
    for i in range(n):
        for k in range(n):
            mask=0
            for j in nbr[i]: mask ^= 1<<(k*n+j)
            if mask: eq.append(mask)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                mask=0
                if k in nbr[j]: mask ^= 1<<(j*n+i)
                if k in nbr[i]: mask ^= 1<<(i*n+j)
                if mask: eq.append(mask)
    pivots={}
    for v in eq:
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v; break
            v ^= pivots[p]
    free=[i for i in range(n*n) if i not in pivots]
    basis=[]
    for t in free:
        v=1<<t
        # Descending pivot substitutions. Row pivot may have only lower variables.
        for p in sorted(pivots):
            if (pivots[p] & v).bit_count()%2: v ^= 1<<p
        basis.append(v)
    assert all(all((a & b).bit_count()%2==0 for a in eq) for b in basis)
    return basis,nbr

def direct_graph_test(n,edges,part_sizes):
    basis,nbr=graph_derivation_basis(n,edges)
    assert len(basis)==sum(s*(s-1)//2 for s in part_sizes), (n,len(basis),part_sizes)
    F=GF2Power(1)
    c=Counter()
    for bits in range(1<<len(basis)):
        m=0
        for j,b in enumerate(basis):
            if (bits>>j)&1: m ^= b
        mat=[[(m>>(i*n+j))&1 for j in range(n)] for i in range(n)]
        if matmul(mat,mat,F)==mat:
            c[rank(mat,F)]+=1
    expected=Counter({0:1})
    for s in part_sizes:
        new=Counter()
        for rank1,count1 in expected.items():
            for rank2,count2 in formula(s,2).items():
                new[rank1+rank2]+=count1*count2
        expected=new
    assert c==expected, (c,expected)
    print('GRAPH',n,len(edges),'derivation_dimension',len(basis),'rank_polynomial',dict(sorted(c.items())))

if __name__=='__main__':
    # A non-bipartite graph: triangle 0-1-2 and three pendant twins 3,4,5 at 0.
    triangle_leaves=[(0,1),(0,2),(1,2)]+[(0,j) for j in range(3,6)]
    direct_graph_test(6,triangle_leaves,[1,1,1,3])
    # Two twin classes in a non-bipartite graph, not a complete multipartite graph.
    two_classes=[(0,1),(0,2),(1,2)]+[(0,j) for j in range(3,6)]+[(1,j) for j in range(6,10)]
    direct_graph_test(10,two_classes,[1,1,1,3,4])
    # Completely different neighborhood structure with identical twin sizes.
    # K_{3,4}, by contrast, has two classes of sizes 3 and 4.
    complete_bip=[(i,j) for i in range(3) for j in range(3,7)]
    direct_graph_test(7,complete_bip,[3,4])
    print('UNIVERSAL_TWIN_CLASS_RANK_CENSUS_VERIFIED')
