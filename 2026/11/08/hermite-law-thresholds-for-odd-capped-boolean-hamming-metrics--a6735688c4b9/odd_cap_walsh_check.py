#!/usr/bin/env python3
"""Independent finite-dimensional checks for negative type of capped binary Hamming metrics.
Uses only the Python standard library for exact Krawtchouk coefficients; no external files.
"""
from math import comb, expm1, log, sqrt

def kvals(n,k,r):
    out = [1]
    s = n - 2*k
    for j in range(r-1):
        out.append((s*out[-1] - (n-j+1)*(out[-2] if j else 0))//(j+1))
    return out

def coeff(n,r,p,k):
    Q=kvals(n,k,r)
    return (r**p)*(-1.0 + sum(expm1(p*log(j/r))*Q[j] for j in range(1,r)))

def pthreshold(n,r):
    lo=0.;hi=1.
    if max(coeff(n,r,hi,k) for k in range(1,n+1))<0:
        while max(coeff(n,r,hi,k) for k in range(1,n+1))<0:hi*=2
    for _ in range(56):
        mid=(lo+hi)/2
        if max(coeff(n,r,mid,k) for k in range(1,n+1))>0:hi=mid
        else:lo=mid
    critical=max(range(1,n+1),key=lambda k:coeff(n,r,(lo+hi)/2,k))
    return (lo+hi)/2,critical

def hermite(j,t):
    a,b=1.,t
    if j==0:return a
    if j==1:return b
    for v in range(1,j):a,b=b,t*b-v*a
    return b

def maxHneg(j):
    # Robust grid search for approximate constants; theorem defines the global min exactly.
    a=0.;b=2*sqrt(j)
    best=(float('inf'),0.)
    for k in range(30001):
        x=a+(b-a)*k/30000
        z=hermite(j,x)
        if z<best[0]:best=z,x
    return -best[0],best[1]

def main():
    # Independent direct character enumeration for small cubes.
    for n in range(3,9):
        for r in range(3,min(7,n+1),2):
            for k in range(1,n+1):
                for j in range(r):
                    direct=sum((-1)**((x & ((1<<k)-1)).bit_count()) for x in range(1<<n) if x.bit_count()==j)
                    assert direct==kvals(n,k,r)[j],(n,r,j,k,direct)
    print('EXACT_KRAWTCHOUK_ENUMERATION_OK')
    for r in (3,5,7):
        m=(r-1)//2
        Hmin,loc=maxHneg(2*m)
        const=__import__('math').factorial(2*m)/(log(r/(r-1))*Hmin)
        print('cap',r,'predicted_constant',format(const,'.11g'),'Hermite_min_abs',format(Hmin,'.8g'),'min_location',format(loc,'.6g'))
        for n in (40,100,200,500,1000):
            if n<r:continue
            beta,k=pthreshold(n,r)
            print(' n',n,'rescaled',format(beta*n**m,'.11g'),'frequency',k,'center_scaled',format(abs(n-2*k)/sqrt(n),'.5g'))
    print('ODD_CAP_HAMMING_WALSH_CHECKS_OK')
if __name__=='__main__':main()
