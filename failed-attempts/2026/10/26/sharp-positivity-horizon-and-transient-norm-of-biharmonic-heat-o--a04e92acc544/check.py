"""Independent exact and numerical checks for triangular-graph biharmonic heat."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, exp, log
import numpy as np
from scipy.linalg import expm

COUNT=0

def check(cond, context=''):
    global COUNT
    COUNT+=1
    if not cond:
        raise AssertionError(context or f'assertion {COUNT}')

for n in range(4,12):
    vertices=list(combinations(range(n),2))
    N=len(vertices)
    R=[[len(set(s)&set(t)) for t in vertices] for s in vertices]
    E0=[[F(1,N) for j in range(N)] for i in range(N)]
    E1=[[F(R[i][j],1)-F(4,n) for j in range(N)] for i in range(N)]
    E1=[[x/(n-2) for x in row] for row in E1]
    E2=[[F(int(i==j))-E0[i][j]-E1[i][j] for j in range(N)] for i in range(N)]
    Lap=[[F(2*(n-2) if i==j else -int(R[i][j]==1)) for j in range(N)] for i in range(N)]
    for i in range(N):
        check(sum(E0[i])==1, 'E0 row stochastic')
        check(sum(E1[i])==0, 'E1 row centered')
        check(sum(E2[i])==0, 'E2 row centered')
        for j in range(N):
            check(Lap[i][j]==n*E1[i][j]+2*(n-1)*E2[i][j], 'laplacian spectral identity')
            check(E1[i][j]==(F(R[i][j])-F(4,n))/F(n-2))
            check(E0[i][j]+E1[i][j]+E2[i][j]==(1 if i==j else 0))
    # independent exact matrix multiplication test for projection idempotence and orthogonality
    for i in range(N):
        for j in range(N):
            check(sum(E1[i][k]*E1[k][j] for k in range(N)) == E1[i][j], 'E1 square')
            check(sum(E2[i][k]*E2[k][j] for k in range(N)) == E2[i][j], 'E2 square')
            check(sum(E1[i][k]*E2[k][j] for k in range(N)) == 0, 'cross projection')
    tpeak=log(2*(n-1)/n)/((3*n-2)*(n-2))
    def h0(t):
        u=exp(-n*n*t)
        v=exp(-4*(n-1)**2*t)
        return 2*((n-2)-2*(n-1)*u+n*v)/(n*(n-1)*(n-2))
    check(abs(h0(0.0))<1e-13)
    check(h0(tpeak)<0)
    check(h0(10.)>0)
    check(h0(tpeak-1e-5)<h0(1e-6) if tpeak>1e-5 else True)
    for t in [tpeak/3, tpeak, 1.5*tpeak, 0.1, 1.0]:
        u=exp(-n*n*t);v=exp(-4*(n-1)**2*t)
        H=np.array(E0,dtype=float)+u*np.array(E1,dtype=float)+v*np.array(E2,dtype=float)
        check(np.max(np.abs(H-H.T))<2e-13)
        check(np.max(np.abs(H.sum(axis=1)-1))<2e-12)
        check(abs(H[0][R[0].index(0)]-h0(t))<2e-13)
        expected=1+2*(n-3)/(n*(n-1))*max(0,2*(n-1)*u-n*v-(n-2))
        check(abs(max(np.sum(np.abs(H),axis=1))-expected)<1e-11, 'norm formula')
        check(np.min(H[0][np.array(R[0])==1])>0, 'positive adjacent kernel')
        if n<=7:
            direct=expm(-t*np.linalg.matrix_power(np.array(Lap,dtype=float),2))
            check(np.max(np.abs(direct-H))<5e-10,'independent matrix exponential')
    # verify all off-diagonal entries match scheme formulas
    for i in range(N):
        for j in range(N):
            if R[i][j]==0:
                check(E0[i][j]==F(2,n*(n-1)))
                check(E1[i][j]==F(-4,n*(n-2)))
                check(E2[i][j]==F(2,(n-1)*(n-2)))
            elif R[i][j]==1:
                check(E1[i][j]==F(n-4,n*(n-2)))

# Asymptotic checks on rescaled maximizers (no claim of proof)
for n in [100,1000,10000,100000]:
    tp=log(2*(n-1)/n)/((3*n-2)*(n-2))
    u=exp(-n*n*tp);v=exp(-4*(n-1)**2*tp)
    maximum=1+2*(n-3)/(n*(n-1))*(2*(n-1)*u-n*v-(n-2))
    limit=3*2**(-1/3)-1
    check(abs(maximum-limit) < 400/n)
    check(abs(n*n*tp-log(2)/3) < 100/n)
print(f'CHECK_OK exact_and_numeric_assertions={COUNT}')
