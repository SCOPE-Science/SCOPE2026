"""Finite consistency tests for a reflected-AR(1) Gram family.
Run: python CHECK.py. Requires numpy and scipy; finite tests do not prove limits.
"""
import math
import numpy as np
from scipy.optimize import brentq

checks = 0

def check(ok, msg):
    global checks
    assert ok, msg
    checks += 1

def matrix(n,q):
    j=np.arange(n+1)
    if q==1:
        return 2.+4.*np.minimum.outer(j,j)
    if q==0:
        return np.eye(n+1)
    # Geometric sum form avoids cancellation near q=1.
    a=np.abs(j[:,None]-j[None,:]); m=np.minimum.outer(j,j)
    return (1+q)*np.power(q,a)*(-np.expm1((2*m+1)*np.log(q)))/(-np.expm1(np.log(q)))

def independent_coeff(n,q):
    if q==1: return [1.]+[2.]*n
    return [math.sqrt(q)] + [math.sqrt(q)*(1+q)*q**(k-1) for k in range(1,n+1)]

def from_toeplitz(n,q):
    p=independent_coeff(n,q)
    return np.array([[float(j==k)+sum(p[s]*p[abs(k-j)+s] for s in range(min(j,k)+1)) for k in range(n+1)] for j in range(n+1)])

for n in range(1,16):
    for q in (0.08,0.37,0.8,0.97,1.0):
        G=matrix(n,q)
        check(np.allclose(G,from_toeplitz(n,q),rtol=4e-12,atol=3e-12),(n,q,'coeff'))
        D=np.eye(n+1)
        for i in range(1,n+1): D[i,i-1]=-q
        w=np.array([1+q]+[(1+q)**2]*n)
        check(np.allclose(D@G@D.T,np.diag(w),rtol=2e-11,atol=2e-11),(n,q,'factor'))
        check(np.allclose(np.linalg.slogdet(G)[1],(2*n+1)*np.log1p(q),atol=1e-9),(n,q,'det'))
        check(np.linalg.eigvalsh(G)[0]>=1-1e-8,(n,q,'positive'))
        Gi=D.T@np.diag(1/w)@D
        check(np.allclose(Gi@G,np.eye(n+1),rtol=1e-10,atol=2e-10),(n,q,'inverse'))

for tau in (0.,.5,2.,7.):
    omega=math.pi/2 if tau==0 else brentq(lambda w:w*math.cos(w)+tau*math.sin(w),math.pi/2+1e-10,math.pi-1e-10)
    target=4/(tau*tau+omega*omega)
    prev=float('inf')
    for n in (40,80,160):
        q=1. if tau==0 else math.exp(-tau/n)
        vals=np.linalg.eigvalsh(matrix(n,q))
        value=vals[-1]/(n*n)
        check(abs(value-target)<0.09,(tau,n,value,target))
        check(value<prev+1e-12,(tau,n,'convergence'))
        prev=value

for q in (.12,.6,.9):
    vals=np.linalg.eigvalsh(matrix(320,q))
    target=((1+q)/(1-q))**2
    check(abs(vals[-1]/target-1)<.16,(q,vals[-1],target))
    check(abs(vals[0]-1)<1e-3,(q,vals[0]))

print(f'PASS: {checks} assertions')
