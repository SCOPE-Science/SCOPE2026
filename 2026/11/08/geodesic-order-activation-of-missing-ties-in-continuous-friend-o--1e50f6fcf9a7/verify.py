"""Exact small-time coefficient checks for the continuous triadic-closure edge system.

Run with Python >=3.9: python verify.py. Uses only standard library.
"""
from fractions import Fraction as F
from collections import deque
from itertools import combinations
from random import Random

def distances(A):
    n=len(A)
    out=[[None]*n for _ in range(n)]
    for start in range(n):
        out[start][start]=0
        queue=deque([start])
        while queue:
            u=queue.popleft()
            for v in range(n):
                if u!=v and A[u][v]>0 and out[start][v] is None:
                    out[start][v]=out[start][u]+1
                    queue.append(v)
    return out

def matmul(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def coefficients(A,K):
    """Direct coefficient recursion for W'=(W+W^2/n)*(1-W), off diagonal."""
    n=len(A)
    C=[[[F(0) for j in range(n)] for i in range(n)] for _ in range(K+1)]
    C[0]=[row[:] for row in A]
    for k in range(K):
        U=[[[C[a][i][j]+sum((sum((C[b][i][h]*C[a-b][h][j] for b in range(a+1)),F(0)) for h in range(n)),F(0))/n for j in range(n)] for i in range(n)] for a in range(k+1)]
        for i in range(n):
            for j in range(n):
                if i==j: continue
                rhs=U[k][i][j]-sum((U[a][i][j]*C[k-a][i][j] for a in range(k+1)),F(0))
                C[k+1][i][j]=rhs/F(k+1)
    return C

def check(A):
    n=len(A)
    ds=distances(A)
    K=max(d for row in ds for d in row if d is not None)-1
    cs=coefficients(A,max(K,1))
    P=[row[:] for row in A]
    powers={1:P}
    for k in range(2,K+2):
        P=matmul(P,A); powers[k]=P
    tests=0
    for i in range(n):
        for j in range(n):
            if i==j: continue
            d=ds[i][j]
            if d is None:
                for z in range(K+1):
                    assert cs[z][i][j] == 0
                    tests += 1
            elif d==1:
                assert cs[0][i][j] == A[i][j]
                tests+=1
            else:
                for z in range(d-1):
                    assert cs[z][i][j]==0
                    tests+=1
                assert cs[d-1][i][j]==powers[d][i][j]/(F(n)**(d-1)),(n,i,j,d,cs[d-1][i][j],powers[d][i][j])
                assert cs[d-1][i][j]>0
                tests += 2
    return tests

rng=Random(71093)
tests=0
# paths, cycles, disconnected cases, and weighted random graphs
for n in range(2,8):
    configs=[]
    configs.append([(i,i+1) for i in range(n-1)])
    if n>=3: configs.append([(i,(i+1)%n) for i in range(n)])
    if n>=4: configs.append([(0,1),(2,3)])
    configs.append(list(combinations(range(n),2)))
    for _ in range(18):
        E=[edge for edge in combinations(range(n),2) if rng.random()<rng.uniform(.15,.7)]
        configs.append(E)
    for E in configs:
        A=[[F(int(i==j)) for j in range(n)] for i in range(n)]
        for i,j in E:
            a=F(rng.randint(1,5),rng.randint(5,11))
            A[i][j]=A[j][i]=a
        tests+=check(A)
assert tests>1000,tests
print('VERIFY_OK',tests,'exact coefficient/vanishing/positivity identities')
