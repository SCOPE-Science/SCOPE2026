"""Reproduce independent geometric and integral tests for a boundary-chord midpoint theorem.
Requires NumPy and SciPy. The analytic proof is in RESULT.md; sampling is diagnostic.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.spatial import cKDTree


def ellipse_test(a=2., b=1., n=220_000, eps=0.001, seed=4217):
    rng = np.random.default_rng(seed)
    q = lambda t: np.sqrt(a*a*np.sin(t)**2+b*b*np.cos(t)**2)
    k = lambda t: a*b/q(t)**3
    perim = quad(lambda t: q(t), 0, 2*math.pi, epsabs=1e-12)[0]
    j = quad(lambda t: q(t)/np.sqrt(k(t)), 0, 2*math.pi, epsabs=1e-12)[0]
    hnorm = quad(lambda t: q(t)*np.sqrt(k(t)), 0, 2*math.pi, epsabs=1e-12)[0]
    coeff_uniform = 4*math.sqrt(2)*j/perim**2
    coeff_optimal = 4*math.sqrt(2)/hnorm
    bound = 4/math.sqrt(math.pi*perim)
    assert coeff_uniform > coeff_optimal > bound
    ts = np.linspace(0, 2*math.pi, 100_001)
    qs = q(ts)
    arc = np.concatenate(([0.], np.cumsum((qs[:-1]+qs[1:])*0.5*np.diff(ts))))
    arc *= perim/arc[-1]
    bt = np.linspace(0, 2*math.pi, 40000, endpoint=False)
    boundary = np.column_stack((a*np.cos(bt), b*np.sin(bt)))
    tree = cKDTree(boundary)
    print('ellipse perimeter',perim,'coefficients',coeff_uniform,coeff_optimal,'global_min',bound)
    for model in ('uniform', 'optimal'):
        weight = qs if model=='uniform' else np.sqrt(k(ts))*qs
        cum = np.concatenate(([0.], np.cumsum(0.5*(weight[:-1]+weight[1:])*np.diff(ts))))
        cum /= cum[-1]
        t1 = np.interp(rng.random(n),cum,ts)
        t2 = np.interp(rng.random(n),cum,ts)
        midpoint = np.column_stack((0.5*a*(np.cos(t1)+np.cos(t2)), 0.5*b*(np.sin(t1)+np.sin(t2))))
        dist,_ = tree.query(midpoint,workers=1)
        hits = dist<eps
        obs = hits.mean()
        coeff = coeff_uniform if model=='uniform' else coeff_optimal
        pred = coeff*math.sqrt(eps)
        se = math.sqrt(obs*(1-obs)/n)
        print('model',model,'observed',obs,'predicted',pred,'standard_error',se)
        assert abs(obs-pred)< 6*se + 0.012*pred
        s1=np.interp(t1[hits],ts,arc)
        s2=np.interp(t2[hits],ts,arc)
        hd=(s2-s1+perim/2)%perim-perim/2
        sm=(s1+hd/2)%perim
        tm=np.interp(sm,arc,ts)
        z=hd*np.sqrt(k(tm)/(8*eps))
        print('model',model,'conditional E[Z^2]',np.mean(z*z), 'P(Z>0)',np.mean(z>0))
        assert abs(np.mean(z*z)-1/3)<0.032
        assert abs(np.mean(z>0)-0.5)<0.03
    return coeff_uniform, coeff_optimal


def circle_exact_check():
    r=1.25
    c=2*math.sqrt(2)/(math.pi*math.sqrt(r))
    for e in (0.1,0.01,0.001):
        exact=2*math.acos(1-e/r)/math.pi
        ratio=exact/(c*math.sqrt(e))
        print('circle epsilon',e,'exact',exact,'ratio',ratio)
        assert abs(ratio-1)<0.01


if __name__=='__main__':
    circle_exact_check()
    ellipse_test()
    print('MIDPOINT_BOUNDARY_CHECKS_OK')
