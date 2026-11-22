"""Reproducibility checks for rank-one-boundary positive-cone sensitivity.

Python 3 standard library only. These finite checks supplement the proof; they
are not an exhaustive verification of its dimension-uniform assertions.
"""
import math
import random


def sharp_profile(n, p):
    return n*p*(1-p)+p+2*math.sqrt(n-1)*math.sqrt(p)*(1-p)**1.5


def derivative_profile(n, p):
    return n*(1-2*p)+1+math.sqrt(n-1)*(1-4*p)*math.sqrt((1-p)/p)


def maximizing_p(n):
    if n == 2:
        return 0.5
    lo, hi = 0.25, 0.5
    for _ in range(85):
        mid = (lo+hi)/2
        if derivative_profile(n, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def unit_vector(n, p):
    return [math.sqrt(p)] + [math.sqrt((1-p)/(n-1))]*(n-1)


def extremizing_H(n):
    return [[1.0 if i==0 or j==0 else -1.0 for j in range(n)]
            for i in range(n)]


def derivative(Au, H, epsilon):
    n = len(Au)
    v = [sum(H[i][j]*Au[j] for j in range(n)) for i in range(n)]
    uHu = sum(Au[i]*v[i] for i in range(n))
    t = 1.0/(1.0+epsilon)
    return [[uHu*Au[i]*Au[j]+t*(Au[i]*(v[j]-uHu*Au[j])+(v[i]-uHu*Au[i])*Au[j])
             for j in range(n)] for i in range(n)]


def project_psd(A):
    n=len(A)
    B=[row[:] for row in A]
    V=[[float(i==j) for j in range(n)] for i in range(n)]
    for _ in range(130*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),
                key=lambda ij: abs(B[ij[0]][ij[1]]))
        if abs(B[p][q]) < 5e-14:
            break
        tau=(B[q][q]-B[p][p])/(2*B[p][q])
        t=math.copysign(1,tau)/(abs(tau)+math.sqrt(1+tau*tau)) if tau else 1.0
        c=1/math.sqrt(1+t*t); s=c*t
        bpp,bqq,bpq=B[p][p],B[q][q],B[p][q]
        B[p][p]=bpp-t*bpq
        B[q][q]=bqq+t*bpq
        B[p][q]=B[q][p]=0.0
        for k in range(n):
            if k!=p and k!=q:
                x,y=B[k][p],B[k][q]
                B[k][p]=B[p][k]=c*x-s*y
                B[k][q]=B[q][k]=s*x+c*y
            x,y=V[k][p],V[k][q]
            V[k][p]=c*x-s*y
            V[k][q]=s*x+c*y
    else:
        raise RuntimeError('Jacobi convergence not achieved')
    return [[sum(max(B[k][k],0)*V[i][k]*V[j][k] for k in range(n))
            for j in range(n)] for i in range(n)]


def check():
    checks=0
    rnd=random.Random(17341)
    for n in range(2,25):
        pstar=maximizing_p(n)
        assert 0.25 < pstar <= 0.5
        checks+=1
        assert abs(derivative_profile(n,pstar))<1e-9
        checks+=1
        for _ in range(15):
            p=1e-4+(1-2e-4)*rnd.random()
            u=unit_vector(n,p)
            H=extremizing_H(n)
            D=derivative(u,H,0.0)
            assert abs(D[0][0]-sharp_profile(n,p))<2e-10
            checks+=1
            assert sharp_profile(n,p)<=sharp_profile(n,pstar)+2e-10
            checks+=1
    for n in [2,3,4,6,9]:
        p=maximizing_p(n)
        u=unit_vector(n,p)
        H=extremizing_H(n)
        for eps in [0.005,0.03,0.12]:
            A=[[(1+eps)*u[i]*u[j]-(eps if i==j else 0)
                for j in range(n)] for i in range(n)]
            D=derivative(u,H,eps)
            d=2e-7
            B=[[A[i][j]+d*H[i][j] for j in range(n)] for i in range(n)]
            P=project_psd(A)
            Q=project_psd(B)
            ratio=(Q[0][0]-P[0][0])/d
            assert abs(ratio-D[0][0])<1.5e-4, (n,eps,ratio,D[0][0])
            checks+=1
    for n in [2,3,5,7]:
        p=0.2+0.6*rnd.random()
        u=unit_vector(n,p)
        eps=0.07
        A=[[(1+eps)*u[i]*u[j]-(eps if i==j else 0)
            for j in range(n)] for i in range(n)]
        for trial in range(24):
            H=[[0.0]*n for _ in range(n)]
            for i in range(n):
                for j in range(i,n):
                    H[i][j]=H[j][i]=rnd.uniform(-1,1)
            D=derivative(u,H,eps)
            d=1e-6
            B=[[A[i][j]+d*H[i][j] for j in range(n)] for i in range(n)]
            P=project_psd(A)
            Q=project_psd(B)
            for i in range(n):
                for j in range(n):
                    assert abs((Q[i][j]-P[i][j])/d-D[i][j])<2e-4
                    checks+=1
    assert abs(sharp_profile(2,maximizing_p(2))-1.5)<1e-12
    checks+=1
    for n in [10000,100000,1000000]:
        f=sharp_profile(n,maximizing_p(n))
        approximate=n/4+math.sqrt(n)/2+0.75
        assert abs(f-approximate)<1.2/math.sqrt(n)
        checks+=1
    print(f'{checks} supplementary checks passed (finite numerical tests; not the proof).')

if __name__ == '__main__':
    check()
