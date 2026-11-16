"""Finite consistency tests for the two-circle reproducing-kernel zero cloud.

These tests do not establish the infinite zero-count or equidistribution theorem.
Only Python's standard library is needed.
"""
import cmath
import math


def coeff(a, n, N):
    return 1.0/(1.0+a**(n-N))


def kernel(a, N, z, terms=250):
    return sum(coeff(a,n,N)*z**n for n in range(terms))


def bilateral(a, z, cutoff=160):
    return sum(z**j/(1+a**j) for j in range(-cutoff,cutoff+1))


def qproduct(a, z, terms=160):
    P = 0.5+0j
    for k in range(terms):
        ak=a**k
        P *= (1-a*ak)**2 * (1+z*ak)*(1+a*ak/z) / ((1+a*ak)**2*(1-z*ak)*(1-a*ak/z))
    return P


def winding(a, N, radius, samples=8192):
    """Numerical winding on a circle; illustrative, not certified."""
    initial = kernel(a,N,radius)
    prev = cmath.phase(initial)
    total=0.0
    minimum = abs(initial)
    for j in range(1,samples+1):
        z = radius*cmath.exp(2j*math.pi*j/samples)
        v = kernel(a,N,z)
        minimum=min(minimum,abs(v))
        phase=cmath.phase(v)
        diff=(phase-prev+math.pi)%(2*math.pi)-math.pi
        total+=diff
        prev=phase
    return round(total/(2*math.pi)),minimum,abs(total/(2*math.pi)-round(total/(2*math.pi)))


def main():
    num=0
    for a in (0.2,0.35,0.5):
        for z in (complex((a+1)/2,0.03), complex(-math.sqrt(a),0.02)):
            # Choose argument in open annulus.
            if not (a<abs(z)<1):
                continue
            B=bilateral(a,z)
            Q=qproduct(a,z)
            assert abs(B-Q) < 2e-8*max(1,abs(Q)), (a,z,B,Q)
            num+=1
        for N in (3,5,9):
            r0=(a**N+a)/(a**N+1)
            ratios=[coeff(a,n-1,N)/coeff(a,n,N) for n in range(1,N+25)]
            assert abs(ratios[0]-r0)<1e-10
            assert min(ratios)>=r0-1e-11
            num+=1
    for a,r,Ns in ((0.2,0.6,(5,10,20)), (0.35,0.675,(10,15,20)), (0.5,0.75,(30,40))):
        for N in Ns:
            w,minval,err=winding(a,N,r)
            assert w==N and err<1e-6, (a,r,N,w,minval,err)
            num+=1
    print(f"PASS: {num} finite checks (bilateral identity, coefficient ratios, and sampled winding).")

if __name__=='__main__':
    main()
