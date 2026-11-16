#!/usr/bin/env python3
"""Independent full Gram quadrature, generalized eigenvalues, and thin-slab check."""
from itertools import combinations_with_replacement
from math import comb
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.special import beta, betainc, poch
from mpmath import mp

def six_sector(d,a):
    q=(d+1)/2
    def J(k,r):
        return beta(k+.5,q+r)*betainc(k+.5,q+r,a*a)
    def F(k,r):
        return J(k,r)/beta(k+.5,q+r)
    m1=1/(d+2)
    m2=3/((d+2)*(d+4))
    S=np.array([[1.,m1],[m1,m2]])
    C=np.array([[J(0,0)/beta(.5,q),J(1,0)/beta(.5,q)],
                [J(1,0)/beta(.5,q),J(2,0)/beta(.5,q)]])
    even=eigh(C,S,eigvals_only=True)
    return np.sort(np.array([*even,F(1,0),*([F(1,1)]*(d-1)),
                               *([F(0,1)]*(d-1)),*([F(0,2)]*(d*(d-1)//2))]))

def full_quadrature(d,a):
    E=[tuple([0]*d)]
    for degree in (1,2):
        for inds in combinations_with_replacement(range(d),degree):
            e=[0]*d
            for i in inds:e[i]+=1
            E.append(tuple(e))
    q=(d+1)/2
    cache={}
    def moment(exp, cutoff):
        if any(x%2 for x in exp):return 0.
        key=(exp,cutoff)
        if key not in cache:
            k=[x//2 for x in exp]
            K=sum(k[1:])
            c=(2/beta(.5,q))*np.prod([poch(.5,x) for x in k[1:]])/poch(q,K)
            it=quad(lambda z: z**(2*k[0])*(1-z*z)**(q-1+K),0,cutoff,epsabs=2e-13,epsrel=2e-13)[0]
            cache[key]=c*it
        return cache[key]
    G=np.array([[moment(tuple(x+y for x,y in zip(e,f)),1.) for f in E] for e in E])
    H=np.array([[moment(tuple(x+y for x,y in zip(e,f)),a) for f in E] for e in E])
    assert np.linalg.eigvalsh(G).min()>0
    return np.sort(eigh(H,G,eigvals_only=True))

checks=0
for d in [2,3,4,5,8,10]:
    for a in [.07,.23,.51,.8]:
        r=six_sector(d,a)
        s=full_quadrature(d,a)
        err=np.max(np.abs(r-s))
        assert err<2e-10,(d,a,err,r,s)
        checks+=1
print('PASS:',checks,'independent full-monomial quadratures agree with the predicted entire spectrum; dimension 2–10')
mp.dps=80
for d in (2,3,8):
 q=mp.mpf(d+1)/2
 b=mp.beta(mp.mpf(1)/2,q)
 a=mp.mpf('0.0001')
 M=[mp.betainc(mp.mpf('0.5')+j,q,0,a*a,regularized=False)/b for j in (0,1,2)]
 m1=mp.mpf(1)/(d+2)
 m2=mp.mpf(3)/((d+2)*(d+4))
 detS=m2-m1*m1
 h=m2*M[0]+M[2]-2*m1*M[1]
 detC=M[0]*M[2]-M[1]*M[1]
 eplus=(h+mp.sqrt(h*h-4*detS*detC))/(2*detS)
 eminus=detC/(detS*eplus)
 ratio=eplus/eminus
 predicted=mp.mpf(405)/(8*(d+1)*(d+4))*a**(-4)
 assert abs(ratio/predicted-1)<mp.mpf('1e-6'),(d,ratio,predicted)
print('PASS: 80-digit thin-slab condition-number constant for dimensions 2, 3, and 8')
