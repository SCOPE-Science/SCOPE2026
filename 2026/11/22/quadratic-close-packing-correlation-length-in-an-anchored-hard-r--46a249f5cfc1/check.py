#!/usr/bin/env python3
"""Independent discretization checks for the anchored hard-rod transfer spectrum.

Requires numpy and scipy. Finite matrices are used only as tests; the proof
of the limiting law is analytic.
"""
import math
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs

def spectrum(ratio, cells=1400):
    eps=1.0/ratio
    h=1.0/cells
    ii=[]; jj=[]; ww=[]
    for i in range(cells):
        x=(i+0.5)*h
        first=max(0, int(math.floor((x-eps)/h)))
        last=min(cells, int(math.ceil((x+25*eps)/h)))
        for j in range(first,last):
            lo=max(j*h,x-eps)
            hi=(j+1)*h
            if lo>=hi:
                continue
            # Exact exponential jump mass in cell j, killed outside [0,1].
            mass=math.exp(-1.0-(lo-x)/eps)-math.exp(-1.0-(hi-x)/eps)
            ii.append(i);jj.append(j);ww.append(mass)
    P=csr_matrix((ww,(ii,jj)), shape=(cells,cells))
    vals=eigs(P,k=2,which='LM',tol=1e-10,maxiter=20000,return_eigenvectors=False)
    vals=sorted(vals,key=lambda z:-abs(z))
    assert all(abs(v.imag)<1e-7 for v in vals)
    assert vals[0].real>vals[1].real>0.0
    return (vals[0].real, vals[1].real)

def main():
    target=2.0/(3.0*math.pi**2)
    measured=[]
    for ratio in (5,10,20,30):
        u,v=spectrum(ratio)
        c=1.0/math.log(u/v)/(ratio**2)
        measured.append(c)
        print(f'ratio={ratio:>2}; mu1={u:.10f}; mu2={v:.10f}; scaled_xi={c:.9f}')
        assert c>target and c<0.11
    assert all(measured[i]>measured[i+1] for i in range(len(measured)-1))
    assert abs(measured[-1]-target)<0.007
    for m in (50,100,500):
        # Centered gamma return density with eps=1/sqrt(m).
        eps=1/math.sqrt(m)
        p=math.exp((m-1)*math.log(m)-m-math.lgamma(m))/eps
        assert abs(p-1/math.sqrt(2*math.pi))<0.01
    print('PASS: normalized discretization and exact return-density checks')
if __name__=='__main__': main()
