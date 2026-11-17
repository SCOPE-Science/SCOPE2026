"""Finite consistency checks for the regular-polygon pedal contraction profile.

Only the accompanying analytic argument establishes the result for every
integer order and every interior point; these checks do not certify infinity.
Run with Python 3, numpy, and scipy: python verify_pedal.py.
"""
import math
import numpy as np
from scipy.special import eval_chebyt


def formula(n, r, phi):
    c = math.cos(math.pi / n)
    if r == 0:
        return c ** n
    s = math.cos(n * phi)
    return 2.0 ** (1-n) * r ** n * (eval_chebyt(n, c / r) + s) / math.sqrt(1 + r**(2*n) - 2*r**n*s)


def product(n, p):
    j = np.arange(n)
    vertices = np.exp(2j * np.pi * j / n)
    normals = np.exp(1j * (2*j+1) * np.pi / n)
    numer = np.prod(np.cos(np.pi / n)-np.real(p*np.conj(normals)))
    denom = np.prod(np.abs(vertices-p))
    return float(numer / denom)


def pedal_iterate(n, p):
    j = np.arange(n)
    initial = np.exp(2j * np.pi * j / n)
    vertices = initial.copy()
    for k in range(n):
        edges = np.roll(vertices, -1)-vertices
        assert np.all(np.abs(edges)>1.e-12)
        t = np.real((p-vertices)*np.conj(edges))/(np.abs(edges)**2)
        vertices = vertices+t*edges
    ratios = (np.roll(vertices,-1)-vertices)/(np.roll(initial,-1)-initial)
    assert np.max(np.abs(ratios-ratios[0])) < 3e-9
    return abs(ratios[0])


def main():
    checks=0
    rng=np.random.default_rng(16927)
    for n in list(range(3,18)) + [19,23,31]:
        c = math.cos(math.pi/n)
        assert abs(formula(n,0,0) - c**n) < 1e-14
        checks+=1
        for t in range(120):
            r=float(rng.uniform(.005,.98))
            phi=float(rng.uniform(-math.pi/n,math.pi/n))
            # Reject points outside the regular polygon.
            p=r*np.exp(1j*phi)
            j=np.arange(n)
            normals=np.exp(1j*(2*j+1)*np.pi/n)
            if np.min(c-np.real(p*np.conj(normals)))<=1e-6: continue
            a=formula(n,r,phi)
            b=product(n,p)
            assert abs(a-b) <= 2e-9*max(1.0,abs(a)),(n,r,phi,a,b)
            checks+=1
            if t<30:
                d=pedal_iterate(n,p)
                assert abs(a-d) <= 4e-9*max(1.0,abs(a)),(n,r,phi,a,d)
                checks+=1
        for r in [0.1*c,0.4*c,0.7*c,0.97*c]:
            samples=[formula(n,r,k*math.pi/(150*n)) for k in range(151)]
            assert all(x>y-1e-11 for x,y in zip(samples,samples[1:])),(n,r)
            # For high order and tiny radius, this positive difference is
            # below binary64 resolution; assert positivity of the stable
            # analytical gap rather than comparing rounded endpoints.
            if r**n > 1e-13:
                assert samples[0]>samples[-1]
            am=eval_chebyt(n,c/r)
            q=r**n
            vmax=2.**(1-n)*q*(am+1)/(1-q)
            vmin=2.**(1-n)*q*(am-1)/(1+q)
            gap=2.**(2-n)*q*(1+q*am)/(1-q*q)
            assert abs(samples[0]-vmax)<1e-10
            assert abs(samples[-1]-vmin)<1e-10
            assert abs(vmax-vmin-gap)<1e-10
            checks+=4
    print('PASS:',checks,'finite checks, including actual n-step pedal simulations')

if __name__=='__main__':
    main()
