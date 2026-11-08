"""Finite exact checks for loss on prime-order Paley quantum networks.

The infinite-prime theorem relies on Chebotarev full-spark Fourier minors;
this script checks finite adjacency, Krylov ranks and the order-nine boundary.
Standard library only.  Run: python verify.py
"""
from itertools import combinations
from math import comb

MOD = 1000000007


def adjacency_paley(p):
    assert p % 4 == 1 and p > 2
    residues = {a*a % p for a in range(1,p)}
    return [[int(i!=j and (j-i)%p in residues) for j in range(p)] for i in range(p)]


def adjacency_rook(n):
    return [[int(i != j and (i//n == j//n or i%n == j%n))
             for j in range(n*n)] for i in range(n*n)]


def matvec(A, v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]


def add_basis(basis, vec):
    v=[x % MOD for x in vec]
    for col,pivot in basis:
        if v[pivot]:
            q=v[pivot]
            for j in range(pivot,len(v)):
                v[j]=(v[j]-q*col[j])%MOD
    for pivot,x in enumerate(v):
        if x:
            inv=pow(x,-1,MOD)
            v=[a*inv%MOD for a in v]
            basis.append((v,pivot))
            basis.sort(key=lambda z:z[1])
            return True
    return False


def basis_from_columns(columns):
    b=[]
    for col in columns: add_basis(b,col)
    return b


def krylov_columns(A, traps):
    n=len(A)
    out=[]
    for s in traps:
        v=[int(i==s) for i in range(n)]
        for _ in range(3):
            out.append(v)
            v=matvec(A,v)
    return out


def verify_prime(p, exhaustive):
    A=adjacency_paley(p)
    n=len(A); m=(p-1)//2
    assert all(sum(row)==m for row in A)
    assert all(A[i][j]==A[j][i] for i in range(p) for j in range(p))
    # Exact strongly regular identity A^2 = (k-mu)I + (lam-mu)A + mu J.
    lam=(p-5)//4; mu=(p-1)//4
    A2=[[sum(A[i][z]*A[z][j] for z in range(p)) for j in range(p)] for i in range(p)]
    for i in range(p):
        for j in range(p):
            assert A2[i][j] == (m-mu)*int(i==j)+(lam-mu)*A[i][j]+mu
    # rank of rational Krylov span equals number of bright modes.
    from random import Random
    rng=Random(24601+p)
    count=0
    for t in range(1,m+1):
        opts=list(combinations(range(p),t)) if exhaustive else [tuple(sorted(rng.sample(range(p),t))) for _ in range(25)]
        for S in opts:
            actual=len(basis_from_columns(krylov_columns(A,S)))
            expected=1+2*t
            assert actual == expected, (p,S,actual,expected)
            assert p-actual==2*(m-t)
            assert (expected)/(p)==(1+2*t)/p
            count+=1
    print(f'P({p}): n={n}, degree={m}, checked={count} sink sets, predicted bright dimensions 3..{p}')


def integer_determinant(mat):
    """Bareiss integer fraction-free determinant."""
    M=[row[:] for row in mat]
    n=len(M); sign=1; prev=1
    if any(len(row)!=n for row in M): raise ValueError('square matrix required')
    if n==0: return 1
    for k in range(n-1):
        if M[k][k]==0:
            j=next((j for j in range(k+1,n) if M[j][k]), None)
            if j is None: return 0
            M[k],M[j]=M[j],M[k]; sign=-sign
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top=M[i][j]*pivot-M[i][k]*M[k][j]
                assert top%prev==0
                M[i][j]=top//prev
        for i in range(k+1,n): M[i][k]=0
        prev=pivot
    return sign*M[-1][-1]


def verify_order_nine_boundary():
    A=adjacency_rook(3)
    S=(0,1,3,4) # 2x2 corner, candidate four traps
    dark=[0,0,3,0,0,3,-3,-3,0]
    assert all(dark[v]==0 for v in S)
    assert matvec(A,dark)==dark
    rank=len(basis_from_columns(krylov_columns(A,S)))
    assert rank < 9
    # A different four-sink layout has full rank; exact 9x9 minor = 6.
    Sgood=(0,1,3,5)
    cols=krylov_columns(A,Sgood)
    picks=(0,1,2,3,4,6,7,9,10)
    small=[[cols[j][i] for j in picks] for i in range(9)]
    determinant=integer_determinant(small)
    assert determinant==6, determinant
    assert len(basis_from_columns(cols))==9
    print('Rook/Paley(9): 2x2 sink block leaves dark eigenmode, rank',rank)
    print('Rook/Paley(9): alternative sink set',Sgood,'gives full rank, integer 9x9 determinant',determinant)


def main():
    verify_prime(5,True)
    verify_prime(13,True)
    verify_prime(17,False)
    verify_order_nine_boundary()
    print('ALL FINITE CHECKS PASSED. Infinite-prime claim uses cited full-spark theorem.')

if __name__=='__main__': main()
