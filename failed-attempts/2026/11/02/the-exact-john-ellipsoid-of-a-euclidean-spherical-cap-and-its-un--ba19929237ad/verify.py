#!/usr/bin/env python3
"""Standalone numerical and algebraic checks of the spherical-cap John ellipsoid.
Requires only the Python standard library. Numerical sampling does not certify
optimality; the regular-simplex John decomposition provides the analytic proof.
"""
import math
import random


def axes(d, a):
    assert isinstance(d, int) and d >= 2 and -1.0 < a < 1.0
    delta = math.sqrt(a*a + 4*d*(1-a*a)/(d+1)**2)
    u = (delta-a)/2
    t = (delta+a)/2
    v = math.sqrt(u*u + d*u*t)
    return t, u, v


def ball_volume(d):
    return math.pi**(d/2)/math.gamma(1+d/2)


def assert_near(x, y, atol=2e-11, rtol=2e-11):
    assert abs(x-y) <= atol+rtol*max(abs(x), abs(y)), (x, y)


def contact_simplex(d):
    # Euclidean realization in R^(d+1) of a d-dimensional zero-sum subspace.
    c = math.sqrt((1-1/d**2)*d/(d-1))
    vectors = [[-1.] + [0.]*d]
    for j in range(d):
        vectors.append([1/d] + [c*((1. if k == j else 0.)-1/d)
                                    for k in range(d)])
    return vectors


def test_exact_and_contact():
    rng = random.Random(20261026)
    for d in (2, 3, 4, 7, 13):
        for a in (-.95, -.3, 0., .4, .93):
            t, u, v = axes(d, a)
            assert_near(t-u, a)
            assert_near(u*t, d*(1-a*a)/(d+1)**2)
            assert_near(v*v, u*u+d*u*t)
            assert_near(t*t+v*v+t*u/d, 1.)
            for k in range(300):
                s = rng.uniform(-1., 1.)
                norm2 = (t+u*s)**2 + v*v*(1-s*s)
                exact = 1-d*t*u*(s-1/d)**2
                assert_near(norm2, exact)
                assert norm2 <= 1. + 2e-12
                assert t+u*s >= a-2e-12
            pts = contact_simplex(d)
            assert len(pts) == d+1
            for i in range(d+1):
                for j in range(d+1):
                    dot = sum(x*y for x,y in zip(pts[i], pts[j]))
                    assert_near(dot, 1. if i == j else -1/d)
            w = d/(d+1)
            center = [sum(w*p[k] for p in pts) for k in range(d+1)]
            assert max(map(abs, center)) < 4e-12
            # Orthogonal projection onto the physical d-dimensional subspace.
            for i in range(d+1):
                for j in range(d+1):
                    lhs = sum(w*p[i]*p[j] for p in pts)
                    rhs = (1. if i==j else 0.) if i==0 or j==0 else ((1. if i==j else 0.) - 1/d)
                    assert_near(lhs,rhs)
            assert_near(pts[0][0], -1.)
            for p in pts[1:]:
                s = p[0]
                assert_near(s, 1/d)
                norm2 = (t+u*s)**2+v*v*(1-s*s)
                assert_near(norm2, 1.)
    print('CONTAINMENT_IDENTITY_AND_CONTACT_SIMPLEX_PASSED')


def test_normalized_volumes():
    for d in (2, 3, 4, 5, 9):
        t,u,v = axes(d,0.)
        hemisphere_ratio = 2*u*v**(d-1)
        target = 2*d**(d/2)/(d+1)**((d+1)/2)
        assert_near(hemisphere_ratio,target)
        target_thin = ball_volume(d)/ball_volume(d-1)*(d/(d+1))**d
        eps = 1e-6
        t,u,v = axes(d,1-eps)
        ell_norm = ball_volume(d)*u/eps*(v/math.sqrt(eps))**(d-1)
        steps = 20000
        q = (d-1)/2
        s = 0.
        for j in range(steps+1):
            y = j/steps
            f=(2*y-eps*y*y)**q
            s += f*(1 if j==0 or j==steps else (4 if j%2 else 2))
        cap_norm=ball_volume(d-1)*s/(3*steps)
        assert_near(ell_norm/cap_norm,target_thin,atol=0.00005,rtol=0.00005)
    print('HEMISPHERE_AND_THIN_CAP_RATIOS_PASSED')


def test_dimension_scales():
    d = 100000
    for a in (-.6,-.2,.2,.6):
        t,u,v=axes(d,a)
        if a>0:
            assert_near(d*u,(1-a*a)/a,rtol=0.001)
            assert_near(t,a,rtol=0.001)
            assert_near(v,math.sqrt(1-a*a),rtol=0.001)
        else:
            assert_near(u,-a,rtol=0.001)
            assert_near(d*t,(1-a*a)/(-a),rtol=0.001)
            assert_near(v,1,rtol=0.001)
    for sigma in (-3.,-1.,0.,1.,3.):
        a=sigma/math.sqrt(d)
        t,u,v=axes(d,a)
        assert_near(math.sqrt(d)*u,(math.sqrt(sigma*sigma+4)-sigma)/2,rtol=.0002)
        assert_near(math.sqrt(d)*t,(math.sqrt(sigma*sigma+4)+sigma)/2,rtol=.0002)
        assert_near(v,1,rtol=.0002)
    # The known planar half-disk special case.
    t,u,v=axes(2,0.)
    assert_near(t,math.sqrt(2)/3)
    assert_near(u,math.sqrt(2)/3)
    assert_near(v,math.sqrt(2/3))
    print('SHARP_DIMENSION_SCALINGS_AND_PLANAR_BENCHMARK_PASSED')


if __name__=='__main__':
    test_exact_and_contact()
    test_normalized_volumes()
    test_dimension_scales()
    print('ALL_CHECKS_PASSED')
