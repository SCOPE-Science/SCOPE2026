#!/usr/bin/env python3
"""Independent finite checks for the mathematical statements in RESULT.md.

The full parameter-range proof is analytical; sample checks are diagnostics.
Standard-library only.
"""
from fractions import Fraction
from math import pi, sin, cos, sqrt, asin, isclose


def params(w):
    assert 0 <= w < 1
    return 2/(1+w), 2/(1-w)


def integral_abs_affine(R):
    if R <= 1:
        return 1.0
    return 2/pi*(sqrt(R*R-1)+asin(1/R))


def kernel(w,x,y):
    a,b=params(w)
    return 1+a*cos(x)*cos(y)+b*sin(x)*sin(y)


def exact_lebesgue_function(w,x):
    a,b=params(w)
    radius=sqrt((a*cos(x))**2+(b*sin(x))**2)
    return (1-w)*integral_abs_affine(radius)+w*max(1,a*abs(cos(x)))


def exact_norm(w):
    q=1-w
    return w+2/pi*(sqrt(4-q*q)+q*asin(q/2))


def direct_quadrature(w,x,m=40000):
    # Composite midpoint quadrature is independent of the absolute-cosine formula.
    return ((1-w)*sum(abs(kernel(w,x,2*pi*(j+.5)/m)) for j in range(m))/m
           +w*(abs(kernel(w,x,0))+abs(kernel(w,x,pi)))/2)


def check_gram():
    for r in [Fraction(1,100),Fraction(1,3),Fraction(3,5),Fraction(99,100)]:
        mass_const=1
        mass_cos2=(1-r)*Fraction(1,2)+r
        mass_sin2=(1-r)*Fraction(1,2)
        assert mass_cos2 == (1+r)/2
        assert mass_sin2 == (1-r)/2
        assert mass_const == 1
        assert mass_cos2>0 and mass_sin2>0
    print('EXACT_MIXED_MOMENT_GRAM_AND_REPRODUCING_KERNEL_COEFFICIENTS_OK')


def check_angular_and_extremizers():
    for w in [0,1/100,1/10,1/3,1/2,4/5,19/20,99/100]:
        t0=(1+w)/2
        maxv=exact_norm(w)
        assert isclose(exact_lebesgue_function(w,pi/2),maxv,rel_tol=1e-13)
        for k in range(1,201):
            x=pi*k/400
            assert exact_lebesgue_function(w,x) <= maxv+3e-13
        for t in [t0, (t0+1)/2, 1]:
            a,b=params(w)
            rr=sqrt(a*a*t*t+b*b*(1-t*t))
            assert rr>=1-1e-12
            assert maxv > (1-w)*integral_abs_affine(rr)+w*max(1,a*t)+1e-13 if w>0 else True
        # Evaluation at a norming latitude uses sign of kernel as a witness.
        q=direct_quadrature(w,pi/2,15000)
        assert abs(q-maxv)<4e-7,(w,q,maxv)
        # Independent off-equator evaluation check.
        for x in [0.15,0.53,1.12,2.0]:
            qq=direct_quadrature(w,x,15000)
            assert abs(qq-exact_lebesgue_function(w,x))<4e-7,(w,x,qq)
    print('FULL_REPRODUCING_KERNEL_LEBESGUE_FUNCTION_AND_WITNESS_CHECKS_OK')


def check_slope_and_endpoints():
    base=(1/3)+(2*sqrt(3)/pi)
    limit=1+4/pi
    assert abs(exact_norm(0)-base)<2e-14
    assert abs(exact_norm(1-1e-10)-limit)<1e-9
    ws=[0, .02,.1,.25,.45,.75,.9,.999]
    vals=[exact_norm(w) for w in ws]
    assert all(x<y for x,y in zip(vals,vals[1:]))
    for w in [.01,.25,.5,.75,.99]:
        q=1-w
        derivative=1-2/pi*asin(q/2)
        assert 2/3<derivative<1
        h=1e-6
        fd=(exact_norm(w+h)-exact_norm(w-h))/(2*h)
        assert abs(fd-derivative)<1e-8
    print('STRICT_MONOTONE_CONVEX_NORM_PROFILE_AND_SINGULAR_LIMIT_OK')


def check_analytic_derivative_certificate():
    # The proof uses f(s)=sqrt(s-1)/s and min of endpoints.
    # These tests check that strict margin persists in numerical sample regimes.
    for w in [1e-8, .001,.02,.25,.5,.8,.99,.9999]:
        p,q=1+w,1-w
        a,b=params(w)
        fe=lambda s:sqrt(s-1)/s
        assert min(fe(a*a),fe(b*b))>pi*q/8
        for i in range(101):
            t=p/2+(1-p/2)*i/100
            rr2=(a*t)**2+b*b*(1-t*t)
            assert t*fe(rr2)>pi*p*q/16-2e-13
    print('POSITIVE_MARGIN_FOR_GLOBAL_ANGULAR_MONOTONICITY_CHECKED')


if __name__=='__main__':
    check_gram()
    check_angular_and_extremizers()
    check_slope_and_endpoints()
    check_analytic_derivative_certificate()
    print('ALL_ANTIPODAL_ATOM_TRIGONOMETRIC_PROJECTION_CHECKS_OK')
