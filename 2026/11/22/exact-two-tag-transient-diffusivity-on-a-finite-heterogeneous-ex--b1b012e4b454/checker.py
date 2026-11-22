#!/usr/bin/env python3
"""Independent generator, exact arithmetic, and spectral checks for two distinguishable exclusion walkers on a cycle."""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import expm


def transitions(L, r1, r2):
    n=L-1
    for k in range(1,n+1):
        a=[]
        if k>1:
            a += [(k-1, r1,1,0),(k-1,r2,0,-1)]
        if k<n:
            a += [(k+1,r1,-1,0),(k+1,r2,0,1)]
        yield a

def generator(L,r1,r2):
    n=L-1; Q=np.zeros((n,n)); B=[np.zeros((n,n)) for _ in range(2)]; C=[np.zeros((n,n)) for _ in range(2)]
    for k,trs in enumerate(transitions(L,r1,r2)):
        for j,rate,dx1,dx2 in trs:
            j-=1; Q[k,j]+=rate; Q[k,k]-=rate
            for i,dx in enumerate([dx1,dx2]):
                B[i][k,j]+=rate*dx
                C[i][k,j]+=rate*dx*dx
    return Q,B,C

def matrix_msd(L,r1,r2,t,i):
    Q,B,C=generator(L,r1,r2)
    n=L-1
    A=np.block([[Q,np.zeros_like(Q),np.zeros_like(Q)],[B[i],Q,np.zeros_like(Q)],[C[i],2*B[i],Q]])
    v=np.concatenate([np.ones(n),np.zeros(n),np.zeros(n)])
    ans=expm(t*A)@v
    return np.mean(ans[2*n:3*n])

def spectral_msd(L,r1,r2,t,i):
    n=L-1; q=r1+r2; d=[r1,r2][i]
    d_eff=(n-1)*r1*r2/(n*q)
    total=2*d_eff*t
    for m in range(1,n,2):
        th=m*math.pi/(2*n); lam=4*q*math.sin(th)**2
        total+=(d/q)**2 * (math.cos(th)**2/(n*n*math.sin(th)**4))*(-math.expm1(-lam*t))
    return total

def spectral_derivative(L,r1,r2,t,i):
    n=L-1; q=r1+r2; d=[r1,r2][i]
    deff=(n-1)*r1*r2/(n*q)
    return deff+(d/q)**2/2*sum((math.cos(m*math.pi/(2*n))**2/(n*n*math.sin(m*math.pi/(2*n))**4))*(4*q*math.sin(m*math.pi/(2*n))**2)*math.exp(-4*q*math.sin(m*math.pi/(2*n))**2*t) for m in range(1,n,2))

def exact_corrector_check(L,a,b):
    n=L-1; q=a+b
    u=[Fraction(a,q)*(Fraction(k)-Fraction(n+1,2)) for k in range(1,n+1)]
    for k in range(1,n+1):
        Qu=Fraction(0)
        if k>1:Qu+=Fraction(q)*(u[k-2]-u[k-1])
        if k<n:Qu+=Fraction(q)*(u[k]-u[k-1])
        g=Fraction(a)*((k==n)-(k==1))
        assert Qu==-g
    var=sum(x*x for x in u)/n
    assert 2*var==Fraction(a*a,q*q)*Fraction(n*n-1,6)
    return 1


def main():
    count=0
    for L in range(3,18):
        for a,b in [(1,1),(1,2),(3,7),(11,2)]:
            count += exact_corrector_check(L,a,b)
    for L in range(3,15):
        for a,b in [(0.3,1.7),(1.2,1.2),(4.2,.6)]:
            for t in [.015,.1,1.,3.]:
                for i in [0,1]:
                    x=matrix_msd(L,a,b,t,i)
                    y=spectral_msd(L,a,b,t,i)
                    assert abs(x-y) < 3.e-8*(1+abs(y)),(L,a,b,t,i,x,y)
                    count+=1
            n=L-1;q=a+b;Deff=(n-1)*a*b/(n*q)
            for t in [0,.01,.1,1.]:
                ds=[spectral_derivative(L,a,b,t,i)-Deff for i in range(2)]
                if min(ds)<1e-14: continue
                assert all(x>0 for x in ds)
                assert abs(ds[0]/ds[1]-(a/b)**2)<1e-7
                count+=1
            for i,d in enumerate([a,b]):
                y=spectral_msd(L,a,b,200,i)-2*Deff*200
                B=(d/q)**2*(n*n-1)/6
                assert abs(y-B)<5e-8*(1+B), (L,a,b,i,y,B)
                count+=1
    print('PASSED',count,'independent-generator and exact Poisson-corrector tests')

if __name__=='__main__':main()
