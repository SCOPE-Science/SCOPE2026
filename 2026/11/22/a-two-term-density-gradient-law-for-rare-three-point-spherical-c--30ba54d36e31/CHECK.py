#!/usr/bin/env python3
"""Standalone numerical checks for the three-point spherical-cap clustering formulas.
No third-party dependencies; calculations are diagnostics, not a substitute for proof.
"""
import math

PI = math.pi

def simpson(func, lo, hi, n=40000):
    assert n > 0 and n % 2 == 0
    h = (hi - lo) / n
    total = func(lo) + func(hi)
    for j in range(1, n):
        total += (4 if j & 1 else 2) * func(lo + j * h)
    return total * h / 3

def lens(d):
    assert 0 <= d <= 2
    beta = math.acos(min(1.0, max(-1.0, d/2)))
    a = 2*beta - d*math.sqrt(max(0.0, 4-d*d))/2
    p = 4*beta
    return a + p + PI

def F0(eps):
    c = math.cos(eps)
    return (1-c)**2 * (4+5*c)/4

def H1(eps):
    c = math.cos(eps)
    return c*(1+c)*(1-c)**2*(13*c+5)/16

def quadratic_coefficient_l2(eps):
    c = math.cos(eps)
    return 3*c*(1-c)**2*(1+c)*(23*c**3+7*c**2-10*c-2)/80

def sphere_lens_outer_area(theta, eps):
    c, s = math.cos(eps), math.sin(eps)
    argb = (c/s) * math.tan(theta/2)
    argg = (math.cos(theta)-c*c)/(s*s)
    b = math.acos(min(1.0, max(-1.0, argb)))
    g = math.acos(min(1.0, max(-1.0, argg)))
    return 2*PI-2*c*g-4*math.cos(2*eps)*b

def pair_moment_integral(eps, moment):
    def integrand(theta):
        return math.sin(theta) * moment(math.cos(theta)) * sphere_lens_outer_area(theta,eps) / (8*PI)
    return simpson(integrand,0,2*eps,40000)

def check_close(a,b,rtol,atol=1e-13):
    assert abs(a-b) <= atol+rtol*max(abs(a),abs(b)), (a,b,a-b)

if __name__ == '__main__':
    C0 = 2*PI*simpson(lambda d: d*lens(d), 0,2)
    T = 2*PI*simpson(lambda d: d**3*lens(d),0,2)
    check_close(C0,9*PI**2,5e-8)
    check_close(T,15*PI**2,5e-8)
    print('Euclidean lens moments PASS:',C0,T)
    for eps in (0.15,0.3,0.5,0.8,1.2):
        raw_F=pair_moment_integral(eps,lambda z: 1.0)
        raw_H=pair_moment_integral(eps,lambda z: z)
        raw_Q=3/5*pair_moment_integral(eps,lambda z:(3*z*z-1)/2)
        check_close(raw_F,F0(eps),1e-6)
        check_close(raw_H,H1(eps),1e-6)
        check_close(raw_Q,quadratic_coefficient_l2(eps),1e-6)
        print('Spherical quadrature PASS:',eps,raw_F,raw_H,raw_Q)
    # Independent second-order diagnostics: two nonuniform families with
    # quadratic Legendre perturbations. Coefficients come from the theorem.
    for eps in (0.08,0.1,0.12):
        dip_asym=(9/16)*eps**4-(23/32)*eps**6
        quad_asym=(27/80)*eps**4-(159/160)*eps**6
        assert abs(H1(eps)-dip_asym)/eps**8 < 0.5
        assert abs(quadratic_coefficient_l2(eps)-quad_asym)/eps**8 < 1.6
        print('Small-radius expansion PASS:',eps)
    print('ALL CHECKS PASSED')
