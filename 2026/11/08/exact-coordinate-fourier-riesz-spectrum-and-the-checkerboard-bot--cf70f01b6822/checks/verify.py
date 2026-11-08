#!/usr/bin/env python3
"""Direct character-Gram check for the three-factor Segre Fourier frame."""
from itertools import product
from math import sqrt
import numpy as np


def mult(x,y,q):
    if q!=4:return (x*y)%q
    z=0
    for i in range(2):
        for j in range(2):
            if (x>>i)&1 and (y>>j)&1:z^=1<<(i+j)
    if z&8:z^=14
    if z&4:z^=7
    return z


def analyze(q):
    elt=range(q); nv=[(a,b) for a in elt for b in elt if (a,b)!=(0,0)]
    X=set()
    for u,v,w in product(nv,repeat=3):
        X.add(tuple(mult(mult(u[i],v[j],q),w[k],q) for i in range(2) for j in range(2) for k in range(2)))
    X.add((0,)*8)
    W=len(X)
    assert W==1+(q-1)*(q+1)**3
    C=np.array(sorted(X),dtype=np.int64)
    labels=[None]+[(i,t) for i in range(8) for t in range(1,q)]
    B=np.ones((len(labels),W),dtype=complex)
    for row,label in enumerate(labels[1:],1):
        i,t=label
        if q==4:
            exponent=np.array([0 if mult(t,int(x),q) in (0,1) else 1 for x in C[:,i]])
            B[row,:]=1-2*exponent
        else:
            B[row,:]=np.exp((2j*np.pi/q)*t*C[:,i])
    gram=B@B.conj().T/W
    direct=np.linalg.eigvalsh(gram)
    D=q**3+2*q**2-2
    a=2*(q*q-1)/D
    mu0=(12*q**3-10*q*q-17*q+16)/D
    mu1=q*(2*q-1)**2/D
    mu2=q*(2*q-1)/D
    mu3=q/D
    h=a*sqrt(8*(q-1))
    rad=sqrt((mu0-1)**2+4*h*h)
    Lp=(1+mu0+rad)/2; Lm=(1+mu0-rad)/2
    expected=[Lp,Lm]+[mu1]*3+[mu2]*3+[mu3]
    if q>=3:expected += [1-a]*(8*(q-2))
    expected=np.array(sorted(expected))
    assert len(direct)==len(expected)
    assert np.max(np.abs(direct-expected))<1e-8,(q,direct,expected)
    checkerboard=np.array([(-1)**sum(map(int,f'{i:03b}')) for i in range(8)],dtype=float)
    v=np.zeros(len(labels),complex)
    for idx,(i,t) in enumerate(labels[1:],1):v[idx]=checkerboard[i]/sqrt(8*(q-1))
    assert np.max(abs(gram@v-mu3*v))<1e-9
    assert min(direct)>0
    print(q,'points',W,'columns',len(labels),'smallest',round(direct[0],10),'largest',round(direct[-1],10),
         'condition_sq',round(direct[-1]/direct[0],10))

if __name__=='__main__':
    for q in (2,3,4,5): analyze(q)
    print('SEGRE_COORDINATE_FOURIER_RIESZ_PASS')
