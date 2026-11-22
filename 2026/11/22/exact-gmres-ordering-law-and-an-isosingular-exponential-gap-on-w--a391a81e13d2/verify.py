"""Exact-rational checks for GMRES residuals on weighted bidiagonal chains."""
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial

def A_of(weights):
    n=len(weights)+1
    A=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j,w in enumerate(weights): A[j+1][j]=-F(w)
    return A

def solve(M,b):
    n=len(b)
    A=[list(M[i])+[b[i]] for i in range(n)]
    for j in range(n):
        q=next(i for i in range(j,n) if A[i][j])
        A[j],A[q]=A[q],A[j]
        v=A[j][j]
        A[j]=[x/v for x in A[j]]
        for i in range(n):
            if i==j: continue
            v=A[i][j]
            A[i]=[A[i][h]-v*A[j][h] for h in range(n+1)]
    return [A[i][-1] for i in range(n)]

def direct_r2(weights,k):
    n=len(weights)+1
    if not k: return F(1)
    A=A_of(weights)
    Q=[[A[i][j] for j in range(k)] for i in range(n)]
    gram=[[sum(Q[i][j]*Q[i][h] for i in range(n)) for h in range(k)] for j in range(k)]
    rhs=[Q[0][j] for j in range(k)]
    x=solve(gram,rhs)
    return sum((F(int(i==0))-sum(Q[i][j]*x[j] for j in range(k)))**2 for i in range(n))

def closed_r2(weights,k):
    p=F(1)
    s=F(1)
    for v in weights[:k]:
        p/=F(v)**2
        s+=p
    return F(1)/s

def transpose(M): return list(map(list, zip(*M)))
def mmul(A,B): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def test():
    N=0
    palette=[F(1,2),F(2,3),F(3,2),F(2)]
    for l in range(1,7):
        for t in product(palette, repeat=l):
            # Avoid unneeded test combinations for l=7.
            if l>=6 and sum(x==palette[0] for x in t)>1: continue
            for k in range(1,l+1):
                assert closed_r2(t,k)==direct_r2(t,k),(t,k)
                N+=1
            assert all(closed_r2(tuple(sorted(t)),k)<=closed_r2(t,k)<=closed_r2(tuple(sorted(t,reverse=True)),k) for k in range(1,l+1)), t
            N+=l
    for m in range(1,13):
        asc=(F(1,2),)*m+(F(2),)*m
        desc=asc[::-1]
        ka=2*m
        assert 1/closed_r2(asc,ka)==F(5*4**m-2,3)
        assert 1/closed_r2(desc,ka)==(F(8,3)-F(5,3*4**m))
        A=A_of(asc); B=A_of(desc)
        n=2*m+1
        # B equals the reversed transpose of A, hence has the same singular spectrum.
        if n<=13:
            J=[[F(int(i+j==n-1)) for j in range(n)] for i in range(n)]
            assert mmul(mmul(J,transpose(A)),J)==B
            N+=1
        N+=2
    print('VERIFY_OK',N)
if __name__=='__main__': test()
