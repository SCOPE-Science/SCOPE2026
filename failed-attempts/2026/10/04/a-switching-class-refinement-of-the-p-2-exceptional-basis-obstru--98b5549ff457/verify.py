from math import comb
from collections import Counter

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def gram_standard(p):
    B=[[0]*p for _ in range(p)]
    for i in range(p):
        for j in range(i,p):
            B[i][j]=comb(p-1+j-i,p-1)
    return B

def modmat(A,p):
    return [[x%p for x in row] for row in A]

def norm_skew(B,p):
    n=len(B)
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d=B[i][j]-B[j][i]
            assert d%p==0
            A[i][j]=(d//p)%p
    return A

def inv(a,p):
    return pow(a%p,-1,p)

def perm_matrix(n,i):
    P=[[0]*n for _ in range(n)]
    for r in range(n):
        P[r][r]=1
    P[i][i]=P[i+1][i+1]=0
    P[i][i+1]=P[i+1][i]=1
    return P

def right_mutation_T(B,i):
    n=len(B)
    m=B[i][i+1]
    # Columns express the new ordered basis in the old basis:
    # ..., e_{i+1}, e_i - m e_{i+1}, ...
    T=[[0]*n for _ in range(n)]
    for c in range(n):
        if c<i or c>i+1:
            T[c][c]=1
    T[i+1][i]=1
    T[i][i+1]=1
    T[i+1][i+1]=-m
    return T

def congruence(B,T):
    return matmul(transpose(T),matmul(B,T))

def diag_sign(n,i):
    D=[[0]*n for _ in range(n)]
    for r in range(n):
        D[r][r]=-1 if r==i else 1
    return D

for p,expected in [
    (5,Counter({1:5,4:5})),
    (7,Counter({1:14,2:21}))
]:
    B=gram_standard(p)
    assert all(B[i][j]%p==(1 if i==j else 0)
               for i in range(p) for j in range(p))
    A=norm_skew(B,p)
    for i in range(p):
        assert A[i][i]==0
        for j in range(i+1,p):
            assert A[i][j]==inv(j-i,p)
            assert A[j][i]==(-inv(j-i,p))%p

    hist=Counter()
    for i in range(p):
        for j in range(i+1,p):
            for k in range(j+1,p):
                q=(A[i][j]*A[j][k]*A[k][i])%p
                q=(q*q)%p
                formula=pow(((j-i)*(k-j)*(k-i))%p,-2,p)
                assert q==formula
                hist[q]+=1
    assert hist==expected

    # Exact mutation replay; after each step compare to adjacent permutation.
    Bcur=[row[:] for row in B]
    Acur=norm_skew(Bcur,p)
    for i in list(range(p-1))+list(reversed(range(p-1))):
        T=right_mutation_T(Bcur,i)
        P=perm_matrix(p,i)
        Bnew=congruence(Bcur,T)
        Anew=norm_skew(Bnew,p)
        pred=modmat(congruence(Acur,P),p)
        assert Anew==pred
        Bcur,Acur=Bnew,Anew

    # Sign switching.
    D=diag_sign(p,1)
    Bsign=congruence(B,D)
    Asign=norm_skew(Bsign,p)
    pred=modmat(congruence(A,D),p)
    assert Asign==pred

    print(f"p={p}")
    print("triangle_square_hist="+",".join(f"{a}:{expected[a]}" for a in sorted(expected)))

print("VERIFY_OK")
