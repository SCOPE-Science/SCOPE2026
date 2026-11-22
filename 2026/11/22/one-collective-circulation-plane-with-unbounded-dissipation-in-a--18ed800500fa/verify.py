#!/usr/bin/env python3
"""Independent exact-rational verification of all-bath harmonic-network identities.
Uses only the Python standard library. This is a finite consistency check,
not the proof for arbitrary network size or positive real parameters.
"""
from fractions import Fraction as F
from itertools import product


def dot(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def transpose(A):
    return [list(c) for c in zip(*A)]

def solve(A, b):
    n=len(A)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if M[i][j])
        M[j],M[pivot]=M[pivot],M[j]
        factor=M[j][j]
        M[j]=[x/factor for x in M[j]]
        for i in range(n):
            if i!=j:
                scale=M[i][j]
                M[i]=[x-scale*y for x,y in zip(M[i],M[j])]
    return [row[-1] for row in M]

def inverse(A):
    n=len(A)
    return transpose([solve(A,[F(i==j) for i in range(n)]) for j in range(n)])

def check(n,a,b,temps):
    one=F(1)
    mu=sum(temps)/n
    K=[[a*F(i==j)+b*(F(i==j)-one/n) for j in range(n)] for i in range(n)]
    D=[[temps[i]*F(i==j) for j in range(n)] for i in range(n)]
    # Solve Lyapunov equation using an unrelated Kronecker linear system.
    B=[]
    for i,j in product(range(n),repeat=2):
        B.append([K[i][k]*F(j==l)+F(i==k)*K[l][j] for k,l in product(range(n),repeat=2)])
    c=solve(B,[2*D[i][j] for i,j in product(range(n),repeat=2)])
    C=[c[i*n:(i+1)*n] for i in range(n)]
    KC=dot(K,C)
    CK=dot(C,K)
    assert all(KC[i][j]+CK[i][j]==2*D[i][j] for i,j in product(range(n),repeat=2))
    A=[[D[i][j]-KC[i][j] for j in range(n)] for i in range(n)]
    coeff=b/(n*(2*a+b))
    assert all(A[i][j]==coeff*(temps[j]-temps[i]) for i,j in product(range(n),repeat=2))
    assert all(A[i][j]==-A[j][i] for i,j in product(range(n),repeat=2))
    factor=b/(2*a+b)
    omega2=factor*factor*sum((t-mu)**2 for t in temps)/n
    A3=dot(dot(A,A),A)
    assert all(A3[i][j]==-omega2*A[i][j] for i,j in product(range(n),repeat=2))
    KCK=dot(dot(K,C),K)
    h=[KCK[i][i]-temps[i]*K[i][i] for i in range(n)]
    assert all(h[i]==b*b/(n*(2*a+b))*(mu-temps[i]) for i in range(n))
    assert sum(h)==0
    sig=sum(h[i]/temps[i] for i in range(n))
    expected=b*b/(n*(2*a+b))*(mu*sum(1/t for t in temps)-n)
    assert sig==expected
    Ci=inverse(C)
    DCi=dot([[F(i==j)/temps[i] for j in range(n)] for i in range(n)],A)
    # sigma = Tr(C^{-1} A^T D^{-1} A)
    ent_matrix=dot(dot(Ci,transpose(A)),DCi)
    assert sig==sum(ent_matrix[i][i] for i in range(n))
    assert (sig>0)==(len(set(temps))>1)
    return 1

def main():
    total=0
    for n in range(2,6):
        for a,b in [(F(1,3),F(2,5)),(F(7,4),F(13,6)),(F(3),F(1,9))]:
            for temps in ([F(2*i+1, i+2) for i in range(n)], [F(5,7)]*n, [F(2),F(3)]+[F(1,2)]*(n-2)):
                total+=check(n,a,b,temps)
    print('ALL_BATH_EXACT_RATIONAL_CHECKS_PASSED',total)

if __name__=='__main__':
    main()
