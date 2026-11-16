#!/usr/bin/env python3
"""Independent moment-matrix checks for low-degree spherical orthant restriction.
Uses exact gamma-moment identities, plus numerical Hermitian diagonalization.
No external research or operational dependencies; Python3, numpy and scipy.
"""
import math
from itertools import combinations
import numpy as np
from scipy.special import gammaln

def blocks(d):
    assert d >= 3
    pi=math.pi; t=2/pi; m=d*(d-1)/2; H=d*(d+2)
    h=math.exp(gammaln(d/2)-gammaln((d+1)/2))/math.sqrt(pi)
    b0=np.array([[1., d*h, 2/pi*math.sqrt(m*(d+2)/d)],
                 [d*h,1+t*(d-1),2*h*math.sqrt(m*H)/(d+1)*(1+(d-2)/pi)],
                 [2/pi*math.sqrt(m*(d+2)/d),2*h*math.sqrt(m*H)/(d+1)*(1+(d-2)/pi),
                  1+4*(d-2)/pi+2*(d-2)*(d-3)/pi**2]])
    b1=np.array([[1-t,h*math.sqrt(d*H/2)/(d+1),h*math.sqrt(d*H*(d-2))/(d+1)*(1-t)],
                 [h*math.sqrt(d*H/2)/(d+1),1,math.sqrt(2*(d-2))/pi],
                 [h*math.sqrt(d*H*(d-2))/(d+1)*(1-t),math.sqrt(2*(d-2))/pi,
                  1+(d-4)*t-(d-3)*t*t]])
    return b0,b1,(1-t)**2

def direct_matrix(d):
    H=d*(d+2)
    zero=(0,)*d
    basis=[{zero:1.}]
    for j in range(d):
        ex=list(zero); ex[j]=1
        basis.append({tuple(ex):math.sqrt(d)})
    # Helmert basis for the trace-free diagonals
    for k in range(1,d):
        v=np.zeros(d);v[:k]=1/math.sqrt(k*(k+1));v[k]=-k/math.sqrt(k*(k+1))
        pol={}
        for j in range(d):
            if v[j]:
                e=list(zero);e[j]=2
                pol[tuple(e)]=math.sqrt(H/2)*v[j]
        basis.append(pol)
    for i,j in combinations(range(d),2):
        e=list(zero);e[i]=e[j]=1
        basis.append({tuple(e):math.sqrt(H)})
    # independent unconditional moment formula for absolute sphere coordinates
    memo={}
    def moment(exponents):
        k=tuple(exponents)
        if k not in memo:
            q=sum(k)
            v=math.exp(gammaln(d/2)-gammaln((d+q)/2)+sum(gammaln((a+1)/2)-gammaln(.5) for a in k))
            memo[k]=v
        return memo[k]
    N=len(basis)
    A=np.zeros((N,N))
    for i in range(N):
        for j in range(i,N):
            val=sum(c1*c2*moment(tuple(a+b for a,b in zip(exp1,exp2)))
                    for exp1,c1 in basis[i].items() for exp2,c2 in basis[j].items())
            A[i,j]=A[j,i]=val
    return A

def main():
    checks=0
    for d in range(3,10):
        b0,b1,scalar=blocks(d)
        A=direct_matrix(d)
        ref=np.concatenate([np.linalg.eigvalsh(b0),np.tile(np.linalg.eigvalsh(b1),d-1),np.full(d*(d-3)//2,scalar)])
        actual=np.linalg.eigvalsh(A)
        err=np.max(np.abs(np.sort(actual)-np.sort(ref)))
        assert err < 8e-11, (d,err)
        assert np.min(actual)>0 and np.max(actual)< 2**d, d
        dim=(d*(d+1)//2)+d
        assert len(ref)==dim
        assert abs(np.trace(A)-dim)<1e-10, (d,np.trace(A),dim)
        checks += len(actual) + 3
    print('PASS: direct absolute-sphere monomial moments vs block spectra, dimensions 3..9:',checks,'checks')
    for d in (10,20,50,100,300,1000):
        b0,b1,s=blocks(d)
        a=np.linalg.eigvalsh(b0);b=np.linalg.eigvalsh(b1)
        k=math.sqrt(max(a[-1],b[-1],s)/min(a[0],b[0],s))
        print('d=%d normalized_max=%0.12g normalized_min=%0.12g condition=%0.12g normalized_cond=%0.12g' % (d, max(a[-1],b[-1],s)/2**d,min(a[0],b[0],s)/2**d,k,k/d**2))
    print('asymptotic target:',2/(math.pi*(math.pi-3)))

if __name__=='__main__':
    main()
