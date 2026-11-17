#!/usr/bin/env python3
"""Independent finite-case checks for degree-one Fourier sampling on Hamming balls.
Requires Python 3 and NumPy; uses unnormalized Fourier characters and uniform-ball Gram normalization.
"""
from fractions import Fraction
from itertools import product
from math import comb, cos, sin, pi, sqrt, erf, exp
import numpy as np


def moments_exact(n, q, r):
    counts=[comb(n,j)*(q-1)**j for j in range(r+1)]
    N=sum(counts)
    e=Fraction(sum(j*x for j,x in enumerate(counts)),N)
    e2=Fraction(sum(j*j*x for j,x in enumerate(counts)),N)
    return e,e2-e*e


def levels(n,q,r):
    e,v=moments_exact(n,q,r)
    p1=e/n
    p2=(v+e*e-e)/(n*(n-1))
    b=1-Fraction(q,q-1)*p1
    c=1-2*Fraction(q,q-1)*p1+Fraction(q*q,(q-1)**2)*p2
    color=1-b
    site=1+(q-2)*b-(q-1)*c
    m=(n*(q-1)-q*float(e))/sqrt(n*(q-1))
    rv=q*q*float(v)/(n*(q-1))
    trace=1+m*m+rv
    discriminant=sqrt((1-m*m-rv)**2+4*m*m)
    hi=(trace+discriminant)/2
    low=rv/hi
    return [float(color)]*(n*(q-2))+[float(site)]*(n-1)+[low,hi]


def group_char(a,h,mods):
    ang=2*pi*sum(ai*hi/m for ai,hi,m in zip(a,h,mods))
    return complex(cos(ang),sin(ang))


def direct_gram_eigen(n,mods,r):
    alphabet=list(product(*[range(m) for m in mods]))
    zero=tuple(0 for m in mods)
    freq=[(None,zero)]
    for i in range(n):
        for a in alphabet:
            if a!=zero:freq.append((i,a))
    rows=[x for x in product(alphabet,repeat=n) if sum(v!=zero for v in x)<=r]
    mat=np.empty((len(rows),len(freq)),dtype=complex)
    for i,x in enumerate(rows):
        mat[i,0]=1
        for j,(axis,a) in enumerate(freq[1:],1):
            mat[i,j]=group_char(x[axis],a,mods)
    gram=mat.conj().T@mat/len(rows)
    return np.linalg.eigvalsh(gram)


def boundary_distribution(n,q,r):
    # Exact unnormalized binomial-weight ratios, avoiding large binomial coefficients.
    w=1.0; terms=[(0,w)]
    for j in range(r,0,-1):
        w*=j/((n-j+1)*(q-1))
        if w==0.0:break
        terms.append((r-j+1,w))
    z=sum(w for _,w in terms)
    d=sum(t*w for t,w in terms)/z
    var=sum((t-d)**2*w for t,w in terms)/z
    return r-d,var


def approx_cond(n,q,r):
    e,var=boundary_distribution(n,q,r)
    p1=e/n
    p2=(var+e*e-e)/(n*(n-1))
    col=q*p1/(q-1)
    site=q*q*(p1-p2)/(q-1)
    m=(n*(q-1)-q*e)/sqrt(n*(q-1))
    rv=q*q*var/(n*(q-1))
    hi=(1+m*m+rv+sqrt((1-m*m-rv)**2+4*m*m))/2
    lo=rv/hi
    return sqrt(max(hi,col,site)/min(lo,col,site))


def window_limit(s):
    cdf=(1+erf(s/sqrt(2)))/2
    ell=exp(-s*s/2)/(sqrt(2*pi)*cdf)
    v=1-s*ell
    hi=(1+v+sqrt((1-v)**2+4*ell*ell))/2
    lo=(1+v-sqrt((1-v)**2+4*ell*ell))/2
    return sqrt(hi/lo)


def run():
    cases=0
    for mods in [(3,),(4,),(2,2),(5,)]:
        q=1
        for x in mods:q*=x
        for n in range(2,5):
            for r in range(1,n+1):
                predicted=sorted(levels(n,q,r))
                observed=direct_gram_eigen(n,mods,r)
                error=max(abs(x-y) for x,y in zip(predicted,observed))
                assert error<2e-12,(mods,n,r,error)
                assert observed[0]>1e-12,(mods,n,r,observed[0])
                cases+=1
    for q in (3,4,5):
        for a in (.2,.4):
            if a>=(q-1)/q:continue
            C=q-1-q*a
            predicted=C**3/(q*(q-1)*sqrt(a*(1-a)))
            values=[approx_cond(n,q,round(n*a))/n**1.5 for n in (1000,3000,10000)]
            assert abs(values[-1]/predicted-1)<.015,(q,a,values,predicted)
        for s in (-1,0,1):
            n=15000
            radius=round(n*(q-1)/q + s*sqrt(n*(q-1))/q)
            observed=approx_cond(n,q,radius)
            predicted=window_limit(s)
            assert abs(observed/predicted-1)<.075,(q,s,observed,predicted)
    print('HAMMING_BALL_FIRST_BAND_CHECKS_PASS finite_cases=%d'%cases)

if __name__=='__main__':run()
