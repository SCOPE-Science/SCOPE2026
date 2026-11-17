"""Reproducible checks for a curvature-weighted small-inradius law.
These checks do not replace the geometric proof or asymptotic estimates.
"""
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid


def radius_of_three(points):
    x,y,z=np.asarray(points)
    twice_area=abs(np.linalg.det(np.stack([y-x,z-x])))
    perimeter=sum(np.linalg.norm(a-b) for a,b in [(x,y),(y,z),(z,x)])
    return twice_area/perimeter


def ellipse_grid(a,b,n=180001):
    theta=np.linspace(0,2*math.pi,n)
    speed=np.hypot(a*np.sin(theta),b*np.cos(theta))
    arc=np.concatenate([[0.0], cumulative_trapezoid(speed,theta)])
    kappa=a*b/speed**3
    return theta, arc, kappa


def ellipse_point(s, theta, arc, a, b):
    th=np.interp(s%arc[-1],arc,theta)
    return np.array([a*np.cos(th),b*np.sin(th)])


def run():
    # Local uniform estimate, tested at different highly unequal gap sizes.
    a,b=2.0,1.0
    theta,arc,kappa=ellipse_grid(a,b)
    L=arc[-1]
    for sfrac in (.10,.35,.61):
        s=L*sfrac
        kap=np.interp(s,arc,kappa)
        for h in (.04,.016,.006):
            for q in (.25,2.0,5.0):
                u=h;v=h*q
                pts=[ellipse_point(s,theta,arc,a,b), ellipse_point(s+u,theta,arc,a,b),ellipse_point(s+u+v,theta,arc,a,b)]
                ratio=radius_of_three(pts)/(kap*u*v/4)
                # At small enough h the local ratio must approach 1.
                if h==.006:
                    assert abs(ratio-1)<.08, (sfrac,u,v,ratio)
    # Circle: exact three-gap formula and determinant inradius agree.
    for g1,g2 in ((.6,1.1),(.01,.14),(.30,.05),(2.5,1.2)):
        g3=2*math.pi-g1-g2
        pts=[np.array([1.0,0]),np.array([math.cos(g1),math.sin(g1)]),np.array([math.cos(g1+g2),math.sin(g1+g2)])]
        assert abs(radius_of_three(pts)-4*np.prod([math.sin(g/4) for g in (g1,g2,g3)]))<1e-13
    # The universal cusp coefficient recovers the known circle value.
    I_circle=(2*math.pi)*(1/(2*math.pi))**3
    assert abs(24*I_circle-6/math.pi**2)<1e-12
    # Explicit two-curvature density optimization via quadrature on an ellipse.
    f0=1/L
    I_uniform=np.trapezoid((f0**3/kappa)*np.gradient(arc,theta),theta)
    sqrtint=np.trapezoid(np.sqrt(kappa)*np.gradient(arc,theta),theta)
    fstar=np.sqrt(kappa)/sqrtint
    I_opt=np.trapezoid((fstar**3/kappa)*np.gradient(arc,theta),theta)
    assert I_opt < I_uniform
    assert abs(I_opt-1/sqrtint**2)<3e-8
    assert 24*I_uniform>12/(math.pi*L)
    print('SMALL_INRADIUS_CURVATURE_CHECKS_OK')
    print(f'ellipse perimeter={L:.9f}, uniform coefficient={24*I_uniform:.9f}, optimal coefficient={24*I_opt:.9f}')

if __name__=='__main__':
    run()
