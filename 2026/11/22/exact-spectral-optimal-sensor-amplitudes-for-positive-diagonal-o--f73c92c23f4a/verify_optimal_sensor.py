"""Exact rational diagnostics for E-optimal single-orbit sensing.

Run with Python 3: python verify_optimal_sensor.py
The general theorem uses total positivity and Perron--Frobenius theory;
finite rational tests are reproducible checks, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random

checks = 0

def ck(condition, description):
    global checks
    assert condition, description
    checks += 1

def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def det(M):
    n = len(M)
    if not n:
        return F(1)
    X = [list(row) for row in M]
    sign, product = 1, F(1)
    for j in range(n):
        k = next((i for i in range(j,n) if X[i][j]), None)
        if k is None:
            return F(0)
        if k != j:
            X[j], X[k] = X[k], X[j]
            sign = -sign
        pivot = X[j][j]
        product *= pivot
        for i in range(j+1,n):
            factor = X[i][j] / pivot
            for h in range(j+1,n):
                X[i][h] -= factor*X[j][h]
            X[i][j] = F(0)
    return product*sign

def inverse(M):
    n = len(M)
    A = [list(row) + row2 for row, row2 in zip(M, identity(n))]
    for j in range(n):
        k = next(i for i in range(j,n) if A[i][j])
        A[j], A[k] = A[k], A[j]
        pivot = A[j][j]
        A[j] = [v / pivot for v in A[j]]
        for i in range(n):
            if i != j:
                x = A[i][j]
                A[i] = [a-x*b for a,b in zip(A[i],A[j])]
    return [row[n:] for row in A]

def minor(M, I, J):
    return det([[M[i][j] for j in J] for i in I])

def test(nodes, N):
    n=len(nodes)
    C=[[sum((nodes[i]*nodes[j])**k for k in range(N+1)) for j in range(n)] for i in range(n)]
    for m in range(1,n+1):
        for I in combinations(range(n),m):
            for J in combinations(range(n),m):
                ck(minor(C,I,J)>0, 'Gram is strictly totally positive')
    B=inverse(C)
    for i in range(n):
        for j in range(n):
            ck((-1)**(i+j)*B[i][j]>0,'checkerboard inverse')
    r=[sum((-1)**(i+j)*B[i][j] for j in range(n)) for i in range(n)]
    L=sum(r)
    ck(all(x>0 for x in r),'positive row sums')
    ck(L>0,'positive optimum reciprocal')
    p=[v/L for v in r]
    ck(sum(p)==1,'probabilities sum to one')
    K=[[C[i][j]-(F(1,r[i]) if i==j else 0) for j in range(n)] for i in range(n)]
    # Exact PSD certificate by nonnegative principal minors.
    for m in range(1,n+1):
        for I in combinations(range(n),m):
            ck(minor(K,I,I)>=0,'sharp Gram certificate is positive semidefinite')
    ck(det(K)==0,'sharp Gram certificate has zero determinant')
    e=[F((-1)**i) for i in range(n)]
    for i in range(n):
        ck(sum(K[i][j]*e[j]*r[j] for j in range(n))==0,'sharp null direction')
    return C,r,L,p

sample_nodes=[F(1,4),F(1,2),F(3,4)]
C,r,L,p=test(sample_nodes,2)
ck(L==2097,'three-mode sharp constant')
ck(r==[F(597),F(1045),F(455)],'three-mode row sums')
ck(p==[F(597,2097),F(1045,2097),F(455,2097)],'three-mode weights')
rng=Random(2026)
for n in (2,3,4):
    for case in range(5):
        population=list(range(1,18))
        draws=sorted(rng.sample(population,n))
        nodes=[F(x,19) for x in draws]
        N=n-1 + case%3
        test(nodes,N)
print('OPTIMAL_ORBIT_SENSOR_RATIONAL_OK',checks)
