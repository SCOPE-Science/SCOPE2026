"""Reproducibility checks for finite-window diagonal-semigroup frame bounds.

Python 3 standard library only. Numerical tests supplement the analytical proof.
"""
from math import exp, sqrt, factorial, comb
from fractions import Fraction
from decimal import Decimal, getcontext
import random

checks = 0

def verify(condition, description):
    global checks
    assert condition, description
    checks += 1

def inverse(M):
    n = len(M)
    Z = [[M[i][j] for j in range(n)] + [M[i][0]*0 + int(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = max(range(col,n), key=lambda r: abs(Z[r][col]))
        Z[col],Z[pivot] = Z[pivot],Z[col]
        z = Z[col][col]
        assert z != 0
        Z[col] = [x/z for x in Z[col]]
        for row in range(n):
            if row == col:
                continue
            m = Z[row][col]
            Z[row] = [a-m*b for a,b in zip(Z[row],Z[col])]
    return [row[n:] for row in Z]

def symmetric_eigenvalues(A):
    n = len(A)
    M = [row[:] for row in A]
    for _ in range(400*n*n):
        p,q = max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(M[ij[0]][ij[1]]))
        if abs(M[p][q]) < 5e-13:
            break
        tau = (M[q][q]-M[p][p])/(2*M[p][q])
        t = (1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t);s=t*c;v=M[p][q]
        app=M[p][p]; aqq=M[q][q]
        M[p][p]=app-t*v;M[q][q]=aqq+t*v;M[p][q]=M[q][p]=0.0
        for k in range(n):
            if k not in (p,q):
                x,y=M[k][p],M[k][q]
                M[k][p]=M[p][k]=c*x-s*y
                M[k][q]=M[q][k]=s*x+c*y
    return sorted(M[i][i] for i in range(n))

def q_and_bound(lambdas, T):
    n=len(lambdas)
    K=[[(1-exp(-(lambdas[i]+lambdas[j])*T))/(lambdas[i]+lambdas[j]) for j in range(n)] for i in range(n)]
    Q=inverse(K)
    R=[[(-1)**(i+j)*Q[i][j] for j in range(n)] for i in range(n)]
    q=[sum(row) for row in R]
    S=sum(q)
    return [u/S for u in q],1/S,K,R

rng=random.Random(1701)
for lambdas in ([1.,2.],[1.,2.,3.],[1.,2.,3.,4.],[.7,1.4,2.8]):
    n=len(lambdas)
    for T in (.4,1.,3.):
        q,E,K,R=q_and_bound(lambdas,T)
        verify(all(x>0 for x in q),'positive optimal modal weights')
        verify(abs(sum(q)-1)<1e-7,'weights sum to one')
        verify(all(R[i][j]>0 for i in range(n) for j in range(n)),'inverse checkerboard')
        W=[[sqrt(q[i]*q[j])*K[i][j] for j in range(n)] for i in range(n)]
        ev=symmetric_eigenvalues(W)
        verify(abs(ev[0]-E)<1e-7,'sharp frame bound achieved')
        for _ in range(80):
            raw=[rng.random()+1e-3 for i in range(n)]
            norm=sum(z*z for z in raw)
            b=[z/sqrt(norm) for z in raw]
            X=[[b[i]*b[j]*K[i][j] for j in range(n)] for i in range(n)]
            verify(symmetric_eigenvalues(X)[0]<=E+1e-8,'random competitor bound')

for n,wanted in [(2,[Fraction(7,17),Fraction(10,17)]),
                  (3,[Fraction(41,321),Fraction(155,321),Fraction(125,321)])]:
    K=[[Fraction(1,i+j) for j in range(1,n+1)] for i in range(1,n+1)]
    Q=inverse(K)
    R=[[(-1)**(i+j)*Q[i][j] for j in range(n)] for i in range(n)]
    r=[sum(z) for z in R];S=sum(r)
    verify([z/S for z in r]==wanted,'exact infinite-window rational reference')

# High-precision small-time normalized leading constants, independent of matrix eigensolver.
getcontext().prec=85
for n in (2,3,4):
    lam=list(range(1,n+1))
    beta=[Fraction(1,1)/__import__('math').prod(lam[i]-lam[j] for j in range(n) if i!=j) for i in range(n)]
    c=factorial(n-1)**2*(2*n-1)*comb(2*n-2,n-1)**2
    prediction=Decimal(1)/(Decimal(c)*Decimal(sum(abs(b) for b in beta).numerator)**2/Decimal(sum(abs(b) for b in beta).denominator)**2)
    T=Decimal('0.01')
    K=[[(1-(-(i+j)*T).exp())/Decimal(i+j) for j in lam] for i in lam]
    Q=inverse(K)
    S=sum((-1)**(i+j)*Q[i][j] for i in range(n) for j in range(n))
    observed=(Decimal(1)/S)/(T**(2*n-1))
    verify(abs(observed/prediction-1)<Decimal('.04'),'short-time asymptotic coefficient')
print('FINITE_WINDOW_FRAME_CHECK_OK',checks)
