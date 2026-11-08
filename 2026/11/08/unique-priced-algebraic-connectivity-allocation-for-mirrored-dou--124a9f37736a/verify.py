#!/usr/bin/env python3
"""Reproducible tests of the mirrored-cost double-star spectral allocation.
No third-party dependencies. Exact rational certificates supplement numerical tests.
An arbitrary finite test cannot replace the infinite-family proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, atan2, sin, cos
from random import Random

def weights(cost, bridge, budget):
    s=[sqrt(c) for c in cost];t=sqrt(bridge)
    K=2*sum(cost)+2*t*sum(s)+(len(cost)+1)*bridge/2
    lam=budget/K
    return lam,[lam*(1+t/(2*v)) for v in s],lam*((len(cost)+1)/2+sum(s)/t),K

def laplacian(left,right,q):
    m=len(left);n=2*m+2;L=[[0.0]*n for _ in range(n)]
    def add(i,j,w):
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    for i in range(m):
        add(0,i+1,left[i]);add(m+1,m+2+i,right[i])
    add(0,m+1,q)
    return L

def eigenvalues_sym(A):
    # Jacobi diagonalization, suitable for small test graphs.
    A=[r[:] for r in A];n=len(A)
    for _ in range(150*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(A[ij[0]][ij[1]]))
        if abs(A[p][q])<1e-11:break
        tau=(A[q][q]-A[p][p])/(2*A[p][q]);t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t);s=t*c
        a,b,v=A[p][p],A[q][q],A[p][q]
        A[p][p]=a-t*v;A[q][q]=b+t*v;A[p][q]=A[q][p]=0.0
        for j in range(n):
            if j==p or j==q:continue
            x,y=A[j][p],A[j][q];A[j][p]=A[p][j]=c*x-s*y;A[j][q]=A[q][j]=s*x+c*y
    return sorted(A[i][i] for i in range(n))

def exact(csq,dsq,B):
    m=len(csq);s=[F(v) for v in csq];t=F(dsq);cost=[v*v for v in s];d=t*t
    K=2*sum(cost)+2*t*sum(s)+F(m+1,2)*d
    lam=F(B)/K
    p=[lam*(1+t/(2*v)) for v in s]
    q=lam*(F(m+1,2)+sum(s)/t)
    assert sum(2*cost[i]*p[i] for i in range(m))+d*q==B
    x=[t/2]+[t/2+u for u in s]+[-t/2]+[-t/2-u for u in s]
    assert sum(x)==0 and sum(u*u for u in x)==K
    edges=[(0,1+i,p[i]) for i in range(m)]+[(m+1,m+2+i,p[i]) for i in range(m)]+[(0,m+1,q)]
    L=[[F(0) for _ in x] for _ in x]
    for a,b,w in edges:
        L[a][a]+=w;L[b][b]+=w;L[a][b]-=w;L[b][a]-=w
    assert all(sum(L[i][j]*x[j] for j in range(len(x)))==lam*x[i] for i in range(len(x)))
    assert sum(w*(x[i]-x[j])**2 for i,j,w in edges)==B
    # Odd-sector PSD ground-state identity coefficients strictly positive.
    assert all(v>lam for v in p)
    assert q>0
    return float(lam)

def main():
    exact_cases=0;cases=0;competitors=0
    for m in range(1,7):
        for k in range(18):
            sq=[1+((i+3*k)%9) for i in range(m)];d=1+(k*7)%11
            exact(sq,d,2+k)
            exact_cases+=1
    rng=Random(8675309)
    for m in range(1,7):
        for _ in range(20):
            costs=[10**rng.uniform(-2,2) for i in range(m)]
            dc=10**rng.uniform(-2,2);B=10**rng.uniform(-1,1)
            lam,p,q,K=weights(costs,dc,B)
            eig=eigenvalues_sym(laplacian(p,p,q))
            assert abs(eig[1]-lam)<2e-7*max(1,lam)
            assert abs(2*sum(c*w for c,w in zip(costs,p))+dc*q-B)<1e-10*max(1,B)
            cases+=1
            for _ in range(12):
                z=[rng.expovariate(1) for j in range(2*m+1)]
                norm=sum(costs[i]*(z[i]+z[m+i]) for i in range(m))+dc*z[-1]
                L=laplacian([B*z[i]/norm for i in range(m)],[B*z[m+i]/norm for i in range(m)],B*z[-1]/norm)
                assert eigenvalues_sym(L)[1]<=lam+2e-7*max(1,lam)
                competitors+=1
    print('VERIFY_OK exact_certificates=%d eigenvalue_instances=%d asymmetric_competitors=%d'%(exact_cases,cases,competitors))
if __name__=='__main__':main()
