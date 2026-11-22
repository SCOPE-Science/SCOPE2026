#!/usr/bin/env python3
"""Exact reconstruction and prime-local Smith verification of the theta--Steiner graph.
Only the Python standard library is needed; no numerical eigensolvers.
"""
from collections import Counter
from math import prod


def q(v):
    return sum(((v >> i) & 1) & ((v >> (i+3)) & 1) for i in range(3)) % 2


def omega(v, w):
    return q(v) ^ q(w) ^ q(v ^ w)


def build_incidence():
    odd = [v for v in range(64) if q(v)]
    nonzero = list(range(1, 64))
    assert len(odd) == 28
    B = [[int((q(a) ^ omega(v, a)) == 0) for a in nonzero] for v in odd]
    assert all(sum(row) == 27 for row in B)
    assert all(sum(B[i][j] for i in range(28)) == 12 for j in range(63))
    for i in range(28):
        for j in range(28):
            common = sum(B[i][k] * B[j][k] for k in range(63))
            assert common == (27 if i == j else 11)
    return B


def laplacian(B):
    L = [[0]*91 for _ in range(91)]
    for i in range(28):
        L[i][i] = 27
        for j in range(63):
            if B[i][j]:
                L[i][28+j] = L[28+j][i] = -1
    for j in range(63):
        L[28+j][28+j] = 12
    assert all(sum(r)==0 for r in L)
    return L


def local_valuations(R, prime, exponent):
    """Smith diagonal valuations over Z/(prime**exponent).

    At every step the pivot has smallest valuation in the remaining block.
    Its quotient by prime**v is invertible modulo prime**(exponent-v).
    Unimodular row and column operations clear its row and column.
    All pivots must be strictly below the exponent, certifying the full
    prime-primary Smith list over Z by elementary divisor stability.
    """
    n = len(R)
    modulus = prime ** exponent
    A = [[x % modulus for x in row] for row in R]

    def valuation(x):
        if x == 0:
            return exponent
        v = 0
        while x % prime == 0:
            x //= prime
            v += 1
        return v

    vals=[]
    for k in range(n):
        v = exponent
        ip = jp = None
        for i in range(k,n):
            for j in range(k,n):
                x = A[i][j]
                if x:
                    vv = valuation(x)
                    if vv < v:
                        v = vv
                        ip, jp = i, j
                        if v == 0: break
            if v == 0: break
        if ip is None:
            raise AssertionError('Insufficient prime precision at %d' % k)
        A[k], A[ip] = A[ip], A[k]
        for i in range(n):
            A[i][k], A[i][jp] = A[i][jp], A[i][k]
        ppower = prime**v
        inv = pow(A[k][k]//ppower, -1, modulus//ppower)
        # Row clearing, a product of invertible elementary operations.
        for i in range(k+1, n):
            x=A[i][k]
            assert x % ppower == 0
            c=(x//ppower * inv) % (modulus//ppower)
            if c:
                for j in range(k,n):
                    A[i][j]=(A[i][j]-c*A[k][j])%modulus
        # Column clearing, also elementary and invertible.
        for j in range(k+1, n):
            x=A[k][j]
            assert x % ppower == 0
            c=(x//ppower * inv) % (modulus//ppower)
            if c:
                for i in range(k,n):
                    A[i][j]=(A[i][j]-c*A[i][k])%modulus
        assert all(A[i][k] == 0 for i in range(k+1, n))
        assert all(A[k][j] == 0 for j in range(k+1, n))
        vals.append(v)
    return Counter(vals)


def rank_mod_p(R,p):
    A=[[x%p for x in row] for row in R]
    n=len(A)
    row=0
    for col in range(n):
        pivot=next((i for i in range(row,n) if A[i][col]%p),None)
        if pivot is None:continue
        A[pivot],A[row]=A[row],A[pivot]
        inv=pow(A[row][col],-1,p)
        for j in range(col,n):A[row][j]=A[row][j]*inv%p
        for i in range(row+1,n):
            if A[i][col]:
                c=A[i][col]
                for j in range(col,n):A[i][j]=(A[i][j]-c*A[row][j])%p
        row+=1
        if row==n:break
    return row


def main():
    B=build_incidence()
    L=laplacian(B)
    # Matrix-tree theorem from Gram spectrum:
    # B B^t = 16 I + 11 J, yielding Laplacian eigenvalues
    # 0^1, 39^1, 28^27, 11^27, 12^35.
    # (39*28**27*11**27*12**35)/91 = 2**124*3**36*7**26*11**27.
    order=2**124 * 3**36 * 7**26 * 11**27
    assert (39 * 28**27 * 11**27 * 12**35)//91 == order
    expected={2: {0:28,1:6,2:50,3:6},3:{0:54,1:36},
              7:{0:64,1:26},11:{0:63,1:27}}
    # Two different types of deleted vertex: an odd-theta vertex and a Steiner vertex.
    for deleted in (0,90):
        R=[[L[i][j] for j in range(91) if j!=deleted]
           for i in range(91) if i!=deleted]
        for p in (2,3,7,11):
            result=local_valuations(R,p,6 if p==2 else 4)
            assert dict(result)==expected[p], (deleted,p,result)
            assert rank_mod_p(R,p)==expected[p][0]
            assert sum(v*c for v,c in result.items())=={2:124,3:36,7:26,11:27}[p]
    # Invariant factors of the full group assembled across the prime valuations.
    inv=[1]*90
    for p in (2,3,7,11):
        e=[]
        for v,c in sorted(expected[p].items()):e += [v]*c
        assert len(e)==90
        for i in range(90):inv[i]*=p**e[i]
    assert Counter(inv)==Counter({1:28,2:6,4:20,12:9,132:1,924:20,1848:6})
    assert prod(inv)==order
    assert all(inv[i+1]%inv[i]==0 for i in range(89))
    assert 756-91+1==666
    print('STEINER_GRAPH_CRITICAL_GROUP_VERIFIED_OK')
    print('invariant factors:', sorted(Counter(inv).items()))
    print('order = 2^124 * 3^36 * 7^26 * 11^27; exponent = 1848; genus = 666')

if __name__=='__main__':main()
