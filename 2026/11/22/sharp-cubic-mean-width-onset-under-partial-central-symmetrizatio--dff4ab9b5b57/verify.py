"""Independent numerical checks for the five-dimensional partial-symmetrization mean-width law.

Requires numpy for the independently sampled symmetric matrices; the angular
quadrature and algebraic checks use only the Python standard library.
"""
from math import sqrt, sin, cos, atan, pi, isclose


def exact_mean(t):
    assert 0 <= t <= 1
    u = 2 * t - 1
    return 9 * sqrt(3) / 16 + (sqrt(3) * u**3 / (4 * (3 + u*u)) if t > .5 else 0)


def theta_width(theta, t):
    """Direct support function, not the proposed piecewise integrated formula."""
    z = sqrt(2 / 3)
    L = z * cos(theta)
    l = z * cos(theta + 2*pi/3)
    return (max(L, -t*l) + max(-l, t*L)) / sqrt(2)


def simpson(f, lo, hi, n=6000):
    assert n % 2 == 0
    h = (hi-lo)/n
    s = f(lo) + f(hi)
    for i in range(1,n):
        s += (4 if i % 2 else 2) * f(lo+i*h)
    return s*h/3


def run():
    for t in [0, .2, .49, .5, .501, .55, .7, .85, 1]:
        v = simpson(lambda q: theta_width(q,t)*1.5*sin(3*q),0,pi/3)
        ex = exact_mean(t)
        print('angular integral',t,'numeric=',format(v,'.14f'),'formula=',format(ex,'.14f'))
        assert abs(v-ex) < 2e-8
    # Exact threshold characterization from trace-one PSD matrices.
    for t in [0,.3,.5,.7,1]:
        min_eigenvalue = (1-2*t)/3
        assert (min_eigenvalue>=0) == (t<=.5)
    # This test independently samples the full 5D unit-direction sphere,
    # builds symmetric matrices in an orthonormal Frobenius basis, and
    # evaluates their extremal eigenvalues without using angular data.
    try:
        import numpy as np
    except ImportError:
        print('Optional NumPy Monte Carlo unavailable; exact-quadrature checks passed')
        return
    rng = np.random.default_rng(20261120)
    N=160000
    g=rng.standard_normal((N,5))
    g/=np.linalg.norm(g,axis=1)[:,None]
    A=np.zeros((N,3,3))
    A[:,0,0]=g[:,0]/sqrt(2)+g[:,1]/sqrt(6)
    A[:,1,1]=-g[:,0]/sqrt(2)+g[:,1]/sqrt(6)
    A[:,2,2]=-2*g[:,1]/sqrt(6)
    for i,(a,b) in enumerate([(0,1),(0,2),(1,2)],start=2):
        A[:,a,b]=A[:,b,a]=g[:,i]/sqrt(2)
    evals=np.linalg.eigvalsh(A)
    lo=evals[:,0];hi=evals[:,-1]
    assert float(np.max(np.abs(np.einsum('nij,nij->n',A,A)-1)))<1e-12
    for t in [0,.4,.5,.55,.7,.85,1]:
        observed=float(np.mean((np.maximum(hi,-t*lo)+np.maximum(-lo,t*hi))/sqrt(2)))
        target=exact_mean(t)
        print('matrix Monte Carlo',t,observed,target)
        assert abs(observed-target)<.0025
    print('PASS: angular quadrature, endpoint threshold and independent 5D matrix sampling')

if __name__=='__main__':
    run()
