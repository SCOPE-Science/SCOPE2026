"""Exact finite-spectrum and direct Fourier checks for first-band q-ary ball restriction.
Run: python verify.py. Requires numpy only for independent direct Fourier tests.
"""
from math import comb, sqrt, pi
from fractions import Fraction as F
from itertools import product

def pmf(n,k,q):
    return F(comb(n,k)*(q-1)**k,q**n) if 0<=k<=n else F(0)

def cdf(n,k,q):
    return sum((pmf(n,j,q) for j in range(max(0,k+1))),F(0))

def blocks(n,k,q):
    alpha=pmf(n-1,k,q)
    beta=cdf(n-1,k-1,q)
    r,s=pmf(n-2,k,q),pmf(n-2,k-1,q)
    m=cdf(n,k,q)
    d=beta+F(q-1,q)*alpha
    e=F(q-1,q*q)*(r-s)
    c2=F(q-1,q*q)*alpha**2
    mu=d-e
    D=d+(n-1)*e
    tr=m+D
    det=m*D-n*c2
    return m,beta,mu,d,e,alpha,c2,D,tr,det,r,s

def test_exact():
    checks=0
    for q in range(3,12):
      for n in range(3,30):
        for k in range(1,n):
            m,beta,mu,d,e,alpha,c2,D,tr,det,r,s=blocks(n,k,q)
            # Consequences needed for strict sector ordering, all exact rational.
            assert m==beta+alpha/q
            assert mu==beta+F(q-1,q)*s
            assert (beta-m)*(beta-D)-n*c2==-F((n-1)*(q-1),q*q)*alpha*s
            assert (mu-m)*(mu-D)-n*c2==-F(n*(q-1),q*q)*r*s
            assert alpha>0 and s>0 and mu>beta
            if k<n-1: assert r>0
            else: assert r==0 and mu==1
            assert tr>0 and det>0
            checks+=1
    return checks

def test_direct():
    import numpy as np
    count=0
    for q,n in ((3,3),(3,4),(3,5),(4,3),(4,4),(5,3)):
        points=list(product(range(q),repeat=n))
        chars=[(None,0)]+[(i,h) for i in range(n) for h in range(1,q)]
        mat=np.empty((q**n,len(chars)),complex)
        for j,x in enumerate(points):
            for a,(i,h) in enumerate(chars):
                mat[j,a]=1 if i is None else np.exp(2j*np.pi*h*x[i]/q)
        for k in range(1,n):
            rows=[j for j,x in enumerate(points) if sum(v!=0 for v in x)<=k]
            Gram=mat[rows].conj().T@mat[rows]/q**n
            eig=np.linalg.eigvalsh(Gram)
            m,beta,mu,d,e,alpha,c2,D,tr,det,r,s=blocks(n,k,q)
            lminus=(float(tr)-sqrt(float(tr**2-4*det)))/2
            lplus=(float(tr)+sqrt(float(tr**2-4*det)))/2
            expected=sorted([lminus,lplus]+[float(mu)]*(n-1)+[float(beta)]*(n*(q-2)))
            assert np.allclose(eig,expected,atol=1e-11,rtol=2e-9),(q,n,k,eig,expected)
            count+=1
    return count

if __name__=='__main__':
    print('QARY_BALL_FIRST_BAND_VERIFY_OK',test_exact(),test_direct())
