"""Standalone numerical and discrete Fourier checks for periodic-geodesic cubature."""
from __future__ import annotations
import cmath
from itertools import product
from math import gcd, pi, sqrt, floor

def loop_fourier(delta, slope, phase):
    p,q=slope
    if delta[0]*p+delta[1]*q:
        return 0j
    return cmath.exp(1j*(delta[0]*phase[0]+delta[1]*phase[1]))

def direction_family(slope, L):
    p,q=slope
    assert gcd(abs(p),abs(q))==1
    # A Bézout transversal: coordinate choice with phase eta=q*x-p*y.
    if q:
        return [(2*pi*j/(L*q), 0.) for j in range(L)]
    return [(0., -2*pi*j/(L*p)) for j in range(L)]

def gram_error(N, families):
    freq=list(product(range(-N,N+1), repeat=2))
    m=0.
    for u in freq:
        for v in freq:
            d=(u[0]-v[0],u[1]-v[1])
            val=0j
            for slope, phase_list, family_weight in families:
                val+=family_weight*sum(loop_fourier(d,slope,a) for a in phase_list)/len(phase_list)
            m=max(m,abs(val-(1. if u==v else 0.)))
    return m

def threshold(N,v):
    return 1+(2*N)//max(abs(v[0]),abs(v[1]))

def run():
    configs=0; max_error=0.
    slopes=[(1,0),(0,1),(1,1),(1,-1),(1,2),(2,1),(2,3),(3,2)]
    for N in (1,2,3):
        for v in slopes:
            for L in (threshold(N,v), threshold(N,v)+1):
                error=gram_error(N,[(v,direction_family(v,L),1.)])
                assert error<1e-12,(N,v,L,error)
                max_error=max(max_error,error)
                configs+=1
            L=threshold(N,v)
            assert L*sqrt(v[0]**2+v[1]**2)>=2*N+1-1e-14
        choices=[(1,0),(1,1),(2,3)]
        mix=[(v,direction_family(v,threshold(N,v)),w) for v,w in zip(choices,(0.2,0.3,0.5))]
        err=gram_error(N,mix)
        assert err<1e-12,(N,err)
        max_error=max(err,max_error)
        configs+=1
    for N in range(1,50):
        for p in range(-2*N-3,2*N+4):
            for q in range(-2*N-3,2*N+4):
                if gcd(abs(p),abs(q))!=1: continue
                m=max(abs(p),abs(q))
                l=threshold(N,(p,q))
                assert l*m>=2*N+1
                if l*sqrt(p*p+q*q)<2*N+1+1e-10:
                    assert (p==0 and abs(q)==1) or (q==0 and abs(p)==1)
    print('PASS',configs,'independent Gram examples; maximum deviation',max_error)
    print('PASS sharp lattice length inequalities and equality classifications for N=1,...,49')

if __name__=='__main__':run()
