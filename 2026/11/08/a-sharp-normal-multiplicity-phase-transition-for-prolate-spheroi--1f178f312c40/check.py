#!/usr/bin/env python3
"""Reproducibility checks for uniform-point normal multiplicity of a prolate spheroid.

Requires NumPy and SciPy. All random sampling seeds are explicit.
The simulation and numerical integrations are checks, not substitutes for the proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def probability_formula(r):
    """Closed form for probability of four normals, semiaxes (1,1,r)."""
    if r <= 1:
        if r == 1:
            return 0.0
        raise ValueError('prolate requires r>=1')
    t = r*r
    main = 8*(t-1)**3/(35*t)
    if t <= 2:
        return main
    # For large r the two terms nearly cancel: use this only at moderate r.
    correction = (t**1.5*(t-2)**2.5*(8*t*t+40*t+77) /
                  (35*math.sqrt(t-1)*(t+1)**3.5))
    return main-correction


def probability_quadrature(r):
    """Independent one-dimensional volume integral, no closed-form primitive."""
    t=r*r
    k=t-1
    if t <= 2+1e-12:
        return 3*k*k*k/t*quad(lambda v:(1-v**(2/3))**3,0,1,epsabs=1e-12)[0]/2
    # positive height integral in normalized (rho,z/r) sphere coordinates:
    # area element p normalized is 3 rho drho dv in upper half space.
    def caustic(u):
        return k/t*max(0.,1-(u/k)**(2/3))**1.5
    def ellipse(u):return math.sqrt(max(0.,1-u*u))
    q = brentq(lambda u:caustic(u)-ellipse(u),1e-12,min(1.,k)-1e-12)
    return 1-3*quad(lambda u:u*(ellipse(u)-caustic(u)),0,q,epsabs=5e-12,epsrel=5e-12)[0]


def point_four_normals(r,rho,z):
    """Directly use the caustic criterion only for Monte Carlo comparison."""
    k=r*r-1
    return ((rho/k)**(2/3)+(r*abs(z)/k)**(2/3))<1


def number_normals_by_meridian_stationarity(r,rho,z,grid=1024):
    """Independent normal-root count via signs of derivative of distance squared.

    For a point with positive cylindrical radius rho, meridian boundary points
    have coordinates (sin theta, r cos theta); stationary normal equation:
    rho*cos(theta) - r*z*sin(theta) - (r*r-1)*sin(theta)*cos(theta) = 0.
    All other azimuths are excluded by orthogonality to rotational tangent.
    """
    t = np.arange(grid,dtype=float)*(2*math.pi/grid)
    st,ct=np.sin(t),np.cos(t)
    f = rho*ct-r*z*st-(r*r-1)*st*ct
    # Generic interior sampled points produce no exact double zeros.
    return int(np.count_nonzero(f * np.roll(f,-1)<0))


def main():
    rng=np.random.default_rng(602714)
    rs=[1.05,1.2,math.sqrt(2),1.45,1.8,2.7,5,9]
    for r in rs:
        a,b=probability_formula(r),probability_quadrature(r)
        assert abs(a-b)<6e-9,(r,a,b)
        # Uniform ball: radius U^(1/3), direction normalized Gaussian;
        # stretch only the third coordinate by r.
        n=72000
        p=rng.normal(size=(n,3));p/=np.linalg.norm(p,axis=1)[:,None]
        p*=rng.random(n)[:,None]**(1/3)
        rho=np.hypot(p[:,0],p[:,1]);z=r*p[:,2]
        indicators=(rho/(r*r-1))**(2/3)+(r*np.abs(z)/(r*r-1))**(2/3)<1
        simulation=indicators.mean()
        stdev=math.sqrt(max(a*(1-a),0)/n)
        assert abs(simulation-a)<6.2*stdev+0.004,(r,simulation,a,stdev)
        # Check caustic-based classification against roots of the normal
        # stationary equation for independently selected points.
        ix=rng.integers(0,n,size=180)
        for j in ix:
            roots=number_normals_by_meridian_stationarity(r,rho[j],z[j],grid=1536)
            assert roots in (2,4)
            assert (roots==4)==bool(indicators[j]),(r,rho[j],z[j],roots)
    assert probability_formula(1)==0
    assert abs(probability_formula(math.sqrt(2))-4/35)<2e-14
    for r in [8,16,32,64]:
        err=1-probability_quadrature(r)
        assert 11 <err*r**4<16,(r,err*r**4)
    print('SPHEROID_NORMAL_COUNT_VOLUME_LAW_OK',len(rs)*72000,'sampled points',len(rs)*180,'normal root tests')

if __name__=='__main__': main()
