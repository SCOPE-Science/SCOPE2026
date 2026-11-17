#!/usr/bin/env python3
"""Independent numerical checks for the normalized ellipse-circumcenter law.

Run: python check_circumcenter_astroid.py
Requires Python 3.10+, numpy 1.24+.
Finite checks corroborate, but never replace, the analytical proof.
"""
from fractions import Fraction
from math import factorial
import numpy as np


def exact_moment(p, q):
    if (p - q) % 4:
        return Fraction(0)
    r, s = sorted((p, q), reverse=True)
    k = (r - s) // 4
    total = Fraction(0)
    for t0 in range(s+1):
        for t1 in range(s-t0+1):
            for t2 in range(s-t0-t1+1):
                t3 = s-t0-t1-t2
                den = 1
                for t in (t0, t1, t2, t3):
                    den *= factorial(t)*factorial(t+k)
                total += Fraction(1, den)
    return Fraction(factorial(r)*factorial(s), 4**(r+s))*total


def direct_centers(angles, a, b):
    P = np.stack([a*np.cos(angles), b*np.sin(angles)], axis=-1)
    mat = 2*(P[:, 1:, :]-P[:, 0:1, :])
    val = np.sum(P**2, axis=-1)
    rhs = val[:, 1:]-val[:, 0:1]
    return np.linalg.solve(mat, rhs[..., None])[..., 0]


def trace_centers(angles, a, b):
    z = np.exp(1j*angles)
    W = z.sum(axis=1)+np.prod(np.conjugate(z),axis=1)
    delta = a*a-b*b
    return np.column_stack((delta/(4*a)*W.real, -delta/(4*b)*W.imag))


def main():
    assert exact_moment(1,0)==0
    assert exact_moment(2,0)==0
    assert exact_moment(4,0)==Fraction(3,32)
    assert exact_moment(2,2)==Fraction(7,64)
    assert exact_moment(1,1)==Fraction(1,4)
    rng = np.random.default_rng(20261111)
    angles = rng.uniform(-np.pi,np.pi,(700000,3))
    for a,b in ((2.,1.),(7.,2.),(1.25,1.)):
        center = direct_centers(angles[:20000],a,b)
        phase = trace_centers(angles[:20000],a,b)
        err = np.max(np.abs(center-phase))
        assert err < 2.e-6, (a,b,err)
    print('INDEPENDENT_CIRCUMCENTER_RECONSTRUCTION_OK')

    z = np.exp(1j*angles)
    W = z.sum(axis=1)+np.prod(np.conjugate(z),axis=1)
    X,Y=W.real/4,W.imag/4
    astroid = np.abs(X)**(2/3)+np.abs(Y)**(2/3)
    assert astroid.max() <= 1.+1.e-11
    assert np.mean(astroid>0.999) > 0
    print('SHARP_ASTROID_SUPPORT_BOUND_OK')

    for name,val,target,tol in (
        ('E_X2',np.mean(X*X),1/8,.0015),
        ('E_Y2',np.mean(Y*Y),1/8,.0015),
        ('E_X4',np.mean(X**4),27/512,.0015),
        ('E_Y4',np.mean(Y**4),27/512,.0015),
        ('E_X2Y2',np.mean(X*X*Y*Y),1/512,.0002),
        ('E_Z4',np.mean((W/4)**4),3/32,.0016),
        ('E_Z2ZBAR2',np.mean(np.abs(W/4)**4),7/64,.0015),
    ):
        assert abs(val-target)<tol,(name,val,target)
        print('%s observed=%s predicted=%s'%(name,val,target))
    print('MOMENT_IDENTITIES_OK')

    # Independent angular variables reproducing the law: the map from
    # (u,v,w) to (theta1,theta2,theta3) is a surjective torus homomorphism.
    u,v,w=rng.uniform(-np.pi,np.pi,(3,700000))
    X2=np.cos(u)*(np.cos(v)+np.cos(w))/2
    Y2=np.sin(u)*(np.cos(v)-np.cos(w))/2
    assert abs(np.mean(X*X)-np.mean(X2*X2))<.0015
    assert abs(np.mean(X*X*Y*Y)-np.mean(X2*X2*Y2*Y2))<.0002
    print('INDEPENDENT_ARCSINE_PARAMETERIZATION_OK')

    # Local Taylor expansions at the right-hand cusp.
    dirs = rng.normal(size=(120000,3))
    dirs /= np.linalg.norm(dirs,axis=1,keepdims=True)
    h = 0.004
    theta = h*dirs
    S = theta.sum(axis=1)
    zz = np.exp(1j*theta).sum(axis=1)+np.exp(-1j*S)
    loss = 1-zz.real/4
    quad = (np.sum(theta*theta,axis=1)+S*S)/8
    ordinate = zz.imag/4
    cubic = (S**3-np.sum(theta**3,axis=1))/24
    assert np.max(np.abs(loss-quad)) < 5e-10
    assert np.max(np.abs(ordinate-cubic)) < 5e-11
    print('CUSP_QUADRATIC_AND_CUBIC_EXPANSIONS_OK')

    large = rng.uniform(-np.pi,np.pi,(3000000,3))
    los = 1-(np.cos(large).sum(axis=1)+np.cos(large.sum(axis=1)))/4
    cusp_constant = 4*np.sqrt(2)/(3*np.pi**2)
    for t in (.08,.04,.02):
        p = np.mean(los<t)
        ratio = p/(cusp_constant*t**1.5)
        print('CUSP_TAIL t=%s empirical=%s ratio_to_leading=%s'%(t,p,ratio))
        assert abs(ratio-1)<.14
    print('CUSP_TAIL_CHECKS_OK')
    print('ELLIPSE_CIRCUMCENTER_ASTROID_CHECKS_OK')


if __name__ == '__main__':
    main()
