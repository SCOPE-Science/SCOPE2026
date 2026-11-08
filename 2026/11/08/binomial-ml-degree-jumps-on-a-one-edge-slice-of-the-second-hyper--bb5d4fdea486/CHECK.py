"""Independent exact Euler-characteristic / principal-rank check for a single-edge-scaled second hypersimplex."""
from itertools import combinations
from fractions import Fraction
import math

def det(M):
    n=len(M)
    if n==0:return 1
    A=[[Fraction(v) for v in row] for row in M]
    sign=1; piv=Fraction(1)
    for j in range(n):
        ind=next((i for i in range(j,n) if A[i][j]),None)
        if ind is None:return 0
        if ind != j:
            A[j],A[ind]=A[ind],A[j];sign=-sign
        p=A[j][j];piv*=p
        for i in range(j+1,n):
            f=A[i][j]/p
            for h in range(j+1,n):A[i][h]-=f*A[j][h]
            A[i][j]=0
    return sign*piv

def rank(A):
    if not A:return 0
    M=[[Fraction(x) for x in row] for row in A]; m=len(M);n=len(M[0]); k=0
    for j in range(n):
        i=next((a for a in range(k,m) if M[a][j]),None)
        if i is None:continue
        M[k],M[i]=M[i],M[k];r=M[k][j]
        for col in range(j,n):M[k][col]/=r
        for a in range(k+1,m):
            u=M[a][j]
            for col in range(j,n):M[a][col]-=u*M[k][col]
        k+=1
        if k==m:break
    return k

def mldeg(d,t):
    C=[[0 if i==j else (t if (i,j) in ((0,1),(1,0)) else 1) for j in range(d)] for i in range(d)]
    chi=0; vanished=[]
    for s in range(1,d+1):
        for S in combinations(range(d),s):
            mat=[[C[i][j] for j in S] for i in S]
            r=rank(mat)
            qchi=(s if r==0 else s-1+(r%2==0))
            chi+=(-1)**(d-s)*qchi
            if s>=2 and r<s:vanished.append(S)
    return (-1)**d*chi,vanished

if __name__=='__main__':
    for d in range(4,10):
        base=2**(d-1)-d
        for t in [Fraction(1),Fraction(-1),Fraction(7,5)]+[Fraction(2*k,k-1) for k in range(2,d-1)]:
            val,van=mldeg(d,t)
            k=next((k for k in range(2,d-1) if t==Fraction(2*k,k-1)),None)
            expected=base-(math.comb(d-2,k) if k else 0)
            assert val==expected,(d,t,val,expected)
            assert (len(van)==(math.comb(d-2,k) if k else 0)),(d,t,van)
            if k:assert all(len(S)==k+2 and 0 in S and 1 in S for S in van)
        print('EXACT_ONE_EDGE_EULER_AND_RANK_OK',d)
    print('ALL_CHECKS_OK')
