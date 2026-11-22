#!/usr/bin/env python3
"""Independent finite checks for a signed ternary binomial-residue theorem.

Uses only Python's standard library. Finite checks are not proofs of asymptotics.
"""
import math

A = ((1,1,1),(1,1,0),(1,0,0))
B = ((1,1,1),(1,-1,0),(1,0,0))
I = ((1,0,0),(0,1,0),(0,0,1))

def matmul(M,N):
    return tuple(tuple(sum(M[i][k]*N[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def scale(M,k):
    return tuple(tuple(k*x for x in row) for row in M)

def plus(M,N):
    return tuple(tuple(a+b for a,b in zip(rowA,rowB)) for rowA,rowB in zip(M,N))

def matrix_powers(M, levels):
    R=I
    out=[]
    for _ in range(levels):
        out.append(sum(R[0]))
        R=matmul(R,M)
    return out

def digit_weight(n):
    prev=0
    sign=1
    while n:
        digit=n%3
        if digit+prev>2:
            return 0
        if digit==prev==1:
            sign=-sign
        prev=digit
        n//=3
    return sign

def direct_ones_twos(L):
    N=[0,0,0]
    for n in range(3**L):
        actual=math.comb(4*n,n)%3
        N[actual]+=1
        pred=digit_weight(n)
        assert pred == (0 if actual==0 else 1 if actual==1 else -1), (n, actual, pred)
    return N

def main():
    # Polynomial matrix equalities are exact 3x3 integer identities.
    assert matmul(matmul(B,B),B)==plus(scale(B,3),I)
    assert matmul(matmul(A,A),A)==plus(plus(scale(matmul(A,A),2),A),scale(I,-1))
    U=matrix_powers(A,14)
    D=matrix_powers(B,14)
    assert (U[:7],D[:7])==([1,3,6,14,31,70,157],[1,3,4,10,15,34,55])
    for L in range(3,len(D)):
        assert D[L]==3*D[L-2]+D[L-3]
        assert U[L]==2*U[L-1]+U[L-2]-U[L-3]
    for L in range(8):
        N=direct_ones_twos(L)
        assert N[1]+N[2]==U[L], (L,N,U[L])
        assert N[1]-N[2]==D[L], (L,N,D[L])
    # Independently compare raw residue against the digit rule on a non-power range.
    for n in range(2187,2600):
        r=math.comb(4*n,n)%3
        assert digit_weight(n)==(0 if r==0 else 1 if r==1 else -1)
    print('VERIFY_OK levels=8 direct_indices=2600 matrix_charpolys=2 rational_recurrences=28')
    for L in range(7):
        n0=(3**L-U[L]);n1=(U[L]+D[L])//2;n2=(U[L]-D[L])//2
        print('L',L,'N0',n0,'N1',n1,'N2',n2)
if __name__=='__main__':
    main()
