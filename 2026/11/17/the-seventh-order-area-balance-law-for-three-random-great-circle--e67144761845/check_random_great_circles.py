"""Checks for the area-spread law of three isotropic great circles.

Run: python check_random_great_circles.py
Requires numpy and sympy; fixed RNG seed for reproducibility.
"""
import itertools
import math
from fractions import Fraction
import numpy as np
import sympy as sp


def sample_unit_vectors(count, rng):
    x = rng.normal(size=(count, 3, 3))
    return x / np.linalg.norm(x, axis=-1, keepdims=True)


def direct_cell_area(normals, signs):
    corners = []
    for i, j in ((0, 1), (1, 2), (2, 0)):
        k = 3-i-j
        p = np.cross(normals[i], normals[j])
        p = p/np.linalg.norm(p)
        if signs[k]*np.dot(normals[k],p) < 0:
            p = -p
        corners.append(p)
    a,b,c = corners
    vol = abs(np.dot(a,np.cross(b,c)))
    denom = 1 + np.dot(a,b) + np.dot(b,c) + np.dot(c,a)
    return 2*np.arctan2(vol,denom)


def area_formula(normals, signs):
    x = np.array([np.dot(normals[0],normals[1]),
                  np.dot(normals[1],normals[2]),
                  np.dot(normals[2],normals[0])])
    t = np.arcsin(np.clip(x,-1,1))
    return np.pi/2 + t[0]*signs[0]*signs[1] + t[1]*signs[1]*signs[2] + t[2]*signs[2]*signs[0]


def exact_polytope_integrals():
    # One of six order cones, each with eight sign orthants.
    # x >= y >= z >= 0 and x+y <= 1.
    x,y,z=sp.symbols('x y z', real=True)
    def integrate(p):
        return sp.simplify(48*sp.integrate(sp.integrate(sp.integrate(p,(z,0,y)),(x,y,1-y)),(y,0,sp.Rational(1,2))))
    V=integrate(sp.Integer(1))
    I4=integrate(x*x*y*y+x*x*z*z+y*y*z*z)
    assert V==2
    assert I4==sp.Rational(7,120)
    leading=sp.simplify(V/(32*sp.pi))  # density 1/(4pi); scaling epsilon^3/8
    nextc=sp.simplify(I4/(1024*sp.pi)) # density 1/(4pi); one half; scaling epsilon^7/128
    assert leading == 1/(16*sp.pi)
    assert nextc == sp.Rational(7,122880)/sp.pi
    return V,I4


def quadrature_probability(eps, order=32):
    """Independent ordered-coordinate quadrature for the exact probability.

    The eight sign choices reduce to two determinant square-root branches.
    The six permutations share one ordered simplex x>=y>=z>=0, x+y<=1.
    """
    u, w = np.polynomial.legendre.leggauss(order)
    u, w = (u + 1)/2, w/2
    mass = 0.0
    for yy, wy in zip(u, w):
        y = yy/2
        for xx, wx in zip(u, w):
            x = y + (1-2*y)*xx
            z = y*u
            t = eps*np.stack([x*np.ones_like(z), y*np.ones_like(z), z])/2
            sn = np.sin(t)
            q = 1-np.sum(sn**2, axis=0)
            p = np.prod(sn, axis=0)
            # Two signs for the triple product; other sign choices are equivalent.
            density_factor = np.prod(np.cos(t),axis=0) * (1/np.sqrt(q+2*p)+1/np.sqrt(q-2*p))/2
            mass += float(np.sum(48 * wy*wx*w * 0.5*(1-2*y)*y * density_factor))
    return mass * (eps/2)**3 / (4*math.pi)


def verify():
    rng = np.random.default_rng(711203)
    signs=np.array(list(itertools.product((-1,1),repeat=3)))
    for normal_set in sample_unit_vectors(80,rng):
        exact=np.array([direct_cell_area(normal_set,s) for s in signs])
        formula=np.array([area_formula(normal_set,s) for s in signs])
        assert np.allclose(exact,formula,atol=2e-10,rtol=2e-10), (exact,formula)
        t=np.array([math.asin(float(np.dot(normal_set[i],normal_set[j])))
                    for i,j in ((0,1),(1,2),(2,0))])
        spread=np.max(exact)-np.min(exact)
        predicted=2*sum(sorted(np.abs(t))[-2:])
        assert abs(spread-predicted)<1e-9
        assert abs(sum(exact)-4*math.pi)<1e-8
    print('DIRECT_SPHERICAL_TRIANGLE_GEOMETRY_OK')
    print('POLYTOPE_VOLUME_QUARTIC_MOMENTS',exact_polytope_integrals())
    print('EXACT_ASYMPTOTIC_COEFFICIENTS_OK')

    # Empirical probability for the extreme near-equal-area event.
    N=2500000
    normals=sample_unit_vectors(N,rng)
    t=np.arcsin(np.clip(np.stack([np.einsum('ij,ij->i',normals[:,0],normals[:,1]),
                                  np.einsum('ij,ij->i',normals[:,1],normals[:,2]),
                                  np.einsum('ij,ij->i',normals[:,2],normals[:,0])],axis=1),-1,1))
    abs_t=np.sort(np.abs(t),axis=1)
    spread=2*(abs_t[:,1]+abs_t[:,2])
    for eps in (0.30, 0.45, 0.65):
        p=float(np.mean(spread<eps))
        pred=eps**3/(16*math.pi)+7*eps**7/(122880*math.pi)
        err=math.sqrt(pred*(1-pred)/N)
        zscore=abs(p-pred)/err
        print(f'eps={eps:.2f} observed={p:.9g} prediction={pred:.9g} z={zscore:.3f}')
        assert zscore<4.0
    print('RARE_EVENT_MONTE_CARLO_OK')
    for eps in (.2, .5, 1.0):
        val=quadrature_probability(eps)
        truncated=eps**3/(16*math.pi)+7*eps**7/(122880*math.pi)
        remainder=val-truncated
        print(f'quadrature epsilon={eps:.2f} P={val:.14g} remainder={remainder:.6g}')
        assert 0 < remainder < 3e-6*eps**9
    print('SEVENTH_ORDER_QUADRATURE_DIAGNOSTICS_OK')

if __name__=='__main__':
    verify()
