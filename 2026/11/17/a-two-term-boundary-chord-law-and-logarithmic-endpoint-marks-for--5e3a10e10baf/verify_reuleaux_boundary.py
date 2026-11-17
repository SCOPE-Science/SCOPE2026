"""Independent finite checks for two arclength-uniform endpoints on the unit Reuleaux triangle.

Run: python verify_reuleaux_boundary.py
Requires numpy and scipy. Finite diagnostics do not replace the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

L = math.pi / 3


def defect(u, v):
    return 8*math.sin(u/2)*math.sin(v/2)*math.cos((u+v)/2)


def distinct_arc_area(eps):
    h = 2*eps-eps*eps
    if not 0 < h < 1:
        raise ValueError('0<eps<1 required')
    u0 = brentq(lambda u: defect(u,L)-h, 1e-15, L)
    def upper(u):
        return math.asin(min(1.0, math.sin(u/2)+h/(4*math.sin(u/2))))-u/2
    integral = quad(upper,u0,L,epsabs=2e-13,epsrel=3e-12,limit=300)[0]
    return L*u0+integral


def exact_probability(eps):
    q = 2*math.asin((1-eps)/2)
    return (6*distinct_arc_area(eps)+3*(L-q)**2)/math.pi**2


def two_term_asymptotic(eps):
    return (6/math.pi**2)*eps*(math.log(1/eps)+1+math.log(4/3))


def random_pairs(n, seed=217):
    rng=np.random.default_rng(seed)
    a=rng.integers(0,3,n)
    b=rng.integers(0,3,n)
    u=rng.uniform(0,L,n)
    v=rng.uniform(0,L,n)
    # Independently construct the three arcs as circles centered at the three vertices.
    verts=np.array([[0.,0.],[1.,0.],[.5,math.sqrt(3)/2]])
    centers=verts
    start_angles=np.array([0,2*math.pi/3,4*math.pi/3])
    px=centers[a,0]+np.cos(start_angles[a]+u)
    py=centers[a,1]+np.sin(start_angles[a]+u)
    qx=centers[b,0]+np.cos(start_angles[b]+v)
    qy=centers[b,1]+np.sin(start_angles[b]+v)
    return np.hypot(px-qx,py-qy)


def run():
    for u,v in [(L/9,L/7),(L/2,L/2),(L/3,L/2),(L,L)]:
        x=(math.cos(u),math.sin(u))
        y=(1-math.cos(v),math.sin(v))
        direct=(x[0]-y[0])**2+(x[1]-y[1])**2
        assert abs((1-direct)-defect(u,v))<3e-14
    # Numerical ratio to full two-term asymptotic.
    for eps in [1e-2,1e-3,1e-4,1e-5,1e-6]:
        p=exact_probability(eps)
        approx=two_term_asymptotic(eps)
        rel=abs(p/approx-1)
        assert rel<0.004 if eps<=1e-2 else True
        print(f'eps={eps:.1e} exact={p:.12g} asympt={approx:.12g} rel={rel:.5g}')
    d=random_pairs(1_200_000)
    for eps in [0.1,0.03,0.01]:
        predicted=exact_probability(eps)
        observed=float(np.mean(d>1-eps))
        std=math.sqrt(predicted*(1-predicted)/len(d))
        print(f'MC eps={eps} obs={observed:.8g} exact={predicted:.8g} std={std:.5g}')
        assert abs(observed-predicted)<5.0*std+0.0002
    print('REULEAUX_BOUNDARY_TWO_TERM_MARKED_DIAGNOSTIC_OK')


if __name__=='__main__':
    run()
