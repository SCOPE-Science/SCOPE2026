"""Finite reproducibility checks for alternating-mass cycle fastest mixing.
Analytic global optimality follows from the proof, not these finite checks.
Requires numpy and sympy; no network or external files.
"""
import math
import random
from fractions import Fraction
import numpy as np
from sympy import Rational, Matrix


def formula(n, A, B):
    assert n >= 3 and A >= B > 0
    c = math.cos(math.pi / n)
    S = 1/A + 1/B
    psi = math.sqrt((1/A-1/B)**2 + 4*c*c/(A*B))
    alpha = S-psi
    w = min(B/2, 2/(3*S-psi))
    rho = 1-alpha*w
    return w, rho, alpha, psi


def matrix(n, A, B, weights):
    masses = np.array([A if j%2 == 0 else B for j in range(2*n)], dtype=float)
    P = np.eye(2*n)
    for j, w in enumerate(weights):
        k = (j+1)%(2*n)
        P[j,k] += w/masses[j]
        P[k,j] += w/masses[k]
        P[j,j] -= w/masses[j]
        P[k,k] -= w/masses[k]
    return P, masses


def slem(P, pi):
    H = np.sqrt(pi)[:,None]*P/np.sqrt(pi)[None,:]
    eig = np.linalg.eigvalsh((H+H.T)/2)
    return max(abs(eig[:-1])), eig


cnt = {'spectral':0,'stochastic':0,'rational':0,'perturbation':0,'threshold':0}
for n in range(3,11):
    for A,B in [(1,1),(6,5),(3,2),(2,1),(5,1),(10,1)]:
        w,rho,alpha,psi=formula(n,A,B)
        P,pi=matrix(n,A,B,[w]*(2*n))
        evrho,eig=slem(P,pi)
        assert abs(evrho-rho)<1.e-11, (n,A,B,evrho,rho)
        assert np.max(abs(P.sum(axis=1)-1))<1.e-12
        assert np.min(P)>-1.e-12
        assert np.max(abs(pi[:,None]*P-(pi[:,None]*P).T))<1.e-12
        cnt['stochastic']+=1
        S=1/A+1/B
        th=[]
        for k in range(n):
            psi_k=math.sqrt((1/A-1/B)**2+4/(A*B)*math.cos(math.pi*k/n)**2)
            th += [1-w*(S-psi_k),1-w*(S+psi_k)]
        assert np.max(abs(np.sort(th)-eig))<1.e-11,(n,A,B)
        cnt['spectral']+=1
        rc=2/(1+math.cos(math.pi/n)**2)
        assert (w < B/2-1.e-10)==(A/B<rc-1.e-10), (n,A,B,rc,w)
        cnt['threshold']+=1
        rng=random.Random(19000+100*n+A*100+B)
        for _ in range(28):
            es=[rng.random() for i in range(2*n)]
            m=np.array([A if i%2==0 else B for i in range(2*n)],float)
            cap=min(m[i]/(es[i]+es[(i-1)%(2*n)]) for i in range(2*n))
            es=[x*cap*rng.random() for x in es]
            Ps,ms=matrix(n,A,B,es)
            r,_=slem(Ps,ms)
            assert r>rho-1.e-10,(n,A,B,r,rho)
            cnt['perturbation']+=1

for n in range(3,7):
    for A,B in [(1,1),(2,1),(3,2),(5,1)]:
        for w in [Fraction(B,2),Fraction(B,4)]:
            masses=[Fraction(A if j%2==0 else B) for j in range(2*n)]
            P=[[Fraction(int(i==j)) for j in range(2*n)] for i in range(2*n)]
            for i in range(2*n):
                j=(i+1)%(2*n)
                P[i][j]+=w/masses[i];P[j][i]+=w/masses[j]
                P[i][i]-=w/masses[i];P[j][j]-=w/masses[j]
            assert all(sum(row)==1 for row in P)
            assert all(masses[i]*P[i][j]==masses[j]*P[j][i]
                       for i in range(2*n) for j in range(2*n))
            assert all(P[i][j]>=0 for i in range(2*n) for j in range(2*n))
            M=Matrix([[Rational(x.numerator,x.denominator) for x in row] for row in P])
            assert M*Matrix([1]*(2*n))==Matrix([1]*(2*n))
            cnt['rational']+=1
print('PASS',cnt)
