"""Numerical checks for near-diameter pair distances on constant-curvature disks.

Requires numpy; the fixed-order product quadrature is not a mathematical proof.
"""
from math import sinh, cosh, tanh, pi, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss


def coefficient(radius, curvature_scale=1.0):
    """Density-normalized leading probability constant, nonnegative scale."""
    if curvature_scale == 0:
        return 32/(15*pi*radius**2.5)
    z = curvature_scale*radius
    return (8/(15*pi))*curvature_scale**2.5 * (cosh(z/2)/sinh(z/2))**2 / sqrt(tanh(z))


def rare_quadrature(radius, eps, curvature_scale=1.0, order=120):
    """Exact polar-coordinate integration over radial boundary deficits.

    The angular probability is integrated analytically, not sampled.
    Return rare-event mass and the conditional means of rescaled radial
    deficits and squared antipodal angular defect.
    """
    assert radius > 0 and 0 < eps < radius and curvature_scale >= 0
    x,w = leggauss(order)
    x=(x+1)/2; w=w/2
    u=eps*x[:,None]
    v=(eps-u)*x[None,:]
    r=radius-u; s=radius-v
    if curvature_scale:
        k=curvature_scale
        density_r=k*np.sinh(k*r)/(np.cosh(k*radius)-1)
        density_s=k*np.sinh(k*s)/(np.cosh(k*radius)-1)
        numerator=np.cosh(k*(r+s))-np.cosh(k*(2*radius-eps))
        denominator=np.sinh(k*r)*np.sinh(k*s)
        a=tanh(k*radius)/(4*k)
    else:
        density_r=2*r/radius**2
        density_s=2*s/radius**2
        numerator=(r+s)**2-(2*radius-eps)**2
        denominator=2*r*s
        a=radius/4
    q=np.clip(numerator/denominator,0,2)
    w_max=np.arccos(1-q)
    weight=eps**2*w[:,None]*w[None,:]*(1-x[:,None])*density_r*density_s*w_max/pi
    total=float(weight.sum())
    means=[float((weight*mark).sum()/total)
           for mark in (u/eps,v/eps,a*w_max**2/(3*eps))]
    return total,means


def test():
    for k in (0.,1.):
        for R in (0.5,1.,2.5):
            C=coefficient(R,k)
            for eps in (0.04,0.02,0.01,0.005):
                mass,means=rare_quadrature(R,eps,k)
                ratio=mass/(C*eps**2.5)
                print('curvature_scale=',k,'radius=',R,'eps=',eps,'ratio=',ratio,'conditional_means=',means)
                assert 0.80 < ratio < 1.02
                assert max(abs(means[i]-target) for i,target in enumerate((2/7,2/7,1/7))) < 0.04
    for R in (0.2,0.8,2.):
        vals=[coefficient(R,k) for k in (0.,0.1,0.5,1.,3.)]
        print('strict curvature ordering',R,vals)
        assert all(vals[i]<vals[i+1] for i in range(4))
    print('HYPERBOLIC_DISK_DIAMETER_RIGIDITY_OK')

if __name__ == '__main__':
    test()
