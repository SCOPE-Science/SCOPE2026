"""Exact finite-arithmetic checks for a two-tap Hardy weighted-composition theorem.
Scientific proof and infinite limits appear in RESULT.md; finite checks are not certificates of limits.
Run: python verify.py (Python 3.10+, no third-party packages).
"""
from fractions import Fraction as F
from itertools import combinations

COUNT = 0

def check(x):
    global COUNT
    assert x
    COUNT += 1

def det(mat):
    mat = [[F(v) for v in row] for row in mat]
    n = len(mat)
    d = F(1)
    for j in range(n):
        k = next((k for k in range(j,n) if mat[k][j]),None)
        if k is None:return F(0)
        if k != j:
            mat[j],mat[k]=mat[k],mat[j]
            d=-d
        p=mat[j][j]
        d *= p
        for i in range(j+1,n):
            if mat[i][j]:
                v=mat[i][j]/p
                for t in range(j+1,n):mat[i][t]-=v*mat[j][t]
                mat[i][j]=0
    return d

def gram(q,a,n):
    return [[q**(i+j)*((1+a*a) if i==j else (a if abs(i-j)==1 else F(0))) for j in range(n)] for i in range(n)]

def run():
    for q in (F(1,2), F(2,3)):
        for a in (F(1,3),F(1),F(3,2)):
            B=gram(q,a,8)
            for n in range(1,7):
                d=sum(a**(2*k) for k in range(n+1))
                check(det([row[:n] for row in B[:n]]) == q**(n*(n-1))*d)
            for n in (2,3,4):
                for ids in combinations(range(6),n):
                    m=sum(ids[j]-j for j in range(n))
                    runs=[]
                    ell=1
                    for j in range(1,n):
                        if ids[j]==ids[j-1]+1:ell+=1
                        else:runs.append(ell);ell=1
                    runs.append(ell)
                    d=F(1)
                    for ell in runs:d*=sum(a**(2*k) for k in range(ell+1))
                    mat=[[B[i][j] for j in ids] for i in ids]
                    check(det(mat)==q**(n*(n-1)+2*m)*d)
                    check(len(runs)*(len(runs)-1)//2 <= m)
            # The Toeplitz diagonal and shift self similarity are exact.
            for i in range(6):
                for j in range(6):
                    check(B[i+1][j+1] == q*q*B[i][j])
    # Exact phase-duality of Gram matrices: A(a)^*A(a)=a^2 U*A(1/a)^*A(1/a)U
    # is NOT an entrywise identity; phase duality is proved using an inner isometry.
    print(f'FINITE_RATIONAL_CHECKS_OK {COUNT} assertions; infinite spectral conclusions require the written proof')

if __name__=='__main__':run()
