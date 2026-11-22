#!/usr/bin/env python3
"""Exact integer certificate for a natural del Pezzo line/conic-bundle incidence graph.

Requires Python 3 standard library only. All arithmetic uses unbounded integers.
"""
from itertools import combinations, product
from collections import Counter

N = 5
E = [(0,) + tuple(-int(i == j) for i in range(N)) for j in range(N)]
LINES = E + [(1,) + tuple(int(i in ab) for i in range(N))
             for ab in combinations(range(N), 2)] + [(2, 1, 1, 1, 1, 1)]
PENCILS = ([(1,) + tuple(int(i == j) for i in range(N)) for j in range(N)]
          + [(2,) + tuple(int(i != j) for i in range(N)) for j in range(N)])

def sumclass(u, v):
    return tuple(a + b for a, b in zip(u, v))

def intersection(u, v):
    return u[0]*v[0] - sum(a*b for a,b in zip(u[1:], v[1:]))

# The independent geometric construction uses the decomposition of a conic
# class into pairs of (-1)-curve classes.
B = [[0]*10 for _ in range(16)]
FIBERS = []
for j, f in enumerate(PENCILS):
    pairs = [(i,k) for i in range(16) for k in range(i+1, 16)
             if sumclass(LINES[i], LINES[k]) == f]
    assert len(pairs) == 4
    for i,k in pairs:
        assert intersection(LINES[i], LINES[k]) == 1
        assert B[i][j] == 0 and B[k][j] == 0
        B[i][j] = B[k][j] = 1
        FIBERS.append((j,i,k))
assert len(FIBERS) == 40
assert all(sum(row) == 5 for row in B)
assert all(sum(B[i][j] for i in range(16)) == 8 for j in range(10))
# A distinct combinatorial realization, which can also rebuild the matrix.
EVEN = [tuple(b) for b in product((0,1), repeat=5) if sum(b)%2==0]
assert len(EVEN) == 16
patterns = [tuple(row[:5]) for row in B]
assert set(patterns) == set(EVEN)
assert all(B[i][5+j] == 1-B[i][j] for i in range(16) for j in range(5))
assert [tuple(row) for row in B] == [tuple(bits) + tuple(1-b for b in bits) for bits in patterns]

M = [[0]*26 for _ in range(26)]
for i in range(16):
    M[i][i] = 5
    for j in range(10):
        if B[i][j]:
            M[i][16+j] = M[16+j][i] = -1
for j in range(10):
    M[16+j][16+j] = 8
assert all(sum(row)==0 for row in M)
assert all(M[i][j]==M[j][i] for i in range(26) for j in range(26))

# Verified 10x10 Gram matrix structure, independently sufficient to derive
# the rational Laplacian characteristic polynomial.
GRAM = [[sum(B[i][j]*B[i][k] for i in range(16)) for k in range(10)]
        for j in range(10)]
for i in range(10):
    for j in range(10):
        assert GRAM[i][j] == (8 if i == j else 0 if i%5 == j%5 else 4)

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row, col)) for col in zip(*B)] for row in A]

def smith_certificate(input_rows):
    """Euclidean Smith reduction, tracking unimodular U,V with UAV=D.

    Swap, sign and integer-addition operations give integral unimodular
    matrices; a nondivisible trailing entry is moved into the pivot row.
    """
    A=[list(row) for row in input_rows]
    n=len(A);m=len(A[0])
    U=[[int(i==j) for j in range(n)] for i in range(n)]
    V=[[int(i==j) for j in range(m)] for i in range(m)]
    def rs(i,j):
        A[i], A[j] = A[j], A[i]
        U[i], U[j] = U[j], U[i]
    def cs(i,j):
        for R in (A,V):
            for row in R:row[i],row[j]=row[j],row[i]
    def ra(i,j,q):
        for R in (A,U):
            R[i]=[a+q*b for a,b in zip(R[i],R[j])]
    def ca(i,j,q):
        for R in (A,V):
            for row in R:row[i]+=q*row[j]
    def neg(i):
        for R in (A,U):R[i]=[-x for x in R[i]]
    for k in range(min(n,m)):
        nz=[(abs(A[i][j]),i,j) for i in range(k,n)
            for j in range(k,m) if A[i][j]]
        if not nz:break
        _,i,j=min(nz);rs(k,i);cs(k,j)
        for _ in range(100000):
            pivot=A[k][k]
            assert pivot
            for i in range(k+1,n):
                if A[i][k]:
                    q=A[i][k]//pivot
                    ra(i,k,-q)
                    if A[i][k]:rs(k,i)
                    break
            else:
                for j in range(k+1,m):
                    if A[k][j]:
                        q=A[k][j]//pivot
                        ca(j,k,-q)
                        if A[k][j]:cs(k,j)
                        break
                else:
                    bad=next(((i,j) for i in range(k+1,n)
                              for j in range(k+1,m) if A[i][j]%pivot),None)
                    if bad is None:break
                    ra(k,bad[0],1)
                continue
            continue
        else:raise AssertionError('Euclidean loop not completed')
        if A[k][k]<0:neg(k)
    assert matmul(matmul(U,input_rows),V)==A
    assert all(A[i][j]==0 for i in range(n) for j in range(m) if i!=j)
    vals=[A[i][i] for i in range(min(n,m))]
    assert all(vals[i]>=0 for i in range(len(vals)))
    assert all(vals[i+1]%vals[i]==0 for i in range(len(vals)-1) if vals[i])
    return vals

def det_bareiss(A):
    A=[list(map(int,row)) for row in A]
    n=len(A); sign=1;prev=1
    for k in range(n-1):
        if A[k][k]==0:
            i=next((i for i in range(k+1,n) if A[i][k]),None)
            if i is None:return 0
            A[k],A[i]=A[i],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=A[i][j]*pivot-A[i][k]*A[k][j]
                assert t%prev == 0
                A[i][j]=t//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]

EXPECTED = [1]*15+[5]+[20]*4+[80]+[320]*4
for omit in (0,16,25):
    reduced=[[M[i][j] for j in range(26) if j!=omit]
             for i in range(26) if i!=omit]
    assert smith_certificate(reduced)==EXPECTED
    assert det_bareiss(reduced)==2**36*5**10
assert len(EXPECTED)==25
print('DEL_PEZZO_CONIC_INCIDENCE_CRITICAL_GROUP_VERIFIED_OK')
print('Smith factors:', ','.join(str(x) for x in EXPECTED))
print('Spanning trees:', 2**36*5**10)
