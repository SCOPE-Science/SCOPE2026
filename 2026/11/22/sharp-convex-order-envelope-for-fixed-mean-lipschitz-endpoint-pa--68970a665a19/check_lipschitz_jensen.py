#!/usr/bin/env python3
"""Independent arithmetic and sampled checks of the stated Lipschitz Jensen envelopes.
The complete proof uses the chain rule and convex-order inequalities, not tests.
No internet, nonstandard imports, or source material are required.
"""
from fractions import Fraction as F
import math, random


def bounds(L, m, phi, integral_phi):
    q = 1 - 1 / L
    if q == 0:
        assert m == 0.5
        return integral_phi, integral_phi
    r = (m - 1 / (2 * L)) / q
    return (integral_phi/L + q*phi(r),
            integral_phi/L + q*((1-r)*phi(0)+r*phi(1)))


def extremal_segments(L, r, kind):
    q = 1 - 1/L
    if kind == 'minimum':
        return [(F(0), r/L, L, F(0)),
                (r/L, r/L+q, F(0), r),
                (r/L+q, F(1), L, -L*q)]
    a = q*(1-r)
    return [(F(0), a, F(0), F(0)),
            (a, a+1/L, L, -L*a),
            (a+1/L, F(1), F(0), F(1))]


def moments(segs):
    a = F(0); b = F(0)
    for lo,hi,s,c in segs:
        a += s*(hi*hi-lo*lo)/2+c*(hi-lo)
        b += s*s*(hi**3-lo**3)/3+s*c*(hi*hi-lo*lo)+c*c*(hi-lo)
    return a, b


def simpson(fn, n=4000):
    h=1/n
    return h/3*(fn(0)+fn(1)+4*sum(fn(i*h) for i in range(1,n,2)) + 2*sum(fn(i*h) for i in range(2,n,2)))


def sample_f(L,k,amp):
    return lambda x: max(0.,min(1.,x+amp*math.sin(2*math.pi*k*x)))


def run():
    exact=0; sampled=0
    for L in [F(2),F(3),F(5)]:
        for r in [F(0),F(1,3),F(1,2),F(2,3),F(1)]:
            q=1-1/L
            m=1/(2*L)+q*r
            lo=1/(3*L)+q*r*r
            hi=1/(3*L)+q*r
            for kind,target in [('minimum',lo),('maximum',hi)]:
                segs=extremal_segments(L,r,kind)
                assert all(a<=b for a,b,s,c in segs)
                assert segs[0][0]==0 and segs[-1][1]==1
                assert all(0<=s<=L for a,b,s,c in segs)
                assert moments(segs)==(m,target), (L,r,kind,moments(segs),target)
                exact+=1
    rng=random.Random(20261120)
    funcs=[(lambda x:x,1.0)]
    for L in [1.25,1.5,2.5,4.,8.]:
        for _ in range(24):
            k=rng.randint(1,6)
            amp=(L-1)/(2*math.pi*k)*rng.uniform(-1,1)
            funcs.append((sample_f(L,k,amp),L))
    for f,L in funcs:
        m=simpson(f)
        if L>1:
            assert 1/(2*L)-1e-8 <=m<=1-1/(2*L)+1e-8
        for phi,intphi in [(lambda t:t*t,1/3),
                            (math.exp, math.e-1),
                            (lambda t:abs(t-0.3), (0.3**2+(0.7)**2)/2)]:
            lo,hi=bounds(L,m,phi,intphi)
            actual=simpson(lambda x:phi(f(x)))
            assert lo-1e-6 <=actual<=hi+1e-6, (L,m,lo,actual,hi)
            sampled+=1
    print('PASS exact polynomial extremal identities:',exact)
    print('PASS numerical convex-envelope inequalities:',sampled)

if __name__=='__main__':run()
