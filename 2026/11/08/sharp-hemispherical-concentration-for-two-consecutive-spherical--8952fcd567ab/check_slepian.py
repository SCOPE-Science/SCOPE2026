#!/usr/bin/env python3
"""Independent finite consistency checks for adjacent-degree hemisphere concentration.
Requires Python 3 with NumPy and SciPy; does not replace the analytic proof.
"""
import math
import numpy as np
from scipy.special import eval_legendre, lpmv, gammaln
from numpy.polynomial.legendre import leggauss

def binratio(n):
    return math.comb(2*n,n)/4**n

def predicted(l,m):
    c=math.sqrt((2*l+1)*(2*l+3))/(4*(l+1))
    if (l+m)%2 == 0:
        r=(l+m)//2; s=(l-m)//2
        f=lambda k: binratio(k)*math.sqrt(2*k+1)
        return c*f(r)*f(s)
    r=(l+m-1)//2; s=(l-m-1)//2
    g=lambda k:binratio(k)*math.sqrt(2*k)
    return c*g(r+1)*g(s+1)

def numeric(l,m,nodes=300):
    t,w=leggauss(nodes)
    x=(t+1)/2; weights=w/2
    a=lpmv(m,l,x); b=lpmv(m,l+1,x)
    z=0.5*(math.log((2*l+1)*(2*l+3)/4)+gammaln(l-m+1)+gammaln(l-m+2)-gammaln(l+m+1)-gammaln(l+m+2))
    return float(np.dot(weights,a*b)*math.exp(z))

def run():
    count=0; worst=0.
    for l in range(0,31):
        arr=[]
        for m in range(l+1):
            p=predicted(l,m)
            q=numeric(l,m,nodes=130)
            err=abs(p-q)
            worst=max(worst,err)
            assert err<3e-10, (l,m,p,q,err)
            arr.append(p)
            count+=1
        assert abs(max(arr)-arr[-1])<1e-12
        if l:
            assert all(x < arr[-1] for x in arr[:-1])
        # Full spectral multiplicities: 2 for m=0, 4 each positive order through l,
        # and two eigenvalues 1/2 from m=+/- (l+1).
        eigs=[]
        for m,g in enumerate(arr):
            multiplicity=1 if m==0 else 2
            eigs += [0.5+g,0.5-g]*multiplicity
        eigs += [0.5,0.5]
        assert len(eigs)==4*l+4
        assert abs(sum(eigs)-(2*l+2)) < 5e-10
        assert min(eigs)>0 and max(eigs)<1
    for l in (50,100,400):
        exact=predicted(l,l)
        asym=1/math.sqrt(2*math.pi)*(1+1/(8*l))
        assert abs(exact-asym)<0.01/l, (l,exact,asym)
        count+=1
    print('ADJACENT_HEMISPHERE_SLEPIAN_PASS checked_pairs=%d max_quadrature_error=%.3g asymptotic_cases=3' % (count,worst))

if __name__=='__main__': run()
