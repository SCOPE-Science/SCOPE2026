#!/usr/bin/env python3
"""Direct numerical checks for support-width formula of a square/regular-polygon free sum.
Uses only Python standard library, does not establish the universal theorem.
"""
from math import sin, cos, pi, sqrt, hypot
from random import Random

def width(q, phi, psi, t):
    # Unit normal = (cos(t)*(cos(phi),sin(phi)), sin(t)*(cos(psi),sin(psi))).
    r, s=cos(t),sin(t)
    # A is regular square at angles j*pi/2, B is regular q-gon at 2*pi*j/q.
    def h(poly,angle):
        return max(cos(angle-2*pi*j/poly) for j in range(poly))
    aplus=h(4,phi); aminus=h(4,phi+pi)
    bplus=h(q,psi); bminus=h(q,psi+pi)
    return max(r*aplus,s*bplus)+max(r*aminus,s*bminus)

def prediction(q):
    b=cos(pi/q) if q%2==0 else cos(pi/(2*q))
    return 2*b/sqrt(1+2*b*b)

def check():
    rng=Random(261110078)
    for q in range(3,31):
        theory=prediction(q)
        # Intended equality from square edge normals and B balanced directions (odd), or its edge normals (even).
        phi=pi/4
        psi=(pi/q if q%2==0 else pi/(2*q))
        # Careful: for q even, B edge normal at pi/q. For q odd, symmetric h(eta)=h(-eta) at pi/(2q).
        b=cos(pi/q) if q%2==0 else cos(pi/(2*q))
        a=cos(pi/4)
        t=__import__('math').atan2(a,b)
        eq=width(q,phi,psi,t)
        assert abs(eq-theory)<2e-12,(q,eq,theory)
        smallest=10
        for _ in range(4000):
            phi2=rng.uniform(0,2*pi);psi2=rng.uniform(0,2*pi);t2=rng.uniform(0,pi/2)
            w=width(q,phi2,psi2,t2)
            smallest=min(smallest,w)
            assert w >= theory-1e-11,(q,w,theory,phi2,psi2,t2)
        print('q=%2d parity=%s exact_target=%.12f nearest_random=%.12f equality_error=%.2g' % (q,'even' if q%2==0 else 'odd',theory,smallest,eq-theory))
    sq=prediction(5)**2
    exact=(20+2*sqrt(5))/19
    assert abs(sq-exact)<1e-14
    print('square-pentagon width squared:',sq,'radical:',exact)
if __name__=='__main__':check()
